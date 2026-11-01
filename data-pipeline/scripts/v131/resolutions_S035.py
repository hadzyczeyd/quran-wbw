# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 35."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_NARROW, P_UNEXP, run  # noqa: E402

DETU = P_UNEXP + ": član al- nema zaseban token; pojačivač ostaje inserted (COMMON; dosljedno 58, 77:18)"
NEGC = "negativna konkordancija: 'niko' nosi particip (vlastiti segment, 'onaj koji …'), NEG ostaje na 'ne' (COMMON; 36:30, 42:20)"
MODAL = "; modalno 'može/možeš' je Mehanovićev dodatak bez arapskog segmenta (inserted)"
BIZ = P_UNEXP + ": ekspletivni bi- u predikatu negacije mā (dosljedno 41:46, 50:29, 68:2)"
PARTREL = "particip preveden kao 'onih koji …' → cijeli izraz uključujući 'onih' i 'koji' (COMMON relativna preoblika); 'onih' nosi i min-hum"

D = {
    "S035-A001-W001-S01": ("E2", DETU),
    "S035-A001-W001-S02": ("E1", "ḥamd → 'hvala'; 'Sva' je pojačivač generičnosti bez vlastitog segmenta"),
    "S035-A001-B001": ("INS", "'Sva' — pojačivač uz 'hvala' (al-ḥamd); član al- nije zasebno izražen (COMMON, dosljedno 77:18)"),
    "S035-A002-W007-S02": ("E2", NEGC),
    "S035-A002-W008-S01": ("E2", "mumsik 'onaj koji uskraćuje' → 'niko … uskratiti,'" + MODAL),
    "S035-A002-W012-S02": ("E2", NEGC),
    "S035-A002-W013-S01": ("E2", "mursil 'onaj koji pušta' → 'niko … dati;'" + MODAL),
    "S035-A012-W023-S01": ("E1", "mawākhir je ḥāl (stanje lađa) → cijeli izraz 'kako … sijeku vodu' (dosljedno pravilu za particip stanja)"),
    "S035-A012-W028-S01": ("E2", P_AUX + ": 'biste bili zahvalni.'; laʿalla → 'da', -kum i -ūna na 'biste' (COMMON)"),
    "S035-A013-W019-S01": ("E2", "la- (pripadanje) → prisvojno 'Njegovom!' zajedno s -hu (lahu l-mulku)"),
    "S035-A013-W020-S02": ("E2", "GOVERNED_PHRASE: 'u posjedu' — 'u' kodira padež imenice mulk"),
    "S035-A014-W014-S02": ("E2", P_AUX + ": 'ste' gradi 'ste … pridruživali' i nosi -kum (kao 'smo poslali' u 35:24)"),
    "S035-A015-W004-S02": ("E2", "fuqarāʾ (potrebiti) → 'siromasi,' i 'treba,' (glagol potrebe nosi značenje korijena fqr; ilā također na 'treba,')"),
    "S035-A017-W005-S01": ("E1", BIZ),
    "S035-A018-W013-S01": ("E1", P_UNEXP + ": partitivni min (minhu šayʾun); 'ih' nosi -hu"),
    "S035-A018-W014-S01": ("E1", P_UNEXP + ": šayʾ nije zasebno izražen; Mehanović preoblikuje u aktivnu rečenicu s objektom 'ih' (= -hu)"),
    "S035-A022-W013-S01": ("E1", BIZ),
    "S035-A022-W013-S02": ("E2", "musmiʿ → 'dozvati,'" + MODAL),
    "S035-A024-W009-S01": ("E2", "illā u dvostrukoj negaciji → 'ni-' u 'nije'[0,2]; '-je' je pomoćni perfekta 'je došao'"),
    "S035-A024-W010-S01": ("E2", P_AUX + ": khalā → 'nije'[2,4] + 'došao'"),
    "S035-A025-W009-S01": ("E1", P_NARROW + ": rusul je subjekat jāʾat → 'oni'; 'poslanike' je Mehanovićev objekat u prvoj rečenici (inserted)"),
    "S035-A026-W004-S02": ("E2", "subjektni sufiks -ū → pomoćni 'nisu' (dosljedno 64:10)"),
    "S035-A027-W003-S01": ("E2", "anna → prvo 'da'; drugo 'da' je Mehanovićevo ponavljanje (fa- nosi 'i')"),
    "S035-A030-W001-S02": ("E2", "yuwaffiya → 'On prema onome što … radili nagradi'; 'su' nosi -hum (njihove nagrade = ono što su radili)"),
    "S035-A030-W002-S02": ("E2", "-hum u ujūrahum → 'su' (3. l. mn. u 'što su radili', jedini token tog lica)"),
    "S035-A031-W007-S01": ("E2", DETU + "; 'sušta'"),
    "S035-A031-W008-S01": ({"targets_from": "E1", "add": ["ona"]},
                           "muṣaddiqan je ḥāl → cijeli izraz 'ona potvrđuje da su istinite' ('ona' izražava subjekat sadržan u participu)"),
    "S035-A031-W009-S01": ("E1", P_UNEXP + ": li- uvodi objekat participa; 'da' pripada izrazu participa stanja"),
    "S035-A032-W009-S01": ("E1", PARTREL),
    "S035-A032-W012-S01": ("E1", PARTREL),
    "S035-A032-W014-S01": ("E1", PARTREL),
    "S035-A032-W019-S01": ("E2", P_UNEXP + ": huwa; 'će' gradi Mehanovićev dodani glagol 'dobiti' (inserted), nije kopula"),
    "S035-A037-W015-S01": ("E1", P_AUX + ": 'da bi … imao … da razmisli,' ('bi' gradi 'imao')"),
    "S035-A037-W016-S01": ("E1", "fīhi (u tom vremenu) → 'vremena'"),
    "S035-A037-W016-S02": ("E1", "-hi (vrijeme) → 'vremena' (fused s fī)"),
    "S035-A037-W021-S02": ("E1", P_NARROW + ": dhūqū → 'iskusite'; 'patnju' je Mehanovićevo objašnjenje (inserted)"),
    "S035-A040-W009-S02": ("E2", "subjektni sufiks -ū → eksplicitna zamjenica 'vi' (COMMON 55.9)"),
    "S035-A040-W014-S01": ("E2", "am → 'i … li'; 'recite mi' je Mehanovićevo ponavljanje (inserted)"),
    "S035-A042-W017-S01": ("E1", P_NARROW + ": zāda → 'je povećao'; 'njegov dolazak' je objašnjenje skrivenog subjekta (inserted)"),
    "S035-A044-W012-S01": ("E2", P_UNEXP + ": okolnosni wa-; 'koji' je relativna zamjenica (referent alladhīna), ne veznik"),
}

if __name__ == "__main__":
    run("S035_Fatir", D)
