# -*- coding: utf-8 -*-
"""Upisuje rezultat browser provjere render chunkova u cp9/RENDER_VERIFIED.json.

Upotreba: uv run scripts/v131/render_verify.py <RUN> <label> <results.json>
results.json: lista {"file": "VIZUELNA_001.html", "rows": N, "colored": K} (izmjereno u browseru)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, load_json, now, sha256_file  # noqa: E402

run, label, res_path = sys.argv[1], sys.argv[2], sys.argv[3]
run_dir = os.path.join(RUNS, run)
mpath = os.path.join(run_dir, "cp9", "render", label, "RENDER_COVERAGE_MANIFEST.json")
man = load_json(mpath)
measured = {r["file"]: r for r in load_json(res_path)}
ok_chunks = 0
rows = 0
for c in man["chunks"]:
    f = os.path.basename(c["output_artifact"])
    m = measured.get(f)
    c["rendered_rows"] = m["rows"] if m else None
    c["colored_cells_rendered"] = m.get("colored") if m else None
    c["status"] = "PASS" if m and m["rows"] == c["expected_rows"] and sha256_file(c["output_artifact"]) == c["sha256"] else "FAIL"
    ok_chunks += c["status"] == "PASS"
    rows += c["rendered_rows"] or 0
man["verified_at"] = now()
mh = atomic_write_json(mpath, man)
vpath = os.path.join(run_dir, "cp9", "RENDER_VERIFIED.json")
v = load_json(vpath) if os.path.exists(vpath) else {"workbooks": {}}
v["workbooks"][label] = {"status": "PASS" if ok_chunks == len(man["chunks"]) else "FAIL", "chunks_expected": len(man["chunks"]),
                         "chunks_verified": ok_chunks, "rows_verified": rows, "manifest_sha256": mh, "xlsx_sha256": man["xlsx_sha256"],
                         "sheet_hashes": man["sheet_hashes"], "verified_at": now()}
atomic_write_json(vpath, v)
print(f"{label}: {ok_chunks}/{len(man['chunks'])} chunkova PASS, {rows} redova")
