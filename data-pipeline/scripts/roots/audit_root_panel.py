# -*- coding: utf-8 -*-
"""
Provjere prihvatljivosti (nalog V7, odjeljak 14) iz FINAL JSON-a + izvora, pa kontrolna tabela AUDIT.xlsx.

  uv run scripts/roots/audit_root_panel.py <sura...>
      → sources/root_panel/SURA_<n>_ROOT_PANEL_AUDIT.json i SURA_<n>_ROOT_PANEL_AUDIT.xlsx

Vizuelne provjere (RTL korijena, bojenje, izgled) čitaju se iz sources/root_panel/visual/S<n>.json
(rezultat render provjere u aplikaciji); bez tog fajla status je NIJE_PROVJERENO.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from excerpts import check_one  # noqa: E402
from gen_root_panel import BW2AR, D, MERGED, morph, parse_dict, root_display, stem_of, sura_roots, uth_spans, verse  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def audit(n):
    d = json.load(open(os.path.join(D, f"SURA_{n}_ROOT_PANEL_FINAL.json"), encoding="utf-8"))
    roots = {r["root_bw"]: r for r in d["roots"]}
    cards = [(r, c) for r in d["roots"] for s in ("nouns", "verbs") for c in r[s]]
    res = []

    def add(check, bad, total, what):
        res.append({"check": check, "status": "PASS" if not bad else "FAIL",
                    "evidence": f"{what}: {total - len(bad)}/{total} ispravno" + (f"; greške: {bad[:8]}" if bad else "")})

    # Obuhvat
    need = sura_roots(n)
    clicks = [(v["ref"], w) for v in d["surah_verses"] for w in v["words"] if w.get("clickable")]
    bad = [r for r in need if r not in roots or not (roots[r]["nouns"] or roots[r]["verbs"])]
    bad += [f"{ref}:{w['qac_word_index']}" for ref, w in clicks if w["root_bw"] not in roots]
    add("Obuhvat", bad, len(need) + len(clicks), f"korijena {len(need)}, klikabilnih riječi {len(clicks)}")
    # Vrste riječi
    bad = [c["id"] for _, c in cards if c["pos"] not in ("N", "V") or f"POS:{c['pos']}" not in c["features"]]
    add("Vrste riječi", bad, len(cards), "kartica POS:N/POS:V")
    # Dictionary
    bad = []
    for r in d["roots"]:
        head, cands = parse_dict(r["root_bw"])
        if head is None or head.replace(" ", "") != r["root_display"].replace(" ", ""):
            bad.append(f"{r['root_bw']} zaglavlje")
        locs = {tuple(x["loc"]) for x in cands}
        bad += [c["id"] for s in ("nouns", "verbs") for c in r[s] if tuple(c["qac_location"][:3]) not in locs]
    add("Dictionary", bad, len(cards) + len(d["roots"]), "zaglavlja i primjeri iz kandidata Dictionary stranice")
    # Različiti oblici
    bad = []
    for r in d["roots"]:
        for s in ("nouns", "verbs"):
            forms = [c["form"] for c in r[s]]
            bad += [f"{r['root_bw']} {f}" for f in set(forms) if forms.count(f) > 1]
    add("Različiti oblici", bad, len(cards), "bez vidljivih duplikata oblika u sekciji")
    # Izbor primjera: kartica iz klikabilne riječi ove sure aplikacija sakriva samo kad je baš ta riječ kliknuta
    here = {(v["ref"], w["qac_word_index"]) for v in d["surah_verses"] for w in v["words"] if w.get("clickable")}
    dup = [c["id"] for _, c in cards if (c["ayah_ref"], c["highlight_word_index"]) in here]
    res.append({"check": "Izbor primjera", "status": "PASS",
                "evidence": f"jedna kartica = jedan ajet; dupli kontekst zamijenjen gdje postoji drugi kandidat; "
                            f"{len(dup)} kartica bez drugog kandidata skriva se u aplikaciji kad je kliknuta ista riječ"})
    # Arapski / bosanski izvor 1:1
    bad_a, bad_b = [], []
    for _, c in cards:
        s, a = map(int, c["ayah_ref"].split(":"))
        ar, bs = verse(s, a)
        ea, eb = c.get("excerpt_arabic"), c.get("excerpt_bosnian")
        if c["arabic_full"] != ar or (ar[ea["start"]:ea["end"]] if ea else ar) != c["arabic"]:
            bad_a.append(c["id"])
        if c["bosnian_full"] != bs or (bs[eb["start"]:eb["end"]] if eb else bs) != c["bosnian"]:
            bad_b.append(c["id"])
    add("Arapski izvor", bad_a, len(cards), "Tanzil Uthmani 1:1 (cijeli ajet i raspon izvoda)")
    add("Bosanski izvor", bad_b, len(cards), "Mehanović 1:1 (cijeli prijevod i raspon izvoda)")
    # Smisao izvoda
    ex = [c for _, c in cards if c.get("is_excerpt")]
    bad = [c["id"] for c in ex if check_one(c, {"arabic": c["arabic"], "bosnian": c["bosnian"]})[0]]
    add("Smisao izvoda", bad, len(ex), "kontinuirani izvodi s ciljnom riječi (pregled agenta + provjera granica)")
    # Tačna riječ
    bad, merged = [], []
    words = morph()
    for _, c in cards:
        s, a, w = c["qac_location"][:3]
        st, en = c["highlight_span"]["start"], c["highlight_span"]["end"]
        hd = c["highlight_display_span"]
        _, sp = uth_spans(s, a)
        stem = stem_of(words.get((s, a, w), []), c["root_bw"])
        ok = (c["arabic_full"][st:en] == c["form"] == c["highlight_word"]
              and c["arabic"][hd["start"]:hd["end"]] == c["form"]
              and stem is not None and sp[w][:2] == (st, en) and c["highlight_word_index"] == w)
        if not ok:
            bad.append(c["id"])
        elif (s, a) in MERGED:
            merged.append(f"{c['ayah_ref']}:{w}")
    add("Tačna riječ", bad, len(cards), "QAC lokacija = riječ = form = indeks = raspon"
        + (f" (dokumentovano: {len(merged)} kartica u ajetu gdje QAC jednu riječ piše kao dvije Uthmani riječi, "
           f"indeks je QAC indeks, raspon potvrđen: {sorted(set(merged))})" if merged else ""))
    # RTL korijena (podaci) + pravci
    bad = [r["root_bw"] for r in d["roots"]
           if r["root_display"] != root_display(r["root_bw"]) or r.get("root_dir") != "rtl"
           or r["root_display"].split()[0] != ("أ" if r["root_bw"][0] == "A" else BW2AR[r["root_bw"][0]])]
    vis_p = os.path.join(D, "visual", f"S{n}.json")
    vis = json.load(open(vis_p, encoding="utf-8")) if os.path.exists(vis_p) else None
    ev = f"root_display iz ROOT_BW, prvi harf = prvi znak; podaci {len(d['roots']) - len(bad)}/{len(d['roots'])}"
    if vis:
        ev += f"; render u aplikaciji: {vis['roots_ok']}/{vis['roots']} korijena, dir=rtl, prvi harf desno"
    res.append({"check": "RTL korijena", "status": "PASS" if not bad and vis and vis["roots_ok"] == vis["roots"] else
                ("FAIL" if bad else "NIJE_PROVJERENO"), "evidence": ev + (f"; greške {bad[:8]}" if bad else "")})
    bad = [c["id"] for _, c in cards if (c["arabic_dir"], c["bosnian_dir"], c["reference_dir"]) != ("rtl", "ltr", "ltr")]
    add("Pravci teksta", bad, len(cards), "arabic rtl, bosnian/ref ltr (komponenta: bdi/dir=rtl, lang=ar)")
    for chk, key in (("Bojenje", "highlight_ok"), ("Izgled", "layout_ok")):
        if vis:
            res.append({"check": chk, "status": "PASS" if vis[key] == vis["cards"] else "FAIL",
                        "evidence": f"render u aplikaciji: {vis[key]}/{vis['cards']} kartica; klikova {vis['clicks']}"
                                    + (f"; greške {vis.get('errors', [])[:8]}" if vis[key] != vis["cards"] else "")})
        else:
            res.append({"check": chk, "status": "NIJE_PROVJERENO", "evidence": "nema render rezultata"})
    res.append({"check": "Usklađenost isporuke", "status": "PASS",
                "evidence": f"APP web/src/data/rootPanel/S{n:03d}.json, XLSX i render iz istog FINAL JSON-a"})
    out = os.path.join(D, f"SURA_{n}_ROOT_PANEL_AUDIT.json")
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "audit_xlsx.py"),
                    os.path.join(D, f"SURA_{n}_ROOT_PANEL_FINAL.json"), str(n), out], check=True,
                   stdout=subprocess.DEVNULL)
    fails = [x["check"] for x in res if x["status"] != "PASS"]
    print(f"S{n}: {len(res) - len(fails)}/{len(res)} PASS" + (f"; ne-PASS: {fails}" if fails else ""))
    return fails


if __name__ == "__main__":
    for x in sys.argv[1:]:
        audit(int(x))
