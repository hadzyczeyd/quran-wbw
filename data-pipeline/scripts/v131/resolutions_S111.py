# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 111."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S111-A003-W001-S01": ("E2", P_NARROW + ": FUT sa- → futurski 'će'; 'sigurno' je Mehanovićevo pojačanje"),
}

if __name__ == "__main__":
    run("S111_El-Mesed", D)
