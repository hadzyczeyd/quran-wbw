# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 105."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_UNEXP, run  # noqa: E402

D = {
    "S105-A002-W004-S01": ("E1", P_UNEXP + ": fī u ja'ala … fī taḍlīl; bosanski glagol 'upropastio' nema prijedlog, veza se ne izmišlja"),
    "S105-A004-W001-S01": ("E2", P_AUX + ": tarmī → 'su … bacale,'; 'koje' bez REL segmenta (dosljedno 43:51)"),
}

if __name__ == "__main__":
    run("S105_El-Fil", D)
