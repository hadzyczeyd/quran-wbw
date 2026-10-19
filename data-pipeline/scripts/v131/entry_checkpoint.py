# -*- coding: utf-8 -*-
"""
Validator + mikro-checkpoint za jedan semantički batch Entry unosa (CP2/CP3).

Upotreba: uv run scripts/v131/entry_checkpoint.py <RUN_DIR_NAME> <entry_dir> <batch_id>
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, load_json, now, sha256_file  # noqa: E402

EVIDENCE = {"DIRECT_LEXICAL", "PHRASE_CONTEXT", "RELATIVE_CLAUSE_ROLE", "LEXICALIZED_NEGATION",
            "PRONOUN_CONTEXT", "GOVERNED_PHRASE", "IDIOMATIC_Mehanovic", "FUNCTION_CONTEXT"}
RISKY_TAGS = {"REL", "NEG", "PRON", "PRO"}


def validate(inp, out):
    errs = []
    if out.get("batch_id") != inp["batch_id"]:
        errs.append("batch_id se ne poklapa")
    in_ayahs = {a["ayah_id"]: a for a in inp["ayahs"]}
    out_ayahs = {a.get("ayah_id"): a for a in out.get("ayahs", [])}
    if set(in_ayahs) != set(out_ayahs):
        errs.append(f"ajeti: očekivano {sorted(in_ayahs)}, dobijeno {sorted(out_ayahs)}")
    for aid, ia in in_ayahs.items():
        oa = out_ayahs.get(aid)
        if oa is None:
            continue
        segs = {s["qac_segment_id"]: s for w in ia["words"] for s in w["segments"]}
        toks = {t["bosnian_token_id"]: t["token"] for t in ia["bosnian_tokens"]}
        seen = {}
        covered_tokens = set()
        parts = {}
        for link in oa.get("segment_links", []):
            sid = link.get("qac_segment_id")
            if sid not in segs:
                errs.append(f"{aid}: nepoznat segment {sid}")
                continue
            seen[sid] = seen.get(sid, 0) + 1
            targets = link.get("targets") or []
            if not targets:
                errs.append(f"{sid}: segment_link bez targeta (koristi unexpressed_segments)")
            for t in targets:
                tid = t.get("bosnian_token_id")
                if tid not in toks:
                    errs.append(f"{sid}: target {tid} nije token ajeta {aid}")
                    continue
                covered_tokens.add(tid)
                p = t.get("part")
                if p is not None:
                    if not (isinstance(p, list) and len(p) == 2 and 0 <= p[0] < p[1] <= len(toks[tid])):
                        errs.append(f"{sid}: neispravan part {p} za '{toks[tid]}'")
                    else:
                        parts.setdefault(tid, set()).add(tuple(p))
            if link.get("evidence_type") not in EVIDENCE:
                errs.append(f"{sid}: evidence_type '{link.get('evidence_type')}' nije dozvoljen")
            for k in ("semantic_role", "bosnian_target_phrase", "note"):
                if not str(link.get(k) or "").strip():
                    errs.append(f"{sid}: prazno polje {k}")
            if segs[sid]["tag"] in RISKY_TAGS and len(str(link.get("note") or "")) < 25:
                errs.append(f"{sid}: rizična veza ({segs[sid]['tag']}) traži konkretniju note (55.12)")
        for u in oa.get("unexpressed_segments", []):
            sid = u.get("qac_segment_id")
            if sid not in segs:
                errs.append(f"{aid}: nepoznat unexpressed segment {sid}")
                continue
            seen[sid] = seen.get(sid, 0) + 1
            if len(str(u.get("reason") or "")) < 20:
                errs.append(f"{sid}: unexpressed bez individualnog obrazloženja")
        review_ids = set()
        for r in oa.get("review_required", []):
            review_ids.add(r.get("id"))
            if r.get("id") in segs:
                seen[r["id"]] = seen.get(r["id"], 0) + 1
        for sid in segs:
            if seen.get(sid, 0) != 1:
                errs.append(f"{sid}: pojavljuje se {seen.get(sid, 0)} puta (mora tačno 1)")
        inserted = set()
        for it in oa.get("inserted_tokens", []):
            tid = it.get("bosnian_token_id")
            if tid not in toks:
                errs.append(f"{aid}: nepoznat inserted token {tid}")
            elif tid in covered_tokens:
                errs.append(f"{tid}: istovremeno inserted i target veze")
            elif len(str(it.get("reason") or "")) < 15:
                errs.append(f"{tid}: inserted bez obrazloženja")
            inserted.add(tid)
        for tid in toks:
            if tid not in covered_tokens and tid not in inserted and tid not in review_ids:
                errs.append(f"{tid} '{toks[tid]}': token nije pokriven (veza / inserted / review)")
        for tid, ps in parts.items():
            ranges = sorted(ps)
            pos = 0
            for a, b in ranges:
                if a != pos:
                    errs.append(f"{tid}: token-part rasponi {ranges} imaju prazninu/preklapanje")
                    break
                pos = b
            else:
                if pos != len(toks[tid]):
                    errs.append(f"{tid}: token-part rasponi {ranges} ne pokrivaju cijeli token")
    return errs


def main():
    run, entry_dir, batch = sys.argv[1], sys.argv[2], sys.argv[3]
    run_dir = os.path.join(RUNS, run)
    inp = load_json(os.path.join(run_dir, "cp1", "batch_inputs", f"{batch}.json"))
    out_path = os.path.join(run_dir, entry_dir, f"{batch}.json")
    out = load_json(out_path)
    errs = validate(inp, out)
    if errs:
        print(f"FAIL {batch}: {len(errs)} grešaka")
        for e in errs[:60]:
            print("  -", e)
        sys.exit(1)
    h = sha256_file(out_path)
    man_path = os.path.join(run_dir, entry_dir, "ENTRY_MANIFEST.json")
    man = load_json(man_path) if os.path.exists(man_path) else {"entry_dir": entry_dir, "batches": {}, "chain": []}
    parent = man["chain"][-1]["sha256"] if man["chain"] else None
    man["batches"][batch] = {"sha256": h, "validated_at": now(), "parent": parent}
    man["chain"].append({"batch": batch, "sha256": h, "parent": parent, "at": now()})
    atomic_write_json(man_path, man)
    print(f"PASS {batch} sha256={h[:16]}… ({len(man['batches'])} batch-eva validirano)")


if __name__ == "__main__":
    main()
