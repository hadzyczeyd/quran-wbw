# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 19."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_GOV, P_NARROW, P_UNEXP, run  # noqa: E402

COORDV = "drugi koordinirani glagol nosi samo svoj token; zajednički pomoćni ostaje uz prvi (dosljedno 30:9, 15:19)"
COORDP = "subjektni sufiks drugog koordiniranog glagola → zajednički pomoćni (dosljedno 30:9, 15:19, 23:44)"
VERBAL = "imenica prevedena glagolskom da-rečenicom → 'da' + glagol pripadaju imenici (dosljedno 23:18, 26:221)"
COPF = "imenica prevedena okvirom 'da + kopula + imenica' → 'da' i kopula bez arapskog segmenta ostaju inserted (dosljedno 23:35, 26:52)"
DAV = "'da' u Mehanovićevoj perifrazi glagola pripada glagolskom izrazu (dosljedno 23:74, 26:3)"
SUBJ = P_UNEXP + ": prijedlog li- s korisnikom preoblikovanim u subjekat/objekat nije izražen (dosljedno 26:155, 26:211)"

D = {
    "S019-A006-W008-S01": ("E1", VERBAL),
    "S019-A012-W007-S01": ("E2", COPF + ": 'dok je … bio,'"),
    "S019-A015-W002-S01": ("E2", "salāmun ʿalayhi → leksikalizovano 'imao' i ponovljeno 'imat' (isti ʿalā za sva tri dana)"),
    "S019-A015-W002-S02": ("E2", "-hi (Jahja) kao nosilac sigurnosti → lični pomoćni 'je' i 'će'"),
    "S019-A021-W009-S01": ("E2", COPF + ": 'da bude'"),
    "S019-A021-W014-S01": ("E1", "amr maqḍiyy → supstantivirano 'određeno' (stvar određena)"),
    "S019-A024-W007-S01": ("E1", "kauzativno jaʿala → 'dao je da … poteče.'"),
    "S019-A024-W010-S01": ("E1", "sariyy → 'potok'"),
    "S019-A026-W014-S01": ("E1", VERBAL),
    "S019-A030-W002-S02": ("E2", "ime inna -ī → eksplicitno '\"Ja'; kopula 'sam' bez arapskog segmenta (inserted)"),
    "S019-A030-W007-S02": ("E1", COORDV),
    "S019-A032-W001-S02": ("E2", COPF + ": 'da … budem,'"),
    "S019-A034-W005-S01": ("E1", P_UNEXP + ": qawl nije zasebno preveden ('prava istina')"),
    "S019-A034-W006-S02": ("E1", "ḥaqq → 'prava istina'"),
    "S019-A035-W002-S01": ("E1", "kāna → kopula 'je'"),
    "S019-A035-W003-S01": ("E1", "mā kāna li-llāhi an → 'Ne|zamislivo je': li- (priliči) nosi '-zamislivo'"),
    "S019-A047-W004-S02": ("E1", DAV),
    "S019-A050-W003-S01": ("E1", P_UNEXP + ": partitivni min nije izražen; 'svako' nosi raḥma (svako dobro)"),
    "S019-A050-W004-S01": ("E1", "raḥma → 'svako dobro'"),
    "S019-A050-W005-S02": ("E1", "kauzativno jaʿala → 'učinismo da' (dosljedno 19:24)"),
    "S019-A050-W006-S01": ("E2", SUBJ),
    "S019-A052-W006-S02": ("E1", COORDV + "; 'Sebi' je cilj sadržan u qarraba"),
    "S019-A052-W006-S03": ("E2", "eksplicitno 'Mi' pokriva oba koordinirana glagola (dosljedno 15:16)"),
    "S019-A052-W007-S01": ("E1", VERBAL),
    "S019-A054-W008-S02": ("E2", P_NARROW + ": waʿd → 'obećanje'; 'dato' je dopuna (inserted)"),
    "S019-A054-W009-S02": ("E1", COORDV),
    "S019-A058-W021-S02": ("E1", COORDV),
    "S019-A058-W021-S03": ("E2", COORDP),
    "S019-A059-W003-S01": ("E2", P_UNEXP + ": baʿd sadržan u 'smijeniše'"),
    "S019-A059-W007-S02": ("E2", "ittabaʿū → 'pođoše;'"),
    "S019-A059-W008-S02": ("E2", P_GOV + ": 'za požudama'"),
    "S019-A060-W004-S02": ("E1", COORDV),
    "S019-A060-W005-S02": ("E1", COORDV),
    "S019-A062-W007-S02": ("E2", SUBJ),
    "S019-A062-W008-S01": ("E1", "rizq → pasivni izraz 'opskrbljeni biti.'; 'će' nosi -hum iz lahum"),
    "S019-A062-W008-S02": ("E2", P_UNEXP + ": posvojni -hum preoblikovan u subjekat pasiva (nosi ga 'će')"),
    "S019-A063-W004-S01": ("E1", DAV + ": 'Dat ćemo da … naslijedi'"),
    "S019-A067-W008-S01": ("E1", "okolnosno wa → 'a da' (a da nije bio)"),
    "S019-A068-W008-S01": ("E1", VERBAL),
    "S019-A070-W006-S01": ("E1", "awlā → 'najviše zaslužili'; 'su' nosi samostalno hum"),
    "S019-A070-W008-S01": ("E1", VERBAL),
    "S019-A072-W008-S01": ("E1", VERBAL + " (dosljedno 19:68)"),
    "S019-A079-W005-S02": ("E1", COORDV),
    "S019-A083-W004-S02": ("E1", "iza anna 'Mi' nosi ime; sufiks glagola bez pomoćnog → fused na 'šaljemo' (COMMON, dosljedno 70:6)"),
    "S019-A084-W002-S01": ("E1", DAV + ": 'traži da što prije'"),
    "S019-A094-W003-S02": ("E1", COORDV),
    "S019-A096-W004-S02": ("E1", COORDV),
    "S019-A096-W004-S03": ("E2", COORDP),
    "S019-A096-W007-S01": ("E2", SUBJ),
    "S019-A097-W004-S02": ("E2", "namjerni li- → 'da'; 'bi' uz glagol (COMMON)"),
    "S019-A097-W007-S02": ("E1", COORDV),
}

if __name__ == "__main__":
    run("S019_Merjem", D)
