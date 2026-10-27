# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 53."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

TRANS = "transliteracija s članom: imenica do člana, 'ul-' (s crticom) nosi al- (dosljedno 52:4 'Bejt'/'ul-')"
HYPH = "token s crticom: crtica pripada lijevom dijelu (dosljedno 52:4, 53:14)"
POSSADJ = "posvojni pridjev se ne dijeli: li- i ime dijele cijeli token (dosljedno 42:49, 45:27, 48:4 'Allahova')"
POSS = "lām posjedovanja → glagol posjedovanja 'pripada'; dativ je padež koji traži glagol (dosljedno 39:3, 40:12)"
AUX = "pomoćni glagol 'bi' pripada glagolskom obliku koji gradi; namjerni li- → 'da' (dosljedno 45:14 li-yajziya)"
SHARED = "drugi koordinirani glagol dobija samo svoj token; zajednički 'bi' nosi prvi (dosljedno 38:51, 52:25, 52:27)"
INS = "pojačivač bez arapskog segmenta ostaje inserted (COMMON)"

D = {
    "S053-A014-W002-S01": ("E2", TRANS),
    "S053-A014-W003-S01": ("E2", TRANS),
    "S053-A025-W001-S02": ("E2", POSS),
    "S053-A026-W010-S01": ("E1", "illā min baʿdi an → 'sve dok … ne': izuzetak nosi 'sve … ne', baʿd 'dok'"),
    "S053-A026-W012-S01": ("E1", "baʿd (vremensko 'nakon') → veznik 'dok' (dosljedno 42:28 'kad')"),
    "S053-A026-W013-S01": ("E1", "an podređuje rečenicu; nosi ga veznik 'dok' (fused; dosljedno 48:24 'što', 42:47 'nego što')"),
    "S053-A028-W010-S02": ("E2", "inna → naglasno 'baš' (dosljedno 37:152, 44:49)"),
    "S053-A031-W001-S02": ("E1", POSSADJ),
    "S053-A031-W001-S03": ("E1", POSSADJ),
    "S053-A031-W008-S01": ("E2", AUX),
    "S053-A031-W008-S02": ("E2", AUX),
    "S053-A031-W013-S02": ("E1", SHARED),
    "S053-A032-W008-S01": ("E2", "inna obrazlaže i naglašava: 'jer' i 'zaista,' (dosljedno 40:26, 44:37, 45:29 inna → 'jer')"),
    "S053-A032-W026-S01": ("E1", HYPH),
    "S053-A032-W026-S02": ("E1", HYPH + "; subjektni sufiks fused na imperativ"),
    "S053-A032-W028-S01": ("E1", HYPH),
    "S053-A032-W030-S02": ("E2", P_NARROW + "; 'svakog' je pojačivač (inserted)"),
    "S053-A034-W003-S02": ("E2", INS + ": 'posve'"),
    "S053-A039-W003-S01": ("E1", POSSADJ + " ('čovjekovo')"),
    "S053-A039-W003-S03": ("E1", POSSADJ + " ('čovjekovo')"),
    "S053-A040-W001-S02": ("E2", "anna → 'da'; 'sigurno' nosi sawfa"),
    "S053-A040-W003-S01": ("E2", "sawfa → 'će sigurno' (dosljedno 43:89 fa-sawfa → 'Sigurno će')"),
    "S053-A042-W004-S02": ("E2", INS + ": 'ponovno' je Mehanovićev dodatak"),
    "S053-A047-W002-S01": ("E2", P_UNEXP + ": ʿalā (obaveza) nije izražen; 'On' nosi -hi"),
}

if __name__ == "__main__":
    run("S053_En-Nedzm", D)
