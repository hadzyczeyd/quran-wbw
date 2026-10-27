# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 54."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

FUSED = "subjektni sufiks bez zamjenice i pomoćnog glagola → fused na glagolski oblik (dosljedno 37:27 'raspitujući', 52:12, 52:16)"
INS = P_NARROW + "; Mehanovićevo objašnjenje ostaje inserted"
DIROBJ = "arapski prijedlog koji traži arapski glagol, a bosanski glagol uzima direktni objekat (akuzativ 'ih') → unexpressed (COMMON)"

D = {
    "S054-A009-W007-S03": ("E1", FUSED),
    "S054-A010-W003-S02": ("E1", "ime inna -ī → eksplicitno 'Ja'; kopula 'sam' ostaje inserted (dosljedno 43:46, 44:18, 51:51)"),
    "S054-A012-W001-S03": ("E1", FUSED + "; 'smo' iz 54:11 nije ponovljen"),
    "S054-A019-W007-S01": ("E2", INS + ": 'Jednog' je neodređeni dodatak"),
    "S054-A027-W005-S01": ("E1", DIROBJ),
    "S054-A028-W005-S02": ("E1", "-hum u baynahum obuhvata narod i kamilu; Mehanović ga razlaže 'njih i nje' (cijeli izraz nosi taj PRON)"),
    "S054-A028-W008-S01": ("E2", INS + ": 'onaj čiji je red' objašnjava ko pristupa"),
    "S054-A029-W004-S02": ("E1", INS + ": objektna enklitika 'je' nema arapskog segmenta (objekt nije dio leksičkog značenja)"),
    "S054-A045-W001-S01": ("E1", "sa- (prijeteća izvjesna budućnost) → 'će sigurno' (dosljedno 40:60, 43:89, 53:40)"),
    "S054-A050-W004-S01": ("E2", INS + ": 'riječ' je podrazumijevana imenica"),
}

if __name__ == "__main__":
    run("S054_El-Kamer", D)
