# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 58."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

EXPL = "subjektni sufiks ide na eksplicitnu zamjenicu (55.9; COMMON; dosljedno 52:30 'Zar oni da govore')"
EXPLAUX = "eksplicitna zamjenica nosi subjektni sufiks; pomoćni glagol ostaje uz glagolski oblik koji gradi (COMMON)"
POSS = "lām posjedovanja → glagol posjedovanja ('čeka'/'pripada'); dativ/akuzativ imenice nosi samu imenicu (dosljedno 53:25, 55:46)"
FUSED = "subjektni sufiks bez zamjenice i pomoćnog glagola → fused na glagolski prilog (dosljedno 37:27, 52:12, 54:9)"
INS = P_NARROW + "; Mehanovićev dodatak/pojačivač ostaje inserted"
RESUMP = P_UNEXP + ": povratna zamjenica/prijedlog nema padežni oblik relativa koji nosi njenu ulogu (COMMON, 89:8)"
DETU = P_UNEXP + ": član al- nema zaseban token; 'pravi' je pojačivač (inserted; dosljedno svim surama)"
CASEP = "bosanski prijedlog koji kodira padež imenice pripada toj imenici (dosljedno 56:50 'u Dan')"

D = {
    "S058-A002-W015-S03": ("E2", EXPL),
    "S058-A002-W023-S01": ("E1", "drugi koordinirani atribut dobija samo svoj token; zajedničko 'Onaj Koji' nosi prvi (dosljedno 38:51, 52:25)"),
    "S058-A004-W018-S02": ("E2", "veznik dopune 'da' je umetnut (nema arapskog an); glagol 'biste potvrdili … vjerujete'"),
    "S058-A004-W024-S02": ("E1", POSS),
    "S058-A005-W013-S02": ("E1", EXPLAUX),
    "S058-A005-W016-S02": ("E1", POSS),
    "S058-A006-W010-S03": ("E1", EXPLAUX),
    "S058-A007-W014-S01": ("E1", P_UNEXP + ": ekspletivni min uz negaciju; genitiv 'razgovora' traži 'Nema' (dosljedno 38:65, 42:15, 50:6)"),
    "S058-A008-W012-S02": ("E1", RESUMP),
    "S058-A008-W024-S01": ("E1", RESUMP),
    "S058-A008-W024-S02": ("E1", RESUMP),
    "S058-A010-W009-S02": ("E2", INS + ": modalno 'može'"),
    "S058-A010-W011-S01": ("E2", "illā → 'osim' (dosljedno 40:78 illā bi-iḏni)"),
    "S058-A010-W012-S01": ("E2", "okolnosni bi- ('uz dopuštenje') Mehanović izražava uslovnim 'ako' (osim ako … dopusti)"),
    "S058-A011-W008-S01": ("E2", "mjesni fī → 'tamo'"),
    "S058-A011-W009-S02": ("E2", "imenica mjesta majlis → opisno 'gdje se sjedi\"' (cijeli izraz je leksičko značenje)"),
    "S058-A011-W026-S01": ("E1", INS + ": 'visoke'"),
    "S058-A012-W010-S02": ("E1", P_UNEXP + ": 'toga' zamjenjuje najwā; posvojni -kum nije izražen"),
    "S058-A014-W019-S02": ("E2", EXPL),
    "S058-A015-W009-S02": ("E2", P_UNEXP + ": kāna nema vlastiti token, pa ni njegov sufiks"),
    "S058-A016-W008-S02": ({"targets_from": "E1", "drop": ["im"]}, POSS + "; dativ 'im' nosi -hum"),
    "S058-A018-W005-S03": ("E1", EXPLAUX),
    "S058-A018-W010-S03": ("E1", FUSED),
    "S058-A018-W017-S01": ("E1", DETU),
    "S058-A019-W015-S01": ("E1", DETU),
    "S058-A020-W006-S01": ("E1", P_UNEXP + ": resumptivni ulāʾika Mehanović ne ponavlja; 'bit će' je kopula predikata"),
    "S058-A020-W008-S01": ("E1", P_UNEXP + ": član al- nije zasebno izražen; 'onim' pripada supstantiviranom elativu"),
    "S058-A020-W008-S02": ("E1", "supstantivirani elativ → 'onim najponiženijim.' (cijeli izraz, kao relativna preoblika N/ADJ)"),
    "S058-A022-W005-S01": ("E2", "bi- → prvo 'u'; drugo 'u' kodira padež imenice i pripada yawm"),
    "S058-A022-W006-S03": ("E2", CASEP),
    "S058-A022-W013-S02": ("E1", "dopusno law (wa-law) → 'pa' (pa bili to …); 'bili' nosi kāna"),
    "S058-A022-W041-S03": ("E1", EXPLAUX),
}

if __name__ == "__main__":
    run("S058_El-Mudzadele", D)
