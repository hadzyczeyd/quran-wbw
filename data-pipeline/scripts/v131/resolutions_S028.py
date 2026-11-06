# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 28."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
P_GOV = "GOVERNED_PHRASE: bosanski prijedlog koji kodira padež/ulogu arapske imenice/zamjenice pripada njoj, ne glagolu (COMMON)"
CASE = "arapski prijedlog kodiran padežom/prilogom bez bosanskog prijedloga → veže se na taj token (dosljedno 7:206 lahu → 'Njemu')"
AMS = "bi-l-amsi → prilog 'jučer/ranije' nosi i bi- (fused)"
OMIT = P_UNEXP + ": SOURCE_TRANSLATION_OMISSION — Mehanović u 28:50 ne prevodi „wa-man aḍallu mimmani ttabaʿa hawāhu“ (DOCUMENTED_EXCEPTIONS); "
ELID = P_UNEXP + ": ponovljeni arapski element Mehanović ne ponavlja (elipsa, dosljedno 11:27, 7:12)"
LIPOSS = P_UNEXP + ": li- posjedovanja preoblikovan; 'ga' pripada objektnom -hu glagola (dosljedno 14:32)"

D = {
    "S028-A006-W003-S01": ("E1", CASE + ": instrumental 'zemljom'"),
    "S028-A011-W003-S01": ("E2", "quṣṣī → '\"Idi'; " + P_GOV),
    "S028-A011-W003-S03": ("E2", P_GOV + ": 'za njim!\"'"),
    "S028-A012-W007-S01": ("E2", "hal (ponuda) → '\"Hoćete li'; dopunsko 'da' ide glagolu (COMMON)"),
    "S028-A017-W002-S01": ("E1", "vokativ rabbi (bez yā) → '\"O Gospodaru' ('O' izražava vokativ, dosljedno 17:3)"),
    "S028-A018-W009-S01": ("E1", AMS),
    "S028-A019-W009-S01": ("E1", CASE + ": dativ 'im'; 'obojici' nosi dual -humā"),
    "S028-A019-W018-S01": ("E1", AMS),
    "S028-A023-W012-S01": ("E2", "min dūni → fused 'dalje' (COMMON); 'malo' inserted"),
    "S028-A023-W013-S01": ("E2", "dūn → 'dalje'"),
    "S028-A023-W013-S02": ("E2", P_GOV + ": 'od njih'"),
    "S028-A026-W007-S01": ("E1", "man istaʾjarta preoblikovano u 'da unajmiš' → man nosi 'da'"),
    "S028-A026-W009-S02": ("E1", "qawiyy → relativna preoblika 'onog ko je snažan'"),
    "S028-A029-W004-S01": ("E2", P_UNEXP + ": DET nije istiġrāq; 'ugovoreni' je Mehanovićev dodatak (COMMON)"),
    "S028-A029-W024-S01": ("E1", "min → pridjev 'zapaljenu' (fused, dosljedno 7:201 'šejtanska')"),
    "S028-A032-W016-S01": ("E2", INS + ": 'jasna'"),
    "S028-A034-W010-S02": ("E1", "-nī → posvojno 'moje,'; 'riječi' je dopuna (inserted)"),
    "S028-A036-W015-S01": ("E1", "fī → 'u'; 'doba' je dopuna (inserted)"),
    "S028-A037-W012-S02": ("E1", "resumptivna zamjenica → relativni izraz 'koji' (COMMON)"),
    "S028-A037-W014-S02": ("E1", "ʿāqibatu d-dār → idiom 'sretan kraj' (dār dijeli izraz)"),
    "S028-A038-W008-S01": ("E1", "partitivni min uz neodređenu imenicu pod negacijom → genitiv 'boga' (COMMON)"),
    "S028-A043-W011-S01": ("E2", "ḥāl baṣāʾir → 'da bude svjetlo' (dopunsko 'da' ide izrazu, COMMON)"),
    "S028-A044-W011-S02": ("E1", "drugi kunta ima vlastiti pomoćni 'si' u 'nisi' → sufiks na njega"),
    "S028-A045-W003-S01": ("E2", "neodređenik 'mnoge' uz neodređenu imenicu ide imenici (COMMON 2026-11-05)"),
    "S028-A048-W022-S02": ("E2", "dual -ā → subjekat recipročnog izraza 'jedna'"),
    "S028-A050-W007-S01": ("E2", "yattabiʿūna → 'se … povode'; " + P_GOV),
    "S028-A050-W008-S01": ("E2", P_GOV + ": 'za hirovima'"),
    "S028-A050-W009-S01": ("UNEXP", OMIT + "wa; 'a' uvodi Mehanovićev nastavak bi-ġayri hudan (inserted)"),
    "S028-A050-W009-S02": ("UNEXP", OMIT + "man"),
    "S028-A050-W010-S01": ("UNEXP", OMIT + "aḍall"),
    "S028-A050-W011-S01": ("UNEXP", OMIT + "min"),
    "S028-A050-W011-S02": ("UNEXP", OMIT + "man"),
    "S028-A050-W012-S01": ("UNEXP", OMIT + "ittabaʿa"),
    "S028-A050-W013-S01": ("UNEXP", OMIT + "hawā"),
    "S028-A050-W013-S02": ("UNEXP", OMIT + "-hu"),
    "S028-A052-W006-S01": ("E1", P_UNEXP + ": samostalno hum Mehanović ne ponavlja ('Oni' nosi allaḏīna)"),
    "S028-A055-W011-S01": ("E1", "salām → 'mirni'; 'od nas' je dopuna (inserted)"),
    "S028-A060-W003-S01": ("E1", "min šayʾin → uopćeno 'Sve' (dosljedno 42:10 'god')"),
    "S028-A061-W001-S01": ("E1", "upitno a- → 'Kako'; 'može biti' je dopuna (inserted)"),
    "S028-A061-W009-S01": ("E2", "apsolutni objekat matāʿ dijeli cijeli glagolski izraz 'se naslađuje' (COMMON)"),
    "S028-A061-W012-S01": ("E2", "ṯumma → 'a … poslije,'"),
    "S028-A066-W005-S02": ("E2", "hum → subjekat recipročnog 'jedan' (ni jedan drugog)"),
    "S028-A067-W001-S01": ("E1", P_UNEXP + ": fa u fa-ammā; 'A' nosi ammā"),
    "S028-A070-W005-S01": ("E1", "illā → 'drugog … osim' (dosljedno 7:59, 7:65 'drugog osim')"),
    "S028-A070-W010-S02": ("E1", "ūlā → 'ovom- prvom … svijetu!' (zajednička imenica, kao āḫira 'drugom svijetu!')"),
    "S028-A070-W012-S02": ("E1", CASE + ": 'Njemu pripada'"),
    "S028-A073-W010-S01": ("E2", P_UNEXP + ": partitivni min uz faḍl; 'za' traži bosanski glagol (P_GOV)"),
    "S028-A073-W011-S01": ("E2", P_GOV + ": 'za dobrima'"),
    "S028-A075-W014-S01": ("E1", CASE + ": dativ 'im'"),
    "S028-A078-W002-S01": ("E2", "innamā: inna i mā zajedno nose 'samo' (dosljedno većini objavljenih)"),
    "S028-A079-W005-S01": ("E1", INS + ": 'punom'"),
    "S028-A079-W008-S01": ("E2", "yurīdu → 'su čeznuli'; " + P_GOV),
    "S028-A079-W009-S02": ("E2", P_GOV + ": 'za životom'"),
    "S028-A079-W011-S01": ("E2", P_UNEXP + ": uzvično yā ispred layta nema dozivnog tokena (dosljedno 39:56, 89:24)"),
    "S028-A079-W011-S02": ("E2", "layta → '\"Ah, da' (nerealna želja)"),
    "S028-A081-W007-S02": ("E2", LIPOSS),
    "S028-A082-W005-S01": ("E1", AMS),
    "S028-A082-W006-S02": ("E1", "sufiks glagola uz infinitiv → finitni 'stadoše' koji nosi lice"),
    "S028-A082-W018-S01": ("E1", "manna → 'je … milost … ukazao'; 'Svoju' inserted"),
    "S028-A083-W011-S02": ("E1", ELID),
    "S028-A084-W004-S02": ("E1", "li- posjedovanja → 'dobit'; 'će' nosi -hu (dosljedno 7:113)"),
    "S028-A084-W016-S01": ("E2", "mā → 'onim što'; 'u srazmjeri s' je dopuna (inserted)"),
    "S028-A087-W001-S02": ("E2", "jusiv: 'neka … glagol' na glagol, NEG 'ne' (dosljedno 7:2, 7:27)"),
    "S028-A087-W002-S01": ("E2", "jusiv: 'neka … oni … odvrate'"),
    "S028-A088-W016-S01": ("E1", CASE + ": 'Njemu … pripada'"),
}

if __name__ == "__main__":
    run("S028_El-Kasas", D)
