# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 82."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S082-A019-W001-S01": ("E1", P_NARROW + ": yawma → 'Dan'; 'kada' uvodi rečenicu i ostaje inserted (dosljedno 83:6, 86:9)"),
    "S082-A019-W009-S01": ("E1", P_NARROW + ": li- (pripadanje) → 'će … imati.'; 'jedino' je Mehanovićevo pojačanje (inserted)"),
}

if __name__ == "__main__":
    run("S082_El-Infitar", D)
