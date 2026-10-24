# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 107."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import run  # noqa: E402

P_VERBP = "bi- uz glagol koji u bosanskom uzima direktni objekat nije zasebno izražen (dosljedno 40:83, 43:24)"

D = {
    "S107-A001-W004-S01": ("E1", P_VERBP + ": kaḏḏaba bi- → 'poriče' + akuzativ 'Sud'"),
}

if __name__ == "__main__":
    run("S107_El-Maun", D)
