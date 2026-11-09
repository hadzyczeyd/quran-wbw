# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 13."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
RESUMP = "resumptivni -hi → relativ 'što' koji nosi njegovu ulogu (COMMON: resumptivna zamjenica uz padežni oblik relativa)"
HUWAF = "huwa u man huwa + particip preveden glagolom: nema zasebne zamjenice ni pomoćnog → fused na glagol (COMMON 55.9, dosljedno unutar sure)"
BISA = "biʾsa/niʿma s kopulom 'je' (dosljedno 3:187 'ružno li je', 8:16, 11:98)"
P_GOV = "GOVERNED_PHRASE: bosanski prijedlog koji kodira padež imenice pripada njoj (COMMON)"
RADE = "'rade-sve': crtica pripada prethodnoj riječi; ṣanaʿū → 'rade-' [0,5], ḥattā → 'sve' [5,8]"

D = {
    "S013-A010-W009-S02": ("E1", "ponovljeno 'onaj koji' istog REL-a nosi taj REL (COMMON)"),
    "S013-A010-W010-S01": ("E1", HUWAF),
    "S013-A010-W013-S02": ("E1", "sārib → 'hodi.'; 'onaj koji' nosi REL man"),
    "S013-A011-W027-S02": ("E1", "lā → 'ne'; negativna konkordancija 'niko' ide imenici maradd (COMMON)"),
    "S013-A011-W028-S01": ("E1", "maradd → 'niko … može spriječiti;' (konkordancija na imenici s vlastitim segmentom)"),
    "S013-A014-W012-S01": ("E2", P_UNEXP + ": illā preoblikovano u poređenje 'kao što'; 'samo' je Mehanovićev dodatak"),
    "S013-A014-W017-S02": ("E1", "yabluġa i bāliġ Mehanović spaja u jedno 'stići' (dijeljeni token)"),
    "S013-A014-W019-S01": ("E2", "wa + NEG mā → aditivno-negativno 'ni' (COMMON 'ni … ni')"),
    "S013-A014-W020-S01": ("E2", "huwa → 'voda' + '-će' (particip preveden glagolom: pomoćni nosi zamjenicu, COMMON)"),
    "S013-A014-W021-S02": ("E2", "bāliġ → samo leksički 'stići' (pomoćni na huwa)"),
    "S013-A016-W012-S01": ("E1", "awliyāʾ → 'kao zaštitnike … one' ('one' je sama ta imenica kao objekat; 'koji' inserted)"),
    "S013-A016-W015-S01": ("E2", "li- → dativ 'sebi'"),
    "S013-A016-W015-S02": ("E2", P_GOV + ": anfus → 'sami sebi' i 'od sebe'"),
    "S013-A016-W032-S01": ("E1", "šurakāʾ → 'oni koje … pridruživali' (leksičko 'ortak' sadržano u 'pridruživali', dijeli s jaʿalū)"),
    "S013-A017-W007-S01": ("E1", "bi- mjere → 'onoliko'"),
    "S013-A017-W007-S02": ("E1", "qadar → 'koliko može da prihvati' (mjera)"),
    "S013-A017-W014-S02": ("E1", RESUMP),
    "S013-A018-W011-S01": ("E2", "posvojni li- → 'njihovo bilo,' (posvojni predikat, dosljedno 'pripada')"),
    "S013-A018-W026-S02": ("E2", BISA),
    "S013-A021-W006-S02": ("E1", RESUMP),
    "S013-A022-W017-S01": ("E1", "posvojni li- → glagoli 'će … pripasti' i 'čeka'; 'njima' nosi -hum (dosljedno 7:113, 22:9)"),
    "S013-A024-W005-S02": ("E2", BISA),
    "S013-A025-W012-S02": ("E1", RESUMP),
    "S013-A031-W036-S01": ("E1", RADE),
    "S013-A031-W036-S02": ("E1", RADE),
    "S013-A031-W043-S01": ("E1", RADE + "; 'dok … ne' također ḥattā"),
    "S013-A033-W002-S01": ("E1", HUWAF),
    "S013-A033-W024-S02": ("E2", INS + ": 'tako'"),
    "S013-A035-W012-S03": ("E2", P_UNEXP + ": drugi posvojni sufiks nije ponovljen (elipsa, dosljedno 10:58)"),
    "S013-A036-W012-S01": ("E1", "baʿḍ → 'nešto'"),
    "S013-A036-W012-S02": ("E1", P_GOV + ": 'od toga.'"),
    "S013-A040-W002-S01": ("E2", "immā (in + mā) → oba dijela nose 'Bilo da' (kao innamā → 'samo')"),
}

if __name__ == "__main__":
    run("S013_Er-Rad", D)
