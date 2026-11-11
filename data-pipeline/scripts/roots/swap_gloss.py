# -*- coding: utf-8 -*-
"""
Kratko značenje kartica preuzetih iz objavljenih panela, a premještenih na drugi ajet (dupli kontekst / kraći ajet).
SWAP_GLOSS_DONE_<k>.json: {"root|form|ref": "OK" | "<novo kratko značenje>"}.

  uv run scripts/roots/swap_gloss.py check <k>      → provjera dijela
  uv run scripts/roots/swap_gloss.py apply <sura>   → meaning_bs u SURA_<n>_ROOT_PANEL_SHORT.json
"""
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
D = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "root_panel")


def done():
    out = {}
    for f in sorted(glob.glob(os.path.join(D, "SWAP_GLOSS_DONE_*.json"))):
        out.update(json.load(open(f, encoding="utf-8")))
    return out


def main():
    cmd, x = sys.argv[1], sys.argv[2]
    if cmd == "check":
        todo = json.load(open(os.path.join(D, f"SWAP_GLOSS_TODO_{x}.json"), encoding="utf-8"))
        d = json.load(open(os.path.join(D, f"SWAP_GLOSS_DONE_{x}.json"), encoding="utf-8"))
        bad = 0
        for it in todo:
            v = d.get(it["key"])
            err = None
            if v is None:
                err = "nema unosa"
            elif v != "OK":
                if re.search(r"[؀-ۿ]", v):
                    err = "arapska slova"
                elif len(v.split()) > 7:
                    err = "više od 7 riječi"
                elif re.search(r"[\"'„“”()\[\]]", v) or re.search(r"[.,;:!?]$", v):
                    err = "navodnici/zagrade/završni znak"
                elif v == it["meaning_bs"]:
                    err = "isto kao staro — upiši OK"
            if err:
                bad += 1
                print(it["key"], err)
        print(f"dio {x}: {len(d)} unosa, promijenjeno {sum(1 for v in d.values() if v != 'OK')}, grešaka {bad}")
        return
    n = int(x)
    g = done()
    p = os.path.join(D, f"SURA_{n}_ROOT_PANEL_SHORT.json")
    d = json.load(open(p, encoding="utf-8"))
    ch = 0
    for r in d["roots"]:
        for s in ("nouns", "verbs"):
            for c in r[s]:
                v = g.get(f"{r['root_bw']}|{c['form']}|{c['ayah_ref']}")
                if v and v != "OK" and c["meaning_bs"] != v:
                    c.setdefault("meaning_bs_published", c["meaning_bs"])
                    c["meaning_bs"] = v
                    ch += 1
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"S{n}: promijenjeno kratko značenje {ch}")


if __name__ == "__main__":
    main()
