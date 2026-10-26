# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 45."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_GOV, P_UNEXP, run  # noqa: E402

DUB = "dublet jedne riječi s veznikom unutar izraza ('ajeti i znakovi', 'nagrađeni ili kažnjeni'): cijeli izraz, uključujući veznik, pripada segmentu (COMMON)"
LAM = "predikatni/posvojni la- (lahum ʿaḏāb) → glagol preoblike 'čeka'/'znaju'/'pripada' (dosljedno 42:26, 85:11, 88:6); zamjenica nosi svoj padežni oblik"
FIN = "subjektni sufiks nosi finitni glagolski oblik; eksplicitno 'oni/im' već nosi samostalnu zamjenicu (dosljedno 41)"
HUZ = "huzuw ponavlja sadržaj glagola → dijeli glagolski izraz 'se ruga(li)' (apsolutni objekat, COMMON)"

D = {
    "S045-A005-W001-S02": ("E2", P_GOV + ": 'u smjeni' (fī iz 45:4 elidiran; padežni prijedlog pripada imenici)"),
    "S045-A006-W002-S01": ("E1", DUB),
    "S045-A007-W002-S01": ("E2", "li- upravlja kull → dativ 'svakom' nosi li-; 'lašcu,' samo slaže"),
    "S045-A009-W003-S01": ("E1", "partitivno min ('nešto od') → 'neke'"),
    "S045-A009-W007-S01": ("E1", HUZ),
    "S045-A009-W009-S01": ("E1", LAM),
    "S045-A010-W017-S02": ("E1", LAM),
    "S045-A011-W005-S02": ("E1", DUB),
    "S045-A011-W007-S01": ("E1", LAM),
    "S045-A013-W006-S02": ("E1", "drugi mā (wa-mā fī al-arḍ) dijeli zajednički relativni izraz 'ono što' koji obuhvata oba člana"),
    "S045-A017-W013-S01": ("E1", DUB + "; 'zbog' kodira razlog"),
    "S045-A019-W003-S02": ("E1", FIN),
    "S045-A019-W010-S02": ("E1", P_UNEXP + ": -hum u baʿḍuhum nije zasebno izražen; 'jedni drugima' nosi baʿḍ … baʿḍ"),
    "S045-A021-W013-S02": ("E2", "posvojno -hum preoblikovano u subjekat 'da će … biti isti'; lice 3MP nosi samo 'će'"),
    "S045-A021-W014-S03": ("E2", "posvojno -hum (mamātuhum) ista preoblika; lice nosi 'će'"),
    "S045-A022-W006-S03": ("E1", DUB),
    "S045-A023-W008-S01": ("E1", "ʿalā ʿilm ('uz znanje') → pridjev 'svjestan' (ʿalā i ʿilm zajedno)"),
    "S045-A024-W014-S01": ("E1", LAM),
    "S045-A024-W021-S02": ("E1", FIN),
    "S045-A025-W016-S01": ("E1", "relativna preoblika participa ṣādiqīn → 'istina to što govorite.\"' (COMMON)"),
    "S045-A028-W004-S01": ("E2", "particip jāṯiya (ḥāl) preveden rečenicom 'kako kleče;' — cijeli izraz pripada N segmentu"),
    "S045-A028-W011-S01": ("E1", DUB),
    "S045-A031-W010-S03": ("E1", "-tum od kuntum nosi zajednički pomoćni 'ste' (dosljedno 84:25 zajednički 'budu')"),
    "S045-A032-W010-S02": ("E1", "povratno -hā (fīhā) nosi padežni oblik teme 'u Čas' (dosljedno 42:21 'zulumćarima')"),
    "S045-A032-W020-S02": ("E1", "NEG mā → 'ni' [0,2] u 'nismo'"),
    "S045-A032-W021-S01": ("E1", "naḥnu → eksplicitno 'mi' + kopulativni dio 'smo' [2,5] u 'nismo' (dosljedno 86:14)"),
    "S045-A034-W011-S02": ("E1", "NEG mā → 'ne' [0,2] u 'neće'"),
    "S045-A034-W014-S01": ("E1", "nāṣirīn glagolizovan → 'pomoći … će moći,' ('će' [2,4] u 'neće')"),
    "S045-A035-W001-S01": ("E1", "dhālikum → pokazni dio 'to' [2,4] u 'zato'"),
    "S045-A035-W002-S01": ("E1", "uzročno bi- → 'za' [0,2] u 'zato'"),
    "S045-A035-W004-S01": ("E1", DUB),
    "S045-A035-W006-S01": ("E1", HUZ),
    "S045-A035-W016-S02": ("E1", FIN),
    "S045-A037-W001-S02": ("E1", LAM),
}

if __name__ == "__main__":
    run("S045_El-Dzasija", D)
