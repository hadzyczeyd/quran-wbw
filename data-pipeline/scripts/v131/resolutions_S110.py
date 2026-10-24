# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 110."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

D = {
    "S110-A003-W001-S01": ("E2", P_UNEXP + ": RSLT fa- (posljedica uslova) Mehanović ne izražava; 'ti' je subjekat imperativa"),
    "S110-A003-W001-S02": ("E2", "sabbiḥ (2MS imperativ) → dublet 'slavi i veličaj' s eksplicitnim subjektom 'ti'"),
    "S110-A003-W004-S02": ("E2", "istaġfir → 'moli … da ti oprosti,'; 'ti' nosi 2MS korisnika traženja oprosta, 'Ga' i 'da' su dopune"),
    "S110-A003-W007-S01": ("E1", P_NARROW + ": tawwāb → 'pokajanje … prima.'; 'stalno' nosi kāna (trajnost)"),
}

if __name__ == "__main__":
    run("S110_En-Nasr", D)
