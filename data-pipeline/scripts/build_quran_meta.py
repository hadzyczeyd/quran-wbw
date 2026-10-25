# -*- coding: utf-8 -*-
"""
Metapodaci sura za web (web/src/data/quranMeta.json): redoslijed objave, broj rukua, džuzevi,
ajeti sedžde (Tanzil quran-data.xml v1.0, preuzeto 2026-10-25) + broj riječi (QAC morphology 0.4).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "v131"))
from common import QAC_MORPH  # noqa: E402

TANZIL = json.load(open(os.path.join(os.path.dirname(__file__), "..", "sources", "tanzil_quran_data.json"), encoding="utf-8"))
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "web", "src", "data", "quranMeta.json")

words = {}
with open(QAC_MORPH, encoding="utf-8") as f:
    for line in f:
        m = re.match(r"\((\d+):(\d+):(\d+):\d+\)", line)
        if m:
            words.setdefault(int(m.group(1)), set()).add((int(m.group(2)), int(m.group(3))))

juzs = TANZIL["juzs"]  # [index, sura, aya]


def juz_of(s, a):
    j = 1
    for idx, js, ja in juzs:
        if (js, ja) <= (s, a):
            j = idx
    return j


surahs = {}
for idx, ayas, order, rukus, typ in TANZIL["suras"]:
    surahs[idx] = {"order": order, "rukus": rukus, "words": len(words[idx]),
                   "juz": sorted({juz_of(idx, a) for a in range(1, ayas + 1)}),
                   "sajda": [[a, t] for s, a, t in TANZIL["sajdas"] if s == idx]}
json.dump({"source": "Tanzil quran-data.xml v1.0; QAC morphology 0.4", "juz": juzs, "surahs": surahs},
          open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("ok", len(surahs), os.path.getsize(OUT))
