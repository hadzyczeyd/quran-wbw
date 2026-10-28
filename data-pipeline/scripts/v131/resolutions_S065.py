# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 65."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_UNEXP, run  # noqa: E402

COORD = "drugi koordinirani glagol dobija samo svoj token; zajednički pomoćni glagol nosi prvi (dosljedno 38:51, 52:25, 59:5)"

D = {
    "S065-A002-W007-S02": ("E1", "subjektni -ū drugog koordiniranog glagola → fused na 'rastavite,'; zajedničko 'vi' nosi prvi glagol (dosljedno 59:5)"),
    "S065-A002-W017-S01": ("E2", "pasiv yūʿaẓu imenski preoblikovan → 'savjet'; 'je' je kopula imenske rečenice (inserted, COMMON)"),
    "S065-A003-W015-S02": ("E1", "posvojno -hi (Njegov) izraženo kao vršilac u 'je odlučio;' — pomoćni glagol i particip nose 3. l. jd."),
    "S065-A005-W012-S02": ("E2", COORD + " ('uvećati.')"),
    "S065-A006-W015-S02": ("E2", "anfiqū (nafaqa = izdržavanje) → 'snosite troškove … izdržavanja'"),
    "S065-A006-W016-S01": ("E2", "ʿalā bez zasebnog prijedloga → padežni (posvojni) oblik 'njihovog' koji nosi -hinna (COMMON)"),
    "S065-A007-W008-S02": ("E2", P_UNEXP + ": resumptivno -hi u ʿalayhi; nominativno 'koji' nosi REL, ne padežnu ulogu zamjenice"),
    "S065-A008-W001-S02": ("E1", "kaʾayyin → 'koliko li'; 'samo' je pojačivač bez arapskog segmenta (inserted, COMMON)"),
    "S065-A008-W004-S01": ("E1", "ʿatat → 'se … ogluši?!'; 'bi' (Mehanovićev egzistencijalni aorist) bez zasebnog segmenta ostaje inserted"),
    "S065-A008-W012-S02": ("E2", COORD + " ('kaznili')"),
    "S065-A011-W019-S02": ("E2", COORD + " ('činio,')"),
    "S065-A012-W008-S02": ("E2", P_UNEXP + ": -hunna u mithlahunna; 'isto toliko' nosi mithl, zamjenica nije zasebno izražena"),
    "S065-A012-W010-S01": ("E2", "DET al- unexpressed (COMMON); 'Njegova' je Mehanovićeva dopuna (inserted)"),
}

if __name__ == "__main__":
    run("S065_Et-Talak", D)
