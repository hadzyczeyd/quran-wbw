# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 21 (21:67: odobrena zamjena teksta — prijevod Besima Korkuta, MEHANOVIC_OVERRIDES.json)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_GOV, P_NARROW, P_UNEXP, run  # noqa: E402

MI = "subjektni sufiks → samo eksplicitna zamjenica; pomoćni pripada glagolskom obliku (COMMON, dosljedno 23:12, 20:40)"
COORDP = "subjektni sufiks drugog koordiniranog glagola → zajednički pomoćni 'smo' (dosljedno 30:9, 15:19, 23:44)"
MINDUNI = "min dūni → fused na 'pored/osim/umjesto' (dosljedno objavljenim surama)"
INS = P_NARROW + "; pojačivač/dopuna bez arapskog segmenta ostaje inserted (COMMON)"
REPP = "ponovljena prijedložna funkcija pred koordiniranim članovima nosi isti segment (dosljedno 57:1, 15:42)"
LALLA = "laʿalla bez zamjenice: -hum i -ūna → 'bi' (dosljedno 30:46, 20:130)"
AFTERL = "iza laʿalla 'oni' nosi ime (-hum); sufiks glagola → pomoćni 'bi' (dosljedno 20:113)"
COPF = "okvir 'da + kopula + imenica' bez arapskog segmenta ostaje inserted (dosljedno 19:21, 19:32)"
NAKAD = "vremenska imenica + rečenica: 'kad(a)' uvodi rečenicu u iḍāfi (dosljedno 26:87, 40:16)"
OBJV = "objekat sadržan u značenju glagola/participa ('Nama', 'Allahu') pripada izrazu (dosljedno 23:59, 23:92)"

D = {
    "S021-A003-W002-S02": ("E1", P_UNEXP + ": posvojni -hum uz qulūb nije zasebno izražen"),
    "S021-A006-W001-S01": ("E1", "NEG mā → 'ni-' u 'nije' (granica ni|je)"),
    "S021-A006-W002-S01": ("E1", P_AUX + ": 'je' iz 'nije' gradi perfekt 'povjerovalo,'"),
    "S021-A006-W006-S02": ("E1", MI),
    "S021-A008-W002-S02": ("E1", MI),
    "S021-A009-W004-S03": ("E2", COORDP),
    "S021-A009-W007-S03": ("E2", COORDP),
    "S021-A013-W004-S01": ("E1", REPP + ": dativ 'uživanjima' i 'domovima'"),
    "S021-A015-W001-S02": ("E2", P_UNEXP + ": NEG u leksikalizovanom mā zāla (trajanje) nije izražen negacijom"),
    "S021-A016-W002-S02": ("E1", MI),
    "S021-A017-W009-S01": ("E1", "in (Mehanović: odricanje) → 'ne'; 'ali' bez arapskog segmenta (inserted)"),
    "S021-A024-W003-S01": ("E2", MINDUNI),
    "S021-A026-W006-S01": ("E1", "bal → 'A'; 'samo' je pojačivač (inserted)"),
    "S021-A027-W002-S01": ("E1", INS + ": 'to'"),
    "S021-A029-W006-S01": ("E2", MINDUNI),
    "S021-A029-W008-S02": ("E1", "ḏālika (taj) → pokazno 'onoga'"),
    "S021-A030-W010-S03": ("E1", MI),
    "S021-A031-W001-S03": ("E1", MI),
    "S021-A031-W013-S02": ({"targets_from": "E1", "drop": ["oni"], "add": ["S021-A031-B022"]}, AFTERL),
    "S021-A034-W002-S02": ("E1", MI),
    "S021-A035-W005-S02": ("E1", "nablū → 'Mi stavljamo'; 'na kušnju' nosi fitnatan"),
    "S021-A036-W006-S01": ("E2", "yattaḫiḏūnaka huzuwan → povratni 'se rugaju:' (dosljedno 23:110)"),
    "S021-A039-W001-S01": ({"targets_from": "E1", "drop": ["bi"]}, "law → samo 'kad'; 'samo' je pojačivač (COMMON: law → 'kad/da')"),
    "S021-A039-W002-S01": ("E2", P_AUX + ": 'bi … znali'"),
    "S021-A039-W005-S01": ("E2", NAKAD),
    "S021-A039-W011-S02": ("E1", P_UNEXP + ": druga negacija nije ponovljena; jedno 'ne' nosi prvi lā"),
    "S021-A043-W005-S01": ("E2", MINDUNI),
    "S021-A044-W002-S02": ("E1", MI),
    "S021-A047-W004-S01": ("E1", "vremensko li- → 'kad'; 'bude,' bez arapskog segmenta (inserted)"),
    "S021-A047-W011-S01": ("E1", "kāna → 'bude'; eksplicitni subjekat 'nešto' nosi lice sadržano u glagolu"),
    "S021-A047-W016-S02": ("E1", MI),
    "S021-A048-W002-S02": ("E1", MI),
    "S021-A049-W005-S02": ("E2", "samostalno hum → kopula 'budu' (COMMON); ponovljeno 'koji' nosi REL"),
    "S021-A049-W007-S02": ("E1", INS + ": 'oživljavanja'"),
    "S021-A051-W002-S02": ("E1", MI),
    "S021-A052-W003-S01": ("E1", REPP + ": dativ 'ocu' i 'narodu'"),
    "S021-A052-W011-S01": ("E1", INS + ": 'tako'"),
    "S021-A058-W006-S02": ("E1", LALLA),
    "S021-A058-W008-S02": ("E1", LALLA),
    "S021-A063-W009-S01": ("E2", "yanṭiqūna → 'umiju govoriti\",' (modalni finitni oblik, dosljedno 26:73)"),
    "S021-A066-W003-S01": ("E2", MINDUNI),
    "S021-A066-W009-S01": ("E1", "šayʾan → neodređeno 'kakvu'"),
    "S021-A067-W005-S01": ("E2", MINDUNI),
    "S021-A074-W002-S03": ("E1", "resumptivni -hu → dativ istaknutog 'Lutu' (COMMON: resumptivna → oblik izraza)"),
    "S021-A075-W005-S01": ("E2", "partitivni min uz genitiv → 'od'"),
    "S021-A075-W006-S02": ("E2", "ṣāliḥīn → 'onih dobrih.' (particip = oni koji …)"),
    "S021-A078-W012-S03": ("E1", MI),
    "S021-A079-W011-S01": ("E2", "'da … slave i veličaju:' ('da' uz glagol, dublet jedne riječi)"),
    "S021-A079-W013-S03": ("E1", MI),
    "S021-A082-W010-S03": ("E1", MI),
    "S021-A084-W006-S01": ("E1", P_UNEXP + ": eksplikativni min nije izražen"),
    "S021-A084-W010-S03": ("E2", P_UNEXP + ": -hum u miṯlahum nije zasebno izražen"),
    "S021-A084-W015-S02": ("E1", COPF + ": 'da bude'"),
    "S021-A084-W016-S03": ("E2", OBJV),
    "S021-A085-W005-S01": ("E1", "kull s tanwīnom (svaki od njih) → 'svi … oni'"),
    "S021-A087-W011-S01": ("E2", INS + ": 'poslije'"),
    "S021-A090-W003-S03": ("E2", COORDP),
    "S021-A090-W006-S03": ("E2", COORDP),
    "S021-A090-W011-S01": ("E2", "yusāriʿūna → 'se trudili … što više … učine'"),
    "S021-A090-W012-S01": ("E2", "fī uz sāraʿa → 'da' koji uvodi dopunu (dosljedno 23:61)"),
    "S021-A091-W008-S03": ("E2", COORDP),
    "S021-A091-W010-S01": ("E1", COPF + ": 'da budu'"),
    "S021-A094-W009-S01": ("E1", P_UNEXP + ": li- s imenicom preoblikovanom u subjekat (dosljedno 19:62)"),
    "S021-A095-W004-S02": ("E1", MI),
    "S021-A097-W004-S01": ("E1", P_UNEXP + ": nastavno fa- nema tokena; 'tada' nosi iḏā"),
    "S021-A097-W012-S02": ("E1", MI),
    "S021-A097-W013-S01": ("E1", P_UNEXP + ": fī ġaflatin preoblikovano u pridjev 'ravnodušni'"),
    "S021-A098-W004-S01": ("E2", MINDUNI),
    "S021-A104-W001-S01": ("E2", NAKAD),
    "S021-A104-W011-S01": ("E1", INS + ": 'iz ništa'"),
    "S021-A105-W002-S02": ("E1", MI),
    "S021-A106-W006-S01": ("E2", OBJV),
    "S021-A107-W004-S01": ("E1", "raḥmatan (akuzativ svrhe) → 'kao milost' (dosljedno 26:29 'kao boga')"),
    "S021-A109-W004-S02": ("E1", MI),
    "S021-A109-W005-S01": ("E1", P_UNEXP + ": ʿalā u idiomu ʿalā sawāʾin; idiom nosi sawāʾ"),
    "S021-A111-W008-S01": ("E2", INS + ": 'izvjesno'"),
}

if __name__ == "__main__":
    run("S021_El-Enbija", D)
