# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 79."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"
AMMA = P_UNEXP + ": ammā nema vlastiti token; 'onom' nosi man, uvodno 'Pa,'/'A' nosi fa/wa (dosljedno 72:15)"

D = {
    "S079-A010-W004-S01": ("E1", "fī → 'u' ispred 'kaburovima' (fī l-ḥāfira strukturno 'u kaburovima'; korijen ḥfr = kopati, grob)"),
    "S079-A010-W005-S02": ("E1", "al-ḥāfira → 'kaburovima' (korijen ḥfr); 'u život?' je Mehanovićeva dopuna uz mardūdūna (inserted)"),
    "S079-A018-W003-S01": ("E1", "la- bez zasebnog prijedloga → dativni oblik 'ti' koji nosi -ka (COMMON)"),
    "S079-A019-W001-S01": ("E2", P_UNEXP + ": wa- (asindetsko nadovezivanje); 'da' već pripada glagolskom izrazu 'da uputim,'"),
    "S079-A022-W003-S01": ("E2", "drugi koordinirani glagol dobija samo svoj token; zajedničko 'se' nosi prvi (dosljedno 59:5, 70:42)"),
    "S079-A037-W001-S02": ("UNEXP", AMMA),
    "S079-A040-W001-S02": ("UNEXP", AMMA),
    "S079-A043-W001-S01": ("E2", P_UNEXP + ": fī u fīma; upitno 'Šta' nosi mā"),
    "S079-A045-W005-S02": ("E2", "-hā (Čas) → 'na njega' (referent premješten u 'upozorenje na njega'); 'Ga' (Allah) nema arapskog segmenta (inserted)"),
    "S079-A046-W002-S01": ("E2", "yawma → 'Dan'; " + INS + ": 'taj,'"),
}

if __name__ == "__main__":
    run("S079_En-Naziat", D)
