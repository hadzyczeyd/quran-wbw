# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 112."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, run  # noqa: E402

D = {
    "S112-A004-W001-S02": ("E2", "QAC NEG lam → 'ni-' u 'nije' (dosljedno 43:7, 43:23)"),
    "S112-A004-W002-S01": ("E2", P_AUX + ": yakun → '-je' u 'nije'; 'ni-' nosi lam"),
}

if __name__ == "__main__":
    run("S112_El-Ihlas", D)
