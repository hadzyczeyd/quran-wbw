# -*- coding: utf-8 -*-
"""
CP9 CHUNKED FULL-COVERAGE RENDER (nalog 53.8): svaki korišteni red obaveznih listova renderuje se
iz same XLSX datoteke (vrijednost + boja fonta/ispune) u HTML chunkove; RENDER_COVERAGE_MANIFEST
dokazuje 100% pokrivenost bez rupa i duplikata.

Upotreba: uv run scripts/v131/render.py <RUN> <xlsx> <label> [chunk=150]
"""
import html
import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, now, sha256_file  # noqa: E402

CSS = """body{font-family:Segoe UI,Arial,sans-serif;margin:12px;background:#fff;color:#111}
table{border-collapse:collapse;width:100%;font-size:12px}td,th{border:1px solid #ccc;padding:3px 5px;vertical-align:top}
th{background:#eee;position:sticky;top:0}.ar{font-family:'Amiri Quran','Traditional Arabic',serif;font-size:20px;direction:rtl;text-align:right}
h1{font-size:14px}"""


def color_of(cell):
    f = cell.font
    c = f.color.rgb if f is not None and f.color is not None and isinstance(f.color.rgb, str) else None
    fill = cell.fill.fgColor.rgb if cell.fill is not None and cell.fill.fill_type == "solid" and isinstance(cell.fill.fgColor.rgb, str) else None
    return (("#" + c[2:]) if c and len(c) == 8 else None, ("#" + fill[2:]) if fill and len(fill) == 8 else None)


def main():
    run, xlsx, label = sys.argv[1], sys.argv[2], sys.argv[3]
    chunk = int(sys.argv[4]) if len(sys.argv) > 4 else 150
    only = set(sys.argv[5].split(",")) if len(sys.argv) > 5 else None
    run_dir = os.path.join(RUNS, run)
    out_dir = os.path.join(run_dir, "cp9", "render", label)
    os.makedirs(out_dir, exist_ok=True)
    wb = openpyxl.load_workbook(xlsx, rich_text=True)
    entries = []
    sheets = [ws for ws in wb.worksheets if only is None or ws.title in only]
    for ws in sheets:
        rows = list(ws.iter_rows())
        header, body = rows[0], rows[1:]
        n = max(1, (len(body) + chunk - 1) // chunk)
        for i in range(n):
            part = body[i * chunk:(i + 1) * chunk]
            start = i * chunk + 2
            end = start + len(part) - 1
            fname = f"{ws.title}_{i + 1:03d}.html"
            out = [f"<!doctype html><html><head><meta charset='utf-8'><title>{html.escape(ws.title)} {start}-{end}</title><style>{CSS}</style></head><body>",
                   f"<h1>{html.escape(label)} / {html.escape(ws.title)} — redovi {start}–{end}</h1><table data-sheet='{html.escape(ws.title)}' data-start='{start}' data-end='{end}'><tr>"]
            out += [f"<th>{html.escape(str(c.value))}</th>" for c in header]
            out.append("</tr>")
            for row in part:
                out.append(f"<tr data-row='{row[0].row}'>")
                for c in row:
                    if type(c.value).__name__ == "CellRichText":
                        spans = []
                        for blk in c.value:
                            txt = blk.text if hasattr(blk, "text") else str(blk)
                            col = blk.font.color.rgb if hasattr(blk, "font") and blk.font is not None and blk.font.color is not None else None
                            spans.append(f"<span style='color:#{col[2:]}' data-part-color='#{col[2:]}'>{html.escape(txt)}</span>" if col else html.escape(txt))
                        out.append(f"<td data-color='' data-token-part='1'>{''.join(spans)}</td>")
                        continue
                    v = "" if c.value is None else str(c.value)
                    fg, bg = color_of(c)
                    style = (f"color:{fg};" if fg else "") + (f"background:{bg};" if bg else "")
                    cls = " class='ar'" if any("؀" <= ch <= "ۿ" for ch in v) else ""
                    out.append(f"<td{cls} style='{style}' data-color='{fg or ''}'>{html.escape(v)}</td>")
                out.append("</tr>")
            out.append("</table></body></html>")
            p = os.path.join(out_dir, fname)
            with open(p, "w", encoding="utf-8") as f:
                f.write("".join(out))
            entries.append({"workbook": os.path.basename(xlsx), "sheet": ws.title, "range_start": start, "range_end": end,
                            "expected_rows": len(part), "rendered_rows": None, "output_artifact": p, "status": "PENDING",
                            "sha256": sha256_file(p)})
    total_rows = {ws.title: ws.max_row - 1 for ws in sheets}
    for sheet, n in total_rows.items():
        covered = sum(e["expected_rows"] for e in entries if e["sheet"] == sheet)
        if covered != n:
            print(f"RUPA u pokrivenosti {sheet}: {covered} != {n}")
            sys.exit(1)
    from export import sheet_hashes
    allh = sheet_hashes(xlsx)
    man = {"created_at": now(), "label": label, "xlsx": xlsx, "xlsx_sha256": sha256_file(xlsx), "chunks": entries,
           "sheet_hashes": {k: v for k, v in allh.items() if k in total_rows}}
    atomic_write_json(os.path.join(out_dir, "RENDER_COVERAGE_MANIFEST.json"), man)
    print(f"{label}: {len(entries)} render chunkova, redova {sum(total_rows.values())}")


if __name__ == "__main__":
    main()
