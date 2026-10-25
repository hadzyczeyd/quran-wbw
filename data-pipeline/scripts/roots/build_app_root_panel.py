# -*- coding: utf-8 -*-
"""
Iz provjerenog ROOT_PANEL JSON-a (nakon verify + prefer_short + excerpts apply) pravi sažeti fajl za web:
web/src/data/rootPanel/S<NNN>.json

  uv run scripts/roots/build_app_root_panel.py <FINAL.json> <sura>

Ostaju samo polja koja panel prikazuje (nalog V7, odjeljak 2) + veza riječ sure → korijen.
Rasponi su u kodnim tačkama; arapski znakovi su u BMP-u pa se poklapaju s JS indeksima stringa.
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "web", "src", "data", "rootPanel")


def card(c):
    hs = c["highlight_display_span"]
    e = c["ellipsis"]
    assert c["arabic"][hs["start"]:hs["end"]] == c["form"], c["id"]
    return {"id": c["id"], "form": c["form"], "meaning": c["meaning_bs"], "ref": c["ayah_ref"], "w": c["qac_location"][2],
            "ar": c["arabic"], "bs": c["bosnian"], "hl": [hs["start"], hs["end"]],
            "ell": [e["arabic_before"], e["arabic_after"], e["bosnian_before"], e["bosnian_after"]]}


def main():
    src, sura = sys.argv[1], int(sys.argv[2])
    d = json.load(open(src, encoding="utf-8"))
    roots = {r["root_bw"]: {"display": r["root_display"], "nouns": [card(c) for c in r["nouns"]],
                            "verbs": [card(c) for c in r["verbs"]]} for r in d["roots"]}
    words = {}
    for v in d["surah_verses"]:
        for w in v["words"]:
            if w.get("clickable"):
                assert w["root_bw"] in roots, w
                words[f"{v['ayah']}:{w['qac_word_index']}"] = w["root_bw"]
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, f"S{sura:03d}.json")
    json.dump({"surah": sura, "roots": roots, "words": words}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, separators=(",", ":"))
    n = sum(len(r["nouns"]) + len(r["verbs"]) for r in roots.values())
    print(f"{out}: {len(roots)} korijena, {n} kartica, {len(words)} riječi za klik, {os.path.getsize(out) // 1024} KB")


if __name__ == "__main__":
    main()
