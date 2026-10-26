# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 50."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

FI = "fī ('u stanju') bez zasebnog prijedloga: stanje nosi predikat u koji je imenica preoblikovana (fused; dosljedno 85:19 fī takḏīb → 'stalno')"

D = {
    "S050-A005-W007-S01": ("E2", FI),
    "S050-A007-W009-S01": ("E2", "kull → 'razno' [0,5] u složenici 'raznovrsno,' (stvarna granica razno|vrsno)"),
    "S050-A007-W010-S01": ("E2", "zawj (vrsta) → 'vrsno,' [5,11] + 'bilje.' (vrste bilja)"),
    "S050-A008-W003-S01": ("E2", "li- ('za svakog roba') preoblikovan u namjeru → 'da'"),
    "S050-A015-W006-S01": ("E2", FI),
    "S050-A022-W003-S01": ("E2", FI),
    "S050-A025-W002-S01": ("E2", "li- (objekat intenzivnog mannāʿ) → 'da' koji uvodi dopunu (dosljedno 89:18 ʿalā → 'da')"),
    "S050-A035-W001-S01": ("E1", "posvojni la- → 'će imati' (dosljedno 85:10 'imat će')"),
    "S050-A039-W007-S01": ("E1", P_NARROW + ": rabb → 'Gospodara'; anaforično 'Mu' je Mehanovićeva dopuna (inserted)"),
    "S050-A042-W004-S01": ("E2", "bi- → 'u' [0,1] u prilogu 'uistinu,' (stvarna granica u|istinu)"),
    "S050-A042-W004-S03": ("E2", "ḥaqq → 'istinu,' [1,8] u 'uistinu,'"),
}

if __name__ == "__main__":
    run("S050_Kaf", D)
