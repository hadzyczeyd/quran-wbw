# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 67."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"
KANA = "kāna u in kuntum + predikat izražen jednim finitnim glagolom → fused na njega (dosljedno 46:4, 49:17, 61:11, 62:6)"
AUX = "subjektni sufiks bez eksplicitne zamjenice → pomoćni glagol koji nosi lice (COMMON / dosljedna konvencija)"

D = {
    "S067-A005-W005-S02": ("E1", INS + ": 'sjajnim' (dosljedno 41:12 maṣābīḥ → 'svjetiljkama')"),
    "S067-A006-W007-S01": ("E1", "DET al- unexpressed (COMMON); 'to' je Mehanovićev pokazni dodatak (inserted, dosljedno 65:12)"),
    "S067-A008-W008-S01": ("E1", INS + ": 'koja' (neodređenost tanwīna nema segment)"),
    "S067-A013-W001-S02": ("E2", "asirrū → 'tiho'; 'Govorili' nosi qawl (bez dijeljenja tokena između V i N)"),
    "S067-A013-W002-S02": ("E2", "posvojno -kum (vaš govor) → govornici 'vi' (jedini token 2. l. mn.)"),
    "S067-A014-W005-S02": ("E1", P_UNEXP + ": huwa; 'Koji' pripada relativnoj preobliki atributa laṭīf (COMMON), nema kopule"),
    "S067-A019-W006-S01": ("E2", "ṣāffāt → 'raširenih krila' (krila sadržana u participu); 'kako' i 'lete,' su Mehanovićeve dopune (inserted)"),
    "S067-A020-W008-S01": ("E2", "min dūni → složeni prijedlog fused na isti token ('osim'; dosljedno 'pored'/'mimo' u objavljenim surama)"),
    "S067-A020-W011-S01": ("E1", "in (NEG) → 'Ništa' + 'ne' u 'nemaju!'[0,2] (negativna konkordancija bez vlastitog segmenta; ne|maju stvarna granica)"),
    "S067-A020-W014-S01": ("E1", "fī ġurūrin preoblikovano u posjedovanje → 'maju!'[2,7]"),
    "S067-A023-W011-S01": ("E2", P_UNEXP + ": mā u qalīlan mā; 'kako samo' je Mehanovićev uzvik (inserted)"),
    "S067-A025-W006-S01": ("E1", KANA + " ('govorite?!\"')"),
    "S067-A027-W007-S02": ("E1", AUX + " ('nisu')"),
    "S067-A027-W009-S01": ("E1", "hādhā → 'ovo'; prezentativ 'Evo,' je Mehanovićev dodatak (inserted)"),
    "S067-A027-W013-S02": ("E1", AUX + " ('ste' u 'ste požurivali')"),
}

if __name__ == "__main__":
    run("S067_El-Mulk", D)
