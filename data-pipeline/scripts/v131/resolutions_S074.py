# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 74."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"
AUX = "pomoćni glagol pripada glagolskom obliku koji gradi (COMMON)"
COORD = "drugi koordinirani glagol dobija samo svoj token; zajednički pomoćni/povratni/zamjenicu nosi prvi (dosljedno 59:5, 70:42)"
INNA = "ime inna s eksplicitnim nosiocem → samo taj token; kopula 'je' inserted (dosljedno 63:1)"

D = {
    "S074-A006-W003-S01": ("E1", "istakthara → 'nadajući se … više!'; " + INS + ": 'da će ti biti uzvraćeno'"),
    "S074-A011-W003-S01": ("E2", AUX + " ('sam … stvorio')"),
    "S074-A011-W003-S02": ("E2", "subjektni -tu → eksplicitna zamjenica 'Ja' (COMMON 55.9)"),
    "S074-A014-W001-S02": ("E2", "mahhada → 'ugodnim učinio,' (sam 'učinio' ne nosi značenje korijena mhd)"),
    "S074-A014-W003-S01": ("E2", "apsolutni objekat tamhīd bez zasebnog izraza dijeli glagolski izraz (COMMON, 89:19–21)"),
    "S074-A018-W002-S01": ("E2", AUX + " ('je smišljao')"),
    "S074-A022-W003-S02": ("E1", COORD + " ('namrštio,')"),
    "S074-A023-W003-S02": ("E1", COORD + " ('uzoholio,')"),
    "S074-A028-W004-S01": ("E1", COORD + "; sinonimni tadharu → 'poštedjeti,'"),
    "S074-A031-W002-S01": ("E2", AUX + " ('smo … postavili')"),
    "S074-A031-W002-S02": ("E2", "subjektni -nā → eksplicitna zamjenica 'Mi' (COMMON 55.9)"),
    "S074-A031-W008-S01": ("E1", COORD + " ('odredili')"),
    "S074-A031-W008-S02": ("E1", COORD + " (-nā fused na 'odredili')"),
    "S074-A031-W010-S01": ("E2", P_UNEXP + ": druga restrikcija illā nije izražena; 'kao' uvodi predikatni objekat i pripada fitna"),
    "S074-A031-W011-S01": ("E2", "fitna → 'kao iskušenje' (jaʿala X Y → odrediti X kao Y)"),
    "S074-A035-W001-S02": ("E2", INNA + " ('to')"),
    "S074-A035-W003-S02": ("E1", "al-kubar → 'od najvećih' (partitivno 'od' kodira genitiv); " + INS + ": 'nevolja,'"),
    "S074-A037-W004-S01": ("E1", P_UNEXP + ": an + subjunktiv izražen infinitivom bez veznika (dosljedno 70:41)"),
    "S074-A049-W002-S01": ("E1", "idiom mā lahum ('šta im je') → 'zašto': li- fused s mā"),
    "S074-A054-W002-S01": ("E1", P_UNEXP + ": inna nema svoj token; 'Uistinu!' nosi kallā"),
    "S074-A054-W002-S02": ("E2", INNA + " ('Kur'an')"),
}

if __name__ == "__main__":
    run("S074_El-Muddessir", D)
