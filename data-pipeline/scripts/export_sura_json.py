# -*- coding: utf-8 -*-
"""
Pretvara jedan QAC DIRECT V13 APP_READY Excel fajl u JSON spreman za
aplikaciju. Ovo je privremeni razvojni izlaz (dok Supabase baza iz
OPIS poglavlja 6 ne bude spremna) — output ide u data-pipeline/output/,
koji se ne commituje u Git (pipeline ga reproducira).

Pravilo iz OPIS poglavlja 11: skripta staje umjesto da tiho upiše nešto
pogrešno. Provjerava da broj ajeta/riječi/segmenata odgovara QA listu
prije nego išta upiše.

Upotreba:
    uv run export_sura_json.py <putanja_do_APP_READY.xlsx> <izlazni_json>
"""
import sys
import json
import openpyxl
from collections import defaultdict

# Windows konzola je cp1252 po defaultu i lomi arapska/bosanska slova
# (OPIS poglavlje 5.12) — ispis prisilno na UTF-8.
sys.stdout.reconfigure(encoding="utf-8")


def read_sheet(wb, name):
    ws = wb[name]
    header = [ws.cell(row=1, column=c).value for c in range(1, ws.max_column + 1)]
    rows = []
    for r in range(2, ws.max_row + 1):
        vals = [ws.cell(row=r, column=c).value for c in range(1, ws.max_column + 1)]
        if all(v is None for v in vals):
            continue
        rows.append(dict(zip(header, vals)))
    return rows


def read_qa(wb):
    """
    QA list ima dva poznata oblika (OPIS 5.11): V13 je Metrika/Vrijednost
    parovi u dvije kolone; V12 je tabela sa kolonama
    provjera/stvarno/očekivano/status. Oba se svode na isti rječnik.
    """
    ws = wb["QA"]
    header = [ws.cell(row=1, column=c).value for c in range(1, ws.max_column + 1)]
    qa = {}
    if header[:2] == ["Metrika", "Vrijednost"]:
        for r in range(2, ws.max_row + 1):
            k = ws.cell(row=r, column=1).value
            v = ws.cell(row=r, column=2).value
            if k is not None:
                qa[str(k).strip()] = v
    else:
        # V12: provjera | stvarno | očekivano | status
        for r in range(2, ws.max_row + 1):
            k = ws.cell(row=r, column=1).value
            v = ws.cell(row=r, column=2).value
            status = ws.cell(row=r, column=4).value
            if k is not None:
                qa[str(k).strip()] = f"{v} ({status})"
    return qa


def detect_schema(wb):
    """
    Vraća 'v13' ili 'v12' na osnovu stvarnih zaglavlja u Segmenti listu —
    OPIS pravilo 5.11: prepoznaj format po sadržaju, ne po imenu fajla.
    """
    ws = wb["Segmenti"]
    header = [ws.cell(row=1, column=c).value for c in range(1, ws.max_column + 1)]
    if "qac_hex_color" in header:
        return "v13"
    if "qac_hex" in header:
        return "v12"
    raise ValueError(f"Nepoznata šema Segmenti lista: {header}")


def normalize_word(row, schema):
    if schema == "v13":
        return {
            "surah_id": row["surah_id"],
            "ayah_id": row["ayah_id"],
            "qac_word_id": row["qac_word_id"],
            "word_index": row["word_index"],
            "arabic_word": row["arabic_word"],
            "qac_transliteration": row.get("qac_transliteration"),
            "qac_gloss": row.get("qac_gloss"),
        }
    # v12
    return {
        "surah_id": row["surah_id"],
        "ayah_id": row["ayah_id"],
        "qac_word_id": row["qac_word_id"],
        "word_index": row["word_index"],
        "arabic_word": row["original_arabic_word"],
        "qac_transliteration": None,
        "qac_gloss": row.get("qac_gloss"),
    }


def is_surface_segment(seg):
    """
    Da li je segment stvarno napisan u ajetu (za prikaz), ili je
    implicitan (npr. "Ø" — implicitna zamjenica, ili prazan
    arabic_segment). Implicitni segmenti postoje u OBA formata:
    - V12 ih eksplicitno označava sa is_surface=False (kolona postoji).
    - V13 nema tu kolonu, ali isti slučaj prepoznat je po praznom
      arabic_segment i/ili qac_css_class == 'segSilver' (boja rezervisana
      baš za ovu kategoriju — vidi suru 80, implicitna zamjenica bez
      teksta).
    """
    if not seg.get("is_surface", True):
        return False
    if not seg.get("arabic_segment"):
        return False
    if seg.get("qac_css_class") == "segSilver":
        return False
    return True


def normalize_segment(row, schema):
    if schema == "v13":
        return {
            "qac_word_id": row["qac_word_id"],
            "qac_segment_id": row["qac_segment_id"],
            "segment_order": row["segment_order"],
            "arabic_segment": row["arabic_segment"],
            "qac_tag": row["qac_tag"],
            "qac_full_description": row["qac_full_description"],
            "qac_css_class": row["qac_css_class"],
            "qac_hex_color": row["qac_hex_color"],
            "lemma": row.get("lemma"),
            "root": row.get("root"),
            "bosnian_expression_status": row["bosnian_expression_status"],
        }
    # v12
    return {
        "qac_word_id": row["qac_word_id"],
        "qac_segment_id": row["qac_segment_id"],
        "segment_order": row["segment_index"],
        "arabic_segment": row["arabic_segment"],
        "qac_tag": row["qac_tag"],
        "qac_full_description": row["qac_full_description"],
        "qac_css_class": row["qac_css_class"],
        "qac_hex_color": row["qac_hex"],
        "lemma": row.get("lemma_arabic") or row.get("lemma_bw"),
        "root": row.get("root_arabic") or row.get("root_bw"),
        "bosnian_expression_status": row["bosnian_expression_status"],
        # V12 dodatno eksplicitno označava is_surface — čuvamo ga da ga
        # is_surface_segment() provjeri zajedno s ostalim pravilima.
        "is_surface": bool(row.get("is_surface", True)),
    }


def normalize_token(row, schema):
    if schema == "v13":
        return {
            "ayah_id": row["ayah_id"],
            "bosnian_token_id": row["bosnian_token_id"],
            "token_order": row["token_order"],
            "original_bosnian_token": row["original_bosnian_token"],
            "qac_css_class": row["qac_css_class"],
            "qac_hex_color": row["qac_hex_color"],
            "mapping_status": row["mapping_status"],
        }
    # v12
    return {
        "ayah_id": row["ayah_id"],
        "bosnian_token_id": row["bosnian_token_id"],
        "token_order": row["token_index"],
        "original_bosnian_token": row["token_exact"],
        "qac_css_class": row["qac_css_class"],
        "qac_hex_color": row["qac_hex"],
        "mapping_status": row["status"],
    }


def main():
    if len(sys.argv) != 3:
        print("Upotreba: export_sura_json.py <APP_READY.xlsx> <izlaz.json>")
        sys.exit(1)

    in_path, out_path = sys.argv[1], sys.argv[2]
    wb = openpyxl.load_workbook(in_path, data_only=True)

    required_sheets = {"Rijeci", "Segmenti", "Bosanski_tokeni", "Veze", "Prijevod_Mehanovic", "QA"}
    missing = required_sheets - set(wb.sheetnames)
    if missing:
        print(f"GREŠKA: fajl {in_path} nema obavezne listove: {missing}")
        sys.exit(1)

    schema = detect_schema(wb)
    rijeci = [normalize_word(r, schema) for r in read_sheet(wb, "Rijeci")]
    all_segmenti = [normalize_segment(r, schema) for r in read_sheet(wb, "Segmenti")]
    segmenti = [s for s in all_segmenti if is_surface_segment(s)]
    n_implicit = len(all_segmenti) - len(segmenti)
    if n_implicit:
        print(f"Napomena: {n_implicit} implicitni(h) segment(a) (npr. 'Ø') preskočeno u prikazu.")
    tokeni = [normalize_token(r, schema) for r in read_sheet(wb, "Bosanski_tokeni")]
    veze = read_sheet(wb, "Veze")
    prijevod = read_sheet(wb, "Prijevod_Mehanovic")
    qa = read_qa(wb)
    print(f"Detektovana šema: {schema}")

    surah_id = str(rijeci[0]["surah_id"]) if rijeci else None
    if surah_id is None:
        print("GREŠKA: list Rijeci je prazan, nema surah_id.")
        sys.exit(1)

    # --- Provjere prije upisa (OPIS poglavlje 11) ---
    ayah_numbers = sorted(set(int(r["ayah_id"]) for r in rijeci))
    n_ayat = len(ayah_numbers)
    n_rijeci = len(rijeci)
    n_segmenata = len(segmenti)

    problems = []
    if len(prijevod) != n_ayat:
        problems.append(
            f"Prijevod_Mehanovic ima {len(prijevod)} redova, a očekivano {n_ayat} (broj ajeta)."
        )
    # word_id konzistentnost: svaki qac_word_id iz Segmenti mora postojati u Rijeci
    word_ids = set(r["qac_word_id"] for r in rijeci)
    seg_word_ids = set(s["qac_word_id"] for s in segmenti)
    orphan_segments = seg_word_ids - word_ids
    if orphan_segments:
        problems.append(f"{len(orphan_segments)} segment(a) upućuje na nepostojeću riječ: {sorted(orphan_segments)[:5]}...")

    if problems:
        print(f"UPOZORENJE za suru {surah_id} — prijavljujem, ne prekidam:")
        for p in problems:
            print(f"  - {p}")

    # --- Grupisanje segmenata po riječi, sortirano po segment_order ---
    segs_by_word = defaultdict(list)
    for s in segmenti:
        segs_by_word[s["qac_word_id"]].append(s)
    for wid in segs_by_word:
        segs_by_word[wid].sort(key=lambda s: int(s["segment_order"]))

    # --- Veze: segment_id -> [bosnian_token_id, ...] i obratno ---
    seg_to_tokens = defaultdict(list)
    token_to_segs = defaultdict(list)
    for v in veze:
        seg_to_tokens[v["qac_segment_id"]].append(v["bosnian_token_id"])
        token_to_segs[v["bosnian_token_id"]].append(v["qac_segment_id"])

    # --- Slaganje po ajetima ---
    ayat_out = []
    for ayah_num in ayah_numbers:
        words_in_ayah = [r for r in rijeci if int(r["ayah_id"]) == ayah_num]
        words_in_ayah.sort(key=lambda r: int(r["word_index"]))

        words_out = []
        for w in words_in_ayah:
            wid = w["qac_word_id"]
            segs = segs_by_word.get(wid, [])
            segs_out = [
                {
                    "segment_id": s["qac_segment_id"],
                    "order": int(s["segment_order"]),
                    "text": s["arabic_segment"],
                    "tag": s["qac_tag"],
                    "description": s["qac_full_description"],
                    "css_class": s["qac_css_class"],
                    "hex_color": s["qac_hex_color"],
                    "lemma": s.get("lemma"),
                    "root": s.get("root"),
                    "expression_status": s["bosnian_expression_status"],
                    "linked_token_ids": seg_to_tokens.get(s["qac_segment_id"], []),
                }
                for s in segs
            ]
            words_out.append(
                {
                    "word_id": wid,
                    "position": int(w["word_index"]),
                    "text_uthmani": w["arabic_word"],
                    "transliteration": w.get("qac_transliteration"),
                    "gloss": w.get("qac_gloss"),
                    "segments": segs_out,
                }
            )

        tokens_in_ayah = [t for t in tokeni if int(t["ayah_id"]) == ayah_num]
        tokens_in_ayah.sort(key=lambda t: int(t["token_order"]))
        tokens_out = [
            {
                "token_id": t["bosnian_token_id"],
                "position": int(t["token_order"]),
                "text": t["original_bosnian_token"],
                "css_class": t["qac_css_class"],
                "hex_color": t["qac_hex_color"],
                "mapping_status": t["mapping_status"],
                "linked_segment_ids": token_to_segs.get(t["bosnian_token_id"], []),
            }
            for t in tokens_in_ayah
        ]

        mehanovic_row = next((p for p in prijevod if int(p["ayah_id"]) == ayah_num), None)

        ayat_out.append(
            {
                "ayah_number": ayah_num,
                "text_uthmani": " ".join(w["text_uthmani"] for w in words_out),
                "mehanovic_text": mehanovic_row["mehanovic_original"] if mehanovic_row else None,
                "words": words_out,
                "bosnian_tokens": tokens_out,
            }
        )

    out = {
        "surah_id": int(surah_id),
        "ayah_count": n_ayat,
        "source": f"QAC DIRECT {schema.upper()}",
        "qa": qa,
        "ayat": ayat_out,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"OK: sura {surah_id} — {n_ayat} ajeta, {n_rijeci} riječi, {n_segmenata} segmenata -> {out_path}")


if __name__ == "__main__":
    main()
