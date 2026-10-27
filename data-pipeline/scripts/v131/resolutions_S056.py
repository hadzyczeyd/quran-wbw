# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 56."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićevo objašnjenje ostaje inserted"
PART = "particip kao predikat s futurskom kopulom → cijeli glagolski izraz 'će … biti' (dosljedno 38:51, 44:23, 44:35)"
PARTIT = "partitivni min → 'jedan od' (dosljedno 36:3, 37:143, 44:31); kāna → 'bude'"
EXPL = "subjektni sufiks ide na eksplicitnu zamjenicu 'vi' (55.9; COMMON)"

D = {
    "S056-A003-W001-S01": ("E2", "pomoćni 'će' gradi futur participske radnje; objekt 'neke' je Mehanovićev dodatak (inserted)"),
    "S056-A003-W002-S01": ("E2", INS + ": 'neke'"),
    "S056-A016-W001-S01": ("E2", PART),
    "S056-A019-W003-S01": ("E1", "ʿanhā stoji samo uz prvi glagol; ponovljeno 'zbog koga' uz drugi glagol je Mehanovićev dodatak"),
    "S056-A019-W003-S02": ("E1", "-hā → 'koga' uz 'od'; ponovljeno 'koga' je inserted"),
    "S056-A029-W002-S01": ("E1", INS + ": 'plodovima'"),
    "S056-A036-W001-S03": ("E1", P_UNEXP + ": infinitiv 'učiniti,' nema lica (dosljedno 55:33)"),
    "S056-A047-W009-S02": ("E2", PART),
    "S056-A050-W001-S02": ("E2", PART + " ('bit će sakupljeni,')"),
    "S056-A050-W002-S01": ("E1", "ilā → prvo 'u'; drugo 'u' kodira padež imenice 'Dan' i pripada yawm"),
    "S056-A050-W004-S01": ("E1", "bosanski prijedlog koji kodira padež imenice pripada toj imenici ('u Dan')"),
    "S056-A058-W002-S01": ("E1", "REL mā → relativno 'koje'"),
    "S056-A058-W003-S01": ("E1", "tumnūna (ROOT mny 'izbaciti sjeme') leksički sadrži 'sjeme' → 'sjemenu … ubacujete' (COMMON: objekt sadržan u glagolu)"),
    "S056-A060-W003-S01": ("E1", "bayna-kum → 'od' (vas); distributivno 'ko' je Mehanovićev dodatak"),
    "S056-A060-W004-S02": ("E1", "al-mawt → glagolski izraz 'će … umrijeti,'; 'kad' je dodatak (inserted)"),
    "S056-A069-W002-S02": ("E1", EXPL),
    "S056-A072-W002-S02": ("E1", EXPL),
    "S056-A082-W001-S03": ("E1", EXPL),
    "S056-A082-W002-S01": ("E1", "rizq preobražen u pasiv 'je … darovana': pomoćni 'je' pripada glagolskom obliku koji gradi"),
    "S056-A083-W003-S01": ("E2", INS + ": 'duša' je imenica koju Mehanović dodaje (nije zamjenica)"),
    "S056-A085-W001-S02": ("E2", "naḥnu → eksplicitno 'Mi'; kopula 'smo' ostaje inserted (dosljedno 54:10, 43:46)"),
    "S056-A088-W003-S01": ("E2", PARTIT),
    "S056-A088-W004-S01": ("E2", PARTIT),
    "S056-A088-W005-S02": ("E1", "relativna preoblika participa 'onih koji su … bliski'; 'Allahu' je dodatak (inserted)"),
    "S056-A090-W003-S01": ("E2", PARTIT),
    "S056-A090-W004-S01": ("E2", PARTIT),
    "S056-A092-W003-S01": ("E2", PARTIT),
    "S056-A092-W004-S01": ("E2", PARTIT),
    "S056-A093-W001-S02": ("E2", "nuzul preobražen u pasivni futur 'bit će ugošćen' (pomoćni glagoli pripadaju obliku koji grade)"),
}

if __name__ == "__main__":
    run("S056_El-Vakia", D)
