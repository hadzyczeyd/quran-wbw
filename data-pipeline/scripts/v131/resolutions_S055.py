# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 55."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, run  # noqa: E402

INS = P_NARROW + "; opisni pridjev je Mehanovićevo tumačenje (inserted)"

D = {
    "S055-A008-W003-S01": ("E2", "arapski prijedlog bez bosanskog prijedloga: odnos nosi padežni oblik 'pravde' (fused; CASE)"),
    "S055-A033-W006-S01": ("E1", "an + subjunktiv → bosanski infinitiv 'prodrijeti,' (fused; dosljedno 36:40 'dostići,')"),
    "S055-A035-W006-S02": ("E1", INS + " ('rastopljen')"),
    "S055-A037-W006-S03": ("E1", INS + " ('rastopljeno')"),
    "S055-A046-W001-S02": ({"targets_from": "E1", "drop": ["onome"]},
                           "lām posjedovanja → glagol posjedovanja 'pripast će' (dosljedno 39:3, 40:12, 53:25); dativ 'onome' nosi REL man"),
    "S055-A056-W005-S02": ("E1", "povratna zamjenica → padežni oblik relativa 'koje,' (COMMON, 89:8); ponovljeno 'one' je inserted"),
}

if __name__ == "__main__":
    run("S055_Er-Rahman", D)
