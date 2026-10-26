# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 49."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

D = {
    "S049-A002-W011-S01": ("E2", P_NARROW + ": jahara → 'glasno,'; 'razgovarajte' nosi bi-l-qawl"),
    "S049-A003-W014-S01": ("E2", "posvojni li- → 'pripada'; dativ 'onima' nosi REL i povratno -hum (dosljedno 85:11)"),
    "S049-A011-W027-S01": ("E1", "tanābazū (uzajamno nazivanje pogrdnim nadimcima) → 'zovite jedni druge ružnim' (pogrdnost je dio leksičkog značenja nbz)"),
    "S049-A011-W028-S03": ("E1", "alqāb → 'nadimcima!'"),
    "S049-A011-W030-S02": ("E1", P_NARROW + ": ism → 'imenom'; 'nazivati' je Mehanovićeva dopuna (inserted)"),
    "S049-A012-W013-S01": ("E2", P_NARROW + ": tajassasū → 'uhodite'; 'jedni druge' je dodani objekat (inserted; dosljedno 46:15)"),
    "S049-A013-W008-S03": ("E1", "drugi -nā nosi zajednički pomoćni 'smo' (dosljedno 84:25, 46:27)"),
    "S049-A017-W009-S01": ("E1", "maṣdar islām preoblikovan u rečenicu 'što … islam primili;' (cijela preoblika, dosljedno 88:26)"),
    "S049-A017-W016-S03": ("E2", P_NARROW + ": īmān → 'vjeru'; 'pravu' je Mehanovićevo pojačanje (inserted)"),
}

if __name__ == "__main__":
    run("S049_El-Hudzurat", D)
