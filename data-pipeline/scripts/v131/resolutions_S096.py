# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 96."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import run  # noqa: E402

D = {
    "S096-A009-W001-S01": ("E1", "INTG a- → 'li' u 'Vidjeli' (stvarna granica Vidje|li, upitna čestica)"),
    "S096-A009-W001-S02": ("E1", "ra'ayta → 'Vidje' [0,5]; 'li' nosi INTG"),
    "S096-A015-W006-S02": ("E1", "DET al- unexpressed: QAC ga označava samo kao DET; posvojno 'mu' je Mehanovićevo eksplicitiranje"),
}

if __name__ == "__main__":
    run("S096_El-Alek", D)
