# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 1."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import run  # noqa: E402

D = {
    "S001-A007-W001-S01": ("E1", "ṣirāṭ → 'Na put'; Mehanović isti ṣirāṭ ponavlja u apoziciji ('na put onih …') — ponovljeni izraz istog segmenta nosi taj segment (kao ponovljeni 'koji' istog REL-a)"),
}

if __name__ == "__main__":
    run("S001_El-Fatiha", D)
