# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 61."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import run  # noqa: E402

PART = "particip stanja preveden namjernom rečenicom → cijeli izraz s 'da' pripada participu (dosljedno 46:12, 46:30 'koja potvrđuje')"
IMEC = ("izvorni Mehanovićev tekst ima razdvojeno 'i mecima' (= 'imecima'); oba tokena zajedno nose bi-amwāl, "
        "tekst se ne mijenja")

D = {
    "S061-A006-W012-S01": ("E1", PART + " ('da potvrdim')"),
    "S061-A006-W013-S02": ("E1", "relativna rečenica mā (ono što je prije mene) preoblikovana u atributni particip 'objavljeni' koji nosi njenu ulogu"),
    "S061-A006-W018-S02": ("E1", PART + " ('da donesem radosnu vijest')"),
    "S061-A011-W008-S01": ("E1", "bi- (sredstvo) nema zaseban prijedlog; instrumental nosi bi-; " + IMEC),
    "S061-A011-W008-S02": ("E1", IMEC),
    "S061-A011-W009-S01": ("E1", "wa između amwāl i anfus → 'i' ispred 'životima'; prvo 'i' je dio razdvojenog 'imecima'"),
}

if __name__ == "__main__":
    run("S061_Es-Saff", D)
