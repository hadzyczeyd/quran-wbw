# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 102."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S102-A001-W002-S02": ("E2", P_NARROW + ": takāṯur (nadmetanje u umnožavanju) → 'zgrtanje'; 'imovine' je Mehanovićevo određenje predmeta, nije dio značenja riječi"),
}

if __name__ == "__main__":
    run("S102_Et-Tekasur", D)
