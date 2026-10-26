# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 84."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_UNEXP, run  # noqa: E402

D = {
    "S084-A014-W001-S02": ("E2", P_UNEXP + ": ime inna -hu nema zaseban token; 'mislio' je glagol ẓanna, subjekat i 'je' prenose se iz 84:13"),
    "S084-A015-W004-S01": ("E1", P_UNEXP + ": kāna trajnog svojstva uz baṣīr nije zasebno preveden (prezent 'sve zna'; dosljedno 110:3)"),
    "S084-A025-W004-S02": ("E2", "ʿamila → 'činili,'; zajednički pomoćni 'budu' ostaje uz prvi glagol (dosljedno 85:11 'su vjerovali i radili')"),
    "S084-A025-W004-S03": ("E1", "subjektni -ū drugog glagola nosi zajednički pomoćni 'budu' (55.9; dosljedno 85:11, gdje oba -ū idu na 'su')"),
    "S084-A025-W006-S02": ("E1", "hum u lahum → 'će' (lice), lām → 'imat' (dosljedno 85:10, 42:22)"),
}

if __name__ == "__main__":
    run("S084_El-Insikak", D)
