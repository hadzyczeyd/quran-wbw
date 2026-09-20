# -*- coding: utf-8 -*-
"""
Uvozi jednu QAC DIRECT V13 (ili V12) APP_READY Excel suru direktno u
Supabase, koristeći isto čitanje/normalizaciju šeme kao export_sura_json.py.

Import je ponovljiv (OPIS poglavlje 11): prvo briše SAMO tu suru (u
ispravnom redoslijedu radi stranih ključeva), pa je upisuje nanovo.

Upotreba:
    uv run scripts/import_to_supabase.py <putanja_do_APP_READY.xlsx>
    uv run scripts/import_to_supabase.py --all "D:/zejd APP"
"""
import sys
import os
import glob
import openpyxl
from collections import defaultdict
import requests
from dotenv import dotenv_values

sys.stdout.reconfigure(encoding="utf-8")

# Isti direktorij kao export_sura_json.py — uvozimo njegove funkcije da
# se pravila čitanja Excela ne duplira na dva mjesta.
sys.path.insert(0, os.path.dirname(__file__))
from export_sura_json import (  # noqa: E402
    read_sheet,
    detect_schema,
    normalize_word,
    normalize_segment,
    normalize_token,
    is_surface_segment,
)

ENV_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "web", ".env.local")


def get_supabase_config():
    env = dotenv_values(ENV_PATH)
    url = env.get("NEXT_PUBLIC_SUPABASE_URL")
    key = env.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key:
        print(f"GREŠKA: NEXT_PUBLIC_SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY nisu postavljeni u {ENV_PATH}")
        sys.exit(1)
    return url.rstrip("/"), key


def rest_headers(key, prefer=None):
    h = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    if prefer:
        h["Prefer"] = prefer
    return h


def upsert(base_url, key, table, rows, on_conflict=None):
    if not rows:
        return
    url = f"{base_url}/rest/v1/{table}"
    params = {"on_conflict": on_conflict} if on_conflict else {}
    # PostgREST ima limit na veličinu payloada — šalji u paketima.
    batch_size = 500
    for i in range(0, len(rows), batch_size):
        batch = rows[i : i + batch_size]
        resp = requests.post(
            url,
            headers=rest_headers(key, prefer="resolution=merge-duplicates"),
            params=params,
            json=batch,
            timeout=30,
        )
        if resp.status_code >= 300:
            print(f"GREŠKA pri upisu u {table}: {resp.status_code} {resp.text[:500]}")
            sys.exit(1)


def delete_surah(base_url, key, surah_id):
    """Briše suru u ispravnom redoslijedu (djeca prije roditelja)."""
    headers = rest_headers(key)

    def del_where(table, filter_query):
        resp = requests.delete(f"{base_url}/rest/v1/{table}?{filter_query}", headers=headers, timeout=30)
        if resp.status_code >= 300:
            print(f"GREŠKA pri brisanju iz {table}: {resp.status_code} {resp.text[:500]}")
            sys.exit(1)

    # token_segment_links referenciraju i segmente i tokene ove sure
    word_ids_resp = requests.get(
        f"{base_url}/rest/v1/words?surah_id=eq.{surah_id}&select=word_id", headers=headers, timeout=30
    ).json()
    word_ids = [w["word_id"] for w in word_ids_resp]
    token_ids_resp = requests.get(
        f"{base_url}/rest/v1/bosnian_tokens?surah_id=eq.{surah_id}&select=token_id", headers=headers, timeout=30
    ).json()
    token_ids = [t["token_id"] for t in token_ids_resp]

    if token_ids:
        ids_str = ",".join(token_ids)
        del_where("token_segment_links", f"token_id=in.({ids_str})")
    if word_ids:
        del_where("word_segments", f"word_id=in.({','.join(word_ids)})")
    del_where("words", f"surah_id=eq.{surah_id}")
    del_where("bosnian_tokens", f"surah_id=eq.{surah_id}")
    del_where("ayahs", f"surah_id=eq.{surah_id}")


def import_file(path, base_url, key):
    wb = openpyxl.load_workbook(path, data_only=True)
    schema = detect_schema(wb)

    rijeci = [normalize_word(r, schema) for r in read_sheet(wb, "Rijeci")]
    all_segmenti = [normalize_segment(r, schema) for r in read_sheet(wb, "Segmenti")]
    segmenti = [s for s in all_segmenti if is_surface_segment(s)]
    tokeni = [normalize_token(r, schema) for r in read_sheet(wb, "Bosanski_tokeni")]
    surface_segment_ids = set(s["qac_segment_id"] for s in segmenti)
    all_veze = read_sheet(wb, "Veze")
    veze = [v for v in all_veze if v["qac_segment_id"] in surface_segment_ids]
    n_skipped_veze = len(all_veze) - len(veze)
    if n_skipped_veze:
        print(f"  Napomena: {n_skipped_veze} veza(e) prema implicitnom segmentu preskočeno (nema prikaza).")
    prijevod = read_sheet(wb, "Prijevod_Mehanovic")

    if not rijeci:
        print(f"UPOZORENJE: {path} nema podataka u Rijeci, preskačem.")
        return

    surah_id = int(rijeci[0]["surah_id"])
    print(f"Sura {surah_id}: brišem postojeće podatke...")
    delete_surah(base_url, key, surah_id)

    ayah_numbers = sorted(set(int(r["ayah_id"]) for r in rijeci))
    prijevod_by_ayah = {int(p["ayah_id"]): p["mehanovic_original"] for p in prijevod}

    ayah_rows = [
        {
            "surah_id": surah_id,
            "ayah_number": a,
            "text_uthmani": " ".join(
                r["arabic_word"] for r in sorted(
                    [x for x in rijeci if int(x["ayah_id"]) == a], key=lambda x: int(x["word_index"])
                )
            ),
            "mehanovic_text": prijevod_by_ayah.get(a),
        }
        for a in ayah_numbers
    ]

    word_rows = [
        {
            "word_id": r["qac_word_id"],
            "surah_id": surah_id,
            "ayah_number": int(r["ayah_id"]),
            "position": int(r["word_index"]),
            "text_uthmani": r["arabic_word"],
            "transliteration": r.get("qac_transliteration"),
            "gloss": r.get("qac_gloss"),
        }
        for r in rijeci
    ]

    segment_rows = [
        {
            "segment_id": s["qac_segment_id"],
            "word_id": s["qac_word_id"],
            "segment_order": int(s["segment_order"]),
            "segment_text": s["arabic_segment"],
            "qac_tag": s["qac_tag"],
            "qac_full_description": s.get("qac_full_description"),
            "qac_css_class": s["qac_css_class"],
            "qac_hex_color": s["qac_hex_color"],
            "lemma": s.get("lemma"),
            "root": s.get("root"),
            "expression_status": s["bosnian_expression_status"],
        }
        for s in segmenti
    ]

    token_rows = [
        {
            "token_id": t["bosnian_token_id"],
            "surah_id": surah_id,
            "ayah_number": int(t["ayah_id"]),
            "position": int(t["token_order"]),
            "display_text": t["original_bosnian_token"],
            "qac_css_class": t["qac_css_class"],
            "qac_hex_color": t["qac_hex_color"],
            "mapping_status": t["mapping_status"],
        }
        for t in tokeni
    ]

    link_rows = [
        {"segment_id": v["qac_segment_id"], "token_id": v["bosnian_token_id"]}
        for v in veze
    ]

    upsert(base_url, key, "ayahs", ayah_rows, on_conflict="surah_id,ayah_number")
    upsert(base_url, key, "words", word_rows, on_conflict="word_id")
    upsert(base_url, key, "bosnian_tokens", token_rows, on_conflict="token_id")
    upsert(base_url, key, "word_segments", segment_rows, on_conflict="segment_id")
    upsert(base_url, key, "token_segment_links", link_rows, on_conflict="segment_id,token_id")

    print(
        f"OK: sura {surah_id} — {len(ayah_rows)} ajeta, {len(word_rows)} riječi, "
        f"{len(segment_rows)} segmenata, {len(token_rows)} tokena, {len(link_rows)} veza"
    )


def main():
    if len(sys.argv) < 2:
        print("Upotreba: import_to_supabase.py <APP_READY.xlsx> | --all <folder>")
        sys.exit(1)

    base_url, key = get_supabase_config()

    if sys.argv[1] == "--all":
        folder = sys.argv[2]
        files = sorted(glob.glob(os.path.join(folder, "*_APP_READY*.xlsx")))
        files = [f for f in files if "(1)" not in os.path.basename(f)]
        print(f"Pronađeno {len(files)} APP_READY fajlova.")
        for f in files:
            import_file(f, base_url, key)
    else:
        import_file(sys.argv[1], base_url, key)


if __name__ == "__main__":
    main()
