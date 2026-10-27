# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 57."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićevo objašnjenje/pojačivač ostaje inserted"
YAWM = "yawma + rečenica → 'Na Dan kad(a)': veznik izražava vezu yawm s rečenicom (dosljedno 40:16, 40:51, 41:47)"
AUX = "pomoćni glagol 'će' pripada glagolskom obliku koji gradi (i nosi subjektni sufiks)"
NAFS = "anfus → povratno-naglasno 'sami sebe' (nafs nose i 'sebe' i 'sami', dosljedno 39:15 'sebe', 51:21 'samima'); -kum → 'sebe' (fused, dosljedno 39:15, 42:45)"

D = {
    "S057-A006-W005-S02": ("E1", "elidirani drugi yūliju dijeli cijeli izraz prvog glagola 'On uvodi'"),
    "S057-A008-W001-S02": ("E1", "retoričko mā lakum lā → 'Kako da': modalno 'da' nosi upitnu konstrukciju (dosljedno am → 'Zar da', 52:30)"),
    "S057-A010-W008-S02": ("E1", "lām posjedovanja → glagol 'pripada' (dosljedno 39:3, 40:12, 53:25); dativ 'Allahu' nosi PN"),
    "S057-A012-W001-S01": ("E1", YAWM),
    "S057-A013-W001-S01": ("E1", YAWM),
    "S057-A013-W009-S01": ("E1", "min bez bosanskog prijedloga: odnos nosi instrumental 'svjetlom' (fused; CASE)"),
    "S057-A013-W022-S01": ("E1", P_UNEXP + ": fī u resumptivnom fīhi nema zaseban token ('unutar' nosi bāṭin)"),
    "S057-A013-W025-S01": ("E1", P_UNEXP + ": min qibalihi nije zasebno preveden ('izvan' nosi ẓāhir)"),
    "S057-A013-W026-S01": ("E1", P_UNEXP + ": qibal ('strana') nije zasebno preveden ('izvan' nosi ẓāhir)"),
    "S057-A014-W001-S01": ("E2", AUX),
    "S057-A014-W005-S01": ("E2", AUX),
    "S057-A014-W009-S01": ("E2", NAFS),
    "S057-A014-W009-S02": ("E2", NAFS),
    "S057-A019-W011-S02": ("E1", "povratna zamjenica: ulogu primaoca nosi dativ 'šehidima' (COMMON; dosljedno 85:11 'onima')"),
    "S057-A022-W012-S01": ("E2", INS + ": 'zapisana'"),
    "S057-A023-W007-S01": ("E2", INS + ": 'previše'"),
    "S057-A025-W008-S03": ("E2", "dublet-apozicija 'Mjerilo - pravdu' za jednu riječ: cijeli izraz pripada mīzān (COMMON dubleti)"),
    "S057-A025-W024-S03": ("E2", INS + ": objekt 'ih'"),
    "S057-A026-W010-S02": ("E2", "partitivni min → 'neki od' (dosljedno 56:88 'jedan od')"),
    "S057-A026-W011-S01": ("E2", P_NARROW + ": 'neki' nosi partitivni min"),
    "S057-A027-W031-S02": ("E1", P_UNEXP + ": drugo -hā (riʿāyatihā) nije ponovljeno; 'o njemu' nosi objekt raʿaw-hā"),
    "S057-A027-W036-S02": ("E1", P_UNEXP + ": 'one' nosi REL allaḏīna; posvojni -hum uz ajr nije zasebno izražen"),
}

if __name__ == "__main__":
    run("S057_El-Hadid", D)
