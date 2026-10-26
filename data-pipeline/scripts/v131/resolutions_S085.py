# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 85."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S085-A009-W002-S02": ("E2", "povratno -hu (posjednik) nosi posvojni relativ 'Čija' zajedno s REL i li- (dosljedno 89:8 -hā → 'kojima')"),
    "S085-A016-W001-S01": ("E1", P_NARROW + ": faʿʿāl → 'radi'; 'On' je Mehanovićev izrečeni subjekat bez arapskog segmenta (inserted)"),
}

if __name__ == "__main__":
    run("S085_El-Burudz", D)
