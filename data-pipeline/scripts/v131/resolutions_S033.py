# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 33."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_FUNC, P_NARROW, P_UNEXP, run  # noqa: E402

REP = "ponovljeni prijedlog/veznik ispred koordiniranog člana nosi isti segment (dosljedno 57:1 'na … na', 35:27, 34:31)"
REPN = "imenica dobija samo svoj token; ponovljeni prijedlog nosi isti prijedložni segment (dosljedno 57:1)"
PRP = "namjerni li- → samo 'da'; 'bi' ide uz glagol (COMMON)"
SUBJ = "subjektni sufiks → eksplicitna zamjenica; pomoćni glagol pripada glagolskom obliku (COMMON 55.9)"
COORD = "drugi koordinirani glagol dobija samo svoj token; zajednički pomoćni ostaje uz prvi, sufiks fused (COMMON)"
ELID = P_NARROW + ": objekat je u arapskom izostavljen kod ženskog participa; Mehanovićevo ponavljanje ostaje inserted"

D = {
    "S033-A005-W018-S01": ("E2", P_UNEXP + ": fī u fīmā; Mehanović mā prevodi uslovnim 'ako'"),
    "S033-A007-W007-S02": ("E2", REP),
    "S033-A007-W009-S02": ("E2", REPN),
    "S033-A007-W010-S02": ("E2", REPN),
    "S033-A007-W011-S02": ("E2", REPN),
    "S033-A008-W001-S01": ("E1", PRP),
    "S033-A009-W011-S03": ("E1", SUBJ),
    "S033-A013-W020-S01": ("E1", "samostalna zamjenica hiya → kopula '-su bile' (COMMON: PRON → kopula)"),
    "S033-A014-W008-S02": ("E1", "fitna → dublet 'smutnja - nevjerovanje,' (Mehanovićev dvostruki prijevod jedne riječi, kao 'ajeta i znakova')"),
    "S033-A015-W001-S03": ("E2", P_UNEXP + ": qad; 'još' je pojačivač uz 'prije' (inserted)"),
    "S033-A015-W002-S01": ("E2", P_AUX + ": kāna → 'bili su' (pluskvamperfekt)"),
    "S033-A015-W003-S02": ("E2", "subjektni sufiks → zajednički pomoćni 'su' (nema eksplicitne zamjenice)"),
    "S033-A015-W011-S01": ("E1", "ʿahd → 'za … datu obavezu' ('za' kodira padež, 'datu' je dio imeničkog izraza)"),
    "S033-A015-W012-S01": ("E1", "Allāh u iḍāfi → dativ 'Allahu'"),
    "S033-A017-W002-S01": ("E1", "man (man dhā alladhī) → '\"Ko'; drugo 'ko vam može nauditi' je Mehanovićevo proširenje (inserted)"),
    "S033-A017-W010-S01": ("UNEXP", P_UNEXP + ": bi- (arāda bi-); 'vas' je akuzativni objekat dodanog glagola 'snađe' (dosljedno 34:9, 34:46)"),
    "S033-A017-W014-S01": ("E1", "bi- bez bosanskog prijedloga → dativni oblik 'vam' (dosljedno 79:18); 'ukaže' inserted"),
    "S033-A020-W010-S01": ("E2", REP),
    "S033-A024-W001-S01": ("E1", PRP + "; 'zato' je Mehanovićev dodatak"),
    "S033-A028-W006-S02": ("E1", "subjektni sufiks bez zamjenice i pomoćnog → fused na finitni glagol 'želite' (kāna u in kuntunna fused, COMMON)"),
    "S033-A029-W002-S02": ("E1", "subjektni sufiks → fused na 'želite' (kao 33:28)"),
    "S033-A035-W020-S03": ("E2", ELID),
    "S033-A035-W024-S03": ("E2", ELID),
    "S033-A036-W002-S01": ("E2", P_UNEXP + ": kāna u mā kāna li- (preoblika); 'maju' nosi yakūna lahum"),
    "S033-A036-W003-S01": ("E2", P_UNEXP + ": li- (za vjernika); 'vjernik' je subjekat u nominativu"),
    "S033-A036-W016-S01": ("E2", P_NARROW + ": amr → 'nahođenju'; 'postupe' je Mehanovićev dodani glagol (inserted)"),
    "S033-A036-W021-S01": ("E1", P_UNEXP + ": fa apodoze; 'taj' je Mehanovićev korelativ"),
    "S033-A037-W007-S03": ("E1", SUBJ),
    "S033-A037-W031-S02": ("E1", SUBJ),
    "S033-A037-W044-S01": ("E1", "drugi waṭaran u idiomu fused na glagolski token 'razvedu.'"),
    "S033-A039-W005-S03": ("E2", COORD),
    "S033-A041-W005-S01": ("E1", "Allāh → 'Allaha' i anaforsko 'Ga,' (ponovljeni objekat, kao ponovljeni prijedlog)"),
    "S033-A041-W006-S01": ("E1", "apsolutni objekat dhikran → vlastiti izraz 'i spominjite'"),
    "S033-A042-W003-S01": ("E2", "korelativno 'i ujutro i navečer': oba 'i' nose wa (kao 'ni … ni', COMMON)"),
    "S033-A043-W006-S01": ("E1", PRP),
    "S033-A049-W011-S01": ("E2", "an + glagol nominalizovano u 'stupanja' (" + P_FUNC + ")"),
    "S033-A049-W015-S01": ("E1", "ʿalayhinna (obaveza) → '-su dužne' (kopula gradi predikat)"),
    "S033-A049-W015-S02": ("E1", "-hinna → 'one'"),
    "S033-A052-W011-S01": ("E1", "partitivni min → neodređeno 'neku'"),
    "S033-A052-W012-S01": ("E1", "azwāj → 'drugu'"),
    "S033-A052-W013-S01": ("E1", "dopusno wa-law: wa → 'i' (čak i), law → 'makar'"),
    "S033-A053-W033-S01": ("E1", P_UNEXP + ": min uz yastaḥyī; 'vam' je dativ dodanog glagola 'rekne'"),
    "S033-A053-W048-S01": ("E2", REP),
    "S033-A053-W049-S02": ("E2", "drugo qulūb dijeli zajedničku imenicu 'srca.'; ponovljeno 'za' nosi li-"),
    "S033-A054-W001-S01": ("E1", P_UNEXP + ": in (bilo da) izražen samo redom riječi 'iznosili vi … ili … krili'"),
    "S033-A055-W004-S01": ("E2", REP),
    "S033-A055-W019-S01": ("E2", REPN.replace("imenica", "relativ")),
    "S033-A057-W008-S01": ("E2", REP),
    "S033-A057-W010-S03": ("E2", REPN),
    "S033-A061-W001-S01": ("E1", "malʿūnīn je ḥāl → cijeli izraz 'prokleti neka su!' (pravilo za particip stanja)"),
    "S033-A061-W005-S03": ("E2", COORD),
    "S033-A070-W007-S01": ("E1", "apsolutni objekat qawlan sadīdan → vlastiti izraz 'istinu,' (COMMON)"),
    "S033-A071-W001-S01": ("E2", "yuṣliḥ (učiniti dobrim) → 'On će … dobra … nagraditi'; 'dobra' nosi korijen ṣlḥ"),
    "S033-A071-W003-S01": ("E2", "aʿmāl → 'za … djela'"),
    "S033-A072-W011-S03": ("E2", COORD),
    "S033-A072-W015-S01": ("E2", P_UNEXP + ": inna; 'on' nosi ime inna"),
    "S033-A072-W017-S01": ("E2", "intenzivni ẓalūm → 'baš zulum učinio' ('baš' izražava obrazac faʿūl); 'prema sebi' je objašnjenje (inserted)"),
    "S033-A073-W001-S01": ("E1", PRP),
    "S033-A073-W008-S01": ("E2", P_UNEXP + ": ponovljeno Allāh; zajednički subjekat 'Allah' ostaje uz prvi glagol"),
}

if __name__ == "__main__":
    run("S033_El-Ahzab", D)
