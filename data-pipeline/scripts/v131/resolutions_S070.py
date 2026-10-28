# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 70."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićev dodatak ostaje inserted"

D = {
    "S070-A003-W001-S01": ("E1", "min Allāhi Mehanović preoblikuje u zavisnu rečenicu 'da (to Allah) ne učini,' — cijeli izraz nosi min (izvor odbijanja); 'to' inserted"),
    "S070-A006-W002-S02": ("E2", "subjektni -ūna → eksplicitna zamjenica 'Oni,' (COMMON 55.9; dosljedno 63:7)"),
    "S070-A028-W001-S01": ("E2", P_UNEXP + ": inna bez potvrdnog tokena; 'a' je veznik (inserted)"),
    "S070-A030-W007-S01": ("E1", P_UNEXP + ": aymān u idiomu mā malakat aymānuhum; 'su u vlasništvu' nosi malakat, 'njihovu' -hum"),
    "S070-A031-W002-S01": ("E2", INS + ": 'nešto'"),
    "S070-A031-W006-S01": ("E1", "odvajajuća hum → kopula koja nosi njeno lice + izraz isticanja 'su baš' (dosljedno 59:19, 59:20)"),
    "S070-A035-W004-S01": ("E1", "particip mukramūn preveden glagolskim oblikom 'će biti počašćeni.'; pomoćni glagoli grade taj oblik (dosljedno 59:9)"),
    "S070-A041-W002-S01": ("E2", P_UNEXP + ": an + subjunktiv izražen infinitivom 'zamijeniti' bez veznika"),
    "S070-A042-W003-S02": ("E1", "drugi koordinirani glagol dobija samo svoj token; zajedničko 'se' nosi prvi glagol (dosljedno 59:5)"),
}

if __name__ == "__main__":
    run("S070_El-Mearidz", D)
