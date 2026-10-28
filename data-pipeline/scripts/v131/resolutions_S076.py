# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 76."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"

D = {
    "S076-A007-W003-S03": ("E2", "drugi koordinirani glagol dobija samo svoj token; zajedničko 'Oni su' nosi prvi (dosljedno 59:5, 71:7)"),
    "S076-A010-W006-S01": ("E2", "ʿabūs (opis dana) → 'smrknuta'; " + INS + ": 'lica'"),
    "S076-A020-W003-S01": ("E2", "ṯamma → mjesno 'kud'; 'god' nosi samo uopćavajuće idhā"),
    "S076-A021-W010-S02": ("E1", "saqā → 'dat će … piju'; podređivač 'da' bez arapskog segmenta (inserted, dosljedno 62:5)"),
    "S076-A031-W008-S02": ("E1", "resumptivno -hum u lahum → dativ 'zulumćarima' koji nosi i li- (COMMON: padežni oblik nosi ulogu)"),
}

if __name__ == "__main__":
    run("S076_El-Insan", D)
