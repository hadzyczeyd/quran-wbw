# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 88."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

D = {
    "S088-A006-W001-S01": ("E2", P_NARROW + ": laysa (negirano 'biti') → 'neće'; 'imati,' nosi posvojno li- (lahum)"),
    "S088-A006-W005-S01": ("E2", P_UNEXP + ": eksplikativno min iza illā; genitiv 'trnja' traži 'osim', ne kodira min"),
    "S088-A026-W004-S01": ("E2", "maṣdar ḥisāb preoblikovan u zavisnu rečenicu → 'da račun svedemo!' (cijela preoblika pripada imenici, kao relativna preoblika N)"),
}

if __name__ == "__main__":
    run("S088_El-Gasija", D)
