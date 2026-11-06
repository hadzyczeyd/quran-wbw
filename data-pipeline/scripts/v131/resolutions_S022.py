# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 22."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
PART = "partitivni min an-nāsi → genitiv 'ljudi'; egzistencijalno 'Ima' je Mehanovićev dodatak (dosljedno 30:29, 34:34)"
TAWK = "anna/huwa (naglasak) → 'što/je' + naglasno 'zaista/uistinu/doista' (kao inna → 'doista')"
MINDUN = "min dūni → fused 'pored' (COMMON: složeni prijedlog)"
LAN = "lan → 'ne-' u 'neće' [0,2]; 'će' gradi futur glagola (dosljedno 11:31, 17:15)"
LANV = "glagol nosi '-će' [2,4] iz 'neće' (pomoćni pripada glagolu koji gradi)"
REPP = "ponovljeni bosanski prijedlog ispred koordiniranog člana nosi isti arapski segment (COMMON: 'na na')"
DETS = "al- iscrpnosti (al-umūr) → 'sve' (COMMON 2026-11-05: DET istiġrāq)"
PARTN = "imenica/particip preveden glagolom: pomoćni nosi zamjenicu (hiya/-hum); imenica samo leksički dio (dosljedno 7:8, 11:23)"

D = {
    "S022-A003-W001-S02": ("E2", PART),
    "S022-A005-W050-S01": ("E1", "li- → 'tako' (posljedica)"),
    "S022-A005-W050-S02": ("E1", "kaylā → 'da,' (kay) + 'ne' (lā)"),
    "S022-A006-W002-S02": ("E2", TAWK),
    "S022-A008-W001-S02": ("E2", PART),
    "S022-A009-W007-S01": ("E1", "li- posjedovanja → glagol 'čeka' (dosljedno 7:113, 28:84 'dobit'); 'Njega' nosi -hu"),
    "S022-A011-W001-S02": ("E2", PART),
    "S022-A011-W023-S01": ("E2", TAWK),
    "S022-A012-W002-S01": ("E2", MINDUN),
    "S022-A012-W008-S02": ("E2", P_UNEXP + ": drugi relativni mā nije ponovljen (elipsa, COMMON)"),
    "S022-A012-W012-S01": ("E2", TAWK),
    "S022-A013-W006-S01": ("E1", "nafʿ → 'od koristi biti;' (paralelno ḍarr → 'će … nauditi')"),
    "S022-A013-W006-S02": ("E1", "resumptivni -hi → relativ 'što' (isti referent kao ḍarruhu, COMMON)"),
    "S022-A015-W005-S01": ("E1", LAN),
    "S022-A015-W006-S01": ("E1", LANV),
    "S022-A015-W008-S01": ("E2", REPP),
    "S022-A015-W010-S03": ("E2", "āḫira → 'ahiretu,'; ponovljeno 'na' nosi fī"),
    "S022-A018-W030-S01": ("E2", "li- kodiran akuzativom 'ga' (dosljedno 7:186)"),
    "S022-A018-W032-S01": ({"targets_from": "E2", "add": ["može"]}, "mukrim → 'niko … može poštovanim učiniti;' (konkordancija ide imenici, dosljedno 7:186)"),
    "S022-A019-W001-S01": ("E1", "hāḏāni → 'Ta'; dual 'dva' nosi imenica"),
    "S022-A019-W002-S01": ("E1", "dual ḫaṣmāni → 'dva protivnička tabora'"),
    "S022-A022-W007-S01": ("E1", INS + ": 'teškog'"),
    "S022-A025-W015-S01": ("E2", P_UNEXP + ": fīhi nije preveden; 'mještanin' prevodi ʿākif"),
    "S022-A025-W015-S02": ("E2", P_UNEXP + ": -hi u fīhi nije preveden"),
    "S022-A025-W021-S02": ("E2", "ẓulm → 'zulum'; 'čineći' nosi bi-"),
    "S022-A026-W013-S03": ("E1", "ṭāʾifīn → 'one koji će … obilaziti,'; objekat 'je' bez segmenta (inserted)"),
    "S022-A034-W008-S01": ("E2", "ʿalā (okolnost) → 'prilikom'; 'klanja' je dopuna (inserted)"),
    "S022-A036-W002-S03": ("E2", P_UNEXP + ": resumptivni objekat -hā nije ponovljen ('kamile' nosi budn)"),
    "S022-A036-W019-S01": ("E1", P_UNEXP + ": partitivni min uz zamjenicu; 'ih' nosi -hā (akuzativ, ne partitivni genitiv)"),
    "S022-A036-W022-S01": ("E2", "wa → 'a i'"),
    "S022-A037-W001-S01": ("E1", LAN),
    "S022-A037-W002-S01": ("E1", LANV),
    "S022-A039-W005-S02": ("E2", "iza imena anna ('im') sufiks fused na glagol 'učinjen' (COMMON)"),
    "S022-A041-W015-S02": ("E1", "li- → dativ 'Allahu' + predikat 'se … vraća.' (dosljedno 28:70 'Njemu pripada')"),
    "S022-A041-W016-S01": ("E1", "ʿāqiba → 'na kraju,'"),
    "S022-A041-W017-S01": ("E1", DETS),
    "S022-A045-W001-S02": ("E2", "kaʾayyin → 'koliko samo'; ponovljeno 'koliko' nosi isti segment; 'ima' inserted (dosljedno 12:105)"),
    "S022-A045-W006-S01": ("E2", PARTN + ": 'su' nosi hiya"),
    "S022-A047-W003-S02": ("E1", LAN),
    "S022-A047-W004-S01": ("E1", LANV),
    "S022-A048-W001-S02": ("E2", "kaʾayyin → 'koliko'; 'je bilo' inserted (dosljedno 12:105)"),
    "S022-A048-W007-S01": ("E2", PARTN + ": 'su' nosi hiya"),
    "S022-A051-W002-S01": ("E1", "saʿaw → 'se budu trudili'"),
    "S022-A051-W003-S01": ("E1", "fī (neprijateljska usmjerenost) → 'da … poreknu,'"),
    "S022-A052-W012-S01": ("E1", "alqā → '-je … ubacio.'; 'nešto' je dopuna (inserted)"),
    "S022-A053-W006-S01": ("E2", REPP + ": 'za za'"),
    "S022-A053-W010-S03": ("E2", "qāsiya → 'one čija su … okrutna'; ponovljeno 'za' nosi li-"),
    "S022-A053-W014-S02": ("E2", "fī → 'u' i 'na' u Mehanovićevom dubletu (ponovljeni prijedlog nosi isti segment)"),
    "S022-A053-W015-S01": ("E2", "šiqāq → dublet 'rascjepu i … stranputici'"),
    "S022-A057-W003-S03": ("E2", "sufiks drugog koordiniranog glagola → zajednički pomoćni 'nisu' (COMMON)"),
    "S022-A060-W004-S01": ("E1", "bi-miṯli → fused 'isto onako'"),
    "S022-A060-W007-S01": ("E1", "bi- povratne fraze → relativ načina 'kako' (RESUMP, COMMON)"),
    "S022-A060-W007-S02": ("E1", "resumptivni -hi → relativ 'kako' (COMMON)"),
    "S022-A061-W012-S02": ("E2", TAWK),
    "S022-A062-W009-S01": ("E2", MINDUN),
    "S022-A063-W014-S01": ("E1", "laṭīf → opisno 'znalac i onoga što je najsitnije' ('i' = čak)"),
    "S022-A063-W015-S01": ("E2", "ḫabīr → 'sve u potpunosti zna.'; 'On' inserted"),
    "S022-A065-W021-S01": ("E2", "illā → 'osim'"),
    "S022-A065-W022-S01": ("E2", "bi-iḏnihi preoblikovan u uslov → bi- nosi 'ako'"),
    "S022-A067-W006-S01": ("E2", "nāsikūhu → bezlično 'da se vlada;'; 'je trebalo' inserted"),
    "S022-A070-W007-S01": ("E2", REPP),
    "S022-A070-W009-S03": ("E2", "arḍ → 'Zemlji?!'; ponovljeno 'na' nosi fī"),
    "S022-A071-W002-S01": ("E2", MINDUN),
    "S022-A071-W011-S01": ("E2", "laysa → 'ne'; negativna konkordancija 'ništa' ide imenici (COMMON)"),
    "S022-A071-W014-S01": ("E2", "ʿilm → 'ništa … znaju.'"),
    "S022-A072-W020-S02": ("E2", "šarr → 'šta … gore'; kopula 'je' inserted"),
    "S022-A073-W010-S01": ("E2", MINDUN),
    "S022-A074-W005-S01": ("E1", "apsolutni objekat qadr dijeli glagolski izraz 'veličaju i … poznaju' (COMMON)"),
    "S022-A075-W006-S02": ("E1", "drugi min nije ponovljen; zajedničko 'među' upravlja i imenicom 'ljudima'"),
    "S022-A076-W003-S01": ("E2", PARTN + ": 'su' nosi -hum"),
    "S022-A076-W004-S01": ("E2", PARTN),
    "S022-A076-W006-S01": ("E2", PARTN + ": 'će' nosi -hum"),
    "S022-A076-W010-S01": ("E1", DETS),
    "S022-A078-W004-S01": ("E2", "ḥaqqa → 'istinski, onako kako … treba'"),
    "S022-A078-W005-S01": ("E2", "jihād → vlastiti izraz 'se … boriti!' (povratno 'se' ide glagolu)"),
}

if __name__ == "__main__":
    run("S022_El-Hadzdz", D)
