# -*- coding: utf-8 -*-
"""CP9: reopen finalnih XLSX, potvrda hashova, upis FINAL_QA_PASS u RUN_MANIFEST. Upotreba: finalize.py <RUN>"""
import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, load_json, now, sha256_file  # noqa: E402

R = os.path.join(RUNS, sys.argv[1]) + "/"
res = load_json(R + "cp9/CP9_RESULT.json")
if not res["qa_ok"]:
    sys.exit("CP9 nije FINAL_QA_PASS")
finals = {}
for label, o in res["outputs"].items():
    wb = openpyxl.load_workbook(o["final"], read_only=True)
    n = len(wb.sheetnames)
    wb.close()
    h = sha256_file(o["final"])
    assert h == o["final_sha256"], f"hash {label}"
    finals[label] = {"path": o["final"], "sha256": h, "sheets": n}
m = load_json(R + "RUN_MANIFEST.json")
m["checkpoints"].append({"seq": len(m["checkpoints"]) + 1, "checkpoint": "CP9", "batch": None, "artifact_path": "cp9/CP9_RESULT.json",
                         "sha256": sha256_file(R + "cp9/CP9_RESULT.json"), "parent_checkpoint_hash": m["checkpoints"][-1]["sha256"],
                         "status": "FINAL_QA_PASS", "timestamp": now(),
                         "extra": {"final_outputs": finals, "render_verified": sha256_file(R + "cp9/RENDER_VERIFIED.json")}})
m.update({"current_checkpoint": "CP9", "run_status": "FINAL_QA_PASS", "delivery_status": "DELIVERED", "delivered_at": now(),
          "final_output_hashes": {k: v["sha256"] for k, v in finals.items()},
          "consensus_master_hash": load_json(R + "cp4/CONSENSUS_MASTER.json")["master_hash"]})
atomic_write_json(R + "RUN_MANIFEST.json", m)
print({k: (v["sheets"], v["sha256"][:16]) for k, v in finals.items()})
