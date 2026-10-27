# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 59."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

HUM = "odvajajuća zamjenica hum → kopula koja nosi njeno lice + izraz isticanja (dosljedno 39:63 'će baš', 49:7 'su baš')"
CASEP = "ponovljeni bosanski prijedlog kodira padež druge imenice i pripada njoj (dosljedno 56:50, 58:22)"
INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"

D = {
    "S059-A005-W006-S01": ("E2", "drugi koordinirani glagol dobija samo svoj token; zajednički 'ste' nosi prvi (dosljedno 38:51, 52:25)"),
    "S059-A006-W001-S02": ("E1", "mā → stvarni bosanski relativni izraz 'onoga što' (COMMON REL)"),
    "S059-A007-W030-S02": ("E2", P_UNEXP + ": povratno -hu u ʿanhu nije zasebno izraženo (dosljedno 58:8 ʿanhu)"),
    "S059-A008-W005-S01": ("E1", "min → prvo 'iz'; drugo 'iz' pripada amwāl"),
    "S059-A008-W007-S02": ("E1", CASEP),
    "S059-A008-W008-S02": ("E2", "subjektni sufiks bez zamjenice i pomoćnog glagola → fused na glagolski prilog (dosljedno 37:27, 52:12, 58:18)"),
    "S059-A008-W017-S01": ("E1", HUM + " ('su, zaista,')"),
    "S059-A009-W030-S01": ("E1", HUM + " ('će sigurno')"),
    "S059-A009-W031-S02": ("E2", "particip mufliḥūn → glagolski izraz 'će … uspjeti.'; pomoćni 'će' gradi oblik (i nosi hum)"),
    "S059-A010-W017-S01": ("E1", INS + ": 'imalo'"),
    "S059-A011-W006-S01": ("E2", INS + ": 'kako' uvodi dopunsku rečenicu"),
    "S059-A014-W009-S01": ("E2", P_UNEXP + ": min u min warāʾi; 'iza' nosi warāʾ (kao min qabli/baʿdi, COMMON)"),
    "S059-A015-W005-S01": ("E2", INS + ": 'tu'"),
    "S059-A016-W007-S02": ("E2", INS + ": korelativno 'onda'"),
    "S059-A019-W007-S02": ("E1", "anfus → 'sami sebe', -hum → 'sebe' (fused; dosljedno 57:14, 39:15)"),
    "S059-A019-W009-S01": ("E1", HUM + " ('su baš')"),
    "S059-A020-W009-S01": ("E1", HUM + " ('baš su')"),
    "S059-A021-W007-S04": ("E1", P_UNEXP + ": objektni -hu preoblikovan u subjekat zavisne rečenice; nema zasebnog tokena"),
    "S059-A021-W008-S01": ("E1", "particip kao opisna rečenica → cijeli izraz 'kako je strahopoštovanja puno' (relativna preoblika N/ADJ)"),
    "S059-A024-W012-S01": ("E1", "fī → prvo 'na'; drugo 'na' pripada arḍ"),
    "S059-A024-W014-S03": ("E1", CASEP),
}

if __name__ == "__main__":
    run("S059_El-Hasr", D)
