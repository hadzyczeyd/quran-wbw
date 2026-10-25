# -*- coding: utf-8 -*-
"""Ulaz za ciljanu reviziju dosljednosti: runs/<RUN>/cp7_third/CONSISTENCY_INPUT.json (trenutno stanje mastera po ajetu)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, load_json  # noqa: E402
from derive import derive  # noqa: E402

run = sys.argv[1]
rd = os.path.join(RUNS, run)
snap = load_json(os.path.join(rd, "cp1", "CP1_SOURCE_SNAPSHOT.json"))
master = load_json(os.path.join(rd, "cp4", "CONSENSUS_MASTER.json"))
der = derive(snap, master)
tok = {t["bosnian_token_id"]: t for t in der["tokens"]}
out = []
for a in sorted({s["ayah"] for s in der["segments"]}):
    out.append({
        "ayah": a,
        "arabic": snap["uthmani"][str(a)]["ayah_text"] if "uthmani" in snap else None,
        "mehanovic": snap["mehanovic"][str(a)]["text"],
        "tokens": [{"id": t["bosnian_token_id"], "text": t["bosnian_original_token"], "status": t["mapping_status"]}
                   for t in der["tokens"] if t["ayah_id"] == a],
        "segments": [{"id": s["qac_segment_id"], "arabic": s["arabic_segment"], "tag": s["tag"], "features": s["features"],
                      "kind": master["links"][s["qac_segment_id"]]["kind"],
                      "targets": master["links"][s["qac_segment_id"]].get("targets", []),
                      "target_text": [tok[t[0]]["bosnian_original_token"] for t in master["links"][s["qac_segment_id"]].get("targets", [])],
                      "note": master["links"][s["qac_segment_id"]].get("note")}
                     for s in der["segments"] if s["ayah"] == a],
    })
atomic_write_json(os.path.join(rd, "cp7_third", "CONSISTENCY_INPUT.json"), out)
print(run, len(out), "ajeta")
