# -*- coding: utf-8 -*-
"""CP4 razrješenja Entry 1 / Entry 2 neslaganja za suru 43 — ponovnim čitanjem source snapshota."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_FUNC, P_NARROW, P_UNEXP, run  # noqa: E402

P_ZAR = "am / a- → upitna konstrukcija 'Zar da' (dosljedno 42:9)"
P_VERBP = "bi- uz glagol koji u bosanskom uzima direktni objekat nije zasebno izražen (dosljedno 40:83, 41)"
P_CASE = "GOVERNED_PHRASE: li-/bi- kodiran bosanskim padežom imenice (dosljedno 42:21)"
P_MIN = "min istiġrāq u negaciji → 'nijedan/ništa/ni' (negativna konkordancija bez zasebnog QAC NEG)"
P_COR = "korelativno 'i … i' / 'i … a i' prenosi wa (dosljedno 42:52)"
P_COP = "kopula/pomoćni glagol bez arapskog segmenta ostaje inserted (dosljedno 42:29)"

D = {
    "S043-A003-W004-S01": ("E2", P_NARROW + ": 'arabiyy → 'arapskom'; 'na … jeziku' je dopuna"),
    "S043-A005-W001-S03": ("E2", P_NARROW + ": naḍribu → 'da odustanemo'; 'saopćavati' je dopuna"),
    "S043-A007-W001-S02": ("E1", "QAC NEG mā → 'ni-' u 'nije'"),
    "S043-A007-W003-S01": ("E1", P_MIN),
    "S043-A011-W011-S01": ("E2", "ka- → 'tako … i' (i = također; dosljedno 42:52)"),
    "S043-A012-W010-S01": ("E1", "REL mā preoblikovan u namjernu rečenicu 'da na njima'"),
    "S043-A016-W001-S01": ("E1", P_ZAR),
    "S043-A016-W002-S01": ("E1", "ittaḫaḏa → 'uzima Sebi'; 'da' pripada am"),
    "S043-A018-W001-S01": ("E1", P_ZAR),
    "S043-A020-W007-S01": ("E1", "QAC NEG mā → 'ne'"),
    "S043-A020-W010-S01": ("E1", P_MIN),
    "S043-A023-W002-S01": ("E1", "QAC NEG mā → 'ni-' u 'nismo'"),
    "S043-A023-W008-S01": ("E1", P_MIN),
    "S043-A023-W012-S01": ("E1", "mutrafū → relativna preoblika 'oni koji su raskošno živjeli' (dosljedno 40:30)"),
    "S043-A024-W004-S01": ("E1", P_VERBP),
    "S043-A025-W007-S02": ("E1", "mukaḏḏibīn → relativna preoblika 'onih koji su … u laž ugonili.'"),
    "S043-A027-W005-S02": ("E2", "yahdī bez objekta → 'na Pravi put uputiti.' (dosljedno 40:28 THIRD)"),
    "S043-A029-W001-S01": ("E1", "bal → 'čak'; 'A' bez arapskog segmenta"),
    "S043-A029-W005-S01": ("E1", "ḥattā → 'sve dok … ni-' (ekspletivno 'ne' uz 'dok' pripada vezniku, nije QAC NEG)"),
    "S043-A029-W006-S01": ("E1", P_AUX + ": 'je … došla'"),
    "S043-A032-W008-S01": ("E2", "ma'īša → 'ono što je potrebno za život'"),
    "S043-A032-W009-S01": ("E2", "fī → 'na'"),
    "S043-A032-W010-S02": ("E2", "al-ḥayāt ad-dunyā → 'dunjaluku' (jedan token nosi oba segmenta)"),
    "S043-A032-W011-S02": ("E2", "dunyā → 'dunjaluku'"),
    "S043-A033-W004-S01": ("E2", "al- generičko (svi ljudi) → 'svi' (dosljedno al-ḥamd → 'svaka')"),
    "S043-A033-W008-S01": ("E2", P_CASE + ": 'onih'"),
    "S043-A033-W011-S01": ("E2", P_CASE + ": 'kuća,'"),
    "S043-A034-W001-S02": ("E2", P_CASE + ": 'kuća'"),
    "S043-A036-W007-S02": ("E2", P_UNEXP + ": -hu u lahu; 'Onome' nosi man"),
    "S043-A036-W011-S01": ("E2", "qarīn (stalni pratilac) → 'nerazdvojni drug' (57:12)"),
    "S043-A037-W004-S02": ("E1", P_NARROW + ": sabīl → 'puta'; 'Pravog' je dopuna (dosljedno 40:37)"),
    "S043-A038-W003-S01": ("E2", P_NARROW + ": jā'a → 'dođe'; 'koji od njih' eksplicira subjekat"),
    "S043-A038-W007-S02": ("E2", P_UNEXP + ": drugo bayna pod jednim 'između' (dosljedno 41:5)"),
    "S043-A038-W008-S01": ("E1", P_NARROW + ": bu'd → 'razdaljina'; 'tolika … kolika' je poredbena preoblika"),
    "S043-A038-W010-S02": ("E2", P_AUX + ": bi'sa → 'Kako si … bio zao'"),
    "S043-A039-W009-S01": ("E1", P_COP + ": muštarikūn → 'zajedno'"),
    "S043-A041-W002-S01": ("E2", P_NARROW + ": naḏhabanna → 'bismo uzeli,'; 'dušu' je dopuna"),
    "S043-A041-W003-S01": ("E1", P_VERBP),
    "S043-A044-W004-S01": ("E2", P_COR),
    "S043-A046-W001-S02": ("E2", P_UNEXP + ": zakletveno la- u la-qad"),
    "S043-A047-W003-S01": ("E1", P_VERBP),
    "S043-A048-W001-S02": ("E1", "QAC NEG mā → 'ni-' u 'nismo'"),
    "S043-A048-W003-S01": ("E1", P_MIN),
    "S043-A048-W011-S01": ("E2", P_CASE + ": 'patnji'"),
    "S043-A051-W007-S02": ("E1", "laysa → 'ne'"),
    "S043-A051-W008-S01": ("E1", "li- (pripadnost) → 'meni pripada' (dosljedno 40:12)"),
    "S043-A051-W013-S01": ("E2", P_NARROW + ": tajrī → 'teku'; 'koje' bez REL segmenta"),
    "S043-A057-W007-S01": ("E2", "qawm → 'narodu'"),
    "S043-A057-W009-S02": ("E2", "subjektni -ūna → eksplicitno 'oni,'"),
    "S043-A058-W007-S01": ("E1", "ḍaraba (navesti kao primjer) → 'naveli su … kao primjer' (57:12)"),
    "S043-A061-W003-S01": ("E2", P_CASE + ": genitiv 'Smaka'"),
    "S043-A063-W004-S01": ("E1", P_VERBP),
    "S043-A063-W008-S01": ("E1", P_VERBP),
    "S043-A064-W005-S01": ("E2", P_COR),
    "S043-A066-W008-S01": ("E1", "wa (ḥāl) → 'i da' (uvod okolnosne rečenice)"),
    "S043-A066-W010-S01": ("E1", "yaš'urūn → 'osjete?!'"),
    "S043-A067-W007-S02": ({"targets_from": "E1", "add": ["Allaha"]},
                           "muttaqīn → relativna preoblika 'onih koji su se Allaha bojali … grijeha klonili.' ('Allaha' = predmet takve)"),
    "S043-A073-W001-S01": ("E2", "la- (posjedovanje) → 'imati' (dosljedno 42:47)"),
    "S043-A073-W001-S02": ("E2", "-kum → 'ćete' (2. lice mn.)"),
    "S043-A075-W006-S01": ("E2", "mublisūn (očaj, bez nade u spas) → 'nikakve nade u spas neće imati.' i 'očajni' (57:12)"),
    "S043-A078-W003-S01": ("E1", P_VERBP),
    "S043-A080-W007-S02": ("E2", "najwā → 'kako se među sobom dogovaraju?'"),
    "S043-A080-W007-S03": ("E2", P_UNEXP + ": -hum; 'sobom' pripada izrazu 'među sobom'"),
    "S043-A081-W003-S01": ("E1", "kāna → 'bi'; 'imao' nosi li-"),
    "S043-A084-W006-S01": ("E2", P_COR),
    "S043-A085-W009-S02": ("E1", P_FUNC + ": istaknuto 'indahu (isključivost) → 'jedini' (dosljedno 41:47)"),
    "S043-A086-W007-S02": ("E2", P_NARROW + ": šafā'a → 'se zauzimati;'; 'za druge' je dopuna"),
    "S043-A088-W007-S02": ("E1", "subjektni -ūna → 'koji' (jedini token koji nosi subjekat; dosljedno 41 THIRD)"),
}

if __name__ == "__main__":
    run("S043_Ez-Zuhruf", D)
