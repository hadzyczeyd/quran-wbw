# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 92."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S092-A001-W003-S01": ("E2", P_NARROW + ": yaġšā → 'zakrije,'; 'sve' je Mehanovićev izrečeni objekt, nije dio značenja glagola"),
    "S092-A019-W003-S01": ("E1", "GOVERNED_PHRASE: 'indahu → dativ 'mu' (odnos prema davaocu kodiran padežom zamjenice)"),
}

if __name__ == "__main__":
    run("S092_El-Lejl", D)
