# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 29."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
PART = "partitivni min → genitiv/izraz 'ljudi/među'; egzistencijalno 'Ima/ima' je Mehanovićev dodatak (dosljedno 30:29, 34:34)"
REPP = "ponovljeni prijedlog pred koordiniranim članovima nosi isti segment (dosljedno 57:1, 27:25)"
RECT = P_UNEXP + ": prijedlog traži samo arapska rekcija; bosanski glagol uzima akuzativni objekat (COMMON)"
GHABIR = "ġābirīn → 'ostati … onima koji će kaznu iskusiti' (dosljedno 26:171); kāna → 'Ona će'"
MODAL = "modalni 'mogu/mogli' kojim Mehanović prevodi imperfekt/particip pripada glagolskom izrazu (dosljedno 26:73)"
NAKAD = "vremenska imenica + rečenica: 'kad' uvodi rečenicu u iḍāfi (dosljedno 26:87, 17:52)"

D = {
    "S029-A002-W008-S01": ("E1", "okolnosno wa → 'a da' (dosljedno 19:67, 27:18)"),
    "S029-A005-W002-S01": ("E1", "kāna + imperfekt bez pomoćnog → fused na glagol 'nada' (COMMON)"),
    "S029-A010-W001-S02": ("E2", PART),
    "S029-A010-W008-S01": ("E2", INS + ": 'neki od njih'"),
    "S029-A017-W015-S01": ("E1", "NEG lā → 'ne'; 'nikakvom' nosi vlastiti segment rizq (COMMON)"),
    "S029-A017-W017-S01": ("E2", RECT),
    "S029-A017-W018-S01": ("E1", "negativna konkordancija na vlastitom segmentu: rizq → 'nikakvom opskrbom' (COMMON)"),
    "S029-A023-W003-S01": ("E2", REPP + ": 'u … u'"),
    "S029-A023-W005-S02": ("E2", "liqāʾ → 'susret'"),
    "S029-A025-W008-S01": ("E1", "mawadda (akuzativ svrhe) → glagolska da-rečenica 'da biste prijateljske odnose održavali,' (dosljedno 19:52)"),
    "S029-A026-W004-S02": ("E2", INS + ": 'Ibrahim' (eksplicitni subjekat, dosljedno 17:102)"),
    "S029-A029-W001-S03": ("E1", "ime inna bez zamjenice u ajetu → fused na glagolski token 'općite,'"),
    "S029-A032-W001-S01": ("E2", INS + ": 'Ibrahim.'"),
    "S029-A032-W014-S01": ("E2", GHABIR),
    "S029-A032-W016-S02": ("E2", GHABIR),
    "S029-A033-W008-S02": ("E2", "ḍāqa → povratni 'se … uznemiri.'"),
    "S029-A033-W021-S01": ("E2", GHABIR),
    "S029-A033-W023-S02": ("E2", GHABIR),
    "S029-A034-W007-S01": ("E2", INS + ": 'strašnu'"),
    "S029-A039-W012-S01": ("E1", "kāna → '-su' u 'nisu'"),
    "S029-A039-W013-S01": ("E1", MODAL + ": 'mogli umaći,'"),
    "S029-A045-W012-S01": ("E2", REPP + ": 'od … od'"),
    "S029-A045-W014-S03": ("E2", "munkar → 'svega što je ružno;'"),
    "S029-A047-W001-S03": ("E2", "ka-ḏālika bez 'Eto' → 'Tako' (COMMON); 'isto' je pojačivač (inserted)"),
    "S029-A047-W010-S02": ("E2", PART),
    "S029-A052-W009-S01": ("E2", REPP + ": 'na … na'"),
    "S029-A052-W011-S03": ("E2", "arḍ → 'Zemlji.'"),
    "S029-A055-W001-S01": ("E1", NAKAD),
    "S029-A060-W001-S02": ("E2", INS + ": 'ima'"),
    "S029-A060-W005-S01": ("E2", MODAL + ": 'mogu skupljati'"),
    "S029-A063-W012-S01": ("E2", "min baʿdi mawtihā sažeto u pridjev 'mrtvu' (baʿd dio izraza)"),
    "S029-A064-W011-S02": ("E1", "samostalna zamjenica hiya → 'to' i kopula 'je' koja nosi njeno lice (COMMON)"),
    "S029-A065-W007-S01": ("E2", "ḥāl muḫliṣīn → 'iskreno'"),
    "S029-A065-W009-S02": ("E2", "dīn (predanost) → 'se predajući,'"),
    "S029-A066-W006-S01": ("E2", "FUT sawfa nosi 'će'; glagol 'znat'"),
    "S029-A068-W011-S01": ("E1", P_UNEXP + ": vremensko lammā preoblikovano u relativ; 'koja' bez segmenta (inserted)"),
}

if __name__ == "__main__":
    run("S029_El-Ankebut", D)
