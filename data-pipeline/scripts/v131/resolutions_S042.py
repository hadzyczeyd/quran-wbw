# -*- coding: utf-8 -*-
"""
CP4 razrješenja Entry 1 / Entry 2 neslaganja za suru 42 — svako ponovnim čitanjem
source snapshota (QAC segment + puni Mehanovićev ajet). Tokeni se razrješavaju
deterministički iz konačnih veza segmenata.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, load_json  # noqa: E402

RUN = "S042_Es-Sura"
P_NARROW = "46.2 najuži dokazivi ekvivalent sadržajnog segmenta; Mehanovićeve objašnjavajuće dopune ostaju inserted"
P_GOV = "GOVERNED_PHRASE: bosanski prijedlog koji kodira padež/ulogu arapske imenice (ACC/GEN) pripada toj imenici, ne glagolu"
P_AUX = "pomoćni glagol pripada glagolskom obliku koji gramatički gradi"
P_NEG = "55.8: 'ne' uz glagol straha / u 'ne bih li' nije QAC NEG; pojačivač 'nimalo' prati stvarnu QAC negaciju"
P_FUNC = "57:12 / 46.2: funkcija segmenta dokazivo izražena postojećim tokenom"
P_UNEXP = "46.3 / 55.9: segment stvarno nije zasebno izražen; veza se ne izmišlja"

# sid -> (izbor, osnov)
P_ZAR = "am → upitna konstrukcija 'Zar ... da' (bosanska retorička nevjerica); glagol na najuži token"
P_RES = P_UNEXP + ": povratna zamjenica (dosljedno 40:70, 41:14)"
P_COP = "kopula 'je/si' bez arapskog segmenta ostaje inserted"
D = {
    "S042-A003-W001-S02": ("E2", "ḏālika → 'Eto,'; 'tako' nosi ka- (bez dupliranja)"),
    "S042-A007-W001-S03": ("E2", "ḏālika → 'Eto,'; 'tako' nosi ka-"),
    "S042-A009-W001-S01": ("E2", P_ZAR),
    "S042-A009-W002-S01": ("E2", P_ZAR),
    "S042-A010-W005-S01": ("E1", P_FUNC + ": min šay'in (bilo šta) → generalizirajuće 'god'"),
    "S042-A010-W009-S01": ("E1", "ḏālikum → 'To vam ... eto,' (deiksa)"),
    "S042-A013-W032-S02": ("E2", "-hi (za Sebe) → 'Svoju'; 'vjeru' je dopuna"),
    "S042-A015-W032-S01": ("E2", P_UNEXP + ": bayna uz 'sabrati nas'; 'sve' je dopuna"),
    "S042-A015-W034-S02": ("E2", "maṣīr → 'konačno odredište.' (dosljedno 40:3)"),
    "S042-A016-W008-S01": ("E2", P_NARROW + ": ustujība → 'je prihvaćen'; 'poziv' eksplicira subjekat"),
    "S042-A020-W007-S02": ("E2", P_UNEXP + ": -hu u lahu; 'njegov' nosi -hi u ḥarṯihi"),
    "S042-A021-W001-S01": ("E2", P_ZAR),
    "S042-A021-W002-S01": ("E2", "la- (posjedovanje) → 'imaju'; 'da' pripada am"),
    "S042-A021-W020-S02": ("E1", P_RES),
    "S042-A022-W014-S01": ("E1", P_NARROW + ": rawḍāt → 'baščama,'; 'divnim' je dopuna"),
    "S042-A023-W015-S01": ("E2", "illā → 'osim'; 'što' je bosanski komplementizer"),
    "S042-A023-W017-S01": ("E2", P_UNEXP + ": fī l-qurbā preoblikovano u pridjev 'rodbinsku'"),
    "S042-A023-W028-S01": ("E2", P_NARROW + ": ġafūr → 'oprašta'; 'Onaj Koji' je dopuna (dosljedno 40:3)"),
    "S042-A024-W001-S01": ("E2", P_ZAR),
    "S042-A024-W002-S01": ("E2", P_ZAR),
    "S042-A026-W010-S02": ("E1", P_RES),
    "S042-A029-W016-S01": ("E1", P_COP + ": qadīr → 'kadar'"),
    "S042-A035-W001-S01": ("E1", P_UNEXP + ": wa nije izražen; rečenicu uvodi namjerno 'da bi'"),
    "S042-A035-W001-S02": ("E1", "ya'lama (subjunktiv namjere) → 'da bi znali'"),
    "S042-A035-W005-S01": ("E1", "āyāt → Mehanovićev dublet 'ajetima i znakovima' (dosljedno ostalim ajetima)"),
    "S042-A039-W003-S02": ("E1", P_FUNC + ": objekt -hum postaje subjekat pasiva; 3. lice mn. nosi 'budu'"),
    "S042-A044-W018-S01": ("E2", P_NARROW + ": maradd → 'budemo vraćeni?\"'; 'opet' je dopuna"),
    "S042-A045-W008-S01": ("E1", P_UNEXP + ": min uz ṭarf; način nosi 'kradimice'"),
    "S042-A047-W004-S01": ("E2", "qabl → 'prije'; 'nego što' nosi an"),
    "S042-A047-W005-S01": ("E2", "an → 'nego što' (qabla an = prije nego što)"),
    "S042-A047-W014-S01": ("E2", "la- (posjedovanje) → 'imati'"),
    "S042-A047-W019-S01": ("E2", "la- (posjedovanje) → 'moći'"),
    "S042-A048-W008-S01": ("E1", P_COP + ": 'alayka → 'dužan'"),
    "S042-A050-W010-S01": ("E2", P_NARROW + ": 'alīm → 'sve zna'; 'Onaj Koji' je dopuna"),
    "S042-A052-W001-S02": ("E2", "ka- (isto tako) → 'Tako ... i' (i = 'također')"),
    "S042-A053-W011-S01": ("E2", "alā (INC) → 'eto,'; 'I,' bez arapskog wa"),
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
