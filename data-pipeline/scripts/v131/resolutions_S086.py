# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 86."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_UNEXP, run  # noqa: E402

D = {
    "S086-A010-W001-S01": ("E2", P_UNEXP + ": fa- nije preveden; 'kada' ponavlja vremensku odredbu iz 86:9 (inserted)"),
    "S086-A013-W003-S01": ("E1", "faṣl (riječ koja razdvaja istinu od neistine) → relativna preoblika ADJ 'koji rastavlja Istinu od neistine,'; objekti su dio leksičkog značenja (COMMON: وَقَبَ → 'razastre tmine')"),
}

if __name__ == "__main__":
    run("S086_Et-Tarik", D)
