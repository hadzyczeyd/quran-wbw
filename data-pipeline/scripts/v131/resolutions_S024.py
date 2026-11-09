# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 24."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
JALD = "jalda (korijen jld 'koža') → 'udaraca po koži' ('po koži' stoji uz imenicu); glagol samo 'udarite'"
COORDS = "sufiks drugog koordiniranog glagola → zajednički pomoćni (COMMON, dosljedno 22:57)"
YAWM = "yawm uz rečenicu → 'na Dan kada' (dosljedno 3:25, 3:30, 7:53, 11:8)"
DA = "dopunsko 'da' bez arapskog veznika ide glagolu/izrazu dopunske rečenice (COMMON, 3:52, 3:86)"
LREQ = P_UNEXP + ": prijedlog traži samo arapski glagol; bosanski glagol uzima direktni objekat (COMMON)"
LIPOSS = P_UNEXP + ": posvojni li- preoblikovan u subjekat glagola (dosljedno 15, 19 LIPOSS)"
COP = "ʿalā obaveze → pridjev 'dužan/dužni'; kopula 'je/ste' bez arapskog segmenta je inserted (COMMON)"

D = {
    "S024-A002-W001-S01": ("E1", P_UNEXP + ": generičko al- (bosanski nema člana)"),
    "S024-A002-W001-S02": ("E1", "zāniya → 'bludnica' [0,8] u 'bludnica-pa'"),
    "S024-A002-W003-S02": ("E1", JALD),
    "S024-A002-W008-S01": ("E1", JALD),
    "S024-A003-W010-S02": ("E1", "resumptivni -hā dijeli izraz teme 's bludnicom' (isti referent, prijedlog kodira padež)"),
    "S024-A004-W009-S02": ("E1", JALD),
    "S024-A004-W011-S01": ("E1", JALD),
    "S024-A012-W009-S03": ("E2", COORDS + ": 'nisu'"),
    "S024-A015-W008-S01": ("E1", LIPOSS),
    "S024-A022-W003-S01": ("E2", "ulū upravlja i s faḍl i sa saʿa → 'milodarni' i 'imućni'"),
    "S024-A024-W001-S01": ("E1", YAWM),
    "S024-A033-W004-S01": ("E1", "lā yajidūna (ne nalaze sredstva) → '-maju mogućnosti' u 'nemaju … mogućnosti'"),
    "S024-A033-W005-S01": ("E1", "nikāḥ → 'da se ožene,'"),
    "S024-A033-W019-S01": ("E2", "ʿalimtum → 'znate'; " + DA),
    "S024-A033-W020-S01": ("E1", P_UNEXP + ": fīhim ḫayran preoblikovano u 'su u stanju'; 'su' nosi -him"),
    "S024-A033-W021-S01": ("E2", DA + ": 'da … u stanju da to učine,'"),
    "S024-A033-W045-S01": ("E1", "baʿd → 'nakon što' (veznik koji uvodi preoblikovani maṣdar)"),
    "S024-A033-W046-S01": ("E1", "ikrāh → 'su bile primorane,'"),
    "S024-A035-W026-S01": ("E2", "yakādu → 'gotovo'"),
    "S024-A035-W028-S01": ("E2", DA),
    "S024-A036-W011-S01": ("E1", LREQ),
    "S024-A037-W010-S02": ("E2", "iqām preveden relativnom preoblikom 'koji … obavljaju' (COMMON: N kao 'onaj koji')"),
    "S024-A039-W006-S02": ("E1", P_UNEXP + ": objektni -hu (priviđenje) nije izražen; 'u kojoj' se odnosi na ravnicu (inserted)"),
    "S024-A040-W022-S01": ("E2", "yakad → 'skoro'"),
    "S024-A040-W023-S01": ("E2", DA + ": 'da … bi vidio'"),
    "S024-A041-W006-S01": ("E1", LREQ),
    "S024-A043-W011-S02": ("E1", "objektni sufiks drugog koordiniranog glagola → zajednički 'ih' (dosljedno 16:121, 3:42)"),
    "S024-A043-W031-S01": ("E2", LREQ),
    "S024-A043-W034-S01": ("E2", "yakādu → 'gotovo'"),
    "S024-A043-W037-S01": ("E2", DA),
    "S024-A047-W006-S01": ("E2", "ṯumma → 'a'; 'potom' nosi min baʿdi ḏālika"),
    "S024-A054-W009-S01": ("E2", COP),
    "S024-A054-W012-S02": ("E2", COP),
    "S024-A055-W006-S03": ("E2", COORDS + ": 'budu'"),
    "S024-A057-W001-S01": ("E2", "lā zabrane → 'ne'; pojačanje -nna nosi 'Nikako' (dosljedno 3:178, 3:188)"),
    "S024-A057-W002-S01": ("E2", "taḥsabanna → 'misli'; " + DA),
    "S024-A057-W002-S02": ("E2", "emfatičko -nna → 'Nikako' (dosljedno 3:178, 3:188)"),
    "S024-A057-W005-S01": ("E2", DA + ": 'da će se … moći suprotstaviti Njemu'"),
    "S024-A058-W004-S02": ("E1", INS + ": 'da vam uđu'"),
    "S024-A058-W030-S01": ("E1", LIPOSS),
    "S024-A059-W006-S03": ("E1", INS + ": 'za ulazak,'"),
    "S024-A061-W045-S01": ("E2", "mā → 'onih'; 'čiji' nosi resumptivni -hu (COMMON 85:9)"),
    "S024-A061-W063-S01": ("E2", "anfus → 'ukućane'; 'njene' je dopuna (inserted)"),
    "S024-A062-W002-S01": ("E2", P_UNEXP + ": DET nije istiġrāq; 'Pravi' je Mehanovićev dodatak (dosljedno 8:2)"),
    "S024-A062-W020-S01": ("E2", P_UNEXP + ": ulāʾika ponavlja temu; 'Oni' nosi prvi REL"),
    "S024-A063-W019-S01": ("E2", LREQ),
    "S024-A064-W013-S02": ("E1", YAWM),
}

if __name__ == "__main__":
    run("S024_En-Nur", D)
