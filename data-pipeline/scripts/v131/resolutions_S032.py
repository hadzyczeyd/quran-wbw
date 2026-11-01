# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 32."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, run  # noqa: E402

KUNTUM = "kāna + imperfekt: -ūna nosi zajednički pomoćni 'ste/su' (dosljedno 52:16, 66:7, 77:43)"
COORD = "drugi koordinirani glagol dobija samo svoj token; zajednički pomoćni 'su' ostaje uz prvi, sufiks fused (COMMON)"
RESUMP = "resumptivni -hum: ulogu nosi padežni oblik relativnog izraza ('One/one koji'), pa se veže na taj token (COMMON, kao 85:11)"

D = {
    "S032-A004-W017-S01": ("E2", "min dūni → fused na 'osim' (COMMON)"),
    "S032-A005-W016-S02": ("E1", "mā (ono što se broji) → 'vremena' u nominalizaciji 'računanju vremena'"),
    "S032-A010-W008-S01": ("E1", P_AUX + ": 'biti' gradi pasivni futur 'ćemo … stvoreni biti\"' (dosljedno 34:7)"),
    "S032-A012-W001-S02": ("E2", "law → samo 'da' (dosljedno 34:31, 39); 'je' pripada optativnoj konstrukciji glagola"),
    "S032-A012-W002-S01": ("E2", "tarā → 'ti je vidjeti' (dativ + je + infinitiv)"),
    "S032-A014-W004-S01": ("E2", P_AUX + ": liqāʾ glagolski preoblikovan u 'da ćete … doživjeti'"),
    "S032-A014-W014-S02": ("E2", KUNTUM),
    "S032-A017-W013-S02": ("E2", KUNTUM),
    "S032-A019-W004-S02": ("E1", COORD),
    "S032-A019-W004-S03": ("E1", COORD),
    "S032-A019-W006-S03": ("E2", RESUMP),
    "S032-A019-W012-S02": ("E2", KUNTUM),
    "S032-A020-W004-S03": ("E2", RESUMP),
    "S032-A020-W021-S02": ("E2", KUNTUM),
    "S032-A023-W005-S02": ("E2", "negativna konkordancija 'nimalo' bez vlastitog segmenta → zabrana lā (COMMON)"),
    "S032-A025-W008-S02": ("E2", "REL → stvarni relativni izraz 'onome … čemu' ('čemu' nosi i resumptivno -hi)"),
    "S032-A025-W011-S02": ("E2", KUNTUM),
}

if __name__ == "__main__":
    run("S032_Es-Sedzda", D)
