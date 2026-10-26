# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 89."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

D = {
    "S089-A006-W006-S02": ("E1", P_NARROW + ": PN ʿĀd → 'Ad'; 'narodom' je Mehanovićeva objašnjavajuća apozicija"),
    "S089-A019-W003-S01": ("E1", "apsolutni objekat aklan ponavlja sadržaj glagola → 'jedete' (dijeli token s glagolom); 'pohlepno' nosi ADJ lammā"),
    "S089-A020-W003-S01": ("E1", "apsolutni objekat ḥubban ponavlja sadržaj glagola → 'volite.' (dijeli token s glagolom); 'pretjerano' nosi ADJ jammā"),
    "S089-A022-W004-S01": ("E1", P_NARROW + ": prvi ṣaffan → 'red'; 'sve' je pojačavajuća dopuna, drugi ṣaffan nosi 'do reda,'"),
    "S089-A024-W002-S01": ("E1", P_UNEXP + ": uzvično yā ispred layta nema zaseban token; želju nosi 'Kamo sreće'"),
    "S089-A024-W002-S02": ("E1", P_NARROW + ": layta → '\"Kamo sreće'; 'da' je bosanski uvod zavisne rečenice (inserted)"),
    "S089-A024-W004-S03": ("E1", P_UNEXP + ": posesivno -ī ('moj') nije izraženo; 'ovaj' ne znači 'moj'"),
    "S089-A025-W004-S01": ("E1", "apsolutni objekat ʿaḏāb ponavlja sadržaj glagola → 'kažnjavati,' (dosljedno 89:19–20)"),
    "S089-A025-W004-S02": ("E1", "-hu ('kaznom Njegovom') → poredba 'kao On'"),
    "S089-A026-W003-S01": ("E1", "waṯāq → 'u okove' ('u' kodira padež imenice)"),
    "S089-A026-W003-S02": ("E1", "-hu ('okivanjem Njegovim') → poredba 'kao On' (dosljedno 89:25)"),
}

if __name__ == "__main__":
    run("S089_El-Fedzr", D)
