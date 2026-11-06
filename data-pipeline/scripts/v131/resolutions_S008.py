# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 8."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
HAQQ = "ḥaqqan → 'zbilja … pravi' (istinski vjernici; u 8:1-2 'pravi' bez ḥaqq ostaje inserted)"
CIRCW = P_UNEXP + ": okolnosno wa preoblikovano u glagolski prilog, nema veznika (dosljedno 26:96)"
CIRCH = "hum okolnosne rečenice → fused na glagolski prilog (dosljedno 7:86 GER, 37:27)"
ANINF = P_UNEXP + ": an uz infinitiv nema bosanskog veznika (dosljedno 14:11, 48:15)"
P_GOV = "GOVERNED_PHRASE: bosanski prijedlog koji kodira padež imenice pripada njoj (COMMON)"
REPP = "ponovljeni bosanski prijedlog ispred koordiniranog člana nosi isti arapski segment (COMMON: 'na na')"

D = {
    "S008-A004-W004-S01": ("E1", HAQQ),
    "S008-A006-W010-S01": ("E1", CIRCW),
    "S008-A007-W017-S01": ("E1", ANINF),
    "S008-A010-W005-S01": ("E2", "bušrā → rečenica 'da bi … obradovao' (dopunsko 'da' ide izrazu, COMMON)"),
    "S008-A012-W021-S01": ("E1", P_UNEXP + ": partitivni min uz zamjenicu; 'ih' nosi -hum (dosljedno 22:36)"),
    "S008-A023-W005-S01": ("E2", "neodređenik 'ikakva' uz neodređenu imenicu u uslovu ide imenici (COMMON 2026-11-05)"),
    "S008-A023-W010-S01": ("E1", CIRCW),
    "S008-A023-W010-S02": ("E2", CIRCH),
    "S008-A026-W016-S01": ("E1", "partitivni min uz množinu kodiran instrumentalom 'ljepotama' (COMMON: linked)"),
    "S008-A027-W010-S02": ("E2", "samostalna zamjenica antum → kopula 'ste' koja nosi njeno lice (dosljedno 19:30, 26:44)"),
    "S008-A027-W011-S01": ("E2", "taʿlamūna → dublet 'znate - svjesni'"),
    "S008-A034-W007-S01": ("E1", INS + ": 'drugima'"),
    "S008-A035-W002-S01": ("E2", "kāna → 'svodi se'; " + P_GOV),
    "S008-A035-W007-S01": ("E2", P_GOV + ": 'na zviždanje'"),
    "S008-A036-W012-S01": ("E2", "kāna (budućnost) → 'će … zbog toga'"),
    "S008-A041-W019-S01": ("E2", REPP + ": 'u u'"),
    "S008-A041-W020-S02": ("E2", "mā → 'ono što'; ponovljeno 'u' nosi bi-"),
    "S008-A042-W015-S02": ("E1", INS + ": 'borbe'"),
    "S008-A042-W019-S01": ("E1", "amran → relativna preoblika 'ono što' (COMMON: N kao 'ono što …')"),
    "S008-A044-W013-S01": ("E1", "amran → relativna preoblika 'ono što' (COMMON)"),
    "S008-A046-W004-S02": ("E1", "lā zabrane → 'ne'"),
    "S008-A046-W006-S01": ("E1", "fa (odgovor na zabranu) → 'da ne' (negativna posljedica sadržana u fa; COMMON fa sababiyya)"),
    "S008-A050-W009-S02": ("E2", "-hum (njihova lica) → 'njihovim'"),
    "S008-A050-W010-S03": ("E2", "-hum (njihova leđa) → objekat 'ih' (udarali ih straga)"),
    "S008-A052-W008-S02": ("E2", "āyāt → 'dokaze'; 'u' nosi arapski bi-"),
    "S008-A053-W012-S01": ("E1", "yuġayyirū → 'se … promijeni' (povratno 'se' ide glagolu)"),
    "S008-A053-W014-S02": ("E1", "anfus → 'sam'"),
    "S008-A056-W007-S01": ("E2", "fī uz akuzativ vremena → 'put,' (dosljedno 28:6 'zemljom')"),
    "S008-A056-W010-S01": ("E1", CIRCW),
    "S008-A056-W010-S02": ("E2", CIRCH),
    "S008-A062-W003-S01": ("E1", ANINF),
    "S008-A062-W004-S02": ({"targets_from": "E2", "drop": ["prevariti"], "add": ["htjednu"]}, "subjektni sufiks infinitivne dopune → finitni 'htjednu' (dosljedno 20:121, 28:82)"),
    "S008-A067-W002-S01": ("E2", "kāna → '-je bilo' u 'nije bilo'"),
    "S008-A067-W003-S01": ({"targets_from": "E1", "add": ["dopušteno"]}, "li- → dativ 'vjerovjesniku' + predikat 'dopušteno' (dosljedno 28:70 'Njemu pripada')"),
    "S008-A067-W004-S01": ("E1", ANINF),
    "S008-A071-W009-S02": ("E1", "amkana → 'je On omogućio da … pobijediš;'; 'ti' bez segmenta (inserted)"),
    "S008-A072-W035-S02": ("E2", "naṣr → 'u pomoć priteći,'; 'im' inserted"),
    "S008-A072-W039-S01": ("E1", "baynakum → 'imate' (ugovor između vas = vi imate); baynahum → 's kojim'"),
    "S008-A074-W014-S01": ("E1", HAQQ),
}

if __name__ == "__main__":
    run("S008_El-Enfal", D)
