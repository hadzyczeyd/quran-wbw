# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 99."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_FUNC, run  # noqa: E402

D = {
    "S099-A001-W004-S01": ("E2", P_FUNC + ": kognatni objekat zilzāl (maf'ūl muṭlaq) nosi pojačanje → 'najžešćim potresom'"),
}

if __name__ == "__main__":
    run("S099_Ez-Zilzal", D)
