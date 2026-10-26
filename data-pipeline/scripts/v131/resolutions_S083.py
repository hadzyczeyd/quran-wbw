# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 83."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

KANA = "u kāna + imperfekt lice oba PRON sufiksa nosi zajednički pomoćni glagol (55.9; dosljedno 85:7 'su radili', 84:25 'budu')"

D = {
    "S083-A003-W004-S01": ("E2", P_NARROW + ": wazana (vagati) → 'na kantar'; zajednički 'mjere' leksički pripada kāla"),
    "S083-A003-W004-S02": ("E1", "subjektni -ū eliptičnog wazanū dijeli fleksiju zajedničkog 'mjere' (kao što objekat hum dijeli 'drugima')"),
    "S083-A014-W008-S02": ("E1", KANA + ": 'su'"),
    "S083-A017-W007-S02": ("E1", KANA + ": 'ste'"),
    "S083-A025-W002-S01": ("E2", "min nema zaseban prijedlog; instrumental glavne imenice 'pićem' (napajani pićem) nosi odnos"),
    "S083-A029-W008-S02": ("E1", KANA + ": 'su'"),
    "S083-A036-W006-S02": ("E1", KANA + ": 'su'"),
}

if __name__ == "__main__":
    run("S083_El-Mutaffifin", D)
