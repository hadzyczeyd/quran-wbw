# -*- coding: utf-8 -*-
"""
CP5/CP6/CP7 revizije (FIRST / SECOND / THIRD) nad CONSENSUS_MASTER-om.

  packets <RUN> <PHASE>          -> <phase_dir>/packets/Bxxx.json (trenutno stanje mastera po batchu,
                                     za SECOND/THIRD samo redovi koji traže semantički recheck)
  check <RUN> <PHASE> <Bxxx>      -> validira <phase_dir>/Bxxx.json + mikro-checkpoint
  apply <RUN> <PHASE>             -> primjenjuje ispravke u novi CONSENSUS_MASTER + Change_impact,
                                     deterministički popunjava ostale redove (SECOND/THIRD)

Format izlaza revizije (po batchu):
{"batch_id": "B001", "phase": "FIRST", "ayahs": [{"ayah_id": 1,
   "translation_completeness": "PASS", "completeness_note": "...",
   "segments": [{"id": "S..-S01", "status": "PASS|FAIL", "note": "...",
                 "correction": null | {"kind": "LINK|UNEXPRESSED", "targets": [["S..-B001", null]],
                                        "semantic_role": "...", "evidence_type": "...",
                                        "bosnian_target_phrase": "...", "note": "..."}}],
   "tokens": [{"id": "S..-B001", "status": "PASS|FAIL", "note": "..."}],
   "links":  [{"id": "S..-S01>S..-B001", "status": "PASS|FAIL", "note": "..."}]}]}
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, UNEXPRESSED, INSERTED, atomic_write_json, canonical_json, load_json, now, sha256_bytes, sha256_file  # noqa: E402
from derive import CONTENT_TAGS, derive  # noqa: E402

PHASE_DIR = {"FIRST": "cp5_first", "SECOND": "cp6_second", "THIRD": "cp7_third"}
RISKY_SEG_STATUSES = {"MAPPED_ONE_TO_MANY", "MAPPED_BY_SEGMENT", "MAPPED_BY_TOKEN_PART", "MAPPED_FUSED_MULTI_SEGMENT", UNEXPRESSED}
RISKY_TAGS = {"REL", "NEG", "PRO", "PRON"}


def current_master(run_dir):
    path = os.path.join(run_dir, "cp4", "CONSENSUS_MASTER.json")
    return load_json(path), path


def risk_set(run_dir, snap, master, der):
    """Redovi koji u SECOND/THIRD obavezno dobijaju semantički recheck (nalog 14, 15, 16)."""
    cmp_ = load_json(os.path.join(run_dir, "cp4", "ENTRY_COMPARE.json"))
    mism = {r["stable_id"] for r in cmp_["rows"] if r["compare_status"] != "MATCH"}
    changed = set()
    for ph in ("FIRST", "SECOND"):
        ci = os.path.join(run_dir, PHASE_DIR[ph], "CHANGE_IMPACT.json")
        if os.path.exists(ci):
            for c in load_json(ci)["changes"]:
                changed.update(c["affected_records"])
    segs = set()
    for s in der["segments"]:
        if (s["mapping_status"] in RISKY_SEG_STATUSES or s["tag"] in RISKY_TAGS
                or s["qac_segment_id"] in mism or s["qac_segment_id"] in changed):
            segs.add(s["qac_segment_id"])
    toks = set()
    for t in der["tokens"]:
        if (t["mapping_status"] in (INSERTED, "MAPPED_ONE_TO_MANY", "MAPPED_BY_SEGMENT", "MAPPED_FUSED_MULTI_SEGMENT", "MAPPED_BY_TOKEN_PART")
                or t["bosnian_token_id"] in mism or t["bosnian_token_id"] in changed
                or any(x in segs for x in t["linked_qac_segment_ids"].split(";") if x)):
            toks.add(t["bosnian_token_id"])
    return segs, toks, mism, changed


def packets(run_dir, phase):
    snap = load_json(os.path.join(run_dir, "cp1", "CP1_SOURCE_SNAPSHOT.json"))
    inv = load_json(os.path.join(run_dir, "cp1", "INVENTORY_BATCH_PLAN.json"))
    master, _ = current_master(run_dir)
    der = derive(snap, master)
    rs, rt, ch = (None, None, set())
    prev_links = set()
    if phase != "FIRST":
        rs, rt, _, ch = risk_set(run_dir, snap, master, der)
    if phase == "THIRD":
        # THIRD pokriva sve što je SECOND semantički provjerio (i kad korekcija SECOND promijeni skup rizičnih redova)
        p = os.path.join(run_dir, PHASE_DIR["SECOND"], "RESULTS.json")
        if os.path.exists(p):
            prev = load_json(p)
            rs |= set(prev["segments"]) & {s["qac_segment_id"] for s in der["segments"]}
            rt |= set(prev["tokens"]) & {t["bosnian_token_id"] for t in der["tokens"]}
            prev_links = set(prev["links"])
    total = {"segments": 0, "tokens": 0, "links": 0}
    for b in inv["batches"]:
        inp = load_json(os.path.join(run_dir, "cp1", "batch_inputs", f"{b['batch_id']}.json"))
        out = {"batch_id": b["batch_id"], "phase": phase, "master_hash": master["master_hash"], "ayahs": []}
        for a in inp["ayahs"]:
            aid = a["ayah_id"]
            seg = [s for s in der["segments"] if s["ayah"] == aid and (rs is None or s["qac_segment_id"] in rs)]
            tok = [t for t in der["tokens"] if t["ayah_id"] == aid and (rt is None or t["bosnian_token_id"] in rt)]
            # Veza ide u recheck i kad je korekcija zahvatila samo njen bosanski token.
            lnk = [l for l in der["links"] if l["ayah_id"] == aid
                   and (rs is None or l["qac_segment_id"] in rs or l["bosnian_token_id"] in ch
                        or f"{l['qac_segment_id']}>{l['bosnian_token_id']}" in prev_links)]
            out["ayahs"].append({
                "ayah_id": aid, "arabic_ayah_uthmani": a["arabic_ayah_uthmani"], "mehanovic_text": a["mehanovic_text"],
                "all_words": a["words"], "all_bosnian_tokens": a["bosnian_tokens"],
                "review_segments": [{"id": s["qac_segment_id"], "arabic_segment": s["arabic_segment"], "tag": s["tag"],
                                     "features": s["features"], "pronoun_type": s["pronoun_type"],
                                     "mapping_status": s["mapping_status"], "linked_bosnian_token_ids": s["linked_bosnian_token_ids"],
                                     # tačni ciljevi s poddijelovima tokena [token_id, [start,end] ili null]
                                     "targets": (master["links"].get(s["qac_segment_id"]) or {}).get("targets", []),
                                     "mapping_note": s["mapping_note"]} for s in seg],
                "review_tokens": [{"id": t["bosnian_token_id"], "token": t["bosnian_original_token"], "mapping_status": t["mapping_status"],
                                   "linked_qac_segment_ids": t["linked_qac_segment_ids"], "mapping_note": t["mapping_note"]} for t in tok],
                "review_links": [{"id": f"{l['qac_segment_id']}>{l['bosnian_token_id']}", "qac_tag": l["qac_tag"],
                                  "mapping_status": l["mapping_status"]} for l in lnk],
            })
            total["segments"] += len(seg)
            total["tokens"] += len(tok)
            total["links"] += len(lnk)
        atomic_write_json(os.path.join(run_dir, PHASE_DIR[phase], "packets", f"{b['batch_id']}.json"), out)
    print(f"{phase} paketi: {len(inv['batches'])} batch-eva, za semantički pregled {total}")


def check(run_dir, phase, batch):
    pk = load_json(os.path.join(run_dir, PHASE_DIR[phase], "packets", f"{batch}.json"))
    out_path = os.path.join(run_dir, PHASE_DIR[phase], f"{batch}.json")
    out = load_json(out_path)
    errs = []
    oa = {a["ayah_id"]: a for a in out.get("ayahs", [])}
    for a in pk["ayahs"]:
        r = oa.get(a["ayah_id"])
        if r is None:
            errs.append(f"ajet {a['ayah_id']} nedostaje")
            continue
        if phase == "FIRST" and r.get("translation_completeness") not in ("PASS", "FAIL"):
            errs.append(f"ajet {a['ayah_id']}: translation_completeness")
        for kind, key in (("segments", "review_segments"), ("tokens", "review_tokens"), ("links", "review_links")):
            want = {x["id"] for x in a[key]}
            got = {x.get("id"): x for x in r.get(kind, [])}
            if set(got) != want:
                errs.append(f"ajet {a['ayah_id']} {kind}: nedostaje {sorted(want - set(got))[:5]} višak {sorted(set(got) - want)[:5]}")
            for x in got.values():
                if x.get("status") not in ("PASS", "FAIL"):
                    errs.append(f"{x.get('id')}: status")
                if len(str(x.get("note") or "")) < 12:
                    errs.append(f"{x.get('id')}: note mora biti konkretna")
                if kind == "segments" and x.get("status") == "FAIL" and not x.get("correction"):
                    errs.append(f"{x.get('id')}: FAIL bez correction")
    if errs:
        print(f"FAIL {batch}: {len(errs)}")
        for e in errs[:50]:
            print("  -", e)
        sys.exit(1)
    h = sha256_file(out_path)
    man_path = os.path.join(run_dir, PHASE_DIR[phase], "REVIEW_MANIFEST.json")
    man = load_json(man_path) if os.path.exists(man_path) else {"phase": phase, "batches": {}, "chain": []}
    parent = man["chain"][-1]["sha256"] if man["chain"] else None
    man["batches"][batch] = {"sha256": h, "validated_at": now(), "parent": parent}
    man["chain"].append({"batch": batch, "sha256": h, "parent": parent, "at": now()})
    atomic_write_json(man_path, man)
    print(f"PASS {phase} {batch} sha256={h[:16]}…")


def apply(run_dir, phase):
    inv = load_json(os.path.join(run_dir, "cp1", "INVENTORY_BATCH_PLAN.json"))
    master, mpath = current_master(run_dir)
    before_hash = master["master_hash"]
    changes = []
    results = {"segments": {}, "tokens": {}, "links": {}, "completeness": {}}
    for b in inv["batches"]:
        out = load_json(os.path.join(run_dir, PHASE_DIR[phase], f"{b['batch_id']}.json"))
        for a in out["ayahs"]:
            if "translation_completeness" in a:
                results["completeness"][str(a["ayah_id"])] = {"status": a["translation_completeness"], "note": a.get("completeness_note", "")}
            for kind in ("segments", "tokens", "links"):
                for x in a.get(kind, []):
                    results[kind][x["id"]] = {"status": x["status"], "note": x["note"], "basis": "SEMANTIC_RECHECK" if phase != "FIRST" else "FIRST_SEMANTIC_AUDIT"}
            for x in a.get("segments", []):
                c = x.get("correction")
                if x["status"] == "FAIL" and c:
                    old = master["links"][x["id"]]
                    new = {"kind": c["kind"], "targets": c.get("targets", []), "semantic_role": c.get("semantic_role"),
                           "evidence_type": c.get("evidence_type"), "bosnian_target_phrase": c.get("bosnian_target_phrase"),
                           "note": c["note"], "resolution": f"CORRECTED_IN_{phase}"}
                    affected = {x["id"]} | {t[0] for t in old.get("targets", [])} | {t[0] for t in new["targets"]}
                    master["links"][x["id"]] = new
                    changes.append({"change_id": f"CI-{phase}-{len(changes) + 1:03d}", "phase": phase,
                                    "description": f"{x['id']}: {x['note']}", "affected_records": sorted(affected),
                                    "before": old, "after": new, "invalidated_statuses": "FIRST/SECOND/THIRD za pogođene redove",
                                    "status": "APPLIED"})
    # tokeni koji su nakon ispravki ostali bez veze postaju inserted (uz obrazloženje iz revizije)
    snap = load_json(os.path.join(run_dir, "cp1", "CP1_SOURCE_SNAPSHOT.json"))
    linked = {t[0] for l in master["links"].values() if l["kind"] == "LINK" for t in l["targets"]}
    for t in snap["tokens"]:
        tid = t["bosnian_token_id"]
        if tid in linked:
            master["inserted"].pop(tid, None)
        elif tid not in master["inserted"]:
            master["inserted"][tid] = results["tokens"].get(tid, {}).get("note") or f"nakon {phase} korekcije token ne prenosi QAC segment"
    master["master_hash"] = sha256_bytes(canonical_json({"links": master["links"], "inserted": master["inserted"]}).encode("utf-8"))
    master["history"] = master.get("history", []) + [{"phase": phase, "before": before_hash, "after": master["master_hash"], "changes": len(changes), "at": now()}]
    atomic_write_json(mpath, master)
    atomic_write_json(os.path.join(run_dir, PHASE_DIR[phase], "CHANGE_IMPACT.json"), {"phase": phase, "changes": changes})
    atomic_write_json(os.path.join(run_dir, PHASE_DIR[phase], "RESULTS.json"), results)
    fails = sum(1 for k in ("segments", "tokens", "links") for v in results[k].values() if v["status"] == "FAIL")
    print(f"{phase} apply: {len(changes)} ispravki, FAIL redova {fails}, master {before_hash[:12]} -> {master['master_hash'][:12]}")


if __name__ == "__main__":
    cmd, run = sys.argv[1], sys.argv[2]
    run_dir = os.path.join(RUNS, run)
    if cmd == "packets":
        packets(run_dir, sys.argv[3])
    elif cmd == "check":
        check(run_dir, sys.argv[3], sys.argv[4])
    elif cmd == "apply":
        apply(run_dir, sys.argv[3])
