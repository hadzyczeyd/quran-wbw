# -*- coding: utf-8 -*-
"""Suha provjera REVIDIRANA APP_READY fajlova (bez upisa u bazu)."""
import sys
import os
import glob
import openpyxl

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(__file__))
from revidirana import load_morphology, parse  # noqa: E402


def main():
    folder = sys.argv[1]
    min_surah = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    morph = load_morphology(os.path.join(folder, "quranic-corpus-morphology-0.4.txt"))
    files = sorted(glob.glob(os.path.join(folder, "*_APP_READY*.xlsx")))
    bad = 0
    for f in files:
        if int(os.path.basename(f).split("_")[0]) < min_surah:
            continue
        wb = openpyxl.load_workbook(f, data_only=True)
        data, problems = parse(wb, morph)
        s = data["stats"]
        print(
            f"{'PROBLEM' if problems else 'ok':7} sura {data['surah_id']:3}: {len(data['words'])} riječi, "
            f"{len(data['segments'])} seg, {len(data['tokens'])} tok, {len(data['links'])} veza, "
            f"fused {s['fused']} (razlika sa fajlom {s['fused_status_disagree']})"
        )
        for p in problems[:8]:
            print("        -", p)
        bad += bool(problems)
    print(f"Fajlova s problemima: {bad}")


if __name__ == "__main__":
    main()
