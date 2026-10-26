# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 38."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

MI = "subjektni sufiks nosi eksplicitna zamjenica ('Mi', 'oni', 'Ja'); pomoćni glagol pripada glagolskom obliku (dosljedno 44:3)"
SHARED = "drugi perfekt dijeli pomoćni 'smo' (dosljedno 84:25, 46:27)"
NEK = P_NARROW + ": neodređenost ('jedne', 'jednom') je Mehanovićeva dopuna (inserted)"
PRON0 = P_UNEXP + ": -hum uz kull/miṯl nije zasebno izražen (dosljedno 48:28, 36:36)"
CASE = "arapski prijedlog bez zasebnog bosanskog prijedloga: odnos nosi oblik riječi kojom upravlja (fused)"
COP = P_NARROW + ": eksplicitna zamjenica/ime nosi subjekat; kopula je inserted"

D = {
    "S038-A003-W002-S02": ("E2", MI),
    "S038-A003-W007-S03": ("E2", MI),
    "S038-A004-W004-S01": ("E1", "munḏir → 'jedan … da … upozorava,' (particip kao osoba); 'ih' je dodani objekat (inserted)"),
    "S038-A007-W007-S01": ("E1", "NEG in → 'nije' + konkordancija 'ništa' (dosljedno 37:15)"),
    "S038-A007-W009-S01": ("E1", "restriktivno illā → 'drugo već'"),
    "S038-A008-W008-S01": ("E2", "fī šakk → glagol 'sumnjaju' (fused; dosljedno 50:15)"),
    "S038-A011-W005-S01": ("E2", CASE + " — min al-aḥzāb → genitiv 'udruženih skupina'"),
    "S038-A016-W004-S01": ("E2", CASE + " — lanā → akuzativ 'nas,'"),
    "S038-A017-W011-S01": ("E2", "relativna preoblika awwāb 'koji se uvijek Allahu pokajnički obraćao.' (COMMON)"),
    "S038-A020-W003-S03": ("E2", SHARED),
    "S038-A024-W006-S01": ("E2", "ilā (pripojiti) → 'da … doda'; 'ovcama' nosi naʿāj"),
    "S038-A024-W027-S02": ("E2", MI),
    "S038-A025-W001-S03": ("E2", MI),
    "S038-A027-W002-S02": ("E2", MI),
    "S038-A028-W013-S01": ("E2", P_NARROW + ": ka- → 'kao'; 'isto' je pojačanje (inserted)"),
    "S038-A030-W001-S03": ("E2", MI),
    "S038-A030-W006-S02": ("E1", P_UNEXP + ": ime inna -hu bez zasebnog tokena (dosljedno 84:14)"),
    "S038-A031-W004-S03": ("E2", NEK),
    "S038-A032-W003-S02": ("E2", "subjektni -tu na finitnom glagolu; 'ja' nosi ime inna (dosljedno 46:15)"),
    "S038-A034-W002-S02": ("E2", MI),
    "S038-A034-W004-S03": ("E2", SHARED),
    "S038-A035-W010-S01": ("E2", "li- (pripasti nekome) → glagol posjedovanja 'imati!' (dosljedno 88:6)"),
    "S038-A036-W001-S03": ("E2", MI),
    "S038-A043-W001-S03": ("E2", MI),
    "S038-A043-W004-S03": ("E2", PRON0),
    "S038-A044-W013-S02": ("E1", P_UNEXP + ": ime inna -hu bez zasebnog tokena (dosljedno 84:14, 38:30)"),
    "S038-A046-W003-S02": ("E2", NEK),
    "S038-A047-W001-S03": ("E2", MI),
    "S038-A058-W002-S01": ("E1", CASE + " — min → pridjev 'slične' (dosljedno 51:36)"),
    "S038-A060-W001-S02": ("E2", MI),
    "S038-A063-W005-S02": ("E2", "-hum (ʿanhum) postaje subjekat bosanske preoblike; lice nosi pomoćni dio 'su' u 'nisu'"),
    "S038-A063-W006-S02": ("E2", P_NARROW + ": abṣār → 'vida'; 'nam' je dopuna (inserted)"),
    "S038-A065-W002-S01": ("E1", "inna u innamā → 'samo' (dosljedno 88:21)"),
    "S038-A065-W003-S01": ("E2", COP),
    "S038-A067-W002-S01": ("E2", COP),
    "S038-A069-W003-S01": ("E2", P_UNEXP + ": posvojni li- u preoblici 'nisam znao' nije izražen"),
    "S038-A073-W003-S02": ("E2", PRON0),
    "S038-A075-W008-S02": ("E2", MI),
    "S038-A077-W002-S01": ("E2", "fa → 'onda'; 'E' je uzvik (inserted)"),
    "S038-A077-W004-S02": ("E2", P_UNEXP + ": inna nije izražena ('da si' je optativ)"),
    "S038-A079-W006-S02": ("E2", MI),
    "S038-A081-W004-S02": ("E1", P_NARROW + ": maʿlūm → 'određenog.\"'; 'već' je pojačanje (inserted)"),
    "S038-A084-W002-S03": ("E2", "zakletveni nominativ al-ḥaqq → '\"Istinom se kunem' (zakletvu nosi sama imenica)"),
    "S038-A087-W001-S01": ("E2", P_UNEXP + ": NEG in u restrikciji preoblikovanoj u afirmaciju; 'doista' nosi illā"),
    "S038-A087-W002-S01": ("E2", COP),
}

if __name__ == "__main__":
    run("S038_Sad", D)
