# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 78."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"
COORD = "koordinirani glagol bez vlastite zamjenice/pomoćnog → subjektni sufiks fused na glagolski oblik (dosljedno 59:5, 71:7)"
VSUBJ = "subjektni sufiks glagola iza inna: zamjenica nosi ime inna, sufiks ide na pomoćni/glagolski token (dosljedno 72:1–13)"

D = {
    "S078-A004-W002-S01": ("E2", "sa- → 'će' (dosljedno svim objavljenim FUT); " + INS + ": 'sigurno!'"),
    "S078-A005-W003-S01": ("E2", "sa- → 'će'; " + INS + ": 'sigurno!'"),
    "S078-A008-W001-S03": ("E2", COORD + " ('stvorili,')"),
    "S078-A009-W001-S03": ("E2", COORD + " ('učinili,')"),
    "S078-A010-W001-S03": ("E2", COORD + " ('učinili,')"),
    "S078-A011-W001-S03": ("E2", COORD + " ('odredili,')"),
    "S078-A012-W001-S03": ("E2", COORD + " ('sazdali,')"),
    "S078-A013-W001-S03": ("E2", COORD + " ('postavili?!')"),
    "S078-A018-W006-S01": ("E2", "afwāj → distributivno 'skupina po skupina'; " + INS + ": 'sve'"),
    "S078-A024-W001-S01": ("E2", "lā → 'ne' u 'neće'[0,2]; 'nikakve' nosi imenica bard (negativna konkordancija s vlastitim segmentom, COMMON)"),
    "S078-A024-W004-S01": ("E2", "bard → 'nikakve svježine' (negativna konkordancija ide na vlastiti segment, COMMON 36:30)"),
    "S078-A027-W002-S02": ("E2", VSUBJ + " ('su' u 'nisu'[2,4])"),
    "S078-A027-W004-S02": ("E2", VSUBJ + " ('nadali')"),
    "S078-A040-W002-S02": ("E2", VSUBJ + " ('upozoravamo,')"),
    "S078-A040-W011-S02": ("E1", "drugi koordinirani glagol dobija samo svoj token; zajedničko 'će' nosi prvi glagol"),
}

if __name__ == "__main__":
    run("S078_En-Nebe", D)
