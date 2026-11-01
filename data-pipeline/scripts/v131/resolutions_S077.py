# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 77."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S077-A018-W003-S02": ("E1", "DET al- unexpressed (COMMON); 'svim' je Mehanovićev pojačivač (inserted, dosljedno 65:12, 67:6)"),
    "S077-A039-W003-S01": ("E1", "posvojno li- (lakum kaydun) preoblikovano u 'se … poslužiti,'; modalno 'znali' nema arapskog segmenta (inserted); " + P_NARROW),
}

if __name__ == "__main__":
    run("S077_El-Murselat", D)
