# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 71."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

RESTR = "restriktivno lam/lā … illā preoblikovano u 'samo': NEG/zabrana ide na restriktivni token zajedno s illā (dosljedno 36:17, 36:29, 37:39, 38:15)"
COORD = "drugi koordinirani glagol dobija samo svoj token; zajednički pomoćni/zamjenicu nosi prvi (dosljedno 59:5, 65:2)"
AUX = "subjektni sufiks bez eksplicitne zamjenice → vlastiti pomoćni glagol koji nosi lice (COMMON 55.9)"
INNA = "ime inna bez eksplicitne zamjenice → token koji nosi njegovo lice (dosljedno 63:3 -hum → 'su')"

D = {
    "S071-A004-W017-S02": ("E2", "-tum u law kuntum taʿlamūn → fused 'znate,' (dosljedno 61:11, 62:9)"),
    "S071-A006-W002-S01": ("E2", "yazid → 'je … više'; 'još' je pojačivač bez segmenta (inserted, COMMON); " + P_NARROW),
    "S071-A007-W001-S03": ("E2", INNA + " ('sam')"),
    "S071-A007-W010-S03": ("E1", COORD + " ('pokrivali')"),
    "S071-A007-W013-S03": ("E1", COORD + " ('oholi.')"),
    "S071-A009-W002-S02": ("E2", INNA + " ('sam')"),
    "S071-A009-W005-S03": ("E1", COORD + " ('šaputao,')"),
    "S071-A021-W005-S02": ("E2", "subjektni -w → eksplicitna zamjenica 'oni' (COMMON 55.9)"),
    "S071-A021-W006-S03": ("E1", COORD + " ('povode')"),
    "S071-A021-W008-S01": ("E1", RESTR),
    "S071-A024-W004-S02": ("E1", RESTR),
    "S071-A025-W003-S02": ("E1", "subjektni -ū → eksplicitna zamjenica 'oni'; 'su' pripada glagolskom obliku 'su potopljeni'"),
    "S071-A025-W004-S03": ("E2", AUX + " ('će' u 'će biti uvedeni')"),
    "S071-A025-W007-S02": ("E2", AUX + " ('će' u 'neće'[2,4])"),
    "S071-A027-W001-S02": ("E2", INNA + " ('ostaviš,' — 2. l. jd. istog referenta)"),
    "S071-A027-W004-S02": ("E1", "subjektni -ū → eksplicitna zamjenica 'oni'; 'će' pripada glagolskom obliku"),
    "S071-A027-W006-S02": ("E1", RESTR),
    "S071-A027-W007-S02": ("E2", AUX + " ('će' u 'samo će … rađati')"),
    "S071-A028-W011-S02": ("E1", RESTR),
}

if __name__ == "__main__":
    run("S071_Nuh", D)
