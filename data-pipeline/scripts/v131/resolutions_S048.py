# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 48."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_UNEXP, run  # noqa: E402

LI = "namjerno li- → 'da'; ponovljeni 'da' ispred koordiniranih glagola u konjunktivu nosi isti li- (kao ponovljeni 'koji' istog REL-a)"
WA = "wa → 'i'; ponovljeno 'da' pripada li-"
WA0 = P_UNEXP + ": wa nije zasebno izražen; koordinaciju nosi ponovljeno 'da' (li-)"
SUBJ = "eksplicitna zamjenica izražava lice sadržano u glagolskom segmentu (nema PRON segmenta) → dio glagolskog izraza (dosljedno 80:18, 81:23, 87:6)"
AUX = "subjektni sufiks nosi pomoćni glagol koji gradi lični oblik (dosljedno 44:58 'bi')"

D = {
    "S048-A002-W001-S01": ("E1", LI),
    "S048-A002-W010-S01": ("E1", WA0),
    "S048-A002-W013-S01": ("E1", WA0),
    "S048-A003-W001-S01": ("E1", WA),
    "S048-A004-W008-S03": ("E2", AUX),
    "S048-A005-W001-S01": ("E1", LI),
    "S048-A005-W011-S01": ("E1", WA),
    "S048-A006-W001-S01": ("E1", WA),
    "S048-A006-W020-S02": ("E2", "sāʾat → 'grozno je to' ('to' nosi implicitni subjekat glagola)"),
    "S048-A009-W001-S01": ("E1", LI),
    "S048-A009-W004-S01": ("E1", WA),
    "S048-A009-W006-S01": ("E1", WA),
    "S048-A010-W023-S03": ("E2", SUBJ),
    "S048-A011-W025-S01": ("E2", SUBJ),
    "S048-A014-W005-S01": ("E2", SUBJ),
    "S048-A015-W009-S01": ("E1", "nattabiʿ → 'pratimo!\"'; 'da' je bosanski uvod dopune (inserted)"),
    "S048-A015-W011-S01": ("E2", P_UNEXP + ": an nije izražen; dopuna je infinitiv bez 'da'"),
    "S048-A015-W012-S02": ("E1", "subjektni -ū uz infinitiv nosi zajednički eksplicitni 'Oni' (dosljedno 46:20)"),
    "S048-A016-W011-S01": ("E1", "tuqātilūna → 'se … borite,'; 'da' je bosanski uvod dopune (inserted)"),
    "S048-A017-W017-S01": ("E2", SUBJ),
    "S048-A018-W005-S01": ("E1", "al- (poznati, upravo ti vjernici) → 'onim' (dosljedno 44:56 al- → 'one')"),
    "S048-A018-W010-S02": ("E2", SUBJ),
    "S048-A020-W013-S02": ("E1", LI),
    "S048-A020-W013-S03": ("E2", "takūna → 'bi to bio' ('to' nosi implicitni subjekat)"),
    "S048-A020-W016-S01": ("E1", WA),
    "S048-A022-W005-S03": ("E2", AUX),
    "S048-A022-W009-S02": ("E2", AUX),
    "S048-A023-W009-S01": ("E2", SUBJ),
    "S048-A025-W020-S01": ("E1", "an ('da ne' — da ih ne biste pogazili) → 'da' + ekspletivno 'ne' (nije NEG)"),
    "S048-A025-W037-S02": ("E2", AUX + "; 'su' u 'nisu'"),
    "S048-A027-W019-S02": ("E2", SUBJ),
    "S048-A027-W024-S01": ("E2", P_UNEXP + ": min u min dūni nema zaseban token (COMMON: min qabli/baʿdi)"),
    "S048-A028-W011-S02": ("E2", P_UNEXP + ": -hi u kullihi nije zasebno izražen ('svih' nosi kull)"),
    "S048-A029-W029-S02": ("E2", P_UNEXP + ": drugo maṯal nije zasebno izraženo; poređenje nosi 'kao' (ka-)"),
    "S048-A029-W036-S02": ("E2", SUBJ),
    "S048-A029-W042-S02": ("E2", SUBJ),
}

if __name__ == "__main__":
    run("S048_El-Feth", D)
