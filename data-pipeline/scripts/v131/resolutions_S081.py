# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 81."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S081-A001-W003-S01": ("E1", P_NARROW + ": kuwwirat → dublet 'bude skupljeno … izgubi sjaj,'; unutrašnje 'i' dubleta je inserted (dosljedno 87:1, 110:3)"),
    "S081-A016-W002-S02": ("E2", "relativna preoblika ADJ bez REL: kunnas → 'što se … sklanja,'; zajednički 'što se' nose oba pridjeva niza (COMMON)"),
    "S081-A029-W001-S02": ("E2", "NEG mā → 'ne' + negativna konkordancija 'ništa' (dosljedno 87:6 'ništa nećeš')"),
}

if __name__ == "__main__":
    run("S081_Et-Tekvir", D)
