# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 51."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_NARROW, P_UNEXP, run  # noqa: E402

CASE = "arapski prijedlog bez zasebnog bosanskog prijedloga: odnos nosi oblik riječi kojom upravlja (fused)"

D = {
    "S051-A013-W001-S01": ("E1", P_NARROW + ": yawma → 'dan'; 'onaj' i 'kada' su uvod rečenice (inserted; dosljedno 82:19)"),
    "S051-A018-W002-S01": ("E2", P_UNEXP + ": samostalno hum bez zamjenice i pomoćnog glagola (dosljedno 42:39, 107:6)"),
    "S051-A036-W006-S01": ("E1", CASE + " — min al-muslimīn → pridjev 'muslimansku'"),
    "S051-A040-W007-S01": ("E1", "mulīm → 'bio osudu zaslužio.'; 'je' nosi huwa (kopula s licem)"),
    "S051-A042-W006-S02": ("E1", "povratno -hi → padežni oblik relativa 'čega' (COMMON); 'god' je uopćavanje (inserted)"),
    "S051-A042-W009-S01": ("E1", P_UNEXP + ": poredbeno ka- nije izraženo ('u gnjilež pretvorio')"),
    "S051-A042-W009-S03": ("E1", "ramīm → 'u gnjilež' ('u' kodira padež imenice uz 'pretvorio')"),
    "S051-A043-W007-S01": ("E2", CASE + " — ḥattā ḥīn → akuzativ trajanja 'neko vrijeme!\"'"),
    "S051-A052-W002-S01": ("E1", "NEG mā → 'ni-' u 'nije' + negativna konkordancija 'ni' (dosljedno 46:13)"),
    "S051-A053-W001-S01": ("E2", "a- → 'li'; 'Jesu' je pomoćni glagol perfekta"),
    "S051-A053-W001-S02": ("E2", P_AUX + ": tawāṣaw → 'Jesu … jedni drugima oporučili?'"),
    "S051-A053-W002-S02": ("E2", "-hi (bihi) → objekat 'to'"),
}

if __name__ == "__main__":
    run("S051_Ez-Zarijat", D)
