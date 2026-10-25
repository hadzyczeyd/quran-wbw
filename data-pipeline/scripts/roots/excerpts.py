# -*- coding: utf-8 -*-
"""
Izvodi za duge ajete (nalog V7, odjeljak 7): kontinuirani arapski i bosanski izvod koji sadrži ciljnu riječ.

  uv run scripts/roots/excerpts.py todo  <SHORT.json> <todo.json> [prag]   → lista kartica za izvod
  uv run scripts/roots/excerpts.py check <SHORT.json> <excerpts.json>      → samo provjera
  uv run scripts/roots/excerpts.py apply <SHORT.json> <excerpts.json> <FINAL.json>

excerpts.json: {"<card id>": {"arabic": "<kontinuirani izvod ili FULL>", "bosnian": "<kontinuirani izvod ili FULL>",
                "note": "zašto je smisao očuvan"}}
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from verify_root_panel import words_with_spans  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def cards(d):
    for root in d["roots"]:
        for sec in ("nouns", "verbs"):
            for c in root[sec]:
                yield root, c


def todo(src, out, limit):
    d = json.load(open(src, encoding="utf-8"))
    res = []
    for root, c in cards(d):
        if len(words_with_spans(c["arabic_full"])) > limit:
            st, en = c["highlight_span"]["start"], c["highlight_span"]["end"]
            full = c["arabic_full"]
            res.append({"id": c["id"], "ref": c["ayah_ref"], "form": c["form"], "meaning_bs": c["meaning_bs"],
                        "arabic_full_marked": full[:st] + "[[" + full[st:en] + "]]" + full[en:],
                        "bosnian_full": c["bosnian_full"]})
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(res)} kartica treba izvod → {out}")


def check_one(c, e):
    errs = []
    full, bs = c["arabic_full"], c["bosnian_full"]
    st, en = c["highlight_span"]["start"], c["highlight_span"]["end"]
    ar = full if e["arabic"] == "FULL" else e["arabic"]
    b = bs if e["bosnian"] == "FULL" else e["bosnian"]
    if full.count(ar) != 1:
        errs.append("arapski izvod nije jedinstven kontinuirani dio ajeta")
        return errs, None
    a0 = full.index(ar)
    if not (a0 <= st and en <= a0 + len(ar)):
        errs.append("arapski izvod ne sadrži ciljnu riječ")
    # granice izvoda moraju biti na razmaku između riječi
    if ar != ar.strip() or (a0 > 0 and not full[a0 - 1].isspace()) or (a0 + len(ar) < len(full) and not full[a0 + len(ar)].isspace()):
        errs.append("arapski izvod siječe riječ")
    if bs.count(b) != 1:
        errs.append("bosanski izvod nije jedinstven kontinuirani dio prijevoda")
        return errs, None
    b0 = bs.index(b)
    if b != b.strip() or (b0 > 0 and bs[b0 - 1].isalnum()) or (b0 + len(b) < len(bs) and bs[b0 + len(b)].isalnum()):
        errs.append("bosanski izvod siječe riječ")
    return errs, (a0, ar, b0, b)


def main():
    cmd = sys.argv[1]
    if cmd == "todo":
        todo(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 12)
        return
    d = json.load(open(sys.argv[2], encoding="utf-8"))
    ex = json.load(open(sys.argv[3], encoding="utf-8"))
    byid = {c["id"]: c for _, c in cards(d)}
    bad = 0
    for cid, e in ex.items():
        if cid not in byid:
            print(cid, "nepoznata kartica")
            bad += 1
            continue
        errs, ok = check_one(byid[cid], e)
        if errs:
            bad += 1
            print(cid, "; ".join(errs))
            continue
        if cmd == "apply":
            c = byid[cid]
            a0, ar, b0, b = ok
            c["arabic"], c["bosnian"] = ar, b
            c["excerpt_arabic"] = {"start": a0, "end": a0 + len(ar)}
            c["excerpt_bosnian"] = {"start": b0, "end": b0 + len(b)}
            c["is_excerpt"] = ar != c["arabic_full"] or b != c["bosnian_full"]
            c["ellipsis"] = {"arabic_before": a0 > 0, "arabic_after": a0 + len(ar) < len(c["arabic_full"]),
                             "bosnian_before": b0 > 0, "bosnian_after": b0 + len(b) < len(c["bosnian_full"])}
            c["highlight_display_span"] = {"start": c["highlight_span"]["start"] - a0, "end": c["highlight_span"]["end"] - a0}
            c["excerpt_note"] = e.get("note", "")
    print(f"izvoda {len(ex)}; grešaka {bad}")
    if cmd == "apply":
        if bad:
            sys.exit(1)
        for _, c in cards(d):
            if "highlight_display_span" not in c or not c.get("is_excerpt"):
                c["highlight_display_span"] = c["highlight_span"]
                c["is_excerpt"] = c.get("is_excerpt", False) and c["arabic"] != c["arabic_full"]
            c.setdefault("ellipsis", {"arabic_before": False, "arabic_after": False, "bosnian_before": False, "bosnian_after": False})
            hs = c["highlight_display_span"]
            assert c["arabic"][hs["start"]:hs["end"]] == c["form"], c["id"]
        json.dump(d, open(sys.argv[4], "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
