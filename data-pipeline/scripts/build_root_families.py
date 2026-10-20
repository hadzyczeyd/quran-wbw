# -*- coding: utf-8 -*-
"""Pretvara QAC_SURA_N_IMENICE_GLAGOLI_PRIDJEVI.xlsx u web/src/data/roots/S{n}.json (test funkcija korijena).

Upotreba: uv run scripts/build_root_families.py <xlsx> [...]
"""
import json
import os
import re
import sys

import openpyxl

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "web", "src", "data", "roots")


def norm(root):
    return re.sub(r"[\sً-ْٰ]", "", root).translate(str.maketrans("أإآٱ", "اااا"))


for path in sys.argv[1:]:
    surah = int(re.search(r"QAC_SURA_(\d+)_", path).group(1))
    ws = openpyxl.load_workbook(path, read_only=True).worksheets[0]
    families, cur = {}, None
    for row in list(ws.iter_rows(values_only=True))[1:]:
        root, *cols = (row + (None,) * 4)[:4]
        if root:
            cur = {"root": str(root).strip(), "imenice": [], "glagoli": [], "pridjevi": []}
            families[norm(cur["root"])] = cur
        if cur is None:
            continue
        for key, v in zip(("imenice", "glagoli", "pridjevi"), cols):
            if v:
                cur[key].append(str(v).strip())
        if not any(row):
            cur = None
    with open(os.path.join(OUT, f"S{surah:03d}.json"), "w", encoding="utf-8") as f:
        json.dump(families, f, ensure_ascii=False, indent=1)
    print(surah, len(families), "korijena")
