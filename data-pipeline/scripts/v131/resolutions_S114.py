# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 114."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S114-A001-W003-S01": ("E1", "GOVERNED_PHRASE: bi- uz a'ūḏu kodiran dativom 'Gospodaru' (dosljedno 42/43)"),
    "S114-A004-W004-S02": ("E1", P_NARROW + ": ḫannās → 'se skrije,'; 'koji' pripada waswās"),
}

if __name__ == "__main__":
    run("S114_En-Nas", D)
