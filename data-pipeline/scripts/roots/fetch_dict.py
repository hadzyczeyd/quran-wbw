# -*- coding: utf-8 -*-
"""
Preuzima QAC Dictionary stranice korijena (nalog V7, odjeljak 3) u keš sources/root_panel/dict/<hex>.html.

  uv run scripts/roots/fetch_dict.py <sure...>     (npr. 2-69)
Ime fajla je hex ROOT_BW (Windows ne razlikuje velika/mala slova). Pauza između zahtjeva 1.5 s.
"""
import os
import re
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
BASE = os.path.join(os.path.dirname(__file__), "..", "..")
MORPH = os.path.join(BASE, "sources", "quranic-corpus-morphology-0.4.txt")
DICT = os.path.join(BASE, "sources", "root_panel", "dict")


def path_of(root):
    return os.path.join(DICT, root.encode("utf-8").hex() + ".html")


def url_of(root):
    return "https://corpus.quran.com/qurandictionary.jsp?q=" + urllib.parse.quote(root, safe="")


def roots_of(suras):
    out = set()
    for line in open(MORPH, encoding="utf-8"):
        m = re.match(r"\((\d+):\d+:\d+:\d+\)\t\S*\t(N|V)\t(\S+)", line)
        if m and int(m[1]) in suras:
            r = re.search(r"ROOT:([^|]+)", m[3])
            if r:
                out.add(r[1])
    return sorted(out)


def parse_suras(args):
    s = set()
    for a in args:
        if "-" in a:
            x, y = a.split("-")
            s |= set(range(int(x), int(y) + 1))
        else:
            s.add(int(a))
    return s


def main():
    os.makedirs(DICT, exist_ok=True)
    roots = roots_of(parse_suras(sys.argv[1:]))
    todo = [r for r in roots if not os.path.exists(path_of(r))]
    print(f"korijena {len(roots)}, za preuzimanje {len(todo)}", flush=True)
    for i, r in enumerate(todo, 1):
        for attempt in range(4):
            try:
                req = urllib.request.Request(url_of(r), headers={"User-Agent": "Mozilla/5.0 (wbw-root-panel)"})
                html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8")
                if "Quran Dictionary" not in html:
                    raise ValueError("neočekivan sadržaj")
                open(path_of(r), "w", encoding="utf-8").write(html)
                break
            except Exception as e:  # noqa: BLE001
                print(f"  {r}: {e} (pokušaj {attempt + 1})", flush=True)
                time.sleep(10 * (attempt + 1))
        if i % 50 == 0:
            print(f"  {i}/{len(todo)}", flush=True)
        time.sleep(1.5)
    print("gotovo", flush=True)


if __name__ == "__main__":
    main()
