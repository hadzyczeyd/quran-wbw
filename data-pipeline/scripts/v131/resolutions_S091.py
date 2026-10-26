# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 91."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_GOV, P_NARROW, run  # noqa: E402

D = {
    "S091-A011-W002-S01": ("E1", P_NARROW + ": PN Ṯamūd → 'Semud'; 'Narod' je Mehanovićevo pojašnjenje"),
    "S091-A013-W005-S01": ("E1", P_GOV + ": 'na devu' (akuzativ upozorenja nāqata; 'na' kodira padež imenice)"),
    "S091-A014-W007-S02": ("E2", P_AUX + ": sawwā → 'je, … obuhvatio' (zajednički pomoćni glagol); 'kaznom' je dopuna"),
}

if __name__ == "__main__":
    run("S091_Es-Sems", D)
