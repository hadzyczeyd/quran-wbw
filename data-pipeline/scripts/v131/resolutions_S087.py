# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 87."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S087-A001-W001-S01": ("E1", P_NARROW + ": sabbiḥ → dublet 'Slavi … uzvisuj'; unutrašnje 'i' dubleta je inserted (dosljedno 110:3 'slavi i veličaj')"),
}

if __name__ == "__main__":
    run("S087_El-Ala", D)
