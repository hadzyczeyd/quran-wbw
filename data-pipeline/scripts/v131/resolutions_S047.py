# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 47."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

HATTA = "ekspletivno 'ne' u 'dok … ne' pripada ḥattā (nije NEG; dosljedno 41:53, 43:83, 97:5, 102:2)"
MIN = P_UNEXP + ": min u min qabli/baʿdi nema zaseban token; 'prije/nakon' nosi qabl/baʿd (dosljedno 41–43, 98:4)"
SHARED_P = "subjektni sufiks drugog koordiniranog glagola nosi zajednički pomoćni glagol; particip nema lica (dosljedno 84:25, 46:27)"

D = {
    "S047-A003-W014-S02": ("E2", "ka-ḏālika: DEM → 'Eto,', ka- → 'tako' (dosljedno 42:3, 44:54)"),
    "S047-A004-W007-S01": ("E2", HATTA),
    "S047-A004-W008-S01": ("E2", P_UNEXP + ": iḏā poslije ḥattā nije zasebno preveden"),
    "S047-A004-W009-S01": ("E2", "aṯxana → 'uništite,'; ekspletivno 'ne' nosi ḥattā"),
    "S047-A004-W017-S01": ("E2", HATTA),
    "S047-A004-W018-S01": ("E2", "waḍaʿa → 'spusti\"'; ekspletivno 'ne' nosi ḥattā"),
    "S047-A009-W003-S02": ("E1", "subjektni sufiks na finitnom 'mrze'; 'oni' nosi ime anna (dosljedno 45:19)"),
    "S047-A010-W010-S01": ("E2", MIN),
    "S047-A010-W015-S02": ("E1", "predikatni li- → dativ 'nevjernicima' + glagol pripadanja 'pripada.' (dosljedno 45:37)"),
    "S047-A012-W011-S01": ("E1", "min taḥtihā → 'kroz' (dosljedno 85:11)"),
    "S047-A012-W013-S02": ("E1", "ponovljeni 'koji' istog REL-a nosi taj REL (COMMON)"),
    "S047-A015-W035-S01": ("E2", P_NARROW + ": ka- → 'kao'; 'isti' je pojačanje (inserted)"),
    "S047-A016-W005-S01": ("E2", "ḥattā iḏā → 'čim' (fused); 'ali' je Mehanovićev veznik (inserted)"),
    "S047-A016-W009-S01": ("E1", "min ʿindika → 'od' (ʿind fused, kao taḥt → 'kroz')"),
    "S047-A016-W014-S01": ("E2", "māḏā → '\"Šta ono' (ḏā nosi 'ono')"),
    "S047-A018-W011-S02": ("E1", "annā lahum ḏikrāhum ('kako/čemu će im') → 'kakve … koristi'"),
    "S047-A018-W015-S01": ("E1", "ḏikrā (primanje pouke) → 'od prihvatanja opomene' (leksičko značenje; 'od' kodira padež)"),
    "S047-A020-W023-S01": ("E2", P_UNEXP + ": ʿalā gradi arapski pasivni particip maġšiyy ʿalayhi; bosanski particip nema prijedloga"),
    "S047-A020-W023-S02": ("E2", P_UNEXP + ": povratno -hi u maġšiyy ʿalayhi nema zaseban token"),
    "S047-A022-W009-S03": ("E1", SHARED_P),
    "S047-A023-W007-S01": ("E2", P_UNEXP + ": abṣār nije zasebno preveden ('slijepim ih učinio')"),
    "S047-A025-W005-S01": ("E1", "adbār (prijašnje stanje) → 'onome … čemu … bili,'; 'su' nosi -him"),
    "S047-A025-W006-S01": ("E2", MIN),
    "S047-A028-W007-S03": ("E1", SHARED_P),
    "S047-A031-W004-S02": ("E1", P_NARROW + ": mujāhidīn → 'borce'; 'na Allahovom putu' je Mehanovićevo objašnjenje (inserted)"),
    "S047-A032-W010-S01": ("E2", MIN),
    "S047-A036-W008-S03": ("E1", SHARED_P),
}

if __name__ == "__main__":
    run("S047_Muhammed", D)
