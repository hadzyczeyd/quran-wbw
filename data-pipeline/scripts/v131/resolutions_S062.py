# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 62."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_UNEXP, run  # noqa: E402

KANA = "kāna u in kuntum + glagol/predikat: kompleks izražen jednim finitnim glagolom → fused na njega (dosljedno 46:4, 49:17, 56:87, 61:11)"

D = {
    "S062-A002-W015-S01": ("E1", "wa-in → 'iako': stvarna unutrašnja granica i|ako; wa (CIRC) → 'i'"),
    "S062-A002-W015-S02": ("E1", "in (COND) → 'ako' unutar 'iako'; zasebne QAC boje se ne kolabiraju"),
    "S062-A005-W001-S01": ("E1", P_UNEXP + ": prvi mathal (subjekat) Mehanović izostavlja; 'slični' nosi ka-mathal (dosljedno 59:15)"),
    "S062-A005-W003-S01": ("E2", "ḥummilū → 'je … nose dat,'; 'da' je podređivač bez arapskog segmenta (inserted, kao dodano 'koji' uz V)"),
    "S062-A005-W003-S02": ("E2", "subjekat pasiva ḥummilū (oni kojima je natovareno) nosi padežni oblik relativa 'kojima' (COMMON, 89:8)"),
    "S062-A006-W007-S02": ("E1", "ime anna -kum → eksplicitno 'vi'; kopula 'ste' inserted (dosljedno innakum → 'vi')"),
    "S062-A006-W016-S01": ("E1", KANA + " ('govorite.\"')"),
    "S062-A008-W002-S01": ("E1", P_UNEXP + ": prvo inna (inna l-mawta) nema svoj token; 'zaista' u predikatu nosi fa-innahu"),
    "S062-A009-W020-S01": ("E1", KANA + " ('znate!')"),
    "S062-A009-W020-S02": ("E1", "2MP lice samo u fleksiji 'znate!' → fused (dosljedno 61:11)"),
    "S062-A011-W009-S01": ("E2", "particip stanja preveden rečenicom 'da stojiš.' → cijeli izraz s 'da' (dosljedno 61:6, 46:30)"),
}

if __name__ == "__main__":
    run("S062_El-Dzumua", D)
