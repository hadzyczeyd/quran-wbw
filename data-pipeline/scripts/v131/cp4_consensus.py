# -*- coding: utf-8 -*-
"""
CP4: deterministički compare Entry 1 / Entry 2 po stabilnim ID-ovima + CONSENSUS_MASTER.

Upotreba:
  uv run scripts/v131/cp4_consensus.py <RUN> compare      -> cp4/ENTRY_COMPARE.json (mismatch lista)
  uv run scripts/v131/cp4_consensus.py <RUN> build        -> cp4/CONSENSUS_MASTER.json
      (traži cp4/RESOLUTIONS.json za svaki mismatch; razrješenje se donosi ponovnim čitanjem snapshota)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, canonical_json, load_json, now, sha256_bytes  # noqa: E402


def load_entry(run_dir, entry_dir, batches):
    out = {}
    for b in batches:
        d = load_json(os.path.join(run_dir, entry_dir, f"{b}.json"))
        for a in d["ayahs"]:
            for l in a.get("segment_links", []):
                out[l["qac_segment_id"]] = {
                    "kind": "LINK",
                    "targets": sorted((t["bosnian_token_id"], tuple(t["part"]) if t.get("part") else None) for t in l["targets"]),
                    "semantic_role": l.get("semantic_role"), "evidence_type": l.get("evidence_type"),
                    "bosnian_target_phrase": l.get("bosnian_target_phrase"), "note": l.get("note"),
                }
            for u in a.get("unexpressed_segments", []):
                out[u["qac_segment_id"]] = {"kind": "UNEXPRESSED", "targets": [], "note": u.get("reason")}
            for r in a.get("review_required", []):
                out.setdefault(("REVIEW", r["id"]), {"kind": "REVIEW", "note": r.get("reason")})
                if r["id"].count("-") == 3:
                    out[r["id"]] = {"kind": "REVIEW", "targets": [], "note": r.get("reason")}
            for it in a.get("inserted_tokens", []):
                out[("INSERTED", it["bosnian_token_id"])] = {"kind": "INSERTED", "note": it.get("reason")}
    return out


def compare(run_dir):
    inv = load_json(os.path.join(run_dir, "cp1", "INVENTORY_BATCH_PLAN.json"))
    snap = load_json(os.path.join(run_dir, "cp1", "CP1_SOURCE_SNAPSHOT.json"))
    batches = [b["batch_id"] for b in inv["batches"]]
    e1 = load_entry(run_dir, "entry_1", batches)
    e2 = load_entry(run_dir, "entry_2", batches)
    rows = []
    for s in snap["segments"]:
        sid = s["qac_segment_id"]
        a, b = e1.get(sid), e2.get(sid)
        fields = []
        if a is None or b is None:
            fields.append("missing_in_" + ("entry_1" if a is None else "entry_2"))
        else:
            if a["kind"] != b["kind"]:
                fields.append("mapping_kind")
            if a.get("targets") != b.get("targets"):
                fields.append("linked_bosnian_token_ids")
        rows.append({
            "entity_type": "SEGMENT", "stable_id": sid, "ayah_id": s["ayah"],
            "compare_status": "MATCH" if not fields else "INDEPENDENT_ENTRY_MISMATCH",
            "mismatch_fields": ";".join(fields),
            "entry_1": {k: (list(map(list, v)) if k == "targets" and v else v) for k, v in (a or {}).items()},
            "entry_2": {k: (list(map(list, v)) if k == "targets" and v else v) for k, v in (b or {}).items()},
        })
    for t in snap["tokens"]:
        tid = t["bosnian_token_id"]
        i1 = ("INSERTED", tid) in e1
        i2 = ("INSERTED", tid) in e2
        rows.append({
            "entity_type": "TOKEN", "stable_id": tid, "ayah_id": t["ayah_id"],
            "compare_status": "MATCH" if i1 == i2 else "INDEPENDENT_ENTRY_MISMATCH",
            "mismatch_fields": "" if i1 == i2 else "inserted_status",
            "entry_1": {"inserted": i1, "note": e1.get(("INSERTED", tid), {}).get("note")},
            "entry_2": {"inserted": i2, "note": e2.get(("INSERTED", tid), {}).get("note")},
        })
    mism = [r for r in rows if r["compare_status"] != "MATCH"]
    result = {"created_at": now(), "rows": rows, "mismatch_count": len(mism),
              "segment_mismatch_count": sum(1 for r in mism if r["entity_type"] == "SEGMENT"),
              "token_mismatch_count": sum(1 for r in mism if r["entity_type"] == "TOKEN")}
    h = atomic_write_json(os.path.join(run_dir, "cp4", "ENTRY_COMPARE.json"), result)
    print(f"compare: {len(rows)} redova, mismatch {len(mism)} (segmenti {result['segment_mismatch_count']}, tokeni {result['token_mismatch_count']}) sha={h[:16]}")


def build(run_dir):
    snap = load_json(os.path.join(run_dir, "cp1", "CP1_SOURCE_SNAPSHOT.json"))
    cmp_ = load_json(os.path.join(run_dir, "cp4", "ENTRY_COMPARE.json"))
    res_path = os.path.join(run_dir, "cp4", "RESOLUTIONS.json")
    resolutions = load_json(res_path) if os.path.exists(res_path) else {}
    seg_rows = {r["stable_id"]: r for r in cmp_["rows"] if r["entity_type"] == "SEGMENT"}
    unresolved = []
    links = {}
    for s in snap["segments"]:
        sid = s["qac_segment_id"]
        r = seg_rows[sid]
        if r["compare_status"] == "MATCH":
            e = r["entry_1"]
            links[sid] = {"kind": e["kind"], "targets": [[t[0], t[1]] for t in e.get("targets") or []],
                          "semantic_role": e.get("semantic_role"), "evidence_type": e.get("evidence_type"),
                          "bosnian_target_phrase": e.get("bosnian_target_phrase"),
                          "note": e.get("note"), "resolution": "CONSENSUS_ACCEPTED"}
        elif sid in resolutions:
            rr = resolutions[sid]
            links[sid] = {"kind": rr["kind"], "targets": rr.get("targets", []),
                          "semantic_role": rr.get("semantic_role"), "evidence_type": rr.get("evidence_type"),
                          "bosnian_target_phrase": rr.get("bosnian_target_phrase"),
                          "note": rr["note"], "resolution": "RESOLVED_FROM_SOURCE: " + rr["basis"]}
        else:
            unresolved.append(sid)
    tok_rows = {r["stable_id"]: r for r in cmp_["rows"] if r["entity_type"] == "TOKEN"}
    inserted_notes = {}
    for t in snap["tokens"]:
        tid = t["bosnian_token_id"]
        r = tok_rows[tid]
        if r["compare_status"] == "MATCH":
            if r["entry_1"]["inserted"]:
                inserted_notes[tid] = r["entry_1"]["note"]
        elif tid in resolutions:
            if resolutions[tid].get("inserted"):
                inserted_notes[tid] = resolutions[tid]["note"]
        else:
            unresolved.append(tid)
    if unresolved:
        print(f"BLOCK: {len(unresolved)} nerazriješenih mismatcha, npr. {unresolved[:10]}")
        sys.exit(1)
    master = {"created_at": now(), "links": links, "inserted": inserted_notes}
    master["master_hash"] = sha256_bytes(canonical_json({"links": links, "inserted": inserted_notes}).encode("utf-8"))
    h = atomic_write_json(os.path.join(run_dir, "cp4", "CONSENSUS_MASTER.json"), master)
    print(f"CONSENSUS_MASTER: {len(links)} segmenata, {len(inserted_notes)} inserted, master_hash={master['master_hash'][:16]} file={h[:16]}")


if __name__ == "__main__":
    run_dir = os.path.join(RUNS, sys.argv[1])
    {"compare": compare, "build": build}[sys.argv[2]](run_dir)
