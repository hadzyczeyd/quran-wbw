# -*- coding: utf-8 -*-
"""
CP4 razrješenja Entry 1 / Entry 2 neslaganja za suru 40 — svako ponovnim čitanjem
source snapshota (QAC segment + puni Mehanovićev ajet). Tokeni se razrješavaju
deterministički iz konačnih veza segmenata.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, load_json  # noqa: E402

RUN = "S040_Gafir"
P_NARROW = "46.2 najuži dokazivi ekvivalent sadržajnog segmenta; Mehanovićeve objašnjavajuće dopune ostaju inserted"
P_GOV = "GOVERNED_PHRASE: bosanski prijedlog koji kodira padež/ulogu arapske imenice (ACC/GEN) pripada toj imenici, ne glagolu"
P_AUX = "pomoćni glagol pripada glagolskom obliku koji gramatički gradi"
P_NEG = "55.8: 'ne' uz glagol straha / u 'ne bih li' nije QAC NEG; pojačivač 'nimalo' prati stvarnu QAC negaciju"
P_FUNC = "57:12 / 46.2: funkcija segmenta dokazivo izražena postojećim tokenom"
P_UNEXP = "46.3 / 55.9: segment stvarno nije zasebno izražen; veza se ne izmišlja"

# sid -> (izbor, osnov)  izbor: "E1" | "E2" | dict(custom: targets + polja)
D = {
    "S040-A003-W005-S01": ("E2", P_NARROW + ": šadīd → 'žestoko'; 'Onoga Koji' su bosanska dopuna bez REL segmenta"),
    "S040-A003-W007-S01": ("E2", P_NARROW + ": ḏū → 'Posjednik'; 'Koji je' bez arapskog segmenta"),
    "S040-A003-W010-S01": ("E2", P_NARROW + ": ilāh → 'Boga'; 'istinskog' je interpretativna dopuna"),
    "S040-A004-W009-S02": ("E1", "QAC NEG lā (zabrana) → 'ne'; 'neka' pripada jusivu glagola"),
    "S040-A004-W010-S01": ("E1", "jusiv yaḡrur (MOOD:JUS) → 'neka obmanjuje': 'neka' nosi jusivni način glagola"),
    "S040-A008-W002-S02": ("E2", P_GOV),
    "S040-A008-W003-S01": ("E2", P_GOV + ": 'u vrtove' (ACC cilja uz adḫil)"),
    "S040-A010-W012-S01": ("E1", "tud'awna → 'pozivani' (umetnuta apozicija); 'ste,' gramatički pripada 'ste ... ostali'"),
    "S040-A010-W015-S02": ("E1", P_AUX + ": 'ste, ... ostali nevjernici' = takfurūna"),
    "S040-A012-W009-S01": ("E2", P_NARROW + ": yušrak → 'bi ... pridružen bio!'; 'neko drugi u obožavanju' je dopuna"),
    "S040-A012-W013-S01": ("E1", "li- (pripadnost) → 'pripada'; 'jedino' je Mehanovićevo naglašavanje bez zasebnog segmenta"),
    "S040-A013-W014-S01": ("E2", P_NARROW + ": yunību → 'se ... obraća.'; 'Njemu' nema arapski segment (implicitni cilj)"),
    "S040-A014-W007-S01": ("E2", P_NARROW + ": kariha → 'bilo mrsko!'; 'to' je implicitni objekat bez segmenta"),
    "S040-A015-W014-S02": ("E2", P_GOV),
    "S040-A015-W015-S01": ("E2", P_GOV + ": 'na Dan' (objekat upozorenja)"),
    "S040-A017-W007-S01": ("E1", "QAC NEG lā (nafiya li-l-jins) → 'neće'; 'biti' je egzistencijalna kopula bez segmenta"),
    "S040-A018-W001-S02": ("E2", P_GOV),
    "S040-A018-W002-S01": ("E2", P_GOV + ": 'na dan,'"),
    "S040-A018-W008-S01": ("E2", P_NARROW + ": kāẓimīn → 'popriječiti se,'; 'i' bez arapskog wa"),
    "S040-A019-W002-S01": ("E2", P_NARROW + ": ḫā'ina → 'kriomice u ono što je zabranjeno'; 'koji' pripada relativnoj 'poglede koji gledaju'"),
    "S040-A019-W003-S02": ("E2", "a'yun → 'poglede koji ... gledaju,' (opisni izraz čina očiju)"),
    "S040-A021-W018-S02": ("E2", P_NARROW + ": āṯār → 'tragova'; 'su ... ostavili' bez arapskog glagola"),
    "S040-A022-W006-S01": ("E1", "bi- uz atā = donijeti → 'donosili;'; 'koje' je bosanski relativ bez REL segmenta"),
    "S040-A022-W010-S02": ("E2", "-hu u innahu je subjekat oba predikata; Mehanović ga ponavlja s 'On ... On' (jedan referent)"),
    "S040-A022-W012-S01": ("E2", P_NARROW + ": šadīd → 'žestoko'; 'On' pripada -hu"),
    "S040-A026-W010-S01": ("E2", P_NEG + ": an uz aḫāfu → bosanski komplementizer straha 'da ... ne'"),
    "S040-A026-W011-S01": ("E2", "yubaddila → 'on ... izmijeni'; 'ne' je dio komplementizera straha, ne glagola"),
    "S040-A026-W014-S01": ("E2", P_NEG + ": drugo an → 'da ... ne'"),
    "S040-A026-W015-S01": ("E2", "yuẓhira → 'izazove.\"'; 'ne' pripada komplementizeru straha"),
    "S040-A028-W028-S01": ("E2", P_NARROW + ": yuṣib → 'će ... stići'; 'onda' bez arapskog fa"),
    "S040-A029-W005-S01": ("E2", P_NARROW + ": ẓāhirīn (ḥāl) → 'nadmoćni'; 'i' i 'ste' bez arapskog segmenta"),
    "S040-A030-W009-S01": ({"targets_from": "E1", "drop": ["su", "kažnjene"]},
                           "yawm → 'dana kada': 'kada' uvodi vremensku odredbu dana (genitivna veza yawmi l-aḥzāb, oba unosa ga vežu); 'su kažnjene' je interpretativna dopuna"),
    "S040-A030-W010-S02": ("E1", "PHRASE_CONTEXT 57:12: al-aḥzāb (saveznici) → 'skupine koje su se protiv poslanika bile urotile,' — Mehanović opisno prenosi značenje 'udruženih skupina'"),
    "S040-A031-W002-S01": ("E2", "da'b → 'je to bilo'; 's' pripada narodu (GOVERNED_PHRASE)"),
    "S040-A031-W003-S01": ("E2", P_GOV + ": 's narodom,'"),
    "S040-A032-W005-S01": ("E2", P_GOV + ": 'na Dan'"),
    "S040-A032-W006-S02": ("E2", "genitiv yawma t-tanād → relativna 'kada jedni druge budete dozivali,' ('kada' kodira genitivnu vezu)"),
    "S040-A033-W009-S01": ("E2", P_NARROW + ": 'āṣim → 'niko ... zaštititi.'; 'moći' bez arapskog segmenta"),
    "S040-A034-W004-S01": ("E2", "min (početna tačka) → 'još'; segmentno precizno, bez fused kolapsa 'još davno'"),
    "S040-A034-W005-S01": ("E2", "qablu → 'davno,'"),
    "S040-A034-W014-S01": ("E2", P_UNEXP + ": ḥattā (sve dok) nije izražen; 'A' je bosanski diskursni veznik"),
    "S040-A035-W008-S01": ("E1", "atā → 'došao.'; 'nije' je već dokazano vezan za ḡayr (W006-S02) u oba unosa"),
    "S040-A036-W007-S01": ("E1", "la'alla → 'ne ... li' (partikula nade); 'bih' gradi kondicional glagola"),
    "S040-A036-W008-S01": ({"targets_from": "E1", "drop": ["do"]}, P_AUX + " ('bih stigao'); 'do' pripada asbāb (GOVERNED_PHRASE)"),
    "S040-A036-W009-S02": ("E2", P_GOV + ": 'do staza,'"),
    "S040-A037-W003-S01": ("E1", "fa (uzročno) → 'ne ... li' (ponovljena konstrukcija nade), dosljedno 40:36"),
    "S040-A037-W003-S02": ("E1", P_AUX + ": 'bih se popeo'"),
    "S040-A037-W017-S01": ("E2", "al- (poznati put) → 'Pravog': određenost 'onog puta' Mehanović izražava pridjevom"),
    "S040-A037-W017-S02": ("E2", "sabīl → 'puta,' (najuži sadržajni ekvivalent)"),
    "S040-A037-W023-S01": ("E2", P_NARROW + ": tabāb → 'štetu.'; 'se završilo ... njegovu' je preoblika bez zasebnih segmenata"),
    "S040-A040-W018-S01": ("E2", P_GOV),
    "S040-A040-W019-S02": ("E2", P_GOV + ": 'u Džennet'"),
    "S040-A042-W002-S01": ("E2", "li- (svrha) upravlja oba glagola; Mehanović ga izražava s 'da' ispred svakog"),
    "S040-A042-W004-S02": ("E2", P_NARROW + ": ušrika → 'pridružujem'; 'u obožavanju' je dopuna; 'da' pripada li-"),
    "S040-A043-W001-S01": ("E2", P_NEG + ": lā jarama → 'Nema nimalo'"),
    "S040-A043-W002-S01": ("E2", "jaram → 'sumnje'; 'nimalo' prati negaciju"),
    "S040-A043-W006-S01": ("E2", "laysa (negirani predikat) → 'neće ... ni' (prvi član korelativne negacije u njegovom dosegu)"),
    "S040-A043-W011-S02": ("E2", "drugo lā → drugo 'ni'"),
    "S040-A045-W001-S02": ("E2", P_GOV),
    "S040-A045-W003-S01": ("E2", P_GOV + ": 'od zala'"),
    "S040-A046-W009-S01": ("E2", P_GOV),
    "S040-A046-W012-S01": ("E2", P_GOV + ": 'u ... najtežu!\"'"),
    "S040-A056-W009-S01": ("E1", "atā → 'došao,'; 'nije' je vezan za ḡayr (W007-S02) u oba unosa"),
    "S040-A056-W017-S02": ("E2", P_NARROW + ": bāliḡ → 'dovesti do'; 'koja' bez REL segmenta"),
    "S040-A059-W002-S01": ("E2", "al- → 'sudnji,': određenost 'onog (poznatog) Časa' Mehanović izražava pridjevom"),
    "S040-A059-W002-S02": ("E2", "sā'a → 'Čas' (najuži sadržajni ekvivalent)"),
    "S040-A060-W011-S02": ("E2", P_GOV),
    "S040-A060-W012-S01": ("E2", P_GOV + ": 'u Džehennem'"),
    "S040-A061-W012-S01": ("E2", P_UNEXP + ": naglasno la- nije izraženo; 'neizmjerno' nosi tanwīn veličine imenice faḍl"),
    "S040-A061-W013-S01": ("E2", "faḍlin (tanwīn veličine) → 'neizmjerno darežljiv'"),
    "S040-A062-W008-S01": ("E2", P_NARROW + ": ilāh → 'boga'; 'drugog' je interpretativna dopuna"),
    "S040-A067-W016-S02": ("E2", P_GOV),
    "S040-A067-W017-S01": ("E2", P_GOV + ": 'do muževnog doba'"),
    "S040-A067-W026-S03": ("E2", P_GOV),
    "S040-A067-W027-S01": ("E2", P_GOV + ": 'do ... roka'"),
    "S040-A067-W029-S02": ("E2", "la'alla → 'da'; lice nosi -kum"),
    "S040-A067-W029-S03": ("E2", "-kum (2MP) → 'biste' (lični oblik kondicionala nosi 2. lice množine)"),
    "S040-A070-W006-S02": ("E2", P_UNEXP + ": povratna zamjenica -hi nema bosanski ekvivalent; 'što' nosi mā"),
    "S040-A071-W006-S01": ("E2", P_NARROW + ": yusḥabūna → 'vučeni'; 'a' bez arapskog wa"),
    "S040-A075-W008-S02": ("E2", P_NARROW + ": al-ḥaqq → 'osnova'; 'ikakva' je pojačivač bez segmenta"),
    "S040-A075-W010-S01": ("E1", "drugi kuntum → zajednički pomoćni 'ste' oba koordinirana predikata ('ste se ... veselili i [ste] drski bili')"),
    "S040-A076-W001-S01": ("E2", P_GOV),
    "S040-A076-W002-S01": ("E2", P_GOV + ": 'kroz kapije'"),
    "S040-A077-W012-S01": ("E2", P_NARROW + ": natawaffayanna → 'život oduzmemo'; 'prije' je interpretativna dopuna"),
    "S040-A078-W007-S01": ("E2", "man (REL) → 'o nekima': 'nekima' nosi referent, 'o' njegovu ulogu"),
    "S040-A078-W008-S01": ("E2", "qaṣaṣnā → 'kazivali smo'"),
    "S040-A078-W011-S01": ("E2", "drugo man → 'o nekima'"),
    "S040-A078-W013-S01": ("E2", "naqṣuṣ → 'nismo.' (elidirani glagol u pomoćnom obliku)"),
    "S040-A078-W016-S01": ("E2", "kāna → 'nije' (kopula u 'mā kāna li-')"),
    "S040-A078-W017-S01": ("E2", P_FUNC + ": li- (pravo/mogućnost) → 'mogao'"),
    "S040-A080-W003-S01": ("E2", P_NARROW + ": manāfi' → 'koristi'; 'i drugih' je dopuna"),
    "S040-A080-W004-S02": ("E1", "li- (svrha) → bosanski namjerni veznik 'da bi'"),
    "S040-A080-W004-S03": ("E1", "tabluḡū → 'ispunili;' ('bi' pripada namjernom vezniku 'da bi')"),
    "S040-A080-W007-S01": ("E2", "fī → 'u'; 'koju ... imate' je relativna preoblika"),
    "S040-A081-W003-S02": ("E2", "ayya → 'koje'"),
    "S040-A081-W004-S01": ("E2", P_GOV + ": partitivni genitiv 'od ... znakova'"),
    "S040-A082-W017-S02": ("E2", P_NARROW + ": āṯār → 'tragova'; dosljedno 40:21"),
    "S040-A083-W008-S01": ("E2", P_UNEXP + ": objasnidbeno min nije izraženo; 'znanjem' nosi 'ilm"),
    "S040-A083-W011-S01": ("E2", P_UNEXP + ": bi uz ḥāqa nije izražen; 'ih' nosi -him"),
    "S040-A084-W004-S01": ("E2", P_NARROW + ": qālū → 'bi govorili:'; 'onda' bez arapskog fa"),
    "S040-A084-W012-S01": ("E2", P_NARROW + ": mušrikīn → 'pridruživali!\"'; 'u obožavanju' je dopuna"),
    "S040-A085-W001-S02": ("E2", P_NEG + ": lam → 'ne ... nimalo'"),
    "S040-A085-W003-S01": ("E2", "yanfa'u → 'koristilo.'"),
    "S040-A085-W008-S01": ("E2", P_GOV + ": sunnata (akuzativ načina) → 'prema ... zakonu'; 'To je' je dopuna"),
    "S040-A085-W014-S01": ("E2", P_NARROW + ": 'ibād → 'robove'; 'sve' je dopuna"),
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
