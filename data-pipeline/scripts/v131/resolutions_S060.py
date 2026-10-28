# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 60."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"
OMIT = ("SOURCE_TRANSLATION_OMISSION (dokumentovano razrješenje bloka, nalog 12/46): izvorni Mehanovićev tekst "
        "(QuranEnc, bosnian_mihanovich v1.1.0) u 60:12 ne sadrži klauzulu „wa-lā yaznīna wa-lā yaqtulna awlādahunna“; "
        "tekst prijevoda se ne mijenja, nijedan token ne nosi ovaj segment, veza se ne izmišlja — ")
IDIOM = ("IDIOMATIC_MEHANOVIC (dokumentovano razrješenje bloka, nalog 12/46): metonimiju „bayna aydīhinna wa-arǧulihinna“ "
         "(dijete koje žena rodi) Mehanović prevodi tefsirskom parafrazom „muževima tuđu djecu podmetati“; doslovno "
         "„između ruku i nogu njihovih“ ne nosi nijedan token, veza se ne izmišlja — ")

D = {
    "S060-A004-W033-S01": ("E2", "illā → 'ali ne'; 'i' sa značenjem 'također' ostaje inserted (COMMON)"),
    "S060-A007-W006-S02": ("E1", "bosansko 'između X i Y' jednim prijedlogom nosi oba bayna (dosljedno 37:158, 42:15, 55:44)"),
    "S060-A007-W007-S01": ("E1", "REL → 'onih … kojima'; padežni oblik relativa nosi i resumptivno -hum (COMMON, 89:8)"),
    "S060-A007-W009-S01": ("E1", "min uz resumptivno -hum → 's' (s kojima); prijedlog pripada svom padežnom obliku"),
    "S060-A007-W009-S02": ("E1", "resumptivno -hum → padežni oblik relativa 'kojima' (COMMON, 89:8)"),
    "S060-A008-W015-S03": ("E1", P_UNEXP + ": objektni -hum uz tabarrū; 'činite dobro' je bez objekta, 'onima' nose alladhīna i ilay-him"),
    "S060-A010-W019-S01": ("E1", "NEG → 'ni' u 'nisu' (stvarna granica ni|su, COMMON; dosljedno 39:25, 41:34)"),
    "S060-A010-W020-S01": ("E1", "hunna → 'one' + kopulativni dio 'su' koji nosi njeno lice (COMMON samostalna zamjenica)"),
    "S060-A011-W008-S02": ("E2", INS + ": 'u borbi'"),
    "S060-A011-W013-S01": ("E1", P_UNEXP + ": mithl ('isto toliko') nije zasebno izražen; 'namirite' nosi ātū"),
    "S060-A012-W006-S01": ("E1", "yubāyiʿna → 'polože prisegu:'; 'da' uvodi stanjsku rečenicu i nema arapskog segmenta (inserted)"),
    "S060-A012-W010-S01": ("E1", "'u obožavanju' izražava domen širka sadržan u glagolu (dosljedno 52:43 'u obožavanju pridružuju')"),
    "S060-A012-W022-S02": ("E1", "buhtān → 'tuđu djecu' (Mehanović konkretizira klevetu kao podmetnuto dijete)"),
    "S060-A012-W023-S01": ("E1", "yaftarīna → 'podmetati,' (lažno pripisati); jedan bosanski glagol nosi yaʾtīna bi- … yaftarīna"),
    "S060-A012-W023-S02": ("E1", "subjektni -na → 'će' u 'neće', isto kao kod yaʾtīna (jedan bosanski glagolski oblik)"),
    "S060-A012-W023-S03": ("E1", P_UNEXP + ": objektni -hu (kleveta) nije ponovljen; 'tuđu djecu' je jedini objekat"),
    "S060-A012-W015-S01": ("UNEXP", OMIT + "veznik wa ispred prve izostavljene zabrane"),
    "S060-A012-W015-S02": ("UNEXP", OMIT + "negacija lā uz yaznīna"),
    "S060-A012-W016-S01": ("UNEXP", OMIT + "glagol yaznīna ('da neće bludničiti')"),
    "S060-A012-W016-S02": ("UNEXP", OMIT + "subjektni -na uz yaznīna"),
    "S060-A012-W017-S01": ("UNEXP", OMIT + "veznik wa ispred druge izostavljene zabrane"),
    "S060-A012-W017-S02": ("UNEXP", OMIT + "negacija lā uz yaqtulna"),
    "S060-A012-W018-S01": ("UNEXP", OMIT + "glagol yaqtulna ('da neće ubijati')"),
    "S060-A012-W018-S02": ("UNEXP", OMIT + "subjektni -na uz yaqtulna"),
    "S060-A012-W019-S01": ("UNEXP", OMIT + "imenica awlād ('djecu svoju')"),
    "S060-A012-W019-S02": ("UNEXP", OMIT + "posvojni -hunna uz awlād"),
    "S060-A012-W024-S01": ("UNEXP", IDIOM + "prijedlog bayna"),
    "S060-A012-W025-S01": ("UNEXP", IDIOM + "imenica aydī ('ruke')"),
    "S060-A012-W025-S02": ("UNEXP", IDIOM + "posvojni -hinna uz aydī"),
    "S060-A012-W026-S01": ("UNEXP", IDIOM + "veznik wa između aydī i arǧul"),
    "S060-A012-W026-S02": ("UNEXP", IDIOM + "imenica arǧul ('noge')"),
    "S060-A012-W026-S03": ("UNEXP", IDIOM + "posvojni -hinna uz arǧul"),
}

if __name__ == "__main__":
    run("S060_El-Mumtehine", D)
