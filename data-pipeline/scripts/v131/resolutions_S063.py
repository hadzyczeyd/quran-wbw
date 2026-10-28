# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 63."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INNA = "ime inna/anna s eksplicitnom bosanskom zamjenicom → samo ta zamjenica; kopula inserted (dosljedno innaka/innahum → 'ti'/'oni')"

D = {
    "S063-A001-W006-S02": ("E2", INNA + " ('ti,')"),
    "S063-A001-W011-S02": ("E2", INNA + " ('ti,')"),
    "S063-A003-W002-S03": ("E2", "ime anna -hum bez eksplicitne zamjenice → kopula/pomoćni 'su' koji nosi njegovo lice (COMMON)"),
    "S063-A003-W009-S02": ("E2", P_UNEXP + ": samostalno hum u fa-hum lā yafqahūn bez bosanske zamjenice (dosljedna većina objavljenih sura)"),
    "S063-A004-W009-S02": ("E2", INNA + " ('oni')"),
    "S063-A004-W016-S01": ("E2", "samostalno hum (subjekat) → eksplicitno 'Oni'; 'su' je inserted kopula"),
    "S063-A005-W013-S01": ("E1", P_UNEXP + ": okolnosno wa u wa-hum mustakbirūn nema svoj token; 'nadmeno' nosi samo particip"),
    "S063-A007-W003-S02": ("E2", "subjektni -ūna → eksplicitna zamjenica 'Oni' (COMMON 55.9)"),
    "S063-A007-W012-S01": ("E2", P_NARROW + "; objekat 'ga' nema arapskog segmenta (inserted)"),
    "S063-A009-W004-S01": ("E2", "lā zabrane + jusiv → 'neka … ne' (dosljedno 49:11 'neka ne')"),
    "S063-A009-W005-S01": ("E2", "glagol → 'zabave'; 'neka' nosi zabranu s lā (49:11)"),
    "S063-A009-W007-S02": ("E1", P_UNEXP + ": drugo lā (wa-lā awlādukum) nema svoj token; jedno 'ne' nosi prvo lā"),
}

if __name__ == "__main__":
    run("S063_El-Munafikun", D)
