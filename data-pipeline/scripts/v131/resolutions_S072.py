# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 72."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"
VSUBJ = ("subjektni sufiks glagola iza inna/anna: zamjenica nosi ime inna, a sufiks glagola ide na pomoćni/glagolski token "
         "(dosljedno većini objavljenih sura i 71:1)")
EXPL = "subjektni sufiks → eksplicitna zamjenica (COMMON 55.9); pomoćni glagol pripada glagolskom obliku"
PRP = "namjerni li- → samo 'da'; 'bi' ide uz glagol (dosljedna konvencija)"

D = {
    "S072-A001-W011-S02": ("E1", VSUBJ + " ('smo,')"),
    "S072-A002-W004-S03": ("E2", EXPL + " ('mi')"),
    "S072-A002-W006-S02": ("E1", "lan → 'ne' u 'nećemo'[0,2]; " + INS + ": 'više'"),
    "S072-A005-W002-S02": ("E1", VSUBJ + " ('smo')"),
    "S072-A005-W004-S01": ("E2", "negativna korelacija: prvo 'ni' i 'ne' na NEG, drugo 'ni' na wa (COMMON, 93:3)"),
    "S072-A006-W007-S02": ("E2", P_UNEXP + ": drugi rijāl (rijālin mina l-jinn) nije zasebno preveden; 'džina' nosi jinn"),
    "S072-A007-W002-S02": ("E1", VSUBJ + " ('misle,')"),
    "S072-A008-W002-S02": ("E1", VSUBJ + " ('smo')"),
    "S072-A009-W001-S03": ("E2", "ime anna bez zamjenice → token koji nosi njegovo lice ('bismo'; dosljedno 71:7)"),
    "S072-A009-W006-S01": ("E1", PRP),
    "S072-A009-W006-S03": ("E1", "samʿ preveden glagolskim izrazom 'bismo … čuli,'; 'bismo' gradi taj oblik"),
    "S072-A010-W003-S01": ("E1", "nadrī → 'znamo'; 'mi' nosi ime anna"),
    "S072-A011-W004-S02": ("E2", "drugo min (wa-minnā) nosi isto 'među' — Mehanović obje grupe stavlja pod jedno 'među nama' (dosljedno ponovljenom bayna 60:7)"),
    "S072-A011-W004-S03": ("E2", "drugo -nā nosi isto 'nama' (zajednički izraz)"),
    "S072-A012-W002-S02": ("E1", VSUBJ + " ('znamo')"),
    "S072-A013-W005-S02": ("E1", VSUBJ + " ('smo,')"),
    "S072-A013-W011-S01": ("E1", "yaḫāfu → 'se boji;'; " + INS + ": modalno 'treba da'"),
    "S072-A013-W012-S01": ("E1", "baḫs → 'umanjivanja'; " + INS + ": 'dobrih,'"),
    "S072-A013-W014-S01": ("E1", "rahaq → 'dodavanja'; " + INS + ": 'loših djela'"),
    "S072-A014-W006-S02": ("E1", "man → cijeli relativni izraz 'oni koji' (COMMON REL)"),
    "S072-A014-W008-S02": ("E1", P_UNEXP + ": ulāʾika spojen s man u jedan subjekat (dosljedno 63:9, 64:10)"),
    "S072-A015-W001-S02": ("E1", P_UNEXP + ": ammā; kontrastno 'a' nosi wa"),
    "S072-A016-W005-S03": ("E2", EXPL + " ('Mi')"),
    "S072-A017-W001-S01": ("E1", PRP),
    "S072-A017-W001-S02": ("E1", "naftina → 'bismo … na kušnju stavili;' (pomoćni 'bismo' uz glagol)"),
    "S072-A021-W003-S01": ("E2", "negativna korelacija: prvi lā → 'ni' u 'nisam'[0,2]; 'niti' nosi wa + drugi lā (COMMON)"),
    "S072-A021-W004-S01": ("E1", "amliku → 'nisam'[2,5] 'u stanju'; " + INS + ": 'otkloniti', 'pribaviti.\"'"),
    "S072-A021-W005-S01": ("E1", "li- u lakum → 'od' (od vas) i dativ 'nekom'; partitivno 'od' u 'nekom od vas' nema arapskog segmenta (inserted)"),
    "S072-A028-W001-S01": ("E1", PRP),
    "S072-A028-W001-S02": ("E1", "yaʿlama → 'bi znao' (pomoćni 'bi' uz glagol)"),
}

if __name__ == "__main__":
    run("S072_El-Dzinn", D)
