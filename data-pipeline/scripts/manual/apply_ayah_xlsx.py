"""Ručna ispravka jednog ajeta u runs/S###_*/final/*APP_READY_REVIDIRANA.xlsx prema istom spec JSON-u kao apply_ayah.mjs.

    uv run --project data-pipeline python data-pipeline/scripts/manual/apply_ayah_xlsx.py spec.json [napomena]

Prepisuje redove ajeta u listovima Bosanski_tokeni i Veze, veze/status u Segmenti i tekst u Prijevod_Mehanovic.
Prije izmjene pravi kopiju fajla (*.prije_rucne_izmjene_<datum>.xlsx) pored originala, jer runs/ nije u gitu.
"""
import datetime
import glob
import json
import os
import shutil
import sys

import openpyxl

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
spec = json.load(open(sys.argv[1], encoding="utf-8"))
note_extra = sys.argv[2] if len(sys.argv) > 2 else ""
surah, ayah = spec["surah"], spec["ayah"]
today = datetime.date.today().isoformat()
NOTE = f"USER_DECISION_{today}: ručna ispravka ajeta. {note_extra}".strip()

path = glob.glob(os.path.join(ROOT, "runs", f"S{surah:03d}_*", "final", "*APP_READY_REVIDIRANA.xlsx"))[0]
backup = path.replace(".xlsx", f".prije_rucne_izmjene_{today}.xlsx")
if not os.path.exists(backup):
    shutil.copy2(path, backup)
wb = openpyxl.load_workbook(path)


def cols(ws):
    return {c.value: i for i, c in enumerate(ws[1])}


def is_ayah(row, c, sk="surah_id", ak="ayah_id"):
    return row[c[sk]].value in (surah, str(surah)) and row[c[ak]].value in (ayah, str(ayah))


# Segmenti: klase/boje i ID riječi
ws_seg = wb["Segmenti"]
cs = cols(ws_seg)
seginfo = {}
for row in ws_seg.iter_rows(min_row=2):
    if is_ayah(row, cs, "surah", "ayah"):
        seginfo[row[cs["qac_segment_id"]].value] = {k: row[i].value for k, i in cs.items()}

tokens_per_seg = {}
for t in spec["tokens"]:
    for s in t["segs"]:
        tokens_per_seg[s] = tokens_per_seg.get(s, 0) + 1


def token_values(k, t, old):
    segs = t["segs"]
    classes = sorted({seginfo[s]["qac_css_class"] for s in segs})
    if not segs:
        css, hexv, status = "inserted_no_arabic_segment", "#000000", "inserted_no_arabic_segment"
    elif len(classes) > 1:
        css, hexv, status = "neutral-fused", "#000000", "MAPPED_FUSED_MULTI_SEGMENT"
    else:
        css, hexv = classes[0], seginfo[segs[0]]["qac_hex_color"]
        status = "MAPPED_ONE_TO_MANY" if any(tokens_per_seg[s] > 1 for s in segs) else "MAPPED_ONE_TO_ONE"
    words = sorted({seginfo[s]["qac_word_id"] for s in segs})
    unchanged = old and (old.get("linked_qac_segment_ids") or "") == ";".join(segs) and old.get("bosnian_original_token") == t["text"]
    v = dict(old or {})
    v.update({
        "surah_id": surah, "ayah_id": ayah, "bosnian_token_order": k + 1, "bosnian_token_id": t["id"],
        "bosnian_original_token": t["text"], "is_lexical": True,
        "linked_qac_segment_ids": ";".join(segs) or None, "linked_qac_word_ids": ";".join(words) or None,
    })
    if not unchanged:
        v.update({"mapping_status": status, "qac_css_class": css, "qac_hex_color": hexv,
                  "highlight_group_id": "|".join(f"HG-{w}" for w in words) or None, "mapping_note": NOTE})
    v.setdefault("source_ref", f"https://quranenc.com/bs/browse/bosnian_mihanovich/{surah}-{ayah}")
    return v


def rewrite_rows(ws, c, new_rows, match):
    """Zamijeni sve redove ajeta (match) novim redovima, na istom mjestu u listu."""
    rows = [r[0].row for r in ws.iter_rows(min_row=2) if match(r)]
    first = rows[0] if rows else ws.max_row + 1
    for r in reversed(rows):
        ws.delete_rows(r)
    if new_rows:
        ws.insert_rows(first, amount=len(new_rows))
    for k, v in enumerate(new_rows):
        for name, i in c.items():
            ws.cell(row=first + k, column=i + 1, value=v.get(name))


# Bosanski_tokeni
ws = wb["Bosanski_tokeni"]
c = cols(ws)
old_tok = {r[c["bosnian_token_id"]].value: {k: r[i].value for k, i in c.items()} for r in ws.iter_rows(min_row=2) if is_ayah(r, c)}
new_tok, pos = [], 0
for k, t in enumerate(spec["tokens"]):
    v = token_values(k, t, old_tok.get(t["id"]))
    start = pos + (1 if k else 0)
    v.update({"gap_before": " " if k else None, "span_start": start, "span_end": start + len(t["text"])})
    pos = start + len(t["text"])
    new_tok.append(v)
if spec.get("text") and pos != len(spec["text"]):
    raise SystemExit(f"tekst ajeta ({len(spec['text'])}) ne odgovara tokenima ({pos})")
rewrite_rows(ws, c, new_tok, lambda r: is_ayah(r, c))

# Veze
ws = wb["Veze"]
c = cols(ws)
old_links = {(r[c["qac_segment_id"]].value, r[c["bosnian_token_id"]].value): {k: r[i].value for k, i in c.items()}
             for r in ws.iter_rows(min_row=2) if is_ayah(r, c)}
tok_by_id = {v["bosnian_token_id"]: v for v in new_tok}
new_links = []
for sid in sorted(seginfo):
    for t in spec["tokens"]:
        if sid in t["segs"]:
            tv = tok_by_id[t["id"]]
            v = old_links.get((sid, t["id"])) or {
                "surah_id": surah, "ayah_id": ayah, "qac_segment_id": sid, "qac_word_id": seginfo[sid]["qac_word_id"],
                "bosnian_token_id": t["id"], "bosnian_token_part_id": None, "qac_tag": seginfo[sid]["tag"],
                "qac_css_class": seginfo[sid]["qac_css_class"], "qac_hex_color": seginfo[sid]["qac_hex_color"],
                "highlight_group_id": f"HG-{seginfo[sid]['qac_word_id']}", "mapping_note": NOTE,
                "source_ref": seginfo[sid].get("source_ref")}
            v["mapping_status"] = tv["mapping_status"]
            new_links.append(v)
rewrite_rows(ws, c, new_links, lambda r: is_ayah(r, c))

# Segmenti: veze i status
for row in ws_seg.iter_rows(min_row=2):
    sid = row[cs["qac_segment_id"]].value
    if sid in seginfo:
        toks = [t["id"] for t in spec["tokens"] if sid in t["segs"]]
        row[cs["linked_bosnian_token_ids"]].value = ";".join(toks) or None
        if not toks:
            row[cs["mapping_status"]].value = "QAC_SEGMENT_NOT_SEPARATELY_EXPRESSED_IN_BOSNIAN"
        elif row[cs["mapping_status"]].value == "QAC_SEGMENT_NOT_SEPARATELY_EXPRESSED_IN_BOSNIAN":
            row[cs["mapping_status"]].value = tok_by_id[toks[0]]["mapping_status"]

# Prijevod
if spec.get("text"):
    ws = wb["Prijevod_Mehanovic"]
    c = cols(ws)
    for row in ws.iter_rows(min_row=2):
        if row[c["ayah_id"]].value in (ayah, str(ayah)):
            row[c["source_exact"]].value = spec["text"]
            if "reconstructed_from_tokens" in c:
                row[c["reconstructed_from_tokens"]].value = spec["text"]

wb.save(path)
sys.stdout.reconfigure(encoding="utf-8")
print(f"{os.path.basename(path)}: {surah}:{ayah} — {len(new_tok)} tokena, {len(new_links)} veza")
