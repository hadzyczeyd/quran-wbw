# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 80."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_UNEXP, run  # noqa: E402

D = {
    "S080-A017-W004-S01": ("E2", P_AUX + ": glagol čuđenja akfara nominalizovan; 'poricanje!' nosi korijen, 'je' predikatni (glagolski) dio istog oblika"),
    "S080-A021-W003-S03": ("E2", P_UNEXP + ": objektni -hu u kauzativnoj preoblici 'učini da bude sahranjen' nema zaseban token (dosljedno 87:5 'čini da postane')"),
    "S080-A037-W005-S01": ("E1", "ša'n (briga) glagolizovan → 'će se … brinuti,'"),
    "S080-A037-W006-S01": ("E1", "yuġnī (zaokuplja tako da ne mari za drugo) → isključivost 'samo'"),
}

if __name__ == "__main__":
    run("S080_Abese", D)
