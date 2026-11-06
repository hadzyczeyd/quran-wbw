# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 14."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
AUXV = "pomoćni glagol pripada glagolskom obliku koji gradi (COMMON, dosljedno 17, 11:41)"
PRONX = "eksplicitna zamjenica nosi subjektni sufiks; pomoćni ostaje glagolu (COMMON)"
COORDPRON = "sufiks drugog koordiniranog glagola → zajednička eksplicitna zamjenica (COMMON)"
ELIDP = P_UNEXP + ": posvojni sufiks uz koordiniranu imenicu nije ponovljen (elipsa)"
ELID = P_UNEXP + ": ponovljeni arapski element Mehanović ne ponavlja (elipsa, dosljedno 11:27, 18:109)"
RESUMP = "resumptivna zamjenica → padežni oblik relativnog izraza (COMMON)"
LIPOSS = P_UNEXP + ": posvojni li- preoblikovan u subjekat (COMMON)"
OBJV = "objekat sadržan u značenju glagola pripada glagolskom izrazu (dosljedno 16:25)"

D = {
    "S014-A003-W015-S01": ("E1", AUXV + ": ḍalāl → 'su … zalutali.'"),
    "S014-A004-W002-S01": ("E1", AUXV + ": '-smo' u 'nismo'"),
    "S014-A004-W002-S02": ("E1", PRONX + ": 'Mi'"),
    "S014-A004-W005-S01": ("E2", "illā iza negacije → 'koji nije' (izuzetak preoblikovan relativnom negacijom)"),
    "S014-A005-W002-S01": ("E1", AUXV),
    "S014-A006-W014-S01": ("E1", AUXV),
    "S014-A006-W017-S02": ("E1", AUXV),
    "S014-A006-W020-S02": ("E2", ELIDP),
    "S014-A007-W005-S01": ("E1", AUXV + ": 'budete zahvalni,'"),
    "S014-A007-W008-S01": ("E1", AUXV + ": 'budete … nezahvalni,'"),
    "S014-A008-W004-S01": ("E1", AUXV + ": 'budete nezahvalni'"),
    "S014-A009-W021-S02": ("E1", AUXV),
    "S014-A009-W021-S03": ("E1", PRONX + ": 'oni'"),
    "S014-A009-W025-S03": ("E1", COORDPRON + ": 'oni'"),
    "S014-A009-W030-S02": ("E1", RESUMP + ": 'što'"),
    "S014-A010-W018-S01": ("E1", AUXV),
    "S014-A010-W018-S02": ("E1", PRONX + ": 'Oni'"),
    "S014-A011-W020-S01": ("E2", P_UNEXP + ": an uz infinitiv 'donijeti' nema bosanskog veznika"),
    "S014-A012-W002-S01": ("E2", "idiom mā lanā → '\"Zašto' (dosljedno 12:11)"),
    "S014-A012-W002-S02": ("E2", "-nā preoblikovan u subjekat 'uzdamo' (fused)"),
    "S014-A015-W001-S02": ("E1", AUXV),
    "S014-A015-W001-S03": ("E2", "subjektni sufiks → pomoćni 'su'; 'poslanici' je Mehanovićev subjekat (inserted, COMMON)"),
    "S014-A017-W013-S02": ("E2", "min warāʾi → 'poslije toga' (složeni prijedlog fused, COMMON); 'čeka' inserted"),
    "S014-A017-W014-S01": ("E2", "warāʾ → 'poslije toga'"),
    "S014-A018-W016-S01": ("E1", AUXV),
    "S014-A021-W001-S02": ("E1", AUXV + ": 'izići će'"),
    "S014-A021-W007-S01": ("E1", AUXV),
    "S014-A021-W009-S01": ("E1", AUXV),
    "S014-A021-W019-S01": ("E1", "partitivni min uz neodređenost → 'bar' (COMMON)"),
    "S014-A021-W020-S01": ("E1", "šayʾ → 'malo'"),
    "S014-A021-W021-S01": ("E1", AUXV + ": 'odgovorit će'"),
    "S014-A021-W021-S02": ("E1", PRONX + ": 'oni,'"),
    "S014-A021-W025-S02": ("E1", AUXV + ": 'bismo bili … uputili.'"),
    "S014-A021-W025-S03": ("E1", PRONX + ": 'mi'"),
    "S014-A021-W030-S02": ("E1", COORDPRON + ": 'mi'"),
    "S014-A022-W011-S02": ("E1", AUXV),
    "S014-A022-W011-S03": ("E1", PRONX + ": 'ja'"),
    "S014-A022-W012-S02": ("E2", OBJV + ": 'svoja obećanja iznevjerio;'"),
    "S014-A022-W012-S03": ("E1", COORDPRON + ": 'ja'"),
    "S014-A022-W021-S01": ("E1", AUXV),
    "S014-A022-W022-S02": ("E1", AUXV),
    "S014-A022-W022-S03": ("E1", PRONX + ": 'vi'"),
    "S014-A022-W026-S02": ("E1", ELID),
    "S014-A022-W026-S03": ("E1", ELID),
    "S014-A022-W037-S01": ("E1", AUXV + "; 'Njemu' sadržan u širku; 'u obožavanju' je dopuna (inserted)"),
    "S014-A022-W042-S02": ("E1", RESUMP + ": 'Zulumćare'"),
    "S014-A023-W003-S01": ("E1", AUXV),
    "S014-A024-W013-S03": ("E2", ELIDP),
    "S014-A025-W003-S01": ("E1", "kulla ḥīnin (akuzativ vremena) → 'u svakom'"),
    "S014-A025-W004-S01": ("E1", "ḥīn → 'momentu'"),
    "S014-A026-W001-S02": ("E1", "maṯal spojen s poređenjem → 'kao' (dosljedno 14:18)"),
    "S014-A028-W005-S01": ("E1", AUXV + ": 'su umjesto … uzvratili'"),
    "S014-A029-W002-S01": ("E1", AUXV + ": 'će gorjeti'"),
    "S014-A030-W001-S02": ("E1", AUXV),
    "S014-A032-W014-S01": ("E2", "rizq → opisna rečenica 'kojima se hranite;'"),
    "S014-A032-W015-S01": ("E2", LIPOSS),
    "S014-A036-W003-S01": ("E1", AUXV),
    "S014-A037-W003-S01": ("E1", AUXV),
    "S014-A040-W002-S01": ("E2", "kauzativ jaʿala → 'daj da' (COMMON)"),
    "S014-A040-W003-S01": ("E1", "muqīm → 'u obavljanju … ustrajni;'; kopula 'budemo' inserted"),
    "S014-A040-B012": ("INS", "kopula uz particip bez arapskog segmenta ostaje inserted (COMMON)"),
    "S014-A043-W007-S02": ("E2", ELIDP),
    "S014-A044-W008-S01": ("E1", AUXV),
    "S014-A044-W024-S01": ("E2", LIPOSS),
    "S014-A044-W026-S01": ("E2", "zawāl → glagolski izraz 's ovog svijeta … -ćete otići?' (pomoćni ide obliku)"),
    "S014-A045-W001-S02": ("E1", AUXV + ": 'nastanili ste se bili'"),
    "S014-A045-W005-S01": ("E1", AUXV),
    "S014-A045-W010-S01": ("E1", AUXV),
    "S014-A045-W012-S02": ("E1", AUXV),
    "S014-A046-W010-S01": ("E2", "lām nijekanja uz kāna → modalno 'mogu' (dijeli s kāna)"),
    "S014-A052-W004-S03": ("E1", AUXV + ": 'budu opomenuti,'"),
}

if __name__ == "__main__":
    run("S014_Ibrahim", D)
