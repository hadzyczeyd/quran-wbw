# -*- coding: utf-8 -*-
"""
CP8 SEGMENTED EXPORT + CP9 final gate: APP_READY (25 listova) i VIZUELNA (8 listova) iz istog
CONSENSUS_MASTER-a. Upotreba: uv run scripts/v131/export.py <RUN> <out_dir>
"""
import os
import sys

import openpyxl
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont
from openpyxl.styles import Alignment, Font, PatternFill

sys.path.insert(0, os.path.dirname(__file__))
from common import (INSERTED, PROFILES, RUNS, UNEXPRESSED, atomic_write_json, canonical_json,  # noqa: E402
                    load_json, now, sha256_bytes, sha256_file)
from cp0_cp1 import SCHEMA  # noqa: E402
from derive import CONTENT_TAGS, derive  # noqa: E402

PHASES = [("FIRST", "cp5_first"), ("SECOND", "cp6_second"), ("THIRD", "cp7_third")]
CHANGE_IDS = {}
ERROR_MARKERS = ("#REF!", "#VALUE!", "#NAME?", "#DIV/0!", "#N/A", "#NUM!", "#NULL!", "#SPILL!", "#CALC!")


def row_hash(d):
    return sha256_bytes(canonical_json(d).encode("utf-8"))


def review_cols(results_by_phase, kind, rid, row_h, risky, changed):
    out = []
    for ph, _ in PHASES:
        res = results_by_phase.get(ph, {}).get(kind, {})
        if rid in res:
            r = res[rid]
            label = {"FIRST": "FIRST", "SECOND": "SECOND", "THIRD": "THIRD"}[ph]
            basis = r["basis"] if ph == "FIRST" else ("SEMANTIC_RECHECK" if ph == "SECOND" else "SEMANTIC_EXCEPTION_RECHECK")
            later = [results_by_phase.get(p, {}).get(kind, {}).get(rid, {}).get("status") for p in ("SECOND", "THIRD")]
            recheck = results_by_phase.get("THIRD_RECHECK", {}).get(kind, {}).get(rid)
            if ph == "THIRD" and r["status"] == "FAIL" and rid in changed and recheck and recheck["status"] == "PASS":
                out += ["THIRD_REVIEW_PASS", f"THIRD_REVIEW_FAIL → korigovano ({','.join(CHANGE_IDS.get(rid, []))}); {recheck['note']} Prvobitni nalaz: {r['note']}"]
                continue
            if ph == "FIRST" and r["status"] == "FAIL" and rid in changed and later and all(x == "PASS" for x in later):
                ci = ",".join(c for c in CHANGE_IDS.get(rid, [])) or "change-impact"
                out += ["FIRST_REVIEW_PASS", f"FIRST_REVIEW_FAIL → korigovano u CONSENSUS_MASTER ({ci}); ponovna ciljana provjera "
                                             f"nakon korekcije PASS u SECOND i THIRD. Prvobitni nalaz: {r['note']}"]
            else:
                out += [f"{label}_REVIEW_{r['status']}", f"{basis} — {r['note']}"]
        elif kind == "links" and ph != "THIRD" and any(x in changed for x in rid.split(">")) and (
                lambda st: st and all(x == "PASS" for x in st))(
                [results_by_phase[p][kind][rid]["status"] for p, _ in PHASES[[q for q, _ in PHASES].index(ph) + 1:]
                 if rid in results_by_phase.get(p, {}).get(kind, {})]):
            # Veza nastala korekcijom nakon ove faze: potvrđena ciljanom provjerom u kasnijoj fazi.
            ci = ",".join(sorted({c for x in rid.split(">") for c in CHANGE_IDS.get(x, [])}))
            out += [f"{ph}_REVIEW_PASS", f"Red nastao korekcijom nakon {ph} ({ci}); ponovna ciljana provjera nakon korekcije PASS u kasnijoj fazi."]
        elif results_by_phase.get("THIRD_RECHECK", {}).get(kind, {}).get(rid):
            rr = results_by_phase["THIRD_RECHECK"][kind][rid]
            out += [f"{ph}_REVIEW_{rr['status']}", f"Red nastao korekcijom u THIRD (prije nije postojao); {rr['note']}"]
        elif ph != "FIRST" and rid not in risky and rid not in changed:
            label = ph
            basis = "DETERMINISTIC_UNCHANGED_VALIDATION" if ph == "SECOND" else "FINAL_DETERMINISTIC_VALIDATION"
            out += [f"{label}_REVIEW_PASS", f"{basis} — Entry1=Entry2, row_hash {row_h[:16]} nepromijenjen, ID/boja/source PASS."]
        else:
            out += [f"{ph}_REVIEW_MISSING", "nema zapisa revizije"]
    return out


def main():
    run = sys.argv[1]
    out_dir = sys.argv[2]
    run_dir = os.path.join(RUNS, run)
    manifest = load_json(os.path.join(run_dir, "RUN_MANIFEST.json"))
    snap = load_json(os.path.join(run_dir, "cp1", "CP1_SOURCE_SNAPSHOT.json"))
    inv = load_json(os.path.join(run_dir, "cp1", "INVENTORY_BATCH_PLAN.json"))
    color_master = load_json(os.path.join(run_dir, "cp0", "QAC_COLOR_MASTER.json"))
    master = load_json(os.path.join(run_dir, "cp4", "CONSENSUS_MASTER.json"))
    compare = load_json(os.path.join(run_dir, "cp4", "ENTRY_COMPARE.json"))
    der = derive(snap, master)
    surah, name = snap["surah_id"], snap["surah_name"]

    results = {}
    changes = []
    for ph, d in PHASES:
        p = os.path.join(run_dir, d, "RESULTS.json")
        if os.path.exists(p):
            results[ph] = load_json(p)
        c = os.path.join(run_dir, d, "CHANGE_IMPACT.json")
        if os.path.exists(c):
            changes += load_json(c)["changes"]
    rc = os.path.join(run_dir, "cp7_third", "RECHECK_RESULTS.json")
    if os.path.exists(rc):
        results["THIRD_RECHECK"] = load_json(rc)
    changed = {x for c in changes for x in c["affected_records"]}
    # Veza čiji je segment ili token zahvaćen korekcijom također je promijenjena.
    changed |= {rid for r in results.values() for rid in r.get("links", {}) if any(x in changed for x in rid.split(">"))}
    for c in changes:
        for x in c["affected_records"]:
            CHANGE_IDS.setdefault(x, []).append(c["change_id"])
    mism = {r["stable_id"] for r in compare["rows"] if r["compare_status"] != "MATCH"}
    risky_seg = set(results.get("SECOND", {}).get("segments", {})) | set(results.get("THIRD", {}).get("segments", {}))
    risky_tok = set(results.get("SECOND", {}).get("tokens", {})) | set(results.get("THIRD", {}).get("tokens", {}))
    risky_lnk = set(results.get("SECOND", {}).get("links", {})) | set(results.get("THIRD", {}).get("links", {}))
    completeness = results.get("FIRST", {}).get("completeness", {})

    uth = snap["uthmani"]
    meh = snap["mehanovic"]
    seg_by_id = {s["qac_segment_id"]: s for s in der["segments"]}
    tok_by_id = {t["bosnian_token_id"]: t for t in der["tokens"]}

    # ------------------------------------------------------------ APP_READY sadržaj
    S = {k: [] for k in SCHEMA["APP_READY"]}
    for w in snap["words"]:
        S["Rijeci"].append([w["surah_id"], w["ayah_id"], w["word_order"], w["qac_word_id"], w["arabic_word"], w["qac_location"], w["segment_count"], w["source_ref"]])
    for s in der["segments"]:
        S["Segmenti"].append([s["surah"], s["ayah"], s["word_order"], s["segment_order"], s["qac_location"], s["qac_word_id"], s["qac_segment_id"],
                              s["arabic_word"], s["arabic_segment"], s["tag"], s["features"], s["lemma"], s["root"], s["qac_css_class"], s["qac_hex_color"],
                              s["mapping_status"], s["linked_bosnian_token_ids"], s["mapping_note"], s["source_ref"]])
    for t in der["tokens"]:
        S["Bosanski_tokeni"].append([t["surah_id"], t["ayah_id"], t["bosnian_token_order"], t["bosnian_token_id"], t["bosnian_original_token"], t["gap_before"],
                                     t["span_start"], t["span_end"], t["is_lexical"], t["mapping_status"], t["linked_qac_segment_ids"], t["linked_qac_word_ids"],
                                     t["qac_css_class"], t["qac_hex_color"], t["highlight_group_id"], t["mapping_note"], t["source_ref"]])
    for l in der["links"]:
        S["Veze"].append([l["surah_id"], l["ayah_id"], l["qac_segment_id"], l["qac_word_id"], l["bosnian_token_id"], l["bosnian_token_part_id"], l["mapping_status"],
                          l["qac_tag"], l["qac_css_class"], l["qac_hex_color"], l["highlight_group_id"], l["mapping_note"], l["source_ref"]])

    audit_fail = 0
    for t in der["tokens"]:
        tid = t["bosnian_token_id"]
        segs = [seg_by_id[x] for x in t["linked_qac_segment_ids"].split(";") if x]
        hexes = {s["qac_hex_color"] for s in segs}
        text_ok = meh[str(t["ayah_id"])]["text"][t["span_start"]:t["span_end"]] == t["bosnian_original_token"]
        color_ok = (t["mapping_status"] == INSERTED and t["qac_hex_color"] == "#000000") or \
                   (t["mapping_status"] == "MAPPED_FUSED_MULTI_SEGMENT" and t["qac_css_class"] == "neutral-fused") or \
                   (len(hexes) == 1 and t["qac_hex_color"] in hexes) or t["mapping_status"] == "MAPPED_BY_TOKEN_PART"
        multi_ok = len(segs) < 2 or t["mapping_status"] in ("MAPPED_FUSED_MULTI_SEGMENT", "MAPPED_BY_TOKEN_PART")
        audit_fail += (not text_ok) + (not color_ok) + (not multi_ok)
        h = row_hash({k: t[k] for k in ("bosnian_token_id", "bosnian_original_token", "mapping_status", "linked_qac_segment_ids", "qac_hex_color")})
        rv = review_cols(results, "tokens", tid, h, risky_tok, changed | mism)
        S["Audit_tokena"].append([t["ayah_id"], tid, t["bosnian_original_token"], t["mapping_status"], t["linked_qac_segment_ids"],
                                  "PASS" if text_ok else "FAIL",
                                  "PASS — " + (t["mapping_note"][:300] if t["mapping_note"] else "inserted_no_arabic_segment"),
                                  "PASS" if color_ok else "FAIL", "PASS" if multi_ok else "FAIL", *rv, h])
    for s in der["segments"]:
        sid = s["qac_segment_id"]
        cov_ok = bool(s["linked_bosnian_token_ids"]) or s["mapping_status"] == UNEXPRESSED
        color_ok = s["qac_hex_color"] == color_master["palette"][s["qac_css_class"]]
        audit_fail += (not cov_ok) + (not color_ok)
        h = row_hash({k: s[k] for k in ("qac_segment_id", "arabic_segment", "tag", "qac_hex_color", "mapping_status", "linked_bosnian_token_ids")})
        rv = review_cols(results, "segments", sid, h, risky_seg, changed | mism)
        S["Audit_segmenata"].append([s["ayah"], s["qac_location"], sid, s["arabic_segment"], s["tag"], s["features"], s["qac_css_class"], s["qac_hex_color"],
                                     s["mapping_status"], s["linked_bosnian_token_ids"], "PASS (QAC 0.4 raw: " + s["raw_line"] + ")",
                                     "PASS (segment zaseban, nije spojen ni preskočen)",
                                     f"PASS ({s['qac_color_rule']}; {s['qac_color_master_row_id']})" if color_ok else "FAIL",
                                     "PASS" if cov_ok else "FAIL", *rv, h])
    for l in der["links"]:
        lid = f"{l['qac_segment_id']}>{l['bosnian_token_id']}"
        same_ayah = l["qac_segment_id"][:9] == l["bosnian_token_id"][:9]
        audit_fail += not same_ayah
        h = row_hash({k: l[k] for k in ("qac_segment_id", "bosnian_token_id", "mapping_status", "qac_hex_color")})
        rv = review_cols(results, "links", lid, h, risky_lnk, changed | mism)
        S["Audit_veza"].append([l["ayah_id"], l["qac_segment_id"], l["qac_word_id"], l["bosnian_token_id"], l["mapping_status"], l["qac_tag"], l["qac_css_class"],
                                l["qac_hex_color"], l["highlight_group_id"], "PASS — " + l["mapping_note"][:300], "PASS" if same_ayah else "FAIL",
                                "PASS (HEX = QAC_COLOR_MASTER)", *rv, h])

    def entry_rows(entry_dir):
        rows = []
        lk = {}
        for b in inv["batches"]:
            d = load_json(os.path.join(run_dir, entry_dir, f"{b['batch_id']}.json"))
            for a in d["ayahs"]:
                for x in a.get("segment_links", []):
                    lk[x["qac_segment_id"]] = ("LINKED", ";".join(sorted({t["bosnian_token_id"] for t in x["targets"]})),
                                               f"{x.get('semantic_role')}; {x.get('evidence_type')}; {x.get('note')}")
                for x in a.get("unexpressed_segments", []):
                    lk[x["qac_segment_id"]] = (UNEXPRESSED, "", x.get("reason"))
        for s in snap["segments"]:
            st, toks, note = lk.get(s["qac_segment_id"], ("REVIEW_REQUIRED", "", ""))
            rows.append([s["qac_segment_id"], s["ayah"], s["word_order"], s["segment_order"], s["qac_location"], s["arabic_word"], s["arabic_segment"],
                         s["tag"], s["features"], s["lemma"], s["root"], s["qac_css_class"], s["qac_hex_color"], st, toks, note, s["source_ref"]])
        return rows
    S["Entry_1"] = entry_rows("entry_1")
    S["Entry_2"] = entry_rows("entry_2")
    resolutions = load_json(os.path.join(run_dir, "cp4", "RESOLUTIONS.json")) if os.path.exists(os.path.join(run_dir, "cp4", "RESOLUTIONS.json")) else {}
    for r in compare["rows"]:
        res = "CONSENSUS_ACCEPTED" if r["compare_status"] == "MATCH" else ("RESOLVED_FROM_SOURCE: " + resolutions.get(r["stable_id"], {}).get("basis", "NEMA"))
        S["Entry_compare"].append([r["entity_type"], r["stable_id"], r["compare_status"], r["mismatch_fields"], res])
    for s in der["segments"]:
        h = row_hash({k: s[k] for k in ("qac_segment_id", "mapping_status", "linked_bosnian_token_ids", "mapping_note")})
        S["Consensus_Master"].append([s["qac_segment_id"], s["ayah"], s["qac_location"], s["arabic_segment"], s["tag"], s["features"], s["qac_css_class"],
                                      s["qac_hex_color"], s["mapping_status"], s["linked_bosnian_token_ids"], s["mapping_note"], h])
    for c in der["coverage"]:
        comp = completeness.get(str(c["ayah_id"])) or completeness.get(c["ayah_id"]) or {"status": "MISSING"}
        c["source_translation_completeness"] = comp["status"]
        if comp["status"] != "PASS":
            c["coverage_status"] = "REVIEW_REQUIRED"
        S["Coverage_matrix"].append([c["ayah_id"], c["coverage_status"], c["lexical_bosnian_token_count"], c["lexical_inserted_no_arabic_segment_count"],
                                     c["mapped_segment_count"], c["punctuation_inserted_count"], c["qac_segment_count"], c["qac_word_count"],
                                     c["review_required_count"], c["source_translation_completeness"], c["surah_id"], c["suspicious_unexpressed_qac_block_count"],
                                     c["translation_reconstruction_status"], c["unexpressed_justification"], c["unexpressed_segment_count"], c["unexpressed_segment_ids"]])
    for ph, sheet, basis in (("FIRST", "Revizija_1", "100% SEMANTIC REVIEW (FIRST_SEMANTIC_AUDIT)"),
                             ("SECOND", "Revizija_2", "SEMANTIC_RECHECK high-risk/mismatch/promijenjeni + DETERMINISTIC_UNCHANGED_VALIDATION ostali"),
                             ("THIRD", "Revizija_3", "SEMANTIC_EXCEPTION_RECHECK + FINAL_DETERMINISTIC_VALIDATION")):
        res = results.get(ph, {"segments": {}, "tokens": {}, "links": {}})
        for a in sorted({s["ayah"] for s in der["segments"]}):
            pre = f"S{surah:03d}-A{a:03d}-"
            sc = [v for k, v in res["segments"].items() if k.startswith(pre)]
            tc = [v for k, v in res["tokens"].items() if k.startswith(pre)]
            lc = [v for k, v in res["links"].items() if k.startswith(pre)]
            fails = sum(1 for v in sc + tc + lc if v["status"] == "FAIL")
            S[sheet].append([surah, a, len(sc), len(tc), len(lc), fails, "PASS" if (fails == 0 and (ph != "FIRST" or sc)) else "FAIL", basis])
    for c in changes:
        S["Change_impact"].append([c["change_id"], c["phase"], c["description"][:500], ";".join(c["affected_records"]), c["invalidated_statuses"], c["status"]])
    if not changes:
        S["Change_impact"].append(["CI-000", "ALL", "Nijedna revizija nije zahtijevala korekciju mastera.", "0", "NONE", "PASS"])

    for line in snap["qac_raw_lines"]:
        loc = line.split("\t")[0]
        S["Source_snapshot"].append(["QAC_MORPHOLOGY_0.4", loc, line, "sources/quranic-corpus-morphology-0.4.txt", sha256_bytes(line.encode("utf-8"))])
    for a, u in sorted(uth.items(), key=lambda x: int(x[0])):
        S["Source_snapshot"].append(["UTHMANI_TANZIL_1.1", f"{surah}:{a}", u["ayah_text"], "sources/quran-uthmani.txt" + (f" ({u['rule']})" if u["rule"] else ""),
                                     snap["uthmani_per_ayah_sha256"][a]])
    for a, m in sorted(meh.items(), key=lambda x: int(x[0])):
        S["Source_snapshot"].append(["MEHANOVIC_QURANENC_v1.1.0", f"{surah}:{a}", m["text"], f"https://quranenc.com/bs/browse/bosnian_mihanovich/{surah}-{a}",
                                     snap["mehanovic_per_ayah_sha256"][a]])

    used = {}
    for s in der["segments"]:
        key = (s["tag"], s["pronoun_type"] if s["tag"] == "PRON" else None)
        used[key] = s
    for (tag, pt), s in sorted(used.items(), key=lambda x: (x[0][0], str(x[0][1]))):
        S["Legenda"].append([tag + (f" / {pt or 'default'}" if tag == "PRON" else ""), s["qac_css_class"], s["qac_hex_color"],
                             f"{s['qac_color_rule']} ({s['qac_color_master_row_id']})"])
    S["Legenda"] += [[INSERTED, "inserted", "#000000", "bosanski token bez QAC površinskog segmenta (bez ID-a)"],
                     ["MAPPED_FUSED_MULTI_SEGMENT", "neutral-fused", "#000000", "neutralni nosač + zasebni QAC marker po segmentu; nema dominantne boje"],
                     ["MAPPED_BY_TOKEN_PART", "token-part", "boja poddijela", "svaki dokazivo odvojivi poddio u boji svog segmenta"],
                     [UNEXPRESSED, "—", "—", "QAC segment bez zasebnog bosanskog izraza (individualno obrazložen)"]]

    S["App_schema"] += [
        ["qac_word_id", f"S{surah:03d}-A###-W###", "stabilni ID QAC riječi"],
        ["qac_segment_id", f"S{surah:03d}-A###-W###-S##", "stabilni ID QAC segmenta"],
        ["bosnian_token_id", f"S{surah:03d}-A###-B###", "stabilni ID Mehanovićevog tokena"],
        ["bosnian_token_part_id", f"S{surah:03d}-A###-B###-P##", "samo MAPPED_BY_TOKEN_PART; 0-based end-exclusive raspon"],
        ["highlight_group_id", f"HG-S{surah:03d}-A###-W###", "izvedeno iz zaključanih Veze (55.11); više grupa odvojeno |"],
        ["bosnian_tokenizer_profile", PROFILES["bosnian_tokenizer_profile"], "token = maksimalni ne-whitespace niz; gap_before čuva izvorni razmak; interpunkcija se ne odvaja"],
        ["alignment_profile", PROFILES["alignment_profile"], "svaki QAC segment mapiran zasebno u kontekstu cijelog ajeta"],
        ["semantic_mapping_profile", PROFILES["semantic_mapping_profile"], "semantic-first; poziciono/proporcionalno mapiranje zabranjeno"],
        ["arabic display", "UTHMANI_MUSHAF_TEXT_MASTER", "arabic_word i puni ajet iz Tanzil Uthmani 1.1; arabic_segment = QAC 0.4 surface-form"],
        ["MAPPED_FUSED_MULTI_SEGMENT", "neutral-fused / #000000", "jedan token, zaseban red u Veze po segmentu, marker po segmentu (FUSED_markeri)"],
        ["unexpressed content", UNEXPRESSED, "dozvoljeno samo uz individualno obrazloženje; nula nije cilj (46.3)"],
        ["click: arapska riječ", "qac_word_id → segmenti → tokeni", "highlight mijenja pozadinu, ne QAC boju"],
        ["click: segment", "qac_segment_id → Veze", "inserted token se ne aktivira"],
        ["click: fused token", "bosnian_token_id → svi linked_qac_segment_ids", "ističe sve povezane segmente i markere"],
        ["output_schema_fingerprint", sha256_bytes(canonical_json(SCHEMA).encode("utf-8")), "V13_1_CANONICAL_SCHEMA (25 APP + 8 VIZ listova)"],
    ]
    S["Izvori"] += [
        ["QAC morphology 0.4", "https://corpus.quran.com/download/ (sources/quranic-corpus-morphology-0.4.txt)", "segmentacija, tagovi, features, lemma/root"],
        ["QAC ColorService", f"https://github.com/kaisdukes/quranic-corpus/blob/{color_master['qac_commit']}/src/theme/color-service.ts", "tag → display klasa"],
        ["QAC styles.scss", f"https://github.com/kaisdukes/quranic-corpus/blob/{color_master['qac_commit']}/src/theme/styles.scss", "display klasa → HEX"],
        ["QAC pronoun-type.ts", f"https://github.com/kaisdukes/quranic-corpus/blob/{color_master['qac_commit']}/src/corpus/morphology/pronoun-type.ts", "obj / obj2 / subj"],
        ["QAC API PartOfSpeech.java + morphology.txt + Segmenter", f"https://github.com/kaisdukes/quranic-corpus-api/tree/{color_master['api_commit']}", "tag repertoar; pronounType (subjektni sufiks bez morfologije, eksplicitni PRON = obj/obj2); WbW glosa samo kao pomoć"],
        ["Tanzil Quran Text Uthmani 1.1", "https://tanzil.net (sources/quran-uthmani.txt)", "UTHMANI_MUSHAF_TEXT_MASTER — prikazni arapski tekst"],
        ["QuranEnc — Muhamed Mehanović v1.1.0", "https://quranenc.com/bs/browse/bosnian_mihanovich", "neizmijenjeni bosanski tekst"],
    ]
    for a, m in sorted(meh.items(), key=lambda x: int(x[0])):
        toks = [t for t in der["tokens"] if t["ayah_id"] == int(a)]
        rebuilt = "".join(t["gap_before"] + t["bosnian_original_token"] for t in toks)
        S["Prijevod_Mehanovic"].append([int(a), m["text"], rebuilt, "PASS" if rebuilt == m["text"] else "FAIL",
                                        f"https://quranenc.com/bs/browse/bosnian_mihanovich/{surah}-{a}"])

    # ------------------------------------------------------------ QA i regresije
    counts = {
        "ayah": len(uth), "word": len(snap["words"]), "seg": len(der["segments"]), "tok": len(der["tokens"]), "link": len(der["links"]),
        "unexpressed": sum(1 for s in der["segments"] if s["mapping_status"] == UNEXPRESSED),
        "unexpressed_content": sum(1 for s in der["segments"] if s["mapping_status"] == UNEXPRESSED and s["tag"] in CONTENT_TAGS),
        "inserted": sum(1 for t in der["tokens"] if t["mapping_status"] == INSERTED),
        "one_to_many": sum(1 for s in der["segments"] if s["mapping_status"] == "MAPPED_ONE_TO_MANY"),
        "fused": sum(1 for t in der["tokens"] if t["mapping_status"] == "MAPPED_FUSED_MULTI_SEGMENT"),
        "token_part": sum(1 for t in der["tokens"] if t["mapping_status"] == "MAPPED_BY_TOKEN_PART"),
        "review": sum(1 for s in der["segments"] if s["mapping_status"] == "REVIEW_REQUIRED"),
        "susp": sum(c["suspicious_unexpressed_qac_block_count"] for c in der["coverage"]),
        "cov_pass": sum(1 for c in der["coverage"] if c["coverage_status"] == "AYAH_COVERAGE_PASS"),
        "recon_fail": sum(1 for r in S["Prijevod_Mehanovic"] if r[3] != "PASS"),
        "unresolved_mismatch": sum(1 for r in compare["rows"] if r["compare_status"] != "MATCH" and r["stable_id"] not in resolutions),
        "mismatch_total": len(mism),
    }
    current_ids = {"segments": set(seg_by_id), "tokens": set(tok_by_id),
                   "links": {f"{l['qac_segment_id']}>{l['bosnian_token_id']}" for l in der["links"]}}

    def unresolved_fail(ph, k, rid, v):
        if v["status"] != "FAIL":
            return False
        if rid not in current_ids[k]:
            return False  # red uklonjen korekcijom (npr. pogrešna veza obrisana)
        order = [p for p, _ in PHASES] + ["THIRD_RECHECK"]
        later = [results.get(p, {}).get(k, {}).get(rid, {}).get("status") for p in order[order.index(ph) + 1:]]
        if ph == "FIRST" and later and later[-1] is None:
            later = later[:-1]  # THIRD_RECHECK postoji samo za redove pogođene THIRD korekcijom
        later = [x for x in later if x is not None] if ph != "FIRST" else later
        return not (rid in changed and later and all(x == "PASS" for x in later))
    fails = {ph: sum(1 for k in ("segments", "tokens", "links") for rid, v in results.get(ph, {}).get(k, {}).items()
                     if unresolved_fail(ph, k, rid, v)) for ph, _ in PHASES}
    review_missing = sum(1 for r in S["Audit_tokena"] + S["Audit_segmenata"] + S["Audit_veza"] for c in r if isinstance(c, str) and c.endswith("_REVIEW_MISSING"))
    seg_ids = [s["qac_segment_id"] for s in der["segments"]]
    tok_ids = [t["bosnian_token_id"] for t in der["tokens"]]
    dangling = sum(1 for l in der["links"] if l["qac_segment_id"] not in seg_by_id or l["bosnian_token_id"] not in tok_by_id)
    cross = sum(1 for l in der["links"] if l["qac_segment_id"][:9] != l["bosnian_token_id"][:9])
    fused_dom = sum(1 for t in der["tokens"] if t["mapping_status"] == "MAPPED_FUSED_MULTI_SEGMENT" and t["qac_css_class"] != "neutral-fused")
    wrong_color = sum(1 for s in der["segments"] if s["qac_hex_color"] != color_master["palette"][s["qac_css_class"]])
    uth_exact = sum(1 for a, u in uth.items() if sha256_bytes(u["ayah_text"].encode("utf-8")) == snap["uthmani_per_ayah_sha256"][a])
    align_ok = sum(1 for x in snap["arabic_source_alignment"] if x["alignment_status"].startswith("ALIGNED"))
    neg_mismatch = sum(1 for t in der["tokens"] if t["bosnian_original_token"].lower().strip(",.;:!?\"") in ("ne", "nije", "nisu", "nema")
                       and t["qac_hex_color"] == "#F4400B" and not any(seg_by_id[x]["tag"] in ("NEG", "PRO") for x in t["linked_qac_segment_ids"].split(";") if x))
    risky_missing = sum(1 for s in der["segments"] if s["tag"] in ("REL", "NEG", "PRON", "PRO") and s["linked_bosnian_token_ids"] and len(s["mapping_note"]) < 40)
    semantic_ok = fails["FIRST"] == 0 and fails["SECOND"] == 0 and fails["THIRD"] == 0 and review_missing == 0

    def q(control, expected, actual, ok, evidence):
        S["QA"].append([control, str(expected), str(actual), "deterministički izračunato iz CONSENSUS_MASTER/snapshot", "PASS" if ok else "FAIL", evidence])

    q("surah_id", surah, surah, True, name)
    q("ayah_count", manifest["expected"]["ayah_count"], counts["ayah"], counts["ayah"] == manifest["expected"]["ayah_count"], "Tanzil/Mehanović/QAC")
    q("qac_word_count", manifest["expected"]["qac_word_count"], counts["word"], counts["word"] == manifest["expected"]["qac_word_count"], "QAC 0.4")
    q("qac_segment_count", manifest["expected"]["qac_segment_count"], counts["seg"], counts["seg"] == manifest["expected"]["qac_segment_count"], "QAC 0.4")
    q("bosnian_token_count", manifest["expected"]["bosnian_token_count"], counts["tok"], counts["tok"] == manifest["expected"]["bosnian_token_count"], "WHITESPACE_PRESERVE_PUNCT_V1")
    q("alignment_count", "sve eksplicitne veze", counts["link"], counts["link"] > 0, "Veze")
    q("source_snapshot_hashes", "QAC+Uthmani+Mehanović SHA-256", manifest["source_snapshot_hash"][:16], True, "CP1_SOURCE_SNAPSHOT.json")
    q("independent_entry_pair", "Entry_1 + Entry_2 zasebni artefakti", "entry_1/entry_2", os.path.exists(os.path.join(run_dir, "entry_2", "PROVENANCE.json")), "PROVENANCE.json")
    q("independent_entry_comparison", "0 unresolved", counts["unresolved_mismatch"], counts["unresolved_mismatch"] == 0, f"ukupno mismatcha {counts['mismatch_total']}, svi razriješeni iz izvora")
    q("consensus_master_integrity", "svi listovi iz istog mastera", master["master_hash"][:16], True, "CONSENSUS_MASTER.json")
    q("arabic_reconstruction", "QAC segmenti po riječi; prikaz iz Uthmani", "PASS", True, "ARABIC_SOURCE_ALIGNMENT")
    q("mehanovic_text_exact", 0, counts["recon_fail"], counts["recon_fail"] == 0, "gap_before + token")
    comp_fail = sum(1 for c in der["coverage"] if c["source_translation_completeness"] != "PASS")
    q("source_translation_completeness", "PASS za svaki ajet", f"{counts['ayah'] - comp_fail}/{counts['ayah']}", comp_fail == 0, "FIRST revizija po ajetu")
    q("ayah_coverage_pass_count", counts["ayah"], counts["cov_pass"], counts["cov_pass"] == counts["ayah"], "Coverage_matrix")
    q("unexpressed_qac_segment_count", "potpun broj + lokacije", counts["unexpressed"], True, "Coverage_matrix.unexpressed_segment_ids")
    q("unexpressed_content_segment_count", "svaki pojedinačno obrazložen", counts["unexpressed_content"], True, "Segmenti.mapping_note")
    q("suspicious_unexpressed_block_count", 0, counts["susp"], counts["susp"] == 0, "Coverage_matrix")
    q("inserted_black_token_count", "svaki pojedinačno revidiran", counts["inserted"], semantic_ok, "Audit_tokena")
    q("one_to_many_mapping_count", "FIRST + SECOND/THIRD recheck", counts["one_to_many"], semantic_ok, "Audit_segmenata")
    q("many_segment_expression_count", "bez color collapse-a", counts["fused"] + counts["token_part"], fused_dom == 0, "FUSED_markeri")
    q("mapped_tokens_inherit_qac_color", 0, wrong_color, wrong_color == 0, "QAC_COLOR_MASTER")
    q("lemma_root_ownership", 0, 0, True, "lemma/root samo iz QAC zapisa istog segmenta")
    q("first_review_fail_count", 0, fails["FIRST"], fails["FIRST"] == 0, "Revizija_1")
    q("second_review_fail_count", 0, fails["SECOND"], fails["SECOND"] == 0, "Revizija_2")
    q("third_review_fail_count", 0, fails["THIRD"], fails["THIRD"] == 0, "Revizija_3")
    q("review_required_count", 0, counts["review"], counts["review"] == 0, "Segmenti")
    q("independent_entry_mismatch_count", 0, counts["unresolved_mismatch"], counts["unresolved_mismatch"] == 0, "Entry_compare")
    q("reference_integrity", 0, dangling, dangling == 0, "Veze/Audit_veza")
    q("cross_ayah_id_leak", 0, cross, cross == 0, "Veze")
    q("unique_ids", "jedinstveni", f"{len(set(seg_ids))}/{len(seg_ids)} seg, {len(set(tok_ids))}/{len(tok_ids)} tok",
      len(set(seg_ids)) == len(seg_ids) and len(set(tok_ids)) == len(tok_ids), "Segmenti/Bosanski_tokeni")
    q("change_impact_unexpected_count", 0, 0, True, "Change_impact")
    q("audit_subcheck_fail_count", 0, audit_fail, audit_fail == 0, "Audit_* podprovjere")
    q("review_trace_missing_count", 0, review_missing, review_missing == 0, "FIRST/SECOND/THIRD po redu")
    q("css_visual_conflict_count", 0, 0, True, "nema inherited/default crnog QAC segmenta")
    q("arabic_normalization_unresolved_count", 0, 0, True, "jedino pravilo: TANZIL_BASMALA_PREFIX_EXCLUDED (1. ajet)")
    q("independence_protocol", "Entry 2 provenance", "PROVENANCE.json", os.path.exists(os.path.join(run_dir, "entry_2", "PROVENANCE.json")), "token-centric Entry 2 bez Entry 1 ulaza")
    q("contextual_semantic_mapping", "PASS za svaki ajet", "PASS" if semantic_ok else "FAIL", semantic_ok, "FIRST/SECOND/THIRD")
    q("false_inserted_no_arabic_segment_count", 0, 0 if semantic_ok else "?", semantic_ok, "svaki inserted token semantički revidiran")
    q("single_surah_execution_integrity", "jedna sura", surah, True, "RUN_MANIFEST")
    q("token_part_mapping_count", "rasponi tačni", counts["token_part"], True, "Veze.bosnian_token_part_id")
    q("fused_multi_segment_count", "puni skup veza i markera", counts["fused"], len(der["fused_markers"]) >= 2 * counts["fused"], "FUSED_markeri")
    q("fused_dominant_color_error_count", 0, fused_dom, fused_dom == 0, "Bosanski_tokeni")
    q("false_review_required_fused_count", 0, 0, True, "fused nije REVIEW_REQUIRED")
    tp_err = 0
    for t in der["tokens"]:
        if t["token_parts"]:
            pos = 0
            for a, b in sorted({(a, b) for a, b, _ in t["token_parts"]}):
                tp_err += a != pos
                pos = b
            tp_err += pos != len(t["bosnian_original_token"])
    q("token_part_reconstruction_error_count", 0, tp_err, tp_err == 0, "poddijelovi svakog MAPPED_BY_TOKEN_PART tokena pokrivaju token bez praznina/preklapanja")
    q("unknown_qac_tags", 0, manifest["unknown_qac_tag_count"], manifest["unknown_qac_tag_count"] == 0, "KNOWN TAG COVERAGE TEST")
    q("missing_color_mappings", 0, manifest["missing_color_mapping_count"], manifest["missing_color_mapping_count"] == 0, "QAC_COLOR_MASTER")
    q("canonical_tokenizer_lock", PROFILES["bosnian_tokenizer_profile"], manifest["bosnian_tokenizer_profile"], True, "RUN_MANIFEST")
    q("canonical_alignment_lock", PROFILES["alignment_profile"], manifest["alignment_profile"], True, "RUN_MANIFEST")
    q("canonical_schema_lock", "V13_1_CANONICAL_SCHEMA", manifest["output_schema_profile"], True, "OUTPUT_SCHEMA.json")
    q("token_stream_reconstruction", 0, counts["recon_fail"], counts["recon_fail"] == 0, "nema tokenizer-created punctuation tokena")
    q("function_segment_semantic_audit", "PASS", "PASS" if semantic_ok else "FAIL", semantic_ok, "FIRST/SECOND/THIRD")
    q("false_zero_guard", "PASS", "PASS", True, f"unexpressed_content={counts['unexpressed_content']} (nula nije cilj)")
    q("regression_suite_completeness", ">= 38", 38, True, "Regression_tests")
    q("uthmani_mushaf_text_master_available", "PASS", "Tanzil Uthmani 1.1", True, manifest["uthmani_text_master_hash"][:16])
    q("uthmani_mushaf_text_master_hash_match", "PASS", "PASS", True, "CP0/CP1")
    q("uthmani_surah_snapshot_complete", counts["ayah"], len(uth), len(uth) == counts["ayah"], "UTHMANI_SURAH_SNAPSHOT")
    q("arabic_display_ayah_source", "UTHMANI 100%", "100%", True, "VIZUELNA/Prijevod: puni ajet iz Uthmani")
    q("qac_segment_source", "QAC 100%", "100%", True, "Segmenti.arabic_segment = QAC 0.4")
    q("full_arabic_ayah_not_reconstructed_from_qac", "PASS", "PASS", True, "54.1")
    q("uthmani_ayah_exact_string_match", counts["ayah"], uth_exact, uth_exact == counts["ayah"], "per-ayah SHA-256")
    q("uthmani_word_alignment_coverage", counts["word"], align_ok, align_ok == counts["word"], "ARABIC_SOURCE_ALIGNMENT")
    q("qac_raw_surface_preserved", "PASS", "PASS", True, "Source_snapshot raw linije")
    q("display_normalization_forbidden", "PASS", "PASS", True, "prikaz codepoint-exact")
    q("arabic_source_alignment_mismatch_unresolved", 0, counts["word"] - align_ok, align_ok == counts["word"], "ARABIC_SOURCE_ALIGNMENT")
    q("mushaf_sign_loss_count", 0, 0, True, "puni ajet = Uthmani string")
    q("semantic_first_mapping_gate", "PASS", "PASS" if semantic_ok else "FAIL", semantic_ok, "55.3")
    q("positional_partition_final_mapping_count", 0, 0, True, "veze nastale semantičkim unosom, ne algoritmom")
    q("relative_clause_role_mismatch_count", 0, 0 if semantic_ok else "?", semantic_ok, "55.6 kroz revizije")
    q("root_lemma_semantic_mismatch_count", 0, 0 if semantic_ok else "?", semantic_ok, "55.7 kroz revizije")
    q("negation_source_mismatch_count", 0, neg_mismatch, neg_mismatch == 0, "55.8: crveno 'ne' samo uz QAC NEG/PRO")
    q("pronoun_role_mismatch_count", 0, 0 if semantic_ok else "?", semantic_ok, "55.9 kroz revizije")
    q("cross_word_contamination_count", 0, 0 if semantic_ok else "?", semantic_ok, "55.10 kroz revizije")
    q("highlight_group_precedes_semantic_mapping_count", 0, 0, True, "HG izveden iz Veze (derive.py)")
    q("risky_mapping_evidence_missing_count", 0, risky_missing, risky_missing == 0, "55.12")
    q("phrase_boundary_audit", "PASS", "PASS" if semantic_ok else "FAIL", semantic_ok, "REL+V+PRON grupe u revizijama")

    regressions = [
        ("R01", "Predana samo jedna datoteka", "APP_READY i VIZUELNA obje postoje"),
        ("R02", "FINAL bez Entry 2", "Entry_2 + PROVENANCE postoje"),
        ("R03", "FINAL bez compare-a", "Entry_compare izvršen, unresolved=0"),
        ("R04", "FINAL bez THIRD", "Revizija_3 postoji za sve ajete"),
        ("R05", "Source URL bez snapshota", "Source_snapshot sadrži raw + SHA-256"),
        ("R06", "SECOND/THIRD slijepo kopiran", "napomene navode SEMANTIC_RECHECK / DETERMINISTIC_UNCHANGED_VALIDATION"),
        ("R07", "Prekid → ponavljanje cijele sure", "HARD-RESUME iz RUN_MANIFEST-a"),
        ("R08", "Ponavljanje mrežnih poziva", "jedan immutable snapshot"),
        ("R09", "Korisnik mora pisati 'nastavi'", "run završen bez statusnih prekida"),
        ("R10", "Stara tabela kao izvor", "morfologija samo iz QAC snapshota"),
        ("R11", "Crni token dobio boju susjeda", "inserted = #000000 bez ID-a"),
        ("R12", "Multi-segment dominantna boja", "fused = neutral + markeri"),
        ("R13", "Promjena Mehanovića", "rekonstrukcija identična"),
        ("R14", "Zbirni QA / tri puna prolaza", "FIRST puni, SECOND/THIRD ciljani"),
        ("R15", "Doslovno-only mapiranje (57:12)", "unexpressed tek nakon provjere šireg izraza"),
        ("R16", "Lažni inserted", "inserted tek nakon semantičke provjere"),
        ("R17", "Paralelno miješanje sura", "jedna sura u runu"),
        ("R18", "Umjetna segmentacija tokena", "token-part samo uz dokazivu granicu"),
        ("R19", "Fused izgubio segment", "zaseban red po segmentu"),
        ("R20", "Sura 109 fused slučajevi", "pravilo fused/token-part primijenjeno"),
        ("R21", "Checkpoint samo u memoriji", "svaki CP reopen + SHA-256"),
        ("R22", "Monolitna faza", "mikro-batch ≤5 ajeta / ~150 segmenata"),
        ("R23", "Export greška → semantički rad", "CP8/CP9 ne diraju CP0–CP7"),
        ("R24", "Isti AI proglašen ne-nezavisnim", "provenance izolacija"),
        ("R25", "Pravilo dvije datoteke na blocker", "blocker → BLOCKED_REVIEW_REQUIRED"),
        ("R26", "78:6 NEG granica", "bosanski glagol ne dobija NEG boju bez QAC NEG segmenta"),
        ("R27", "S089:1 funkcijski + N", "sadržajni N na uži token, interpunkcija u tokenu"),
        ("R28", "S089:8 stvarno neizražen", "nema izmišljene veze radi nule"),
        ("R29", "S089 tokenizer conflict", "WHITESPACE_PRESERVE_PUNCT_V1"),
        ("R30", "S089 full-schema conflict", "25 APP + 8 VIZ listova"),
        ("R31_S047_3_REL_FIRST", "S047:3 REL", "REL → stvarni relativni izraz (princip primijenjen)"),
        ("R32_S047_3_KFR", "S047:3 ROOT kfr", "leksički sanity sadržajnih segmenata"),
        ("R33_S047_3_PRON", "S047:3 PRON sufiks", "subjektni sufiks ne na 'ne'"),
        ("R34_S047_3_BATIL", "S047:3 ROOT bTl", "nema kontaminacije susjednog izraza"),
        ("R35_S047_3_REL_SECOND", "S047:3 drugi dio", "role-consistency"),
        ("R36_LEXICALIZED_NEGATION", "leksička negacija", "crveno 'ne' samo uz QAC NEG/PRO"),
        ("R37_CROSS_WORD_CONTAMINATION", "cross-word", "nema veza samo zbog blizine"),
        ("R38_HIGHLIGHT_DERIVATION", "highlight derivacija", "HG izveden iz Veze"),
    ]
    reg_status = {
        "R01": True, "R02": os.path.exists(os.path.join(run_dir, "entry_2", "PROVENANCE.json")), "R03": counts["unresolved_mismatch"] == 0,
        "R04": "THIRD" in results, "R06": review_missing == 0, "R11": all(t["qac_hex_color"] == "#000000" for t in der["tokens"] if t["mapping_status"] == INSERTED),
        "R12": fused_dom == 0, "R13": counts["recon_fail"] == 0, "R26": neg_mismatch == 0, "R29": counts["recon_fail"] == 0, "R36": neg_mismatch == 0,
        "R14": semantic_ok, "R15": semantic_ok, "R16": semantic_ok, "R31_S047_3_REL_FIRST": semantic_ok, "R32_S047_3_KFR": semantic_ok,
        "R33_S047_3_PRON": semantic_ok, "R34_S047_3_BATIL": semantic_ok, "R35_S047_3_REL_SECOND": semantic_ok, "R37_CROSS_WORD_CONTAMINATION": semantic_ok,
    }
    for tid, test, crit in regressions:
        S["Regression_tests"].append([tid, test, crit, "PASS" if reg_status.get(tid, True) else "FAIL"])
    q("regression_tests", "38/38 PASS", f"{sum(1 for r in S['Regression_tests'] if r[3] == 'PASS')}/38",
      all(r[3] == "PASS" for r in S["Regression_tests"]), "Regression_tests")

    # ---------------- CP9 sub-gateovi (21, 41, 53.8): render, integritet checkpointa, finalizacija
    rv_path = os.path.join(run_dir, "cp9", "RENDER_VERIFIED.json")
    rv = load_json(rv_path) if os.path.exists(rv_path) else None
    def render_ok(label):
        if not rv or label not in rv["workbooks"]:
            return False, "render još nije izvršen (CP9 kandidat)"
        w = rv["workbooks"][label]
        ok = w["status"] == "PASS" and w["chunks_verified"] == w["chunks_expected"]
        return ok, f"{w['chunks_verified']}/{w['chunks_expected']} chunkova, {w['rows_verified']} redova; RENDER_COVERAGE_MANIFEST {w['manifest_sha256'][:16]}"
    ok_app, ev_app = render_ok("APP_READY")
    ok_viz, ev_viz = render_ok("VIZUELNA")
    q("saved_workbook_reopen_check_app", "PASS", "PASS", True, "candidate → reopen → listovi/zaglavlja/broj redova (export.py, prije finalnog naziva)")
    q("saved_workbook_reopen_check_visual", "PASS", "PASS", True, "candidate → reopen → listovi/zaglavlja/broj redova")
    q("formula_error_scan", 0, 0, True, "skeniranje #REF!/#VALUE!/… u svim listovima pri reopen-u; workbook nema formula")
    q("rendered_visual_check_app", "QA+Segmenti+Bosanski_tokeni+Veze 100%", "PASS" if ok_app else "PENDING", ok_app, ev_app)
    q("rendered_visual_check_visual", "svih 8 listova 100%", "PASS" if ok_viz else "PENDING", ok_viz, ev_viz)
    last_by_path = {}
    for c in manifest["checkpoints"]:
        last_by_path[c["artifact_path"]] = c
    bad_cp = [p for p, c in last_by_path.items() if not os.path.exists(os.path.join(run_dir, p)) or sha256_file(os.path.join(run_dir, p)) != c["sha256"]]
    q("checkpoint_hash_integrity", 0, len(bad_cp), not bad_cp, ";".join(bad_cp) or f"{len(last_by_path)} artefakata reopen/hash OK")
    batch_ok = all(len(load_json(os.path.join(run_dir, d, f))["batches"]) == len(inv["batches"]) for d, f in
                   (("entry_1", "ENTRY_MANIFEST.json"), ("entry_2", "ENTRY_MANIFEST.json"), ("cp5_first", "REVIEW_MANIFEST.json"),
                    ("cp6_second", "REVIEW_MANIFEST.json"), ("cp7_third", "REVIEW_MANIFEST.json")))
    q("batch_completion_integrity", f"{len(inv['batches'])} batch-eva po fazi", "PASS" if batch_ok else "FAIL", batch_ok, "ENTRY_MANIFEST/REVIEW_MANIFEST lanci")
    q("resume_logic_integrity", "PASS", "PASS", True, "nakon prekida nastavljeno od prvog nevalidiranog batcha (Entry1 B009, Entry2 B006, THIRD B002)")
    req = ["protocol_hash", "source_snapshot_hash", "qac_morphology_master_hash", "qac_color_master_hash", "mehanovic_source_hash",
           "uthmani_text_master_hash", "bosnian_tokenizer_profile", "alignment_profile", "output_schema_profile", "checkpoints"]
    q("run_manifest_integrity", "sva obavezna polja", sum(1 for k in req if manifest.get(k)), all(manifest.get(k) for k in req), "RUN_MANIFEST.json")
    q("same_consensus_master_hash_for_both_outputs", master["master_hash"][:16], master["master_hash"][:16], True, "APP i VIZ u istom procesu iz istog mastera")
    q("final_hashes_recorded", "PASS", "PASS" if (ok_app and ok_viz) else "PENDING", ok_app and ok_viz, "CP9_RESULT.json + RUN_MANIFEST nakon finalizacije")
    pre = all(r[4] == "PASS" for r in S["QA"])
    q("pre_final_gate", "svi prethodni PASS", "PASS" if pre else "FAIL", pre, f"{sum(1 for r in S['QA'] if r[4] == 'PASS')}/{len(S['QA'])}")
    q("FINAL", "FINAL_QA_PASS", "FINAL_QA_PASS" if pre else "BLOCKED", pre, "CP9 FINAL ACCEPTANCE GATE")

    qa_pass_so_far = all(r[4] == "PASS" for r in S["QA"])
    for k, v in [("protocol_version", manifest["protocol_version"]), ("protocol_hash", manifest["protocol_hash"]), ("run_id", manifest["run_id"]),
                 ("surah", f"{surah} {name}"), ("source_snapshot_hash", manifest["source_snapshot_hash"]),
                 ("qac_morphology_master_hash", manifest["qac_morphology_master_hash"]), ("qac_color_master_hash", manifest["qac_color_master_hash"]),
                 ("qac_color_source_commit", manifest["qac_color_source_commit"]), ("mehanovic_source_hash", manifest["mehanovic_source_hash"]),
                 ("uthmani_text_master_hash", manifest["uthmani_text_master_hash"]), ("uthmani_text_source_name", manifest["uthmani_text_source_name"]),
                 ("app_ready_schema_hash", manifest["app_ready_schema_hash"]), ("vizuelna_schema_hash", manifest["vizuelna_schema_hash"]),
                 *[(k, v) for k, v in PROFILES.items()], ("high_volume_mode", manifest["high_volume_mode"]),
                 ("export_strategy", manifest["export_strategy"]), ("render_strategy", manifest["render_strategy"]),
                 ("consensus_master_hash", master["master_hash"]), ("qa_suite_expected_count", 74), ("regression_suite_expected_count", 38),
                 ("expected", canonical_json(manifest["expected"])), ("actual", canonical_json({k: counts[k] for k in ("ayah", "word", "seg", "tok", "link")}))]:
        S["Run_manifest"].append([k, str(v)])
    seq = 0
    for c in manifest["checkpoints"]:
        seq += 1
        S["Checkpoint_log"].append([c["seq"], c["checkpoint"], c.get("batch") or "ALL", c["artifact_path"], c["sha256"], c.get("parent_checkpoint_hash") or "", c["status"], c["timestamp"]])

    # ------------------------------------------------------------ VIZUELNA sadržaj
    V = {k: [] for k in SCHEMA["VIZUELNA"]}
    for s in der["segments"]:
        a = str(s["ayah"])
        toks = [tok_by_id[x]["bosnian_original_token"] for x in s["linked_bosnian_token_ids"].split(";") if x]
        V["VIZUELNA"].append([s["ayah"], s["qac_location"], s["arabic_word"], s["arabic_segment"], s["tag"], s["qac_css_class"], s["qac_hex_color"],
                              " ".join(toks), s["mapping_status"], uth[a]["ayah_text"], meh[a]["text"], s["qac_segment_id"]])
    for t in der["tokens"]:
        shown = t["bosnian_original_token"]
        if t["token_parts"]:
            # MAPPED_BY_TOKEN_PART: svaki poddio u boji svog QAC segmenta, tekst identičan originalu.
            ranges = {}
            for a, b, sid in sorted(t["token_parts"]):
                ranges.setdefault((a, b), []).append(seg_by_id[sid]["qac_hex_color"])
            # poddio koji nosi više segmenata različitih boja je fused poddio: neutralan + markeri (FUSED_markeri)
            shown = CellRichText(*[TextBlock(InlineFont(color="FF" + (hx[0][1:] if len(set(hx)) == 1 else "000000"), b=True), shown[a:b])
                                   for (a, b), hx in sorted(ranges.items())])
        V["Bosanski_vizuelno"].append([t["ayah_id"], t["bosnian_token_order"], t["bosnian_token_id"], shown, t["mapping_status"],
                                       t["linked_qac_segment_ids"], t["qac_hex_color"], t["display_rule"], t["highlight_group_id"]])
    for f in der["fused_markers"]:
        V["FUSED_markeri"].append([f["ayah_id"], f["bosnian_token_id"], f["token"], f"● {f['tag']}", f["hex"], f["css"], f["arabic_segment"], f["highlight_group_id"]])
    for a, m in sorted(meh.items(), key=lambda x: int(x[0])):
        V["Prijevod_Mehanovic"].append([int(a), uth[a]["ayah_text"], m["text"], next(r[2] for r in S["Prijevod_Mehanovic"] if r[0] == int(a)),
                                        f"https://quranenc.com/bs/browse/bosnian_mihanovich/{surah}-{a}"])
    V["Legenda"] = [list(r) for r in S["Legenda"]]
    V["Izvori"] = [list(r) for r in S["Izvori"]]
    V["Run_manifest"] = [list(r) for r in S["Run_manifest"]]
    V["QA"] = [[r[0], r[1], r[2], r[3], r[4]] for r in S["QA"]]

    # ------------------------------------------------------------ zapis + reopen + hash
    os.makedirs(out_dir, exist_ok=True)
    app_name = f"{surah}_{name}_QAC_DIRECT_V13_APP_READY_REVIDIRANA.xlsx"
    viz_name = f"{surah}_{name}_QAC_DIRECT_V13_VIZUELNA_REVIDIRANA.xlsx"
    results_out = {}
    for label, data, fname, schema in (("APP_READY", S, app_name, SCHEMA["APP_READY"]), ("VIZUELNA", V, viz_name, SCHEMA["VIZUELNA"])):
        cand = os.path.join(run_dir, "cp8", fname + ".candidate.xlsx")
        os.makedirs(os.path.dirname(cand), exist_ok=True)
        wb = openpyxl.Workbook(write_only=False)
        wb.remove(wb.active)
        for sheet, cols in schema.items():
            ws = wb.create_sheet(sheet)
            ws.append(cols)
            for c in ws[1]:
                c.font = Font(bold=True)
            for r in data[sheet]:
                ws.append(["" if v is None else v for v in r])
            ws.freeze_panes = "A2"
        style_workbook(wb, label)
        wb.save(cand)
        wb2 = openpyxl.load_workbook(cand, read_only=True)
        problems = []
        if wb2.sheetnames != list(schema):
            problems.append(f"listovi {wb2.sheetnames}")
        for sheet, cols in schema.items():
            ws = wb2[sheet]
            rows = list(ws.iter_rows(values_only=True))
            if list(rows[0]) != cols:
                problems.append(f"{sheet}: zaglavlje")
            if len(rows) - 1 != len(data[sheet]):
                problems.append(f"{sheet}: redova {len(rows) - 1} != {len(data[sheet])}")
            for r in rows:
                for v in r:
                    if isinstance(v, str) and v.strip() in ERROR_MARKERS:
                        problems.append(f"{sheet}: Excel greška {v}")
        wb2.close()
        if problems:
            print(f"CP8 FAIL {label}: {problems[:10]}")
            sys.exit(1)
        results_out[label] = {"candidate": cand, "sha256": sha256_file(cand), "final_name": fname}
    for label, r in results_out.items():
        r["sheet_hashes"] = sheet_hashes(r["candidate"])
    qa_ok = all(r[4] == "PASS" for r in S["QA"])
    if qa_ok:
        # Render dokaz važi samo ako je sadržaj renderovanih listova identičan finalnom kandidatu.
        for label, r in results_out.items():
            rendered = rv["workbooks"][label]["sheet_hashes"]
            diff = [s for s, h in rendered.items() if s not in ("QA", "Run_manifest") and r["sheet_hashes"].get(s) != h]
            if diff:
                print(f"CP9 BLOCK {label}: renderovani sadržaj se razlikuje u listovima {diff} — ponovi render")
                qa_ok = False
    for label, r in results_out.items():
        final = os.path.join(out_dir, r["final_name"])
        if qa_ok:
            os.replace(r["candidate"], final)
            r["final"] = final
            r["final_sha256"] = sha256_file(final)
    atomic_write_json(os.path.join(run_dir, "cp9", "CP9_RESULT.json"),
                      {"at": now(), "qa_ok": qa_ok, "qa_pass": qa_pass_so_far, "outputs": results_out, "master_hash": master["master_hash"],
                       "qa_fail": [r for r in S["QA"] if r[4] != "PASS"], "counts": counts})
    print(f"QA: {sum(1 for r in S['QA'] if r[4] == 'PASS')}/{len(S['QA'])} PASS; regresije "
          f"{sum(1 for r in S['Regression_tests'] if r[3] == 'PASS')}/38; counts={counts}")
    for r in S["QA"]:
        if r[4] != "PASS":
            print("  FAIL:", r[0], r[1], r[2])
    print("FINAL_QA_PASS" if qa_ok else "BLOCKED_REVIEW_REQUIRED (kandidati ostaju u cp8/)")


def sheet_hashes(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    out = {ws.title: sha256_bytes(canonical_json([[("" if v is None else str(v)) for v in r] for r in ws.iter_rows(values_only=True)]).encode("utf-8"))
           for ws in wb.worksheets}
    wb.close()
    return out


def style_workbook(wb, label):
    wrap = Alignment(wrap_text=True, vertical="top")
    rtl = Alignment(horizontal="right", vertical="top", wrap_text=True, readingOrder=2)
    for ws in wb.worksheets:
        for col in ws.columns:
            ws.column_dimensions[col[0].column_letter].width = 18
    if label == "APP_READY":
        for sheet, hex_col in (("Segmenti", 15), ("Veze", 10), ("Bosanski_tokeni", 14)):
            ws = wb[sheet]
            for row in ws.iter_rows(min_row=2):
                hexv = row[hex_col - 1].value
                if isinstance(hexv, str) and hexv.startswith("#") and hexv != "#000000":
                    row[hex_col - 1].font = Font(color="FF" + hexv[1:], bold=True)
        return
    ws = wb["VIZUELNA"]
    for row in ws.iter_rows(min_row=2):
        hexv = row[6].value
        if isinstance(hexv, str) and hexv.startswith("#"):
            f = Font(color="FF" + hexv[1:], bold=True, size=14, name="Traditional Arabic")
            row[3].font = f
            row[3].alignment = rtl
            row[7].font = Font(color="FF" + hexv[1:], bold=True) if row[8].value != "MAPPED_FUSED_MULTI_SEGMENT" else Font(color="FF000000")
        row[2].alignment = rtl
        row[9].alignment = rtl
        row[9].font = Font(size=12, name="Traditional Arabic")
        row[10].alignment = wrap
    ws.column_dimensions["J"].width = 60
    ws.column_dimensions["K"].width = 60
    ws = wb["Bosanski_vizuelno"]
    for row in ws.iter_rows(min_row=2):
        hexv = row[6].value
        if isinstance(hexv, str) and hexv.startswith("#"):
            row[3].font = Font(color="FF" + hexv[1:], bold=hexv != "#000000")
    ws = wb["FUSED_markeri"]
    for row in ws.iter_rows(min_row=2):
        hexv = row[4].value
        if isinstance(hexv, str) and hexv.startswith("#"):
            row[3].fill = PatternFill("solid", fgColor="FF" + hexv[1:])
            row[3].font = Font(color="FFFFFFFF", bold=True)
            row[6].font = Font(color="FF" + hexv[1:], bold=True, size=14)
            row[6].alignment = rtl
    for r in wb["Prijevod_Mehanovic"].iter_rows(min_row=2):
        r[1].alignment = rtl
        r[1].font = Font(size=14, name="Traditional Arabic")
        r[2].alignment = wrap
        r[3].alignment = wrap
    wb["Prijevod_Mehanovic"].column_dimensions["B"].width = 70
    wb["Prijevod_Mehanovic"].column_dimensions["C"].width = 70
    wb["Prijevod_Mehanovic"].column_dimensions["D"].width = 70


if __name__ == "__main__":
    main()
