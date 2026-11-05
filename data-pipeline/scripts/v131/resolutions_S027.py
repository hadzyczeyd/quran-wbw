# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 27."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
COORDV = "drugi koordinirani glagol nosi samo svoj token; zajednički pomoćni/modalni ostaje uz prvi (dosljedno 30:9, 19:30)"
MINDUNI = "min dūni → fused na 'a ne/mimo/umjesto' (dosljedno objavljenim surama)"
REPP = "ponovljeni prijedlog pred koordiniranim članovima nosi isti segment (dosljedno 57:1, 21:13)"
SUBJ = "samostalna zamjenica kao subjekat → eksplicitna zamjenica; kopula bez arapskog segmenta ostaje inserted (COMMON)"
IMEINNA = "ime inna → eksplicitna/pokazna zamjenica; kopula bez arapskog segmenta inserted (dosljedno 19:30)"
AUXP = "subjektni sufiks bez eksplicitne zamjenice → pomoćni glagol koji nosi lice (COMMON 55.9)"
AGREE = P_UNEXP + ": Mehanović glagol slaže s imenicom 'narod/većina' (3. l. jd.); subjektni sufiks nije zasebno izražen"
NEBILI = "laʿallakum … 'ne bi li': laʿalla → 'ne … li', glagol i sufiksi → 'bi' (dosljedno 46:27, 20:44)"
INNAMA = "innamā: inna i mā zajedno nose restriktivno 'samo/jedino' (većina objavljenih sura)"

D = {
    "S027-A007-W006-S01": ("E1", P_AUX + ": 'Vidio sam'"),
    "S027-A007-W010-S02": ("E2", INS + ": 'kakvu,'"),
    "S027-A008-W003-S01": ("E2", "pasiv nūdiya → 'je dozivao:'; 'neki glas' je Mehanovićev dodatak (inserted)"),
    "S027-A009-W003-S01": ("E1", "samostalno anā → 'Ja' i kopula 'sam'[0,3] (granica na crtici)"),
    "S027-A009-W004-S01": ("E1", "Allāh → '-Allah,'[3,10]"),
    "S027-A012-W008-S01": ("E2", "ġayr → 'neće'; 'ali' bez arapskog segmenta (inserted)"),
    "S027-A014-W003-S02": ("E1", P_AUX + ": 'su … vjerovali'"),
    "S027-A014-W003-S03": ("E1", "objektni -hā (znakovi) → dopunska rečenica 'da su istiniti,'"),
    "S027-A017-W009-S01": ("E1", P_AUX + ": pasiv 'bili su u stroju vođeni,'"),
    "S027-A018-W017-S01": ("E1", "okolnosno wa → 'a da' (dosljedno 19:67)"),
    "S027-A020-W005-S01": ("E1", "idiom mā lī → '\"Zašto' (dosljedno 15:32)"),
    "S027-A020-W005-S02": ("E1", "-ya u idiomu mā lī → '\"Zašto' (dosljedno 15:32)"),
    "S027-A022-W005-S01": ("E1", P_AUX + ": 'Doznao sam'"),
    "S027-A024-W005-S01": ("E1", MINDUNI),
    "S027-A024-W012-S02": ("E2", COORDV),
    "S027-A025-W007-S01": ("E1", REPP),
    "S027-A025-W009-S03": ("E1", "arḍ → 'Zemlji'"),
    "S027-A028-W011-S02": ("E2", AUXP),
    "S027-A030-W004-S03": ("E2", IMEINNA),
    "S027-A032-W006-S02": ("E2", P_UNEXP + ": posvojni -ī nije izražen ('u ovom slučaju')"),
    "S027-A032-W012-S01": ("E2", "tašhadūn (prisustvo) → 'bez'"),
    "S027-A033-W002-S01": ("E1", SUBJ),
    "S027-A033-W009-S01": ("E1", "ilā (do tebe je) sadržan u 'odlučuješ.'"),
    "S027-A035-W002-S01": ("E1", P_AUX + ": particip preveden futurom 'Poslat ću'"),
    "S027-A036-W005-S02": ("E1", "'da … nudite?!' ('da' uz glagol, dosljedno 19:47)"),
    "S027-A040-W027-S01": ({"targets_from": "E1", "drop": ["biti."]},
                           "akfuru → 'ću nezahvalan'; kopula 'biti.' bez segmenta (inserted, dosljedno 23:35)"),
    "S027-A043-W005-S01": ("E1", MINDUNI),
    "S027-A044-W009-S02": ("E2", INS + ": 'haljinu'"),
    "S027-A044-W013-S02": ("E2", IMEINNA),
    "S027-A046-W011-S01": ("E2", NEBILI),
    "S027-A046-W012-S01": ("E2", NEBILI),
    "S027-A047-W011-S01": ("E1", SUBJ),
    "S027-A047-W013-S02": ("E2", AGREE),
    "S027-A048-W006-S01": ("E1", P_AUX + ": 'su … nered činile.'"),
    "S027-A048-W010-S01": ("E2", COORDV),
    "S027-A049-W004-S01": ("E1", "lām odgovora zakletve → dopunsko '\"da' (zaseban token)"),
    "S027-A049-W007-S02": ("E2", COORDV),
    "S027-A052-W011-S02": ("E2", AGREE),
    "S027-A055-W005-S01": ("E1", MINDUNI),
    "S027-A055-W009-S01": ("E1", SUBJ),
    "S027-A055-W011-S02": ("E2", AGREE),
    "S027-A060-W017-S01": ("E2", "mā kāna lakum → 'Ne|moguće je': li- dijeli '-moguće' (dosljedno 19:35)"),
    "S027-A060-W025-S01": ("E1", SUBJ),
    "S027-A060-W027-S02": ("E2", AGREE),
    "S027-A061-W021-S02": ("E2", AGREE),
    "S027-A062-W016-S02": ("E2", "subjektni sufiks fused na 'prisjećate'"),
    "S027-A064-W008-S01": ("E1", REPP + ": 's … iz'"),
    "S027-A064-W010-S03": ("E1", "arḍ → 'zemlje'"),
    "S027-A065-W005-S01": ("E1", REPP),
    "S027-A065-W007-S03": ("E1", "arḍ → 'Zemlji,'"),
    "S027-A065-W014-S01": ("E1", P_AUX + ": 'će oživljeni biti.\"'"),
    "S027-A065-W014-S02": ("E2", AUXP),
    "S027-A066-W008-S01": ("E2", P_UNEXP + ": fī šakkin preoblikovano u glagol 'sumnjaju' (dosljedno 21:97)"),
    "S027-A066-W011-S01": ("E1", "bal → 'pa čak'; 'i' bez segmenta (inserted)"),
    "S027-A070-W004-S02": ("E1", "zabrana lā → 'ni-' u 'nije'"),
    "S027-A070-W005-S01": ("E1", "džusiv takun → 'neka ti … -je' ('neka' gradi oblik, 'ti' nosi lice prefiksa, dosljedno 20:16)"),
    "S027-A072-W006-S01": ("E1", P_UNEXP + ": li- uz radifa; 'stići' uzima akuzativni objekat 'vas' (COMMON)"),
    "S027-A073-W010-S02": ("E2", AGREE),
    "S027-A074-W001-S02": ("E2", P_UNEXP + ": potvrdno inna nema zasebnog tokena; 'dobro' je pojačivač"),
    "S027-A075-W004-S01": ("E1", REPP),
    "S027-A075-W006-S03": ("E1", "arḍ → 'Zemlji,'"),
    "S027-A078-W006-S02": ("E1", SUBJ),
    "S027-A080-W006-S01": ("E2", COORDV),
    "S027-A081-W003-S02": ("E1", "hādī → glagolsko 'možeš uputiti'"),
    "S027-A081-W005-S01": ("E1", "ʿan (odvesti od) → 'iz … izbaviti;'"),
    "S027-A081-W013-S02": ("E1", SUBJ),
    "S027-A083-W011-S02": ("E2", AUXP),
    "S027-A085-W008-S02": ("E2", AUXP + ": '-će' u 'neće'"),
    "S027-A086-W015-S02": ("E2", AGREE),
    "S027-A087-W017-S02": ("E2", AUXP),
    "S027-A090-W005-S02": ("E2", P_UNEXP + ": posvojni -hum (njihova lica) nije zasebno izražen"),
    "S027-A091-W001-S01": ("E1", INNAMA),
    "S027-A092-W012-S01": ("E1", INNAMA),
    "S027-A092-W013-S01": ("E1", SUBJ),
}

if __name__ == "__main__":
    run("S027_En-Neml", D)
