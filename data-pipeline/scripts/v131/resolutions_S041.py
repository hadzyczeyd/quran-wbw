# -*- coding: utf-8 -*-
"""
CP4 razrješenja Entry 1 / Entry 2 neslaganja za suru 41 — svako ponovnim čitanjem
source snapshota (QAC segment + puni Mehanovićev ajet). Tokeni se razrješavaju
deterministički iz konačnih veza segmenata.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, load_json  # noqa: E402

RUN = "S041_Fussilet"
P_NARROW = "46.2 najuži dokazivi ekvivalent sadržajnog segmenta; Mehanovićeve objašnjavajuće dopune ostaju inserted"
P_GOV = "GOVERNED_PHRASE: bosanski prijedlog koji kodira padež/ulogu arapske imenice (ACC/GEN) pripada toj imenici, ne glagolu"
P_AUX = "pomoćni glagol pripada glagolskom obliku koji gramatički gradi"
P_NEG = "55.8: 'ne' uz glagol straha / u 'ne bih li' nije QAC NEG; pojačivač 'nimalo' prati stvarnu QAC negaciju"
P_FUNC = "57:12 / 46.2: funkcija segmenta dokazivo izražena postojećim tokenom"
P_UNEXP = "46.3 / 55.9: segment stvarno nije zasebno izražen; veza se ne izmišlja"

# sid -> (izbor, osnov)
P_VERBP = "P uz glagol koji u bosanskom uzima direktni objekat nije zasebno izražen (dosljedno 40:83)"
P_MINQ = "min uz qabl/ba'd: 'prije'/'poslije' nosi imenicu; min nije zasebno izražen"
P_NEGV = "NEG ostaje na negaciji; glagol na najuži leksički token (bez fused kolapsa)"
D = {
    "S041-A005-W011-S02": ("E2", P_UNEXP + ": min u min bayni nije zasebno izražen"),
    "S041-A005-W013-S02": ("E2", P_UNEXP + ": ponovljeno bayni pokriveno koordinacijom 'nas i tebe' pod jednim 'između'"),
    "S041-A010-W005-S01": ("E2", P_UNEXP + ": fawq nije zasebno izražen; 'po njoj' je jedini lokativ"),
    "S041-A010-W005-S02": ("E2", P_UNEXP + ": -hā u fawqahā bez zasebnog tokena"),
    "S041-A010-W007-S02": ("E2", P_UNEXP + ": -hā u bāraka fīhā; 'blagoslovljenom' nosi glagol, ne zamjenicu"),
    "S041-A014-W007-S02": ("E2", P_UNEXP + ": drugo min pokriveno izrazom 'sa svih strana'"),
    "S041-A014-W011-S01": ("E1", "illā uz zabranu → restriktivni izraz 'nikoga osim' (dosljedno mā…illā → 'samo')"),
    "S041-A014-W022-S02": ("E1", P_UNEXP + ": povratna zamjenica -hi (dosljedno 40:70)"),
    "S041-A015-W013-S03": ("E1", "identične veze u oba unosa (lam → 'nisu')"),
    "S041-A015-W014-S01": ("E2", P_NEGV + ": yara → 'znali'"),
    "S041-A015-W024-S01": ("E2", P_VERBP),
    "S041-A016-W016-S01": ("E1", "aḫzā (elativ) → 'još više ponižavajuća': 'još' pojačava komparativ istog segmenta"),
    "S041-A016-W018-S01": ("E1", "identične veze u oba unosa"),
    "S041-A016-W019-S01": ("E2", P_NEGV + ": yunṣarūna → 'u pomoć priteći.'"),
    "S041-A019-W001-S02": ("E1", "yawma → 'na Dan kad': 'kad' uvodi rečenicu koja određuje dan (dosljedno 40:30)"),
    "S041-A021-W002-S01": ("E2", P_VERBP + " ('upitati kože')"),
    "S041-A022-W001-S02": ("E1", "identične veze u oba unosa"),
    "S041-A022-W002-S01": ("E1", "identične veze u oba unosa"),
    "S041-A022-W012-S01": ("E2", P_UNEXP + ": wa u walākin; suprotnost nosi lākin → 'već'"),
    "S041-A022-W016-S01": ("E1", "identične veze u oba unosa"),
    "S041-A022-W017-S01": ("E2", P_NEGV + ": ya'lamu → 'saznati'"),
    "S041-A025-W018-S01": ("E2", P_MINQ),
    "S041-A026-W006-S01": ("E2", P_VERBP + " ('slušati Kur'an')"),
    "S041-A026-W009-S02": ("E1", P_FUNC + ": -hi u fīhi (Kur'an) nosi 'ga' u 'nadvikali ga'"),
    "S041-A028-W013-S01": ("E2", P_VERBP),
    "S041-A030-W018-S01": ("E1", P_UNEXP + ": kuntum bez zasebnog ekvivalenta"),
    "S041-A030-W019-S01": ("E1", P_AUX + ": 'je obećan.\"'"),
    "S041-A033-W004-S02": ("E2", "REL man → 'onoga koji' i ponovljeni 'koji' uz koordinirane glagole iste relativne rečenice (55.6)"),
    "S041-A033-W008-S02": ("E2", "'amila → 'čini' (najuži; 'koji' pripada REL)"),
    "S041-A033-W010-S02": ("E2", "qāla → 'govori:' (najuži; 'koji' pripada REL)"),
    "S041-A034-W001-S02": ("E1", "identične veze u oba unosa"),
    "S041-A034-W002-S01": ("E2", P_NEGV + ": tastawī → 'isto!'"),
    "S041-A034-W007-S02": ("E1", P_UNEXP + ": allatī nije izražen; 'dobrim' nosi aḥsan"),
    "S041-A034-W011-S01": ("E2", "REL allaḏī + rečenica neprijateljstva preoblikovani u imenicu 'dušmanin' (dosljedno 40:7 'vjernicima')"),
    "S041-A034-W015-S02": ("E2", P_UNEXP + ": -hu u ka'annahu; referent je već 'dušmanin'"),
    "S041-A040-W004-S01": ("E2", P_VERBP + " ('izvrću ajete')"),
    "S041-A040-W006-S01": ("E1", "identične veze u oba unosa"),
    "S041-A040-W007-S01": ("E2", P_NEGV + ": yaḫfā → 'se sakriti.'"),
    "S041-A040-W024-S01": ("E2", P_VERBP + " ('vidi šta')"),
    "S041-A043-W004-S01": ("E1", "identične veze u oba unosa"),
    "S041-A043-W007-S01": ("E2", P_NEGV + ": qīla → 'rečeno'"),
    "S041-A043-W009-S01": ("E2", P_MINQ),
    "S041-A044-W024-S02": ("E1", P_FUNC + ": -him u 'alayhim → 3. lice mn. u 'slijepi su'"),
    "S041-A047-W001-S01": ("E1", P_FUNC + ": istaknuto ilayhi (isključivost) → 'Samo'"),
    "S041-A047-W007-S01": ("E2", "min istiḡrāqa u negaciji → 'ni' (ni plodovi)"),
    "S041-A047-W019-S02": ("E1", "yawma → 'na Dan kad' (dosljedno 41:19, 40:30)"),
    "S041-A047-W028-S01": ("E2", P_NARROW + ": šahīd → 'tvrdi.\"'; 'to' je dopuna"),
    "S041-A048-W006-S01": ("E2", P_MINQ),
    "S041-A050-W005-S01": ("E2", P_MINQ),
    "S041-A051-W011-S02": ("E2", "ḏū du'ā' → 'se moli.' ('se' je dio glagola moliti se)"),
    "S041-A052-W004-S01": ("E2", P_NARROW + ": kāna → 'je'; 'Kur'an' eksplicira implicitni subjekat"),
    "S041-A053-W003-S01": ("E2", P_GOV + ": fī → 'na'; 'u daljini' je dopuna"),
    "S041-A053-W004-S02": ("E2", P_NARROW + ": āfāq → 'obzorjima,'"),
    "S041-A053-W012-S03": ("E1", "identične veze u oba unosa"),
    "S041-A053-W013-S01": ("E2", P_NEGV + ": yakfi → 'dovoljno'"),
    "S041-A054-W003-S01": ("E1", P_UNEXP + ": fī miryatin preoblikovano u glagol 'sumnjaju'"),
    "S041-A054-W006-S01": ("E2", "liqā' → 'će ... stati,'; 'pred' pripada rabb (GOVERNED_PHRASE)"),
    "S041-A054-W007-S01": ("E2", P_GOV + ": 'pred Gospodara'"),
    "S041-A054-W010-S01": ("E2", P_VERBP + " ('obuhvata sve')"),
}


def main():
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
            targets = [t for t in e["targets"] if tok_text[t[0]] not in choice["drop"]]
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


if __name__ == "__main__":
    main()
