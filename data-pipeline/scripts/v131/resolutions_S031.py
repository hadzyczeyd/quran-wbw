# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 31."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_FUNC, P_NARROW, P_UNEXP, run  # noqa: E402

PRP = "namjerni li- → samo 'da' (ponovljeno 'da' nosi isti li-); 'bi' ide uz glagol (COMMON)"
VBI = "glagol u namjernoj rečenici → 'bi …' (COMMON: 'bi' uz glagol)"
PART = "partitivni min an-nāsi → genitiv 'ljudi' (" + P_FUNC + ", dosljedno 34:34); egzistencijalno 'Ima' je Mehanovićev dodatak"
COP = P_AUX + ": predikat preveden glagolski, 'će' gradi taj oblik i ujedno nosi samostalnu zamjenicu (dosljedno 32:10)"
LAHUM = "ulāʾika lahum → 'Njima' (DEM i -hum isti referent), lām → glagol pripadanja (dosljedno 34:37)"

D = {
    "S031-A005-W008-S02": ("E1", COP),
    "S031-A006-W001-S02": ("E1", PART),
    "S031-A006-W007-S01": ("E2", PRP),
    "S031-A006-W007-S02": ("E2", VBI),
    "S031-A006-W013-S02": ("E2", VBI),
    "S031-A006-W015-S01": ("E2", LAHUM),
    "S031-A006-W016-S01": ("E2", LAHUM),
    "S031-A008-W006-S01": ("E2", "lām u lahum → glagol pripadanja 'pripadaju' (dosljedno 34:37); 'Onima' nosi -hum"),
    "S031-A015-W002-S01": ("E2", "jāhada ʿalā (pritiskati, nagovarati) → 'budu nastojali … nagovore'"),
    "S031-A015-W003-S01": ("E2", "ʿalā (cilj nastojanja) → prvo 'da'; drugo 'da' nosi an"),
    "S031-A015-W009-S01": ("E2", "posvojni lām u laka preoblikovan u glagol 'znaš,' (" + P_FUNC + ")"),
    "S031-A016-W019-S01": ("E2", P_UNEXP + ": bi- (atā bi-); 'iznijeti' uzima akuzativni objekat (dosljedno 34:9)"),
    "S031-A016-W019-S02": ("E1", P_UNEXP + ": resumptivni -hā nije ponovljen; isturen objekat 'dobro i zlo,' nosi -hā iz innahā"),
    "S031-A016-W022-S01": ("E2", "Allāh → 'Allah' i ponovljeni subjekat 'On' (kao anaforsko 'Ga' u 33:41)"),
    "S031-A020-W018-S02": ("E1", PART),
    "S031-A022-W002-S01": ("E1", "yuslim → 'preda'"),
    "S031-A022-W003-S01": ("E1", "aslama wajhahu (predati sebe) → 'se sasvim' (wajh = cijelo biće, objekat predavanja)"),
    "S031-A028-W003-S01": ("E2", "korelativno 'I … i': oba 'i' nose wa (dosljedno 33:42)"),
    "S031-A030-W006-S02": ("E2", P_UNEXP + ": drugi anna nije ponovljen; 'što' nosi prvi anna"),
    "S031-A031-W010-S01": ("E2", PRP),
    "S031-A031-W010-S02": ("E2", VBI),
    "S031-A033-W007-S01": ("E2", "negativna konkordancija 'nimalo' bez vlastitog segmenta u svojoj rečenici → NEG (COMMON)"),
    "S031-A033-W015-S01": ("E1", COP),
    "S031-A033-W018-S01": ("E2", "šayʾan pripada drugoj rečenici → 'imalo'"),
    "S031-A033-W020-S01": ("E2", P_NARROW + ": waʿd → 'obećanje'; 'prijeteće' je Mehanovićevo objašnjenje (inserted)"),
    "S031-A034-W003-S01": ("E1", "isturen ʿindahu (ograničenje) → 'Samo'; 'zna' nosi ʿilm"),
    "S031-A034-W027-S01": ("E1", "khabīr → 'Onaj Koji u potpunosti, zna.'; 'i' nema arapskog wa (inserted)"),
}

if __name__ == "__main__":
    run("S031_Lukman", D)
