# -*- coding: utf-8 -*-
"""
Kontrolna tabela (nalog V7, odjeljak 12): SURA_<n>_ROOT_PANEL_AUDIT.xlsx iz FINAL JSON-a.
Listovi APP_ROOTS, PANEL_ITEMS, SURA_<n>, AUDIT, ROOT_RTL_QA; arapske ćelije desno poravnate, readingOrder=2.

  uv run scripts/roots/audit_xlsx.py <FINAL.json> <sura> <audit.json>
"""
import json
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment

sys.stdout.reconfigure(encoding="utf-8")
RTL = Alignment(horizontal="right", readingOrder=2, wrap_text=True)
LTR = Alignment(horizontal="left", readingOrder=1, wrap_text=True)


def sheet(wb, name, head, rows, rtl_cols):
    ws = wb.create_sheet(name)
    ws.append(head)
    for r in rows:
        ws.append(r)
    for row in ws.iter_rows(min_row=1):
        for i, c in enumerate(row):
            c.alignment = RTL if head[i] in rtl_cols else LTR


def main():
    src, n, audit = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    d = json.load(open(src, encoding="utf-8"))
    wb = Workbook()
    wb.remove(wb.active)
    sheet(wb, "APP_ROOTS", ["ROOT_BW", "ROOT_DISPLAY", "DICTIONARY_URL", "NOUNS", "VERBS", "SOURCE"],
          [[r["root_bw"], r["root_display"], r["dictionary_url"], len(r["nouns"]), len(r["verbs"]), r.get("source", "")]
           for r in d["roots"]], {"ROOT_DISPLAY"})
    items = []
    for r in d["roots"]:
        for sec in ("nouns", "verbs"):
            for c in r[sec]:
                items.append([c["id"], r["root_bw"], c["pos"], c["lemma"], c["group_key"], c["form"], c["meaning_bs"],
                              c["ayah_ref"], c["arabic"], c["bosnian"], c["highlight_word_index"],
                              f"{c['highlight_display_span']['start']}-{c['highlight_display_span']['end']}",
                              "DA" if c.get("is_excerpt") else "NE", ":".join(map(str, c["qac_location"])), c.get("qa_status", "PASS")])
    sheet(wb, "PANEL_ITEMS", ["ID", "ROOT_BW", "POS", "LEMMA", "GROUP_KEY", "FORM", "MEANING_BS", "REF", "ARABIC", "BOSNIAN",
                              "WORD_INDEX", "HIGHLIGHT", "IZVOD", "QAC_LOC", "QA"], items, {"FORM", "ARABIC"})
    words = []
    for v in d["surah_verses"]:
        for w in v["words"]:
            if w.get("clickable"):
                words.append([v["ref"], w["qac_word_index"], w["word"], w["root_bw"], ":".join(map(str, w["stem_qac_location"]))])
    sheet(wb, f"SURA_{n}", ["REF", "WORD_INDEX", "WORD", "ROOT_BW", "STEM_QAC"], words, {"WORD"})
    a = json.load(open(audit, encoding="utf-8"))
    sheet(wb, "AUDIT", ["CHECK", "STATUS", "EVIDENCE"], [[x["check"], x["status"], x["evidence"]] for x in a], set())
    sheet(wb, "ROOT_RTL_QA", ["ROOT_BW", "ROOT_DISPLAY_RTL", "FIRST_LETTER", "RTL_QA"],
          [[r["root_bw"], r["root_display"], r["root_display"].split()[0],
            "PASS" if r["root_display"].split()[0] == r["root_display"][0] else "FAIL"] for r in d["roots"]],
          {"ROOT_DISPLAY_RTL", "FIRST_LETTER"})
    out = src.replace("_FINAL.json", "_AUDIT.xlsx")
    wb.save(out)
    print(out)


if __name__ == "__main__":
    main()
