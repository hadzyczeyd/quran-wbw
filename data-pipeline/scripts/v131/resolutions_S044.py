# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 44."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_UNEXP, run  # noqa: E402

AUX = P_AUX + " ('smo/ćemo' uz glagol 1. l. mn.; dosljedno 90:4)"
MI = "subjektni -nā nosi eksplicitna zamjenica 'Mi' (55.9); pomoćni glagol pripada glagolskom obliku"
BI = "bi- koji traži samo arapski glagol (atā/asrā bi-); bosanski glagol uzima direktni objekat → unexpressed"
FUT = "subjektni -ūna bez eksplicitne zamjenice nosi pomoćni 'će' (dosljedno 83:34–35, 85:10)"

D = {
    "S044-A003-W002-S01": ("E1", AUX),
    "S044-A017-W002-S01": ("E1", AUX),
    "S044-A017-W002-S02": ("E1", MI),
    "S044-A019-W008-S01": ("E1", BI),
    "S044-A023-W002-S01": ("E1", BI),
    "S044-A028-W002-S02": ("E1", AUX),
    "S044-A028-W002-S03": ("E1", MI),
    "S044-A030-W002-S01": ("E1", AUX),
    "S044-A031-W007-S02": ("E1", "relativna preoblika participa 'onih koji su … svaku mjeru prevršili,'; 'u zlu' je Mehanovićevo objašnjenje (inserted)"),
    "S044-A032-W002-S01": ("E1", AUX),
    "S044-A033-W001-S02": ("E1", AUX),
    "S044-A033-W004-S01": ("E1", P_UNEXP + ": REL mā fīhi preoblikovan u pridjev 'puna' (nosi fī); relativni izraz ne postoji"),
    "S044-A036-W002-S01": ("E1", BI),
    "S044-A037-W009-S01": ("E1", AUX),
    "S044-A038-W002-S01": ("E1", AUX + "; 'smo' dio [2,5] u 'nismo'"),
    "S044-A038-W002-S02": ("E1", MI),
    "S044-A039-W002-S01": ("E1", AUX),
    "S044-A039-W002-S02": ("E1", MI),
    "S044-A039-W005-S01": ("E2", P_UNEXP + ": wa- u wa-lākinna nema zaseban token; suprotnost nosi 'ali' (dosljedno 41:22, 42:8, 43:76)"),
    "S044-A041-W010-S02": ("E1", FUT),
    "S044-A049-W002-S01": ("E2", "inna (ironično pojačanje) → 'baš,'; 'ta' je uzvična dopuna (inserted)"),
    "S044-A049-W003-S01": ("E2", "samostalno anta → kopula 'si,' (lice); emfazu nosi inna ('baš,')"),
    "S044-A054-W002-S02": ("E1", AUX),
    "S044-A054-W002-S03": ("E1", MI),
    "S044-A055-W001-S02": ("E1", FUT),
    "S044-A056-W002-S02": ("E1", FUT + "; dio 'će' [2,4] u 'neće'"),
    "S044-A057-W005-S01": ("E1", "zamjenica razdvajanja huwa → 'će,' (lice) + 'zaista,' (njena emfaza; nema inna; dosljedno 80:42 'zbilja')"),
    "S044-A058-W002-S01": ("E1", AUX),
}

if __name__ == "__main__":
    run("S044_Ed-Duhan", D)
