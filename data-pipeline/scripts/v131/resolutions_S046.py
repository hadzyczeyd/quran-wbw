# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 46."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

EMPH = P_NARROW + ": pojačavajuća riječ je Mehanovićeva dopuna (inserted)"
SHARED_V = "zajednički pomoćni glagol ostaje uz prvi koordinirani glagol (dosljedno 84:25 'budu vjerovali i … činili')"
SHARED_P = "subjektni sufiks drugog koordiniranog glagola nosi zajednički pomoćni glagol (dosljedno 84:25, 85:11)"

D = {
    "S046-A004-W013-S01": ("E1", "am (ili/zar) → 'ili možda': 'možda' nosi upitno-sumnjičavu nijansu istog am"),
    "S046-A005-W008-S01": ("E2", "ponovljeni 'koji' istog REL-a nosi taj REL (COMMON)"),
    "S046-A005-W015-S02": ("E2", "samostalno hum imenske rečenice → kopula 'su' koja nosi njegovo lice (dosljedno 107:5)"),
    "S046-A008-W008-S01": ("E1", "tamliku lī … šayʾan ('ne posjedujete za mene ništa') → '-mate … moći … odbranite;' (leksičko značenje)"),
    "S046-A011-W019-S01": ("E2", EMPH + " ('još')"),
    "S046-A013-W011-S02": ("E1", "NEG lā → 'ne' + negativna konkordancija 'ni' (dosljedno 87:6, 81:29)"),
    "S046-A013-W013-S01": ("E2", P_NARROW + ": yaḥzanūn → 'tuguju!'; optativno 'nek' nema arapskog segmenta (inserted)"),
    "S046-A015-W025-S01": ("E2", P_NARROW + ": ašhkura → 'zahvalim'; 'Ti' je Mehanovićev dodani objekat (inserted)"),
    "S046-A015-W041-S02": ("E1", "subjektni -tu na finitnom glagolu 'kajem,'; 'Ja' nosi ime inna (dosljedno 45:19)"),
    "S046-A015-W045-S02": ("E1", "dublet jedne riječi 'musliman, predan Tebi.\"' pripada segmentu (COMMON: dublet)"),
    "S046-A016-W008-S02": ("E2", SHARED_V),
    "S046-A017-W011-S02": ("E2", EMPH + " ('toliki')"),
    "S046-A017-W014-S01": ("E2", "okolnosno wa (wa-humā …) → 'A kad'"),
    "S046-A017-W015-S01": ("E2", "yastaġīṯāni → 'zapomažući zbore:' (finitni predikat preoblike)"),
    "S046-A017-W015-S02": ("E2", "dualni -āni na finitnom 'zbore:'"),
    "S046-A019-W002-S01": ("E2", EMPH + " ('posebni')"),
    "S046-A020-W024-S02": ("E2", EMPH + " ('ikakva')"),
    "S046-A026-W012-S02": ("E2", "prvi NEG mā → 'ni' + 'ni-' [0,2] u 'nisu' (pravilo 'ni … ni'); treće 'ni' nosi naglasni min"),
    "S046-A026-W020-S01": ("E2", "naglasni min u negaciji (min šayʾ) → 'ni od'"),
    "S046-A027-W007-S03": ("E1", SHARED_P),
    "S046-A029-W010-S01": ("E2", P_NARROW + ": ḥaḍarū → 'dođoše'; 'čuju,' je Mehanovićevo objašnjenje svrhe (inserted)"),
    "S046-A030-W004-S02": ("E1", "subjektni -nā → pomoćni 'smo'; 'mi' nosi ime inna (dosljedno 44:58)"),
    "S046-A031-W011-S02": ("E2", SHARED_V),
    "S046-A032-W006-S02": ("E2", "laysa → 'takvi' + 'ne' [0,2] u 'neće' (podjela na stvarnoj granici)"),
    "S046-A032-W007-S02": ("E2", "muʿjiz glagolizovan → 'će' [2,4] + 'umaći'"),
    "S046-A032-W010-S02": ("E2", "drugo laysa → 'ne' [0,2] u 'neće'"),
    "S046-A032-W011-S01": ("E2", "posvojni la- → '(ne)će … naći.' (dosljedno 85:10 lām → 'imat će')"),
    "S046-A032-W011-S02": ("E2", "-hu (posjednik) → 'će' [2,4] (dosljedno 85:10)"),
    "S046-A034-W012-S01": ("E2", "zakletveno wa → zakletveni dativ 'nam' (dosljedno 89:1 'Tako mi')"),
    "S046-A034-W012-S03": ("E2", "-nā → 'našeg!\"'"),
    "S046-A034-W016-S01": ("E1", "bi- → '\"zbog'"),
    "S046-A034-W016-S02": ("E1", "REL mā → relativni izraz 'toga što' (kao 'ono što')"),
    "S046-A035-W009-S01": ("E1", "tastaʿjil → 'traži … što prije dođe!'; 'da' je bosanski uvod rečenice (inserted)"),
    "S046-A035-W024-S01": ("E1", "yuhlaku → 'će biti uništen'"),
    "S046-A035-W025-S01": ("E1", "restriktivno illā u pitanju → 'ko drugi … do'"),
}

if __name__ == "__main__":
    run("S046_El-Ahkaf", D)
