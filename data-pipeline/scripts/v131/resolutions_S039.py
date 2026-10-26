# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 39."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_NARROW, P_UNEXP, run  # noqa: E402

AUXP = "subjektni sufiks bez eksplicitne zamjenice nosi pomoćni glagol koji izražava lice (55.9; dosljedno 36:45, 45:12, 44:58)"
SHARED = "sufiks drugog koordiniranog glagola nosi zajednički pomoćni glagol (dosljedno 38:20, 38:51)"
BAYNA = "bayna bez bosanskog prijedloga: odnos nosi dativ kojim upravlja (fused; dosljedno 38:22, 40:48, 45:17)"
HUDA = "hidāya leksički znači 'uputiti na Pravi put'; izraz pripada glagolu kad nema zasebnog ṣirāṭ segmenta (dosljedno 40:28, 43:27, 45:23, 46:10)"
DIROBJ = "arapski prijedlog koji traži arapski glagol, a bosanski glagol uzima direktni objekat (akuzativ) → unexpressed (COMMON)"
CASE = "arapski prijedlog bez zasebnog bosanskog prijedloga: odnos nosi padežni oblik riječi kojom upravlja (fused)"
LAW = "law → samo 'kad'/'da' (dosljedno 36:66, 42:27, 49:7, 102:5); 'bi' pripada glagolskom obliku, 'samo' je pojačivač (inserted)"
LAWS = "law u značenju želje ('kad bi samo', 'da mi je samo') → 'kad/Da … samo': 'samo' izražava optativni smisao law (dosljedno u 39:26 i 39:58)"
SPADA = "kāna min 'spadati u': kāna → pomoćni 'sam/si', min → 'u … spadao' (dosljedno 42:43 'u spada')"
REL = "REL mā → stvarni bosanski relativni izraz 'onome … čemu' (dosljedno 42:23 'ono čime'); 'čemu' dijeli i resumptivni -hi"
NISI = "mā … anta bi-wakīl: NEG nosi cijelo 'nisi', anta 'ti' (dosljedno 42:6)"
HUM = "odvajajuća zamjenica hum → buduća kopula i isticanje 'će baš' (dosljedno 39:18, 49:7 'su baš', 80:42)"
DA = "'da' je umetnuti veznik dopune (nema arapskog an); glagol ide na svoj glagolski izraz"
NEGN = "negativni determinator 'nijedna' pripada svojoj imenici (dosljedno 36:54 'nikome' → nafs; COMMON negativna konkordancija)"
POSS = "lām posjedovanja → glagol posjedovanja ('namijenjene/čekaju/imali'), ne zaseban dativ (dosljedno 89:8, CP4 konvencija)"
RESUMP = "povratna zamjenica: ulogu nosi padežni oblik relativa ('Onoga/onoga/one') (COMMON, 89:8, 85:9)"

D = {
    "S039-A003-W013-S03": ("E1", AUXP),
    "S039-A003-W020-S01": ("E1", BAYNA),
    "S039-A003-W022-S01": ("E2", REL),
    "S039-A003-W029-S01": ("E2", HUDA),
    "S039-A006-W035-S01": ("E2", P_NARROW + ": fa = 'pa'; 'onda' je Mehanovićev dodatak (inserted)"),
    "S039-A007-W015-S02": ("E2", NEGN + "; NEG lā ostaje na 'ne' u 'neće'"),
    "S039-A007-W017-S01": ("E2", NEGN),
    "S039-A007-W023-S01": ("E2", P_AUX + " ('ćete se vratiti,')"),
    "S039-A008-W032-S01": ("E2", P_UNEXP + ": partitivni min nije izražen, jednina 'stanovnik' nosi aṣḥāb"),
    "S039-A009-W002-S01": ("E2", P_UNEXP + ": huwa nema tokena ni kopule; lice je samo u glagolu 'provodi' (COMMON 55.9 dozvoljava)"),
    "S039-A012-W002-S01": ("E2", "li-an → 'da': veznik nosi i namjerni lām i an (jedan token, dva segmenta)"),
    "S039-A017-W003-S02": ("E1", "dublet 'taguta - kumira' za jednu riječ uključuje unutrašnju crticu (COMMON dubleti)"),
    "S039-A017-W005-S03": ("E2", P_UNEXP + ": objektni -hā (tagut) nema vlastitog tokena; 'taguta' nosi aṭ-ṭāġūt"),
    "S039-A017-W009-S01": ("E1", POSS),
    "S039-A018-W008-S01": ("E2", HUDA),
    "S039-A019-W002-S01": ("E2", "ḥaqqa ʿalayhi 'postalo je obavezno za njega' → 'je zaslužio da se … obistine' (oba dijela su leksičko značenje ḥaqqa)"),
    "S039-A019-W007-S01": ("E2", "afa-anta tunqiḏu → modalni glagolski oblik 'možeš da izbaviš'; 'možeš' dijeli i anta"),
    "S039-A020-W005-S02": ("E2", RESUMP),
    "S039-A021-W018-S02": ("E2", P_UNEXP + ": posvojni -hu nema vlastitog dijela u 'raznobojno' (podjela samo na stvarnoj granici)"),
    "S039-A022-W012-S03": ("E2", "relativna preoblika participa: cijeli izraz 'onima čija su … tvrda' pripada qāsiya (COMMON)"),
    "S039-A026-W010-S01": ("E1", LAWS),
    "S039-A027-W010-S02": ("E1", AUXP + " — ime laʿalla"),
    "S039-A028-W003-S01": ("E1", "ġayr nosi negaciju 'nema' i konkordanciju 'nikakve' (nema vlastitog segmenta; COMMON)"),
    "S039-A028-W004-S01": ("E1", "ḏī 'koji ima' → relativni izraz posjedovanja 'u kome'"),
    "S039-A028-W006-S02": ("E1", AUXP + " — ime laʿalla"),
    "S039-A031-W007-S01": ("E2", P_AUX + " ('ćete se sporiti')"),
    "S039-A033-W007-S01": ("E1", P_UNEXP + ": hum nema kopule ni isticanja; 'oni' nosi ulāʾika"),
    "S039-A034-W001-S02": ("E1", AUXP + "; lām posjedovanja nosi 'naći će,'"),
    "S039-A035-W001-S01": ("E1", "ponovljeni 'da' istog li- (wa-yajziya pod istim lām) nosi taj li- (kao ponovljeni 'koji' istog REL)"),
    "S039-A035-W003-S01": ("E1", "kaffara ʿan → 'preći preko': 'preko' nosi ʿan"),
    "S039-A035-W004-S01": ("E1", "aswaʾ → 'ružnih'; 'preko' pripada ʿan"),
    "S039-A036-W013-S02": ("E2", RESUMP),
    "S039-A036-W015-S01": ("E2", HUDA),
    "S039-A037-W002-S01": ("E2", HUDA),
    "S039-A037-W005-S02": ("E2", RESUMP),
    "S039-A038-W017-S01": ("E2", "arāda → 'hoće da … učini,' (glagolski izraz namjere); 'je' nosi ḍurr"),
    "S039-A038-W019-S01": ("UNEXP", DIROBJ + ": bi- uz arāda; 'je' (štetu) je direktni objekat i nosi ḍurr"),
    "S039-A038-W025-S01": ("E2", "arāda → 'On hoće da … podari'; 'On' izražava lice glagola (COMMON); 'je' nosi raḥma"),
    "S039-A038-W026-S01": ("UNEXP", DIROBJ + ": bi- uz arāda; 'je' (milost) je direktni objekat i nosi raḥma"),
    "S039-A038-W028-S01": ("E1", AUXP + " — drugo hunna bez ponovljenog 'oni'"),
    "S039-A041-W014-S01": ("E2", "ʿalā (na štetu) → 'nauditi,' usporedo s li- → 'koristiti' u istom ajetu; 'sebi' nosi nafs/-hā"),
    "S039-A041-W015-S02": ("E2", NISI),
    "S039-A041-W016-S01": ("E2", NISI),
    "S039-A042-W009-S01": ("E1", "fī manām → glagol 'spavaju' (fused; dosljedno 38:8 fī šakk → 'sumnjaju')"),
    "S039-A042-W010-S02": ("E2", P_UNEXP + ": posvojni -hā nema tokena; lice je samo u fleksiji 'spavaju'"),
    "S039-A044-W011-S01": ("E2", P_AUX + " ('ćete se vratiti')"),
    "S039-A045-W004-S02": ("E2", P_UNEXP + ": -hu u waḥdahu nema tokena (dosljedno 40:12)"),
    "S039-A046-W011-S01": ("E1", BAYNA),
    "S039-A046-W014-S01": ("E2", REL),
    "S039-A047-W001-S02": ("E2", LAW),
    "S039-A047-W003-S01": ("E2", POSS + "; 'bi' pripada glagolskom obliku 'bi imali'"),
    "S039-A047-W011-S02": ("E2", "iftadaw bihi → perifraza 'bi … dali kako bi se … iskupili;' (otkupiti se davanjem)"),
    "S039-A047-W012-S01": ("E2", DIROBJ + " ('dali sve to')"),
    "S039-A048-W005-S01": ("E1", P_AUX + " ('su radili')"),
    "S039-A048-W005-S02": ("E1", AUXP + "; 'njihova' izražava vršioce kasabū (sayyiʾāt nema posvojnog sufiksa)"),
    "S039-A048-W007-S01": ("E2", DIROBJ + " ('skolit će ih')"),
    "S039-A051-W004-S01": ("E1", P_AUX + " ('su zaradili')"),
    "S039-A053-W004-S01": ("E2", P_AUX + " ('ste pretjerivali')"),
    "S039-A055-W006-S01": ("E1", P_UNEXP + ": u aktivnoj preoblici nominativ 'Gospodar' ne kodira min"),
    "S039-A055-W014-S01": ("E2", P_UNEXP + ": okolnosni wa- preoblikovan u relativni priključak 'za čiji (dolazak)', bez vlastitog tokena"),
    "S039-A056-W004-S01": ("E1", "uzvično yā bez dozivnog tokena → unexpressed (COMMON, layta/yā)"),
    "S039-A056-W006-S01": ("E2", "mā → uzvično 'koliko'; 'dužnosti' nosi janb"),
    "S039-A056-W009-S01": ("E2", "fī janbi Allāhi 'u pogledu Allahove strane' → 'dužnosti prema Allahu': janb = 'dužnosti', fī = 'prema'"),
    "S039-A056-W012-S01": ("E1", SPADA),
    "S039-A056-W013-S01": ("E1", "emfatičko (razlikovno) la- bez zasebnog tokena → unexpressed; 'doista' nosi in (COMMON)"),
    "S039-A056-W013-S02": ("E1", SPADA),
    "S039-A057-W006-S01": ("E2", HUDA),
    "S039-A058-W006-S01": ("E1", LAWS),
    "S039-A058-W007-S01": ("E1", P_UNEXP + ": anna u law anna nema tokena; optativ nosi law s 'samo'"),
    "S039-A058-W009-S01": ("E1", "karra → 'se vratiti-' (crtica ide uz prvi dio tokena, stvarna granica iza nje)"),
    "S039-A058-W011-S01": ("E1", "min → '-među' dio [8,12]"),
    "S039-A059-W005-S02": ("E2", P_AUX + " ('si poricao')"),
    "S039-A059-W008-S02": ("E1", SPADA),
    "S039-A059-W009-S01": ("E1", SPADA),
    "S039-A060-W005-S01": ("E2", P_AUX + " ('su laži govorili')"),
    "S039-A061-W004-S01": ("E2", P_AUX + " ('su … izvršavali … klonili')"),
    "S039-A062-W006-S01": ("E1", CASE + " — instrumental 'svim' (dosljedno 41:53, 85:9 'svemu')"),
    "S039-A063-W010-S01": ("E1", HUM),
    "S039-A064-W005-S01": ("E2", DA),
    "S039-A068-W022-S02": ({"targets_from": "E2", "drop": ["će,"], "add": ["S039-A068-B034"]},
                           "subjektni sufiks -ūna nosi eksplicitna zamjenica 'oni' (55.9; ista osoba kao hum)"),
    "S039-A069-W011-S01": ("E1", BAYNA),
    "S039-A069-W015-S02": ("E1", "subjektni sufiks -ūna nosi eksplicitni 'nikome' (isti referent kao hum; 55.9)"),
    "S039-A071-W013-S01": ("E2", DIROBJ + " ('upitati ih')"),
    "S039-A071-W023-S03": ("E1", SHARED),
    "S039-A073-W018-S01": ("E1", P_NARROW + ": 'od grijeha' je objašnjavajuća dopuna (inserted)"),
    "S039-A074-W009-S01": ("E2", DA),
    "S039-A075-W011-S01": ("E1", BAYNA),
}

if __name__ == "__main__":
    run("S039_Ez-Zumer", D)
