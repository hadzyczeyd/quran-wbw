# -*- coding: utf-8 -*-
"""
Kratka bosanska značenja kartica (nalog V7, odjeljak 8) — dijelovi za agente i spajanje u GLOSS_DB.json.

  uv run scripts/roots/gloss_pool.py split <broj_dijelova>   → GLOSS_TODO_<k>.json iz GLOSS_TODO.json
  uv run scripts/roots/gloss_pool.py check <k>               → provjera GLOSS_DONE_<k>.json
  uv run scripts/roots/gloss_pool.py merge                   → svi ispravni GLOSS_DONE_*.json u GLOSS_DB.json
GLOSS_DONE_<k>.json: {"<key>": "<kratko značenje>"}.
"""
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
D = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "root_panel")
DB = os.path.join(D, "GLOSS_DB.json")


def load(p):
    return json.load(open(p, encoding="utf-8"))


def errors(item, g):
    e = []
    if not isinstance(g, str) or not g.strip():
        return ["prazno"]
    if g != g.strip() or "  " in g:
        e.append("razmaci")
    if re.search(r"[؀-ۿ]", g):
        e.append("arapska slova")
    if len(g.split()) > 7:
        e.append("predugo (>7 riječi)")
    if g.strip(" .,;:!?") != g.rstrip() and g[-1] in ".;:!?":
        e.append("završna interpunkcija")
    if re.search(r"[\"„“”()\[\]]", g):
        e.append("navodnici/zagrade")
    if len(g) > 12 and g.lower() in item["bosnian"].lower() and len(g.split()) > 4:
        e.append("citat prijevoda umjesto glose")
    return e


def main():
    cmd = sys.argv[1]
    if cmd == "split":
        todo = load(os.path.join(D, "GLOSS_TODO.json"))
        k = int(sys.argv[2])
        # po korijenu zajedno (sve kartice jednog korijena u istom dijelu)
        roots = sorted({i["root"] for i in todo})
        parts = [[] for _ in range(k)]
        sizes = [0] * k
        byroot = {}
        for i in todo:
            byroot.setdefault(i["root"], []).append(i)
        for r in sorted(roots, key=lambda r: -len(byroot[r])):
            j = sizes.index(min(sizes))
            parts[j] += byroot[r]
            sizes[j] += len(byroot[r])
        for j, p in enumerate(parts, 1):
            json.dump(p, open(os.path.join(D, f"GLOSS_TODO_{j}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{len(todo)} kartica u {k} dijelova: {sizes}")
    elif cmd == "check":
        k = sys.argv[2]
        todo = {i["key"]: i for i in load(os.path.join(D, f"GLOSS_TODO_{k}.json"))}
        p = os.path.join(D, f"GLOSS_DONE_{k}.json")
        done = load(p) if os.path.exists(p) else {}
        bad = 0
        for key, item in todo.items():
            if key not in done:
                bad += 1
                print("nema:", key)
                continue
            e = errors(item, done[key])
            if e:
                bad += 1
                print(key, "|", done[key], "|", "; ".join(e))
        extra = set(done) - set(todo)
        if extra:
            bad += len(extra)
            print("višak ključeva:", sorted(extra)[:5])
        print(f"dio {k}: {len(done)}/{len(todo)} značenja, grešaka {bad}")
        sys.exit(1 if bad else 0)
    elif cmd == "merge":
        db = load(DB) if os.path.exists(DB) else {}
        n = 0
        for p in sorted(glob.glob(os.path.join(D, "GLOSS_DONE_*.json"))):
            k = os.path.basename(p)[11:-5]
            todo = {i["key"]: i for i in load(os.path.join(D, f"GLOSS_TODO_{k}.json"))}
            for key, g in load(p).items():
                if key in todo and not errors(todo[key], g):
                    db[key] = g
                    n += 1
        json.dump(db, open(DB, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
        print(f"GLOSS_DB: {len(db)} značenja (dodano/obnovljeno {n})")


if __name__ == "__main__":
    main()
