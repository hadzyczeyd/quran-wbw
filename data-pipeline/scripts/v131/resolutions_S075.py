# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 75."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"
LAKA = "li-ka → 'tebi!' uz prvo awlā; ponovljeno 'tebi!' uz drugo awlā nema arapskog segmenta (inserted)"

D = {
    "S075-A004-W005-S01": ("E2", "eksplicitno 'Mi' izražava 1. l. mn. prefiksa imperfekta nusawwiya → pripada glagolu (COMMON, 80:18)"),
    "S075-A005-W005-S01": ("E1", "amāma → 'pred'; " + INS + ": 'ono što … je'"),
    "S075-A014-W002-S02": ("E2", "insān → 'čovjek'; " + INS + ": 'sam' u drugom dijelu dubleta"),
    "S075-A016-W005-S01": ("E1", "namjerni li- → samo 'da'; 'bi' ide uz glagol (dosljedna konvencija)"),
    "S075-A016-W005-S02": ("E1", "taʿjala → 'bi … što prije zapamtio,' (pomoćni 'bi' uz glagol)"),
    "S075-A017-W002-S02": ("E1", "-nā u ʿalaynā preoblikovano u subjekat 'Mi'; kopula 'smo' imenske rečenice inserted (COMMON)"),
    "S075-A019-W003-S02": ("E1", "-nā u ʿalaynā → 'Mi'; kopula 'smo' inserted (dosljedno 75:17)"),
    "S075-A020-W001-S01": ("E2", "kallā → 'Ali,', bal → 'naprotiv,' po redu riječi (dosljedno 83:14 'Ne, naprotiv!')"),
    "S075-A020-W002-S01": ("E2", "bal → 'naprotiv,' (dosljedno 83:14)"),
    "S075-A026-W003-S01": ("E2", "balaghat → 'dopre'; " + INS + ": podrazumijevani subjekat 'duša'"),
    "S075-A028-W002-S02": ("E1", "ime anna -hu → eksplicitno 'to'; kopula 'je' inserted (dosljedno 63:1, 74:54)"),
    "S075-A034-W002-S01": ("E2", LAKA),
    "S075-A034-W002-S02": ("E2", LAKA),
    "S075-A035-W003-S01": ("E2", LAKA),
    "S075-A035-W003-S02": ("E2", LAKA),
    "S075-A038-W005-S02": ("E2", "sawwā → 'skladnim … lik učini,' (lik sadržan u značenju); 'mu' nema arapskog segmenta (inserted)"),
}

if __name__ == "__main__":
    run("S075_El-Kijame", D)
