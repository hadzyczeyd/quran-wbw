# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 64."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_UNEXP, run  # noqa: E402

D = {
    "S064-A005-W011-S02": ("E1", "li- bez zasebnog prijedloga → padežni oblik zamjenice 'ih' nosi prijedlog (COMMON); 'čeka?' je Mehanovićev dodatak (inserted)"),
    "S064-A006-W007-S01": ("E1", P_UNEXP + ": posljedično fa u fa-qālū; Mehanović obrće red rečenica, a 'kad' uvodi drugu rečenicu (inserted)"),
    "S064-A007-W006-S02": ("E1", "subjektni -ū bez eksplicitne zamjenice → pomoćni 'će' u 'neće'[2,4] (COMMON, dosljedno ostalim surama)"),
    "S064-A010-W005-S01": ("E1", P_UNEXP + ": ulāʾika bez bosanske zamjenice (dosljedno 58:20, 60:9, 63:9)"),
    "S064-A016-W016-S02": ("E2", "mufliḥūn → 'su … uspjeli.'; pomoćni 'su' gradi oblik i nosi hum (dosljedno 59:9 'će … uspjeti.')"),
}

if __name__ == "__main__":
    run("S064_Et-Tegabun", D)
