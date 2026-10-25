# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 103."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_UNEXP, run  # noqa: E402

D = {
    "S103-A002-W003-S01": ("E2", P_UNEXP + ": emfatičko la- uz inna; jedno 'doista' nosi inna (dosljedno 43:46 la-qad)"),
    "S103-A003-W002-S01": ("E2", "REL allaḏīna → 'oni koji'; ponovljeni 'koji' su Mehanovićevo ponavljanje bez novog arapskog segmenta"),
}

if __name__ == "__main__":
    run("S103_El-Asr", D)
