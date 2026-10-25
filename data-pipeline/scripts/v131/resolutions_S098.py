# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 98."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import run  # noqa: E402

D = {
    "S098-A008-W008-S01": ("E2", "min taḥtihā (složeni prostorni prijedlog) → 'kroz'; sadržajni taḥt nosi isti token kao min"),
}

if __name__ == "__main__":
    run("S098_El-Bejjine", D)
