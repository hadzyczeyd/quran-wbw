# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 52."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_UNEXP, run  # noqa: E402

FUSED = "subjektni sufiks bez zamjenice i pomoćnog glagola: lice/broj nosi glagolski oblik (fused; dosljedno u suri: 'prisluškuju', 'pridružuju', 'suoče')"
GER = FUSED + "; glagolski prilog dosljedno 37:27 'raspitujući', 39:75 'veličajući', 47:27 'udarajući'"
SHARED = "sufiks drugog koordiniranog glagola nosi zajednički pomoćni glagol 'će' (dosljedno 38:51, 52:23); glagol dobija svoj uski izraz"
AMZAR = "am u prijekornom pitanju → 'Zar … da' / 'Ili, da …': modalno 'da' nosi upitnu konstrukciju am (dosljedno 42:9, 42:21, 42:24, 43:16, 38:9)"
VERB = "glagol dobija samo svoj glagolski token; modalno 'da' nosi am (dosljedno 42:24 'Zar oni da govore')"

D = {
    "S052-A004-W001-S03": ("E1", "transliteracija 'Bejtul-Ma'mura' ima stvarne granice: 'Bejt' = bayt, 'ul-' = član al-"),
    "S052-A004-W002-S01": ("E1", "član al- je zasebno transliteriran kao 'ul-' (stvarna unutrašnja granica tokena)"),
    "S052-A012-W005-S02": ("E1", GER),
    "S052-A016-W002-S03": ("E1", FUSED),
    "S052-A016-W005-S02": ("E1", FUSED),
    "S052-A018-W005-S01": ("E2", P_UNEXP + ": crtica nije veznik; wa- se nigdje ne veže na interpunkciju"),
    "S052-A021-W001-S02": ("E1", "ponovljeni relativ istog REL-a u koordiniranoj relativnoj rečenici ('za kojima') nosi taj REL (COMMON)"),
    "S052-A022-W004-S01": ("E1", "partitivni min u mimmā nosi relativni oblik 'kakvo' (dosljedno 41:22 'štošta')"),
    "S052-A023-W007-S02": ("E1", P_UNEXP + ": jedna negacija 'neće biti' pokriva oba koordinirana imena (dosljedno 41:34)"),
    "S052-A025-W005-S01": ("E1", "yatasāʾalu → 'jedni druge pitati:' (recipročnost forme VI); 'će' nosi sufiks (zajednički pomoćni glagol)"),
    "S052-A025-W005-S02": ("E2", SHARED),
    "S052-A030-W001-S01": ("E1", AMZAR),
    "S052-A030-W002-S01": ("E1", VERB),
    "S052-A033-W001-S01": ("E1", AMZAR),
    "S052-A033-W002-S01": ("E1", VERB),
    "S052-A039-W001-S01": ("E1", AMZAR + "; oba 'da' iste upitne konstrukcije"),
    "S052-A041-W001-S01": ("E1", AMZAR + "; 'nije' je retorička formula bez NEG segmenta (dosljedno 38:9 'Ili, da nisu')"),
    "S052-A041-W003-S02": ("E1", "'o' zavisi od Mehanovićevog umetnutog 'znanje' (nema arapskog prijedloga) → inserted"),
    "S052-A042-W005-S02": ("E1", FUSED),
    "S052-A043-W001-S01": ("E1", AMZAR),
    "S052-A043-W002-S01": ("E1", "lām posjedovanja → glagol posjedovanja 'imaju?'; modalno 'da' nosi am (dosljedno 42:21)"),
    "S052-A047-W005-S01": ("E1", "dūna = 'drugo osim' i 'prije': 'druga' i 'prije' (dosljedno 42:9 'druge, a ne')"),
    "S052-A047-W010-S02": ("E2", "akṯaruhum lā yaʿlamūna → fused 'zna.' (dosljedno 39:29, 39:49, 44:39, 45:26)"),
}

if __name__ == "__main__":
    run("S052_Et-Tur", D)
