# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 66."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

D = {
    "S066-A003-W004-S01": ("E1", "ilā bez zasebnog prijedloga → dativ riječi kojom upravlja (baʿḍ → 'jednoj'), ne imenice u genitivnoj vezi (COMMON)"),
    "S066-A003-W014-S01": ("E2", "ʿarrafa → 'on … upozna'; 'je' je objektna enklitika ('nju') bez arapskog segmenta (inserted)"),
    "S066-A008-W009-S01": ("E1", "ʿasā → okvir nade 'ne … li'; 'bi' je pomoćni glagol kondicionala koji gradi oblik yukaffira (COMMON)"),
    "S066-A008-W012-S01": ("E1", "yukaffira → 'bi … izbrisao'; pomoćni glagol pripada glagolskom obliku koji gradi"),
    "S066-A010-W014-S01": ("E1", P_UNEXP + ": partitivni ʿibād sažet; 'roba' nosi dual ʿabdayn, 'Naša' nosi -nā"),
    "S066-A010-W027-S02": ("E2", "particip → 'onima koji … ulaze!\"' (relativna preoblika); 'u nju' je Mehanovićeva dopuna (inserted); " + P_NARROW),
}

if __name__ == "__main__":
    run("S066_Et-Tahrim", D)
