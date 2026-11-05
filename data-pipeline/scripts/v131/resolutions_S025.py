# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 25."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_GOV, P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
CAUS = "kauzativno jaʿala/mattaʿa/aḏāqa → 'dao/učinio … da' ('da' pripada glagolskoj perifrazi, dosljedno 19:24, 19:50)"
ELID = P_UNEXP + ": ponovljeni glagol/prijedlog elidiran u koordinaciji; zajednički izraz ostaje uz prvi (dosljedno 30:54)"
SPLIT = "negirani oblik dijeli se ni|su: NEG nosi 'ni-', glagol '-su u stanju …' (COMMON, dosljedno 25:3)"
COORDP = "subjektni sufiks drugog koordiniranog glagola → zajednički pomoćni 'smo' (dosljedno 30:9, 21:9)"
OBJV = "objekat/tamyīz sadržan u značenju glagola dijeli glagolski token (dosljedno 23:59, 21:84)"

D = {
    "S025-A002-W002-S01": ("E2", "posvojni li- izražen glagolom 'pripada' (dosljedno 15:42 'imati')"),
    "S025-A002-W011-S02": ("E2", "resumptivni -hu → nominativni relativ 'Koji' (COMMON: resumptivna → oblik relativa)"),
    "S025-A003-W008-S02": ("E1", "samostalno hum (oni sami) → emfatičko 'sama'; 'koja' bez segmenta (inserted)"),
    "S025-A003-W011-S01": ("E1", "yamlikūna → '-su u stanju'; 'otklone', 'pribave,' su objašnjavajuće dopune (inserted)"),
    "S025-A004-W004-S01": ("E1", "NEG in → 'nije' + negativna konkordancija 'ništa' bez vlastitog segmenta (COMMON)"),
    "S025-A004-W006-S01": ("E1", "restriktivno illā → 'drugo do'"),
    "S025-A004-W007-S01": ("E2", INS + ": 'velika'"),
    "S025-A009-W005-S02": ("E2", "amṯāl → upitni objekat 'šta'"),
    "S025-A009-W008-S01": ("E1", INS + ": 'nađu.'"),
    "S025-A010-W015-S02": ("E1", ELID),
    "S025-A010-W016-S01": ("E1", ELID),
    "S025-A010-W016-S02": ("E1", ELID),
    "S025-A014-W003-S01": ("E2", "DET al- uz yawm unexpressed; 'danas' nosi imenicu (COMMON)"),
    "S025-A016-W001-S01": ("E2", "posvojni li- → glagolski 'će … imati,' (pomoćni uz glagol)"),
    "S025-A017-W014-S01": ("E1", "samostalno hum → 'oni'; 'sami' je pojačivač (inserted)"),
    "S025-A018-W008-S01": ("E2", P_AUX + "; eksplicitno 'mi' nosi lice prefiksa (COMMON)"),
    "S025-A018-W014-S01": ("E1", CAUS),
    "S025-A019-W006-S01": ("E1", INS + ": 'nađete.'"),
    "S025-A019-W013-S01": ("E1", CAUS),
    "S025-A020-W006-S01": ("E2", "illā preoblikovano u relativ s negacijom → 'ni-' u 'nije'"),
    "S025-A020-W008-S02": ("E2", P_AUX + ": '-je jeo' (granica ni|je)"),
    "S025-A020-W009-S02": ("E2", OBJV + ": ṭaʿām → 'jeo'"),
    "S025-A020-W013-S02": ("E1", CAUS),
    "S025-A022-W008-S03": ("E1", "subjektni sufiks → pomoćni 'će'; 'meleki' je Mehanovićevo objašnjenje (inserted)"),
    "S025-A023-W006-S01": ("E2", "min ʿamalin (isti korijen) sadržan u glagolu 'počiniše' (dosljedno apsolutnom objektu, COMMON)"),
    "S025-A023-W008-S01": ("E1", "habāʾ → 'u prah' ('u' kodira rezultat)"),
    "S025-A023-W009-S01": ("E1", "manṯūr → 'i pepeo' (raspršenost)"),
    "S025-A025-W004-S01": ("E2", "bi-l-ġamām → 'iz … se … pojavi'; 'i' i 'njega' bez segmenta (inserted)"),
    "S025-A031-W002-S01": ("E1", CAUS),
    "S025-A034-W011-S01": ("E2", OBJV + ": sabīl → 'zalutati.'"),
    "S025-A035-W006-S01": ("E2", P_UNEXP + ": maʿahu nije zasebno izražen; 'mu' nosi -hu od aḫāhu"),
    "S025-A035-W006-S02": ("E2", P_UNEXP + ": -hu u maʿahu nije zasebno izražen"),
    "S025-A036-W001-S03": ("E2", "subjektni sufiks bez zamjenice i pomoćnog u ajetu → fused 'rekli:' (COMMON 55.9)"),
    "S025-A037-W007-S03": ("E1", COORDP),
    "S025-A039-W005-S02": ("E1", "kullan → 'sve'; 'ih' bez segmenta (inserted)"),
    "S025-A041-W006-S01": ("E2", "huzuwan → povratni 'rugaju se:' (dosljedno 21:36, 23:110)"),
    "S025-A042-W002-S01": ("E1", "kāda → 'Umalo da'"),
    "S025-A042-W003-S02": ("E1", "ekspletivno 'ni-' uz 'umalo' nije NEG; cijelo 'nije odvratio,' nosi glagol (COMMON)"),
    "S025-A044-W014-S01": ("E2", P_AUX + ": elativ preveden glagolski 'su … dalje … skrenuli!'"),
    "S025-A045-W011-S01": ("E1", "sākinan → glagolska da-rečenica 'da miruje.' (dosljedno 19:68)"),
    "S025-A045-W012-S01": ("E1", "ṯumma → 'zatim'; 'A' bez segmenta (inserted)"),
    "S025-A045-W013-S01": ("E1", CAUS),
    "S025-A046-W001-S01": ("E1", "ṯumma → 'poslije'; 'A' bez segmenta (inserted)"),
    "S025-A047-W009-S02": ("E1", ELID),
    "S025-A048-W007-S01": ("E2", "bayna yaday → 'kao prethodnicu' ('kao' kodira ulogu, dosljedno 21:107)"),
    "S025-A052-W005-S01": ("E2", "bi- → instrumental 'njime'; 'Kur'anom' je objašnjenje (inserted)"),
    "S025-A053-W003-S01": ("E1", INS + ": 'jedno pored drugog'"),
    "S025-A054-W007-S02": ("E1", CAUS),
    "S025-A055-W006-S01": ("E2", SPLIT),
    "S025-A055-W007-S01": ("E2", SPLIT),
    "S025-A055-W009-S01": ("E1", INS + ": 'otkloniti.'"),
    "S025-A057-W012-S01": ("E2", "ilā (smjer) → 'vodi'; 'koji' bez segmenta (inserted), dativ 'Gospodaru' nosi rabb"),
    "S025-A059-W010-S01": ("E1", "ṯumma → 'onda'; 'a' bez segmenta (inserted)"),
    "S025-A060-W009-S02": ("E1", "deliberativno 'da činimo sedždu' ('da' uz glagol)"),
    "S025-A060-W012-S02": ("E1", "zāda → 'to … više … poveća.'"),
    "S025-A062-W003-S01": ("E1", CAUS),
    "S025-A068-W015-S01": ("E1", "bi-l-ḥaqqi → uslovna perifraza 'kad se na to ima'; ḥaqq → 'pravo'"),
    "S025-A077-W012-S01": ("E1", INS + ": 'patnja.\"'"),
}

if __name__ == "__main__":
    run("S025_El-Furkan", D)
