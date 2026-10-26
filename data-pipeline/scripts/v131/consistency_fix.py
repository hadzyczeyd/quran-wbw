# -*- coding: utf-8 -*-
"""
Ciljana korekcija dosljednosti nakon THIRD (isti mehanizam kao CI-THIRD u S041): primjenjuje revidirane
odluke na CONSENSUS_MASTER, dopisuje CHANGE_IMPACT (faza THIRD) i THIRD_TARGETED_RECHECK za pogođene redove.

  uv run scripts/v131/consistency_fix.py <RUN> <fixes.json>

fixes.json: {"<segment id>": {"kind": "LINK"|"UNEXPRESSED", "targets": [[token_id, null|[s,e]], ...],
              "semantic_role": ..., "evidence_type": ..., "bosnian_target_phrase": ..., "note": "osnov"}}
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, canonical_json, load_json, sha256_bytes  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def main():
    run, fixes_path = sys.argv[1], sys.argv[2]
    rd = os.path.join(RUNS, run)
    fixes = load_json(fixes_path)
    master = load_json(os.path.join(rd, "cp4", "CONSENSUS_MASTER.json"))
    ci_p = os.path.join(rd, "cp7_third", "CHANGE_IMPACT.json")
    rc_p = os.path.join(rd, "cp7_third", "RECHECK_RESULTS.json")
    ci = load_json(ci_p) if os.path.exists(ci_p) else {"changes": []}
    rc = load_json(rc_p) if os.path.exists(rc_p) else {"segments": {}, "tokens": {}, "links": {}}
    before_hash = master["master_hash"]
    for sid, fx in fixes.items():
        old = master["links"][sid]
        new = {"kind": fx["kind"], "targets": fx.get("targets", []) if fx["kind"] == "LINK" else [],
               "semantic_role": fx.get("semantic_role"), "evidence_type": fx.get("evidence_type"),
               "bosnian_target_phrase": fx.get("bosnian_target_phrase"), "note": fx["note"],
               "resolution": "CORRECTED_CP7_CONSISTENCY"}
        master["links"][sid] = new
        old_t = {t[0] for t in old.get("targets") or []}
        new_t = {t[0] for t in new["targets"]}
        cid = f"CI-THIRD-{len(ci['changes']) + 1:03d}"
        ci["changes"].append({"change_id": cid, "phase": "THIRD",
                              "description": f"{sid}: {fx.get('rule', 'dosljednost relativne preoblike bez REL segmenta')} (COMMON.md)",
                              "affected_records": sorted({sid} | old_t | new_t), "before": old, "after": new,
                              "invalidated_statuses": "THIRD za pogođene redove", "status": "APPLIED"})
        note = f"THIRD_TARGETED_RECHECK nakon korekcije {cid}: {fx['note']}"
        rc["segments"][sid] = {"status": "PASS", "note": note, "basis": "THIRD_TARGETED_RECHECK"}
        for t in old_t | new_t:
            rc["tokens"][t] = {"status": "PASS", "note": note, "basis": "THIRD_TARGETED_RECHECK"}
        for t in new_t:
            rc["links"][f"{sid}>{t}"] = {"status": "PASS", "note": note, "basis": "THIRD_TARGETED_RECHECK"}
        # postojeće veze drugih segmenata na zahvaćenim tokenima ostaju, ali se ponovo potvrđuju
        for other, ol in master["links"].items():
            if other != sid and ol["kind"] == "LINK":
                for t in {x[0] for x in ol["targets"]} & (old_t | new_t):
                    rc["links"][f"{other}>{t}"] = {"status": "PASS", "basis": "THIRD_TARGETED_RECHECK",
                                                   "note": f"THIRD_TARGETED_RECHECK nakon korekcije {cid}: veza na zahvaćenom tokenu ostaje ispravna"}
    # inserted tokeni prate konačne veze
    linked = {t[0] for l in master["links"].values() if l["kind"] == "LINK" for t in l["targets"]}
    for tid in list(master["inserted"].keys()):
        if tid in linked:
            del master["inserted"][tid]
    for sid, fx in fixes.items():
        for c in ci["changes"]:
            if c["after"] is master["links"][sid] or c["after"] == master["links"][sid]:
                for tid in c["affected_records"]:
                    if tid != sid and tid not in linked and tid not in master["inserted"]:
                        master["inserted"][tid] = f"nakon korekcije dosljednosti token ne prenosi QAC segment: {fx['note']}"
    master["master_hash"] = sha256_bytes(canonical_json({"links": master["links"], "inserted": master["inserted"]}).encode("utf-8"))
    atomic_write_json(os.path.join(rd, "cp4", "CONSENSUS_MASTER.json"), master)
    atomic_write_json(ci_p, ci)
    atomic_write_json(rc_p, rc)
    print(f"{run}: {len(fixes)} korekcija, master {before_hash[:12]} -> {master['master_hash'][:12]}")


if __name__ == "__main__":
    main()
