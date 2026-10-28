# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 68."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import run  # noqa: E402

AUX = "pomoćni glagol pripada glagolskom obliku koji gradi (COMMON; dosljedno 'smo stvorili', 'su poricali' u objavljenim surama)"
SUBJ = "subjektni sufiks istog subjekta → eksplicitna zamjenica / pomoćni glagol koji nosi lice (COMMON 55.9)"

D = {
    "S068-A002-W001-S01": ("E1", "NEG mā (laysa) → 'ni' u 'nisi'[0,2] (stvarna granica ni|si; dosljedno 60:10)"),
    "S068-A002-W002-S01": ("E1", "anta → 'ti,' + kopulski dio 'si'[2,4] koji nosi njeno lice (dosljedno 60:10 hunna → 'one' + 'su')"),
    "S068-A017-W002-S01": ("E1", AUX),
    "S068-A017-W004-S01": ("E1", AUX),
    "S068-A017-W008-S01": ("E1", AUX),
    "S068-A017-W009-S01": ("E1", "zakletveno la- zajedno s -nna pojačava sadržaj zakletve → 'sigurno'; 'da' je podređivač (inserted)"),
    "S068-A018-W002-S01": ("E1", AUX + " ('su' u 'nisu'[2,4])"),
    "S068-A029-W005-S01": ("E1", AUX),
    "S068-A031-W001-S01": ("E1", AUX),
    "S068-A031-W004-S01": ("E1", AUX),
    "S068-A033-W008-S02": ("E1", SUBJ + " ('oni')"),
    "S068-A038-W002-S01": ("E1", "posvojno li- → glagol posjedovanja 'ćete imati' (pomoćni 'ćete' gradi oblik)"),
    "S068-A039-W010-S01": ("E1", "posvojno li- → glagol posjedovanja 'ćete … imati?!' (pomoćni 'ćete' gradi oblik)"),
    "S068-A042-W005-S02": ("E1", AUX),
    "S068-A042-W009-S01": ("E1", AUX),
    "S068-A043-W006-S01": ("E1", AUX),
    "S068-A043-W007-S02": ("E1", SUBJ + " ('su')"),
    "S068-A044-W006-S02": ("E1", "istidrāj = postepeno voditi ka propasti; 'patnji' izražava odredište sadržano u značenju glagola (COMMON)"),
    "S068-A047-W003-S02": ("E1", "al-ghayb → 'onome što je čulima nedokučivo,' (relativna preoblika); 'o' nema arapskog prijedloga (inserted)"),
    "S068-A047-W005-S02": ("E1", SUBJ + " ('oni')"),
    "S068-A049-W009-S02": ("E1", "samostalna zamjenica stanjske rečenice → pomoćni glagol koji nosi njeno lice ('bi'; COMMON)"),
}

if __name__ == "__main__":
    run("S068_El-Kalem", D)
