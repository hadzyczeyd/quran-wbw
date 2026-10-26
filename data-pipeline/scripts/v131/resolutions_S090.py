# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 90."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_GOV, run  # noqa: E402

D = {
    "S090-A004-W002-S01": ("E2", P_AUX + ": ḫalaqnā → 'smo stvorili' (dosljedno 97:1, 108:1)"),
    "S090-A006-W002-S01": ("E2", P_AUX + ": ahlaktu → '\"Utrošio sam'"),
    "S090-A013-W001-S01": ("E1", "fakk (odvezivanje) → 'ropstva osloboditi,' (genitiv odvajanja pripada radnji oslobađanja)"),
    "S090-A013-W002-S01": ("E1", "raqaba (metonimija: rob) → 'Roba'"),
    "S090-A018-W002-S01": ("E2", "aṣḥāb → 'oni'; 's' kodira genitiv imenice maymana"),
    "S090-A018-W003-S02": ("E2", P_GOV + ": 's desne strane!'"),
    "S090-A019-W005-S01": ("E2", "aṣḥāb → 'oni'; 's' kodira genitiv imenice maš'ama"),
    "S090-A019-W006-S02": ("E2", P_GOV + ": 's lijeve strane,'"),
}

if __name__ == "__main__":
    run("S090_El-Beled", D)
