# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 69."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

FUSED = "subjektni sufiks bez zamjenice i pomoćnog glagola → fused na glagolski oblik (dosljedno u suri; 61:11, 62:9)"
QALIL = P_UNEXP + ": mā u qalīlan mā; uzvično 'kako' je Mehanovićev dodatak (inserted, dosljedno 67:23)"

D = {
    "S069-A005-W003-S03": ("E1", "subjektni -ū → pomoćni glagol 'je' koji nosi lice (COMMON 55.9; kolektiv Semud u jednini)"),
    "S069-A006-W003-S03": ("E1", FUSED + " ('uništen')"),
    "S069-A014-W004-S03": ("E1", FUSED + " ('zdrobljena,')"),
    "S069-A015-W003-S02": ("E1", "al-wāqiʿa → 'Događaj'; 'strahoviti' je Mehanovićev pridjev bez segmenta (inserted); " + P_NARROW),
    "S069-A026-W003-S01": ("E1", P_UNEXP + ": upitno mā u mā ḥisābiyah svedeno na imensku dopunu; 'za' traži bosanski glagol 'saznati' (inserted)"),
    "S069-A030-W002-S04": ("E1", P_UNEXP + ": objektni -hu drugog glagola nije ponovljen; 'ga' nosi -hu prvog glagola (dosljedno koordinaciji 59:5)"),
    "S069-A035-W002-S01": ("E1", "posvojno li- → glagol posjedovanja 'nema' (dosljedno 68:38 'ćete imati'); 'on' nosi -hu"),
    "S069-A041-W006-S01": ("E1", QALIL),
    "S069-A042-W005-S01": ("E1", QALIL),
    "S069-A046-W002-S03": ("E1", FUSED + " ('presjekli,')"),
    "S069-A047-W005-S01": ("E1", "ʿan traži arapski glagol; bosansko 'odbraniti' uzima direktni objekat 'ga' (COMMON) → unexpressed; 'od toga' inserted"),
}

if __name__ == "__main__":
    run("S069_El-Hakka", D)
