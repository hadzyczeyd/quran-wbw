# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 23."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_GOV, P_NARROW, P_UNEXP, run  # noqa: E402

MI = "subjektni sufiks / ime inna → eksplicitna zamjenica; pomoćni pripada glagolskom obliku (COMMON, dosljedno 15:16, 26:44)"
COORD = "drugi koordinirani glagol nosi samo svoj token; njegov subjektni sufiks → zajednički pomoćni (dosljedno 30:9, 15:19)"
AUXP = "subjektni sufiks bez eksplicitne zamjenice → pomoćni glagol koji nosi lice (COMMON 55.9)"
RECT = P_UNEXP + ": prijedlog traži samo arapska rekcija; bosanska dopuna je bez prijedloga (COMMON)"
MASDAR = "glagolska imenica prevedena da-rečenicom → 'da' + glagol (dosljedno 26:221)"
KUNVI = "kāna + imperfekt s eksplicitnom zamjenicom: oba sufiksa → 'vi', 'ste' nosi kāna (dosljedno 26:75, 37:21, 41:22)"
COP = "kopula 'biti/bili' uz particip bez arapskog segmenta ostaje inserted; 'će/bismo' nosi ime/zamjenicu (dosljedno 26:52)"
INS = P_NARROW + "; pojačivač bez arapskog segmenta ostaje inserted (COMMON)"

D = {
    "S023-A012-W002-S02": ("E1", MI),
    "S023-A015-W002-S02": ("E1", MI),
    "S023-A017-W002-S02": ("E1", MI),
    "S023-A017-W007-S02": ("E1", MI),
    "S023-A018-W010-S01": ("E2", RECT),
    "S023-A018-W011-S01": ("E2", MASDAR),
    "S023-A023-W002-S02": ("E1", MI),
    "S023-A024-W004-S02": ("E2", AUXP),
    "S023-A025-W001-S01": ("E1", "NEG in → 'ni-' u 'nije' + negativna konkordancija 'ništa' (nema vlastitog segmenta)"),
    "S023-A025-W002-S01": ("E1", "samostalno huwa → 'on' i kopula 'je' u 'nije' koja nosi njegovo lice (COMMON)"),
    "S023-A025-W009-S01": ("E1", P_UNEXP + ": ḥattā nije izražen; 'vrijeme' je akuzativ trajanja"),
    "S023-A030-W006-S02": ("E1", MI),
    "S023-A033-W006-S02": ("E2", AUXP),
    "S023-A033-W008-S01": ("E2", RECT),
    "S023-A033-W008-S02": ("E2", "liqāʾ → Mehanovićeva da-rečenica 'da će biti oživljeni,' (" + MASDAR + ")"),
    "S023-A035-W009-S01": ({"targets_from": "E1", "drop": ["biti?!"]}, COP),
    "S023-A041-W004-S03": ("E1", MI),
    "S023-A041-W005-S01": ("E1", "ġuṯāʾ → 'kao što … nanos riječni'; 'je' je kopula bez segmenta (inserted)"),
    "S023-A044-W002-S02": ("E1", "subjektni sufiks bez zamjenice i pomoćnog u ajetu → fused na glagolski token (COMMON 55.9)"),
    "S023-A044-W011-S03": ("E1", MI),
    "S023-A044-W014-S03": ("E2", COORD),
    "S023-A046-W005-S03": ("E1", "subjektni sufiks kānū → eksplicitni subjekat 'to'; 'bili su' nosi kāna"),
    "S023-A049-W001-S01": ("E1", P_UNEXP + ": narativni wa nema tokena; 'onda' je Mehanovićev dodatak (inserted)"),
    "S023-A050-W006-S03": ("E2", COORD),
    "S023-A055-W004-S01": ("E1", "bi- (sredstvo) → instrumental 'imetkom' (padež nosi prijedlog)"),
    "S023-A055-W005-S01": ("E1", P_UNEXP + ": eksplikativni min nije izražen"),
    "S023-A059-W005-S01": ("E1", P_NARROW + ": objekat 'druge' sadržan u značenju širka; 'u obožavanju' je dopuna (inserted)"),
    "S023-A061-W003-S01": ("E1", "fī uz sāraʿa → 'da' koji uvodi dopunu; 'čine' je Mehanovićeva dopuna (inserted)"),
    "S023-A063-W013-S01": ("E2", RECT),
    "S023-A065-W005-S01": ("E2", P_UNEXP + ": pasiv s agensom pretvoren u aktiv; min nema zasebnog tokena"),
    "S023-A066-W006-S03": ({"targets_from": "E2", "drop": ["ste"]}, KUNVI),
    "S023-A071-W011-S02": ("E1", MI),
    "S023-A074-W007-S02": ("E2", P_NARROW + ": ṣirāṭ → 'puta,'; 'Pravog' je objašnjavajuća dopuna (inserted)"),
    "S023-A075-W003-S02": ("E2", "kašafa → 'otklonili,'"),
    "S023-A075-W003-S03": ("E2", COORD),
    "S023-A075-W005-S02": ({"targets_from": "E1", "add": ["S023-A075-B013"]}, P_GOV + ": -him (njih) → 'od njih'; 'nalaze' je Mehanovićeva dopuna (inserted)"),
    "S023-A076-W002-S02": ("E1", MI),
    "S023-A078-W008-S01": ("E1", "qalīl → 'malo'"),
    "S023-A078-W009-S01": ("E1", "pojačajno mā uz qalīlan → uzvično 'kako'"),
    "S023-A084-W004-S02": ("E2", INS + ": 'sve'"),
    "S023-A092-W006-S01": ("E1", "ašraka → 'Mu pridružuju!' (objekat sadržan u značenju glagola, dosljedno 23:59)"),
    "S023-A096-W002-S02": ("E1", P_UNEXP + ": relativna konstrukcija sažeta u pridjev 'lijepim' (nosi aḥsan)"),
    "S023-A100-W014-S01": ("E2", INS + ": 'sve'"),
    "S023-A101-W005-S02": ("E1", "lā (negacija vrste, 'nema') → egzistencijalno 'neće biti'"),
    "S023-A104-W006-S01": ("E1", COP),
    "S023-A105-W006-S03": ({"targets_from": "E2", "drop": ["ste"]}, KUNVI),
    "S023-A107-W006-S03": ("E1", COP),
    "S023-A110-W001-S02": ("E1", P_AUX + ": 'ste … se … rugali'"),
    "S023-A110-W001-S03": ("E1", MI),
    "S023-A110-W002-S01": ("E1", "siḫriyy → leksički sadržaj 'rugali' (idiom ittaḫaḏa … siḫriyyan)"),
    "S023-A110-W004-S01": ("E2", "kauzativ ansā → 'ste zbog toga … zaboravljali'"),
    "S023-A110-W004-S02": ("E2", P_UNEXP + ": uzročnik kauzativa preoblikovan u 'zbog toga' (nosi glagol)"),
    "S023-A110-W005-S01": ("E2", "ḏikr → dopuna 'na Mene'"),
    "S023-A110-W005-S02": ("E2", "-ī → 'Mene'"),
    "S023-A035-B017": ("INS", COP),
    "S023-A117-W012-S01": ("E1", "ḥisāb → 'račun … polagati,'; 'će' nosi -hu"),
}

if __name__ == "__main__":
    run("S023_El-Muminun", D)
