# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 73."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_UNEXP, run  # noqa: E402

AUX = "pomoćni glagol pripada glagolskom obliku koji gradi (COMMON; dosljedno 68:17 'smo … na kušnju stavili')"

D = {
    "S073-A006-W004-S01": ("E2", P_UNEXP + ": hiya; 'je' je kopula druge rečenice ('izgovor je razboritiji', inserted), ne nosi hiya"),
    "S073-A015-W002-S01": ("E2", AUX),
    "S073-A015-W008-S01": ("E2", AUX),
    "S073-A016-W004-S02": ("E2", AUX),
    "S073-A017-W002-S01": ("E2", AUX + " ('ćete se, … sačuvati')"),
    "S073-A020-W022-S01": ("E2", "lan → 'ne' u 'nećete'[0,2] (stvarna granica ne|ćete, COMMON)"),
    "S073-A020-W023-S01": ("E2", "tuḥṣū → 'nećete'[2,6] 'moći izdržati' (pomoćni dio futura uz glagol)"),
    "S073-A020-W037-S01": ("E2", AUX + " ('će … putovati,')"),
    "S073-A020-W040-S02": ("E2", "drugi koordinirani glagol dobija samo svoj token; zajedničko 'će' nosi prvi (dosljedno 59:5, 71:7)"),
    "S073-A020-W045-S01": ("E2", AUX + " ('će se … boriti.')"),
    "S073-A020-W066-S01": ("E2", AUX + " ('naći ćete')"),
}

if __name__ == "__main__":
    run("S073_El-Muzzemmil", D)
