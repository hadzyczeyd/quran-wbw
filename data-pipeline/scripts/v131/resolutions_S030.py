# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 30."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_FUNC, P_NARROW, P_UNEXP, run  # noqa: E402

COORD = "drugi koordinirani glagol dobija samo svoj token; zajednički pomoćni ostaje uz prvi (COMMON)"
INS = P_NARROW + "; pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
NAFS = "anfus (sami sebe) → povratno-emfatički izraz 'sami … sebi'"
KADH = "ka-dhālika → 'tako' (ka i DEM zajedno); 'Eto,' je Mehanovićev dodatak (inserted)"

D = {
    "S030-A003-W008-S03": ("E1", "'oni' nosi samostalnu zamjenicu hum (temu); sufiks glagola ide na pomoćni 'će,' (kao iza inna, 32:3)"),
    "S030-A008-W004-S01": ("E1", NAFS),
    "S030-A009-W018-S02": ("E1", COORD),
    "S030-A009-W031-S01": ("E1", NAFS),
    "S030-A013-W002-S01": ("E1", "yakun lahum (imat će) → 'neće'[2,4] 'imati' ('imati' dijeli s lām)"),
    "S030-A015-W004-S02": ("E1", COORD),
    "S030-A015-W006-S02": ("E1", "samostalna zamjenica hum → buduća kopula 'će' (COMMON: PRON → kopula)"),
    "S030-A018-W008-S02": ("E1", "subjektni sufiks bez zamjenice i pomoćnog → fused na glagolski token 'podne.' (COMMON 55.9)"),
    "S030-A020-W011-S01": ("E2", INS + ": 'svuda'"),
    "S030-A023-W006-S02": ("E1", P_NARROW + ": ibtighāʾ → 'nastojanje'; 'da steknete' je Mehanovićevo proširenje (inserted)"),
    "S030-A028-W016-S01": ("E1", P_AUX + ": 'smo … opskrbili,'"),
    "S030-A028-W023-S02": ("E2", KADH),
    "S030-A029-W015-S01": ("E2", "min nāṣirīna → genitiv 'pomagača' (" + P_FUNC + ", dosljedno 34:34)"),
    "S030-A032-W005-S02": ("E2", P_AUX + ": kānū (postati) → 'su se podijelili,'"),
    "S030-A038-W015-S01": ("E1", INS + ": 'baš'"),
    "S030-A039-W021-S01": ("E1", "zamjenica odvajanja hum → buduća kopula 'će'; 'upravo' je pojačivač (inserted)"),
    "S030-A039-W022-S02": ("E1", P_AUX + ": predikat preveden glagolski, 'će' gradi oblik i nosi zamjenicu (dosljedno 31:5, 32:10)"),
    "S030-A040-W005-S01": ("E1", COORD),
    "S030-A040-W009-S01": ("E1", COORD),
    "S030-A040-W020-S02": ("E2", "taʿālā → 'Uzvišen'; 'On' nosi -hu iz subḥānahu (drugi koordinirani član samo svoj token)"),
    "S030-A043-W012-S01": ("E1", P_UNEXP + ": lām u lahu; 'koji' je akuzativni objekat 'odbiti' i nosi -hu"),
    "S030-A044-W004-S02": ("E1", "-hu (njegovo nevjerovanje) u glagolskoj preobliči → lice pomoćnog 'nisu' (dosljedno 35:30)"),
    "S030-A045-W004-S02": ("E1", COORD),
    "S030-A046-W016-S02": ("E1", "laʿalla → samo 'da'; -kum/-ūna na 'biste' (COMMON, dosljedno 35:12)"),
    "S030-A046-W017-S01": ("E1", P_AUX + ": 'biste zahvalni bili.' (dosljedno 35:12)"),
    "S030-A047-W015-S01": ("E1", "ḥaqqan → Mehanovićev dvostruki prijevod 'uistinu … dužnost' (dosljedno 33:14)"),
    "S030-A048-W020-S01": ("E2", "aṣāba → 'On prolije,'"),
    "S030-A048-W021-S02": ("E2", "-hi (kiša) → akuzativna enklitika 'je'"),
    "S030-A049-W001-S01": ("E1", "wa-in → 'iako': wa → 'i'[0,1]"),
    "S030-A049-W001-S02": ("E1", "wa-in → 'iako': in → 'ako'[1,4]"),
    "S030-A052-W011-S01": ("E1", "mudbirīn (okrećući leđa, udaljavajući se) → 'od tebe'; 'okrenu,' nosi wallaw"),
    "S030-A054-W013-S01": ("E1", P_UNEXP + ": drugi jaʿala elidiran; zajednički 'daje,' ostaje uz prvi (dosljedno 33:73)"),
    "S030-A056-W011-S01": ("E1", INS + ": 'sve'"),
    "S030-A059-W001-S02": ("E2", KADH),
}

if __name__ == "__main__":
    run("S030_Er-Rum", D)
