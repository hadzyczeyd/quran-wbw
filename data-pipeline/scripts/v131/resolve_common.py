# -*- coding: utf-8 -*-
"""Zajednički CP4 resolver: primjenjuje odluke (E1/E2/custom) na neslaganja i deterministički razrješava tokene."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, load_json  # noqa: E402

P_NARROW = "46.2 najuži dokazivi ekvivalent sadržajnog segmenta; Mehanovićeve objašnjavajuće dopune ostaju inserted"
P_GOV = "GOVERNED_PHRASE: bosanski prijedlog koji kodira padež/ulogu arapske imenice (ACC/GEN) pripada toj imenici, ne glagolu"
P_AUX = "pomoćni glagol pripada glagolskom obliku koji gramatički gradi"
P_FUNC = "57:12 / 46.2: funkcija segmenta dokazivo izražena postojećim tokenom"
P_UNEXP = "46.3 / 55.9: segment stvarno nije zasebno izražen; veza se ne izmišlja"


def run(RUN, D):
    run_dir = os.path.join(RUNS, RUN)
    cmp_ = load_json(os.path.join(run_dir, "cp4", "ENTRY_COMPARE.json"))
    snap = load_json(os.path.join(run_dir, "cp1", "CP1_SOURCE_SNAPSHOT.json"))
    tok_text = {t["bosnian_token_id"]: t["bosnian_original_token"] for t in snap["tokens"]}
    rows = {r["stable_id"]: r for r in cmp_["rows"]}
    seg_mism = [r["stable_id"] for r in cmp_["rows"] if r["entity_type"] == "SEGMENT" and r["compare_status"] != "MATCH"]
    missing = [s for s in seg_mism if s not in D]
    extra = [s for s in D if s not in seg_mism]
    if missing or extra:
        print("nedostaju odluke:", missing, "višak:", extra)
        sys.exit(1)
    res = {}
    for sid, (choice, basis) in D.items():
        r = rows[sid]
        if isinstance(choice, dict):
            e = r["entry_1" if choice["targets_from"] == "E1" else "entry_2"]
            targets = [t for t in e["targets"] if tok_text[t[0]] not in choice.get("drop", [])]
            ayah_toks = [t["bosnian_token_id"] for t in snap["tokens"] if t["bosnian_token_id"][:9] == sid[:9]]
            for word in choice.get("add", []):
                targets.append([next(x for x in ayah_toks if tok_text[x] == word), None])
            res[sid] = {"kind": "LINK", "targets": targets, "semantic_role": e.get("semantic_role"),
                        "evidence_type": e.get("evidence_type"),
                        "bosnian_target_phrase": " ".join(tok_text[t[0]] for t in targets),
                        "note": basis, "basis": basis}
        else:
            e = r["entry_1" if choice == "E1" else "entry_2"]
            res[sid] = {"kind": e["kind"], "targets": e.get("targets") or [], "semantic_role": e.get("semantic_role"),
                        "evidence_type": e.get("evidence_type"), "bosnian_target_phrase": e.get("bosnian_target_phrase"),
                        "note": e.get("note"), "basis": f"{choice}: {basis}"}
    # Konačne veze svih segmenata (MATCH iz Entry 1 + razrješenja) → status tokena.
    final_linked = set()
    for r in cmp_["rows"]:
        if r["entity_type"] != "SEGMENT":
            continue
        e = res.get(r["stable_id"]) if r["compare_status"] != "MATCH" else r["entry_1"]
        if e and e["kind"] == "LINK":
            final_linked.update(t[0] for t in e["targets"])
    for r in cmp_["rows"]:
        if r["entity_type"] != "TOKEN" or r["compare_status"] == "MATCH":
            continue
        tid = r["stable_id"]
        inserted = tid not in final_linked
        note = (r["entry_1"]["note"] if r["entry_1"]["inserted"] else r["entry_2"]["note"]) if inserted else ""
        res[tid] = {"inserted": inserted, "note": note or "token ne prenosi QAC segment nakon razrješenja",
                    "basis": "deterministički iz razriješenih veza segmenata"}
    # Konzistentnost: MATCH token koji je ostao bez veze ili inserted koji je dobio vezu.
    problems = []
    for r in cmp_["rows"]:
        if r["entity_type"] == "TOKEN" and r["compare_status"] == "MATCH":
            tid = r["stable_id"]
            if r["entry_1"]["inserted"] and tid in final_linked:
                problems.append(f"{tid} '{tok_text[tid]}' bio inserted u oba, sada vezan")
            if not r["entry_1"]["inserted"] and tid not in final_linked:
                problems.append(f"{tid} '{tok_text[tid]}' bio vezan u oba, sada bez veze")
    if problems:
        print("token konflikti:", problems)
        sys.exit(1)
    h = atomic_write_json(os.path.join(run_dir, "cp4", "RESOLUTIONS.json"), res)
    print(f"RESOLUTIONS: {sum(1 for k in res if k.count('-') == 3)} segmenata, {sum(1 for k in res if k.count('-') == 2)} tokena, sha={h[:16]}")

