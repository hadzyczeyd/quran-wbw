# -*- coding: utf-8 -*-
"""
Zajednički bazen izvoda: isti primjer (ajet + ciljna riječ) u više sura dobija isti izvod.

  uv run scripts/roots/excerpt_pool.py make  <sure...>          → sources/root_panel/POOL_TODO_<k>.json (dijelovi za agente)
  uv run scripts/roots/excerpt_pool.py check <k>                → provjera POOL_DONE_<k>.json prema POOL_TODO_<k>.json
  uv run scripts/roots/excerpt_pool.py split <sure...>          → EXCERPTS_<sura>.json iz POOL_DONE_*.json + postojećih
Ključ: "ref|start|end" (raspon ciljne riječi u punom ajetu).
"""
import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
D = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "root_panel")


def key_of(c):
    return f"{c['ayah_ref']}|{c['highlight_span']['start']}|{c['highlight_span']['end']}"


def cards(n):
    d = json.load(open(os.path.join(D, f"SURA_{n}_ROOT_PANEL_SHORT.json"), encoding="utf-8"))
    for r in d["roots"]:
        for s in ("nouns", "verbs"):
            yield from r[s]


def known():
    """Već urađeni izvodi (EXCERPTS_*.json i POOL_DONE_*.json) po ključu."""
    k = {}
    for f in glob.glob(os.path.join(D, "EXCERPTS_*.json")):
        n = os.path.basename(f)[9:-5]
        byid = {c["id"]: c for c in cards(n)} if os.path.exists(os.path.join(D, f"SURA_{n}_ROOT_PANEL_SHORT.json")) else {}
        for cid, e in json.load(open(f, encoding="utf-8")).items():
            if cid in byid:
                k[key_of(byid[cid])] = e
    for f in glob.glob(os.path.join(D, "POOL_DONE_*.json")):
        k.update(json.load(open(f, encoding="utf-8")))
    return k


def main():
    cmd, suras = sys.argv[1], sys.argv[2:]
    if cmd == "make":
        have = known()
        todo = {}
        for n in suras:
            for item in json.load(open(os.path.join(D, f"EXCERPT_TODO_{n}.json"), encoding="utf-8")):
                c = next(c for c in cards(n) if c["id"] == item["id"])
                k = key_of(c)
                if k not in have and k not in todo:
                    item = dict(item, key=k)
                    item.pop("id")
                    todo[k] = item
        items = list(todo.values())
        parts = int(os.environ.get("PARTS", "4"))
        for i in range(parts):
            json.dump(items[i::parts], open(os.path.join(D, f"POOL_TODO_{i + 1}.json"), "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
        print(f"novih jedinstvenih izvoda: {len(items)} u {parts} dijela; već poznatih: {len(have)}")
    elif cmd == "check":
        sys.path.insert(0, os.path.dirname(__file__))
        from excerpts import check_one
        k = suras[0]
        todo = {i["key"]: i for i in json.load(open(os.path.join(D, f"POOL_TODO_{k}.json"), encoding="utf-8"))}
        done = json.load(open(os.path.join(D, f"POOL_DONE_{k}.json"), encoding="utf-8"))
        bad = 0
        for key, item in todo.items():
            if key not in done:
                print(key, "nema izvoda")
                bad += 1
                continue
            m = item["arabic_full_marked"]
            st = m.index("[[")
            en = m.index("]]") - 2
            card = {"arabic_full": m.replace("[[", "").replace("]]", ""), "bosnian_full": item["bosnian_full"],
                    "highlight_span": {"start": st, "end": en}}
            errs, _ = check_one(card, done[key])
            if errs:
                bad += 1
                print(key, "; ".join(errs))
        print(f"dio {k}: {len(done)} izvoda, grešaka {bad}")
    elif cmd == "split":
        have = known()
        for n in suras:
            todo = json.load(open(os.path.join(D, f"EXCERPT_TODO_{n}.json"), encoding="utf-8"))
            byid = {c["id"]: c for c in cards(n)}
            out, miss = {}, []
            for item in todo:
                k = key_of(byid[item["id"]])
                if k in have:
                    out[item["id"]] = {kk: v for kk, v in have[k].items() if kk in ("arabic", "bosnian", "note")}
                else:
                    miss.append(item["id"])
            json.dump(out, open(os.path.join(D, f"EXCERPTS_{n}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(n, "izvoda", len(out), "nedostaje", len(miss))


if __name__ == "__main__":
    main()
