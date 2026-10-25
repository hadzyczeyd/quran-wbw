# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 97."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import run  # noqa: E402

D = {
    "S097-A001-W002-S02": ("E2", "subjektni -nā → pomoćni 'smo' (1. l. mn.); 'Mi' nosi PRON od innā (dosljedno 108:1)"),
    "S097-A005-W003-S01": ("E2", "ḥattā → 'sve dok … ne'; ekspletivno 'ne' pripada vezniku (dosljedno 102:2)"),
}

if __name__ == "__main__":
    run("S097_El-Kadr", D)
