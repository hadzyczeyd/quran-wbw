# -*- coding: utf-8 -*-
"""
CP0 PREFLIGHT + CP1 SOURCE SNAPSHOT / inventar / batch plan za jednu suru (V13.1).

Upotreba: uv run scripts/v131/cp0_cp1.py <sura> <naziv>
"""
import os
import sys
import uuid

sys.path.insert(0, os.path.dirname(__file__))
from common import (  # noqa: E402
    API_MORPH, MEHANOVIC_XLSX, PROFILES, PROTOCOL_DOC, QAC_MORPH, RUNS, SOURCES, UTHMANI, WBW,
    api_lines_by_word, assign_pronoun_types, atomic_write_json, build_color_master, canonical_json,
    color_for, is_word_token, load_json, load_mehanovic_surah, load_qac_surah, load_uthmani_surah,
    now, reconstruct, seg_id, sha256_bytes, sha256_file, tok_id, tokenize, word_id,
)

SCHEMA = {
    "APP_READY": {
        "Rijeci": ["surah_id", "ayah_id", "word_order", "qac_word_id", "arabic_word", "qac_location", "segment_count", "source_ref"],
        "Segmenti": ["surah", "ayah", "word_order", "segment_order", "qac_location", "qac_word_id", "qac_segment_id", "arabic_word", "arabic_segment", "tag", "features", "lemma", "root", "qac_css_class", "qac_hex_color", "mapping_status", "linked_bosnian_token_ids", "mapping_note", "source_ref"],
        "Bosanski_tokeni": ["surah_id", "ayah_id", "bosnian_token_order", "bosnian_token_id", "bosnian_original_token", "gap_before", "span_start", "span_end", "is_lexical", "mapping_status", "linked_qac_segment_ids", "linked_qac_word_ids", "qac_css_class", "qac_hex_color", "highlight_group_id", "mapping_note", "source_ref"],
        "Veze": ["surah_id", "ayah_id", "qac_segment_id", "qac_word_id", "bosnian_token_id", "bosnian_token_part_id", "mapping_status", "qac_tag", "qac_css_class", "qac_hex_color", "highlight_group_id", "mapping_note", "source_ref"],
        "Audit_tokena": ["ayah_id", "bosnian_token_id", "bosnian_original_token", "mapping_status", "linked_qac_segment_ids", "text_integrity_check", "segment_link_check", "color_match_check", "multi_segment_token_check", "first_review_status", "first_review_note", "second_review_status", "second_review_note", "third_review_status", "third_review_note", "row_hash"],
        "Audit_segmenata": ["ayah_id", "qac_location", "qac_segment_id", "arabic_segment", "qac_tag", "qac_full_description", "qac_css_class", "qac_hex_color", "mapping_status", "linked_bosnian_token_ids", "source_data_check", "segmentation_check", "color_check", "mapping_coverage_check", "first_review_status", "first_review_note", "second_review_status", "second_review_note", "third_review_status", "third_review_note", "row_hash"],
        "Audit_veza": ["ayah_id", "qac_segment_id", "qac_word_id", "bosnian_token_id", "mapping_status", "qac_tag", "qac_css_class", "qac_hex_color", "highlight_group_id", "semantic_link_check", "id_integrity_check", "color_integrity_check", "first_review_status", "first_review_note", "second_review_status", "second_review_note", "third_review_status", "third_review_note", "row_hash"],
        "Entry_1": ["qac_segment_id", "ayah", "word_order", "segment_order", "qac_location", "arabic_word", "arabic_segment", "tag", "features", "lemma", "root", "qac_css_class", "qac_hex_color", "mapping_status", "linked_bosnian_token_ids", "mapping_note", "source_ref"],
        "Entry_2": ["qac_segment_id", "ayah", "word_order", "segment_order", "qac_location", "arabic_word", "arabic_segment", "tag", "features", "lemma", "root", "qac_css_class", "qac_hex_color", "mapping_status", "linked_bosnian_token_ids", "mapping_note", "source_ref"],
        "Entry_compare": ["entity_type", "stable_id", "compare_status", "mismatch_fields", "resolution"],
        "Consensus_Master": ["qac_segment_id", "ayah_id", "qac_location", "arabic_segment", "qac_tag", "qac_full_description", "qac_css_class", "qac_hex_color", "mapping_status", "linked_bosnian_token_ids", "mapping_note", "master_row_hash"],
        "Coverage_matrix": ["ayah_id", "coverage_status", "lexical_bosnian_token_count", "lexical_inserted_no_arabic_segment_count", "mapped_segment_count", "punctuation_inserted_count", "qac_segment_count", "qac_word_count", "review_required_count", "source_translation_completeness", "surah_id", "suspicious_unexpressed_qac_block_count", "translation_reconstruction_status", "unexpressed_justification", "unexpressed_segment_count", "unexpressed_segment_ids"],
        "Revizija_1": ["surah_id", "ayah_id", "segments_checked", "tokens_checked", "links_checked", "fail_count", "status", "basis"],
        "Revizija_2": ["surah_id", "ayah_id", "segments_checked", "tokens_checked", "links_checked", "fail_count", "status", "basis"],
        "Revizija_3": ["surah_id", "ayah_id", "segments_checked", "tokens_checked", "links_checked", "fail_count", "status", "basis"],
        "Regression_tests": ["test_id", "test", "criterion", "status"],
        "Change_impact": ["change_id", "phase", "description", "affected_records", "invalidated_statuses", "status"],
        "Source_snapshot": ["source_type", "item_id", "raw_content", "source_location", "row_sha256"],
        "Legenda": ["tag/status", "css/display_class", "hex/display", "meaning"],
        "App_schema": ["field/concept", "format", "rule"],
        "Izvori": ["source", "url/location", "use"],
        "Prijevod_Mehanovic": ["ayah_id", "source_exact", "reconstructed_from_tokens", "reconstruction_status", "source_ref"],
        "Run_manifest": ["field", "value"],
        "Checkpoint_log": ["seq", "checkpoint", "batch", "artifact_path", "sha256", "parent_checkpoint_hash", "status", "timestamp"],
        "QA": ["Control", "Expected", "Actual_locked", "Formula_verification", "Status", "Evidence"],
    },
    "VIZUELNA": {
        "VIZUELNA": ["Ajet", "QAC lokacija", "Arapska riječ", "QAC segment", "Tag", "CSS klasa", "HEX", "Mapirani bosanski token(i)", "Mapping status", "Puni arapski ajet", "Mehanović — neizmijenjeno", "qac_segment_id"],
        "Bosanski_vizuelno": ["Ajet", "Red", "bosnian_token_id", "Bosanski token", "Mapping status", "Povezani QAC segmenti", "Display HEX", "Prikazno pravilo", "Highlight grupa"],
        "FUSED_markeri": ["Ajet", "bosnian_token_id", "Fused bosanski token", "QAC koloristički marker", "HEX", "CSS", "Arapski segment", "Highlight grupa"],
        "Prijevod_Mehanovic": ["Ajet", "Arapski tekst", "Mehanović — izvorni tekst", "Rekonstrukcija", "Izvor"],
        "Legenda": ["Tag/status", "CSS/display", "HEX", "Značenje"],
        "Izvori": ["Izvor", "URL", "Uloga"],
        "Run_manifest": ["Polje", "Vrijednost"],
        "QA": ["Kontrola", "Očekivano", "Stvarno", "Formula provjera", "Status"],
    },
}


def schema_hash(name):
    return sha256_bytes(canonical_json(SCHEMA[name]).encode("utf-8"))


def batch_plan(ayah_seg_counts, max_ayahs=5, max_segs=150):
    batches, cur, cur_segs = [], [], 0
    for a, n in ayah_seg_counts:
        if cur and (len(cur) >= max_ayahs or cur_segs + n > max_segs):
            batches.append(cur)
            cur, cur_segs = [], 0
        cur.append(a)
        cur_segs += n
    if cur:
        batches.append(cur)
    return batches


def main():
    surah = int(sys.argv[1])
    name = sys.argv[2]
    run_dir = os.path.join(RUNS, f"S{surah:03d}_{name}")
    manifest_path = os.path.join(run_dir, "RUN_MANIFEST.json")
    if os.path.exists(manifest_path):
        m = load_json(manifest_path)
        print(f"RUN_MANIFEST postoji (current_checkpoint={m['current_checkpoint']}); HARD-RESUME — CP0/CP1 se ne ponavljaju.")
        return

    # ---------------- CP0 PREFLIGHT
    protocol_path = os.path.join(SOURCES, PROTOCOL_DOC)
    color_master = build_color_master()
    write_test = os.path.join(run_dir, "cp0", "workspace_write_test.json")
    wt_hash = atomic_write_json(write_test, {"test": "ok", "at": now()})
    preflight = {
        "protocol_hash": sha256_file(protocol_path),
        "qac_morphology_master_hash": sha256_file(QAC_MORPH),
        "qac_color_master_hash": color_master["master_hash"],
        "qac_color_source_files": color_master["files"],
        "qac_api_morphology_hash": sha256_file(API_MORPH),
        "qac_word_by_word_hash": sha256_file(WBW),
        "uthmani_text_master_hash": sha256_file(UTHMANI),
        "mehanovic_source_hash": sha256_file(MEHANOVIC_XLSX),
        "app_ready_schema_hash": schema_hash("APP_READY"),
        "vizuelna_schema_hash": schema_hash("VIZUELNA"),
        "workspace_write_test": wt_hash,
        "profiles": PROFILES,
    }
    blob_ok = all(f["match"] for f in color_master["files"].values())
    preflight["preflight_status"] = "PASS" if blob_ok else "FAIL"
    if not blob_ok:
        print("PREFLIGHT FAIL: pinned QAC blob SHA se ne poklapa", color_master["files"])
        sys.exit(1)
    cp0_hash = atomic_write_json(os.path.join(run_dir, "cp0", "CP0_PREFLIGHT.json"), preflight)
    cm_hash = atomic_write_json(os.path.join(run_dir, "cp0", "QAC_COLOR_MASTER.json"), color_master)
    schema_file_hash = atomic_write_json(os.path.join(run_dir, "cp0", "OUTPUT_SCHEMA.json"), SCHEMA)

    # ---------------- CP1 SOURCE SNAPSHOT
    qac_raw, segs = load_qac_surah(surah)
    api_map = api_lines_by_word()
    pron_problems = assign_pronoun_types(segs, api_map)
    uth = load_uthmani_surah(surah)
    meh = load_mehanovic_surah(surah)

    ayahs = sorted(uth)
    problems = list(pron_problems)
    problems_fixed = []
    words, segments, tokens, alignment = [], [], [], []
    by_word = {}
    for s in segs:
        by_word.setdefault((s["ayah"], s["word"]), []).append(s)

    unknown_tags = sorted({s["tag"] for s in segs} - set(color_master["repertoire"]))
    for s in segs:
        row = color_for(s, color_master)
        if row is None:
            problems.append(f"nema color mapping: {s['qac_location']} {s['tag']}")
            continue
        s["color_row"] = row

    for a in ayahs:
        uthmani_words = [t for t in uth[a]["ayah_text"].split(" ") if is_word_token(t)]
        qac_words = sorted({w for (aa, w) in by_word if aa == a})
        if len(uthmani_words) == len(qac_words) + 1:
            # Tanzil piše neke QAC riječi kao dvije (npr. 37:130 إِلْ يَاسِينَ): spoji par čiji se kostur slova poklapa s QAC riječju.
            def skel(t):
                return "".join(ch for ch in t if "ء" <= ch <= "ي")
            for i in range(len(uthmani_words) - 1):
                w = i + 1
                q = skel("".join(x["form_ar"] for x in by_word.get((a, w), [])))
                if q and skel(uthmani_words[i] + uthmani_words[i + 1]) == q and skel(uthmani_words[i]) != q:
                    uthmani_words[i:i + 2] = [uthmani_words[i] + " " + uthmani_words[i + 1]]
                    problems_fixed.append(f"ajet {a}: Uthmani '{uthmani_words[i]}' spojeno u jednu QAC riječ {w}")
                    break
        if len(uthmani_words) != len(qac_words):
            problems.append(f"ajet {a}: Uthmani riječi {len(uthmani_words)} != QAC {len(qac_words)}")
        for w in qac_words:
            ws = sorted(by_word[(a, w)], key=lambda x: x["segment"])
            u_word = uthmani_words[w - 1] if w - 1 < len(uthmani_words) else None
            _, gloss = api_map[(surah, a, w)]
            words.append({
                "surah_id": surah, "ayah_id": a, "word_order": w, "qac_word_id": word_id(surah, a, w),
                "arabic_word": u_word, "qac_word_form_bw": "".join(x["form_bw"] for x in ws),
                "qac_word_form_ar": "".join(x["form_ar"] for x in ws),
                "qac_location": f"{surah}:{a}:{w}", "segment_count": len(ws),
                "qac_wbw_gloss_en": gloss,
                "source_ref": f"https://corpus.quran.com/wordmorphology.jsp?location=({surah}:{a}:{w})",
            })
            alignment.append({
                "qac_word_id": word_id(surah, a, w), "uthmani_locator": f"{surah}:{a}:{w}",
                "uthmani_word": u_word, "qac_surface_ar": "".join(x["form_ar"] for x in ws),
                "alignment_status": "ALIGNED_BY_AYAH_WORD_ORDER" if u_word else "MISSING",
                "note": "Uthmani tokeni s pauzalnim znakom (ۖ ۚ ۗ ۙ ۛ ۩) bez slova nisu riječi; ostaju u punom ajetu.",
            })
            for x in ws:
                cr = x["color_row"]
                segments.append({
                    "surah": surah, "ayah": a, "word_order": w, "segment_order": x["segment"],
                    "qac_location": x["qac_location"], "qac_word_id": word_id(surah, a, w),
                    "qac_segment_id": seg_id(surah, a, w, x["segment"]),
                    "arabic_word": u_word, "arabic_segment": x["form_ar"], "arabic_segment_bw": x["form_bw"],
                    "tag": x["tag"], "features": x["features"], "segment_type": x["segment_type"],
                    "pronoun_type": x["pronoun_type"], "api_line": x["api_line"],
                    "lemma": x["lemma_bw"] or "QAC_NO_DATA", "root": x["root_bw"] or "QAC_NO_DATA",
                    "qac_css_class": cr["css_class"], "qac_hex_color": cr["hex"],
                    "qac_color_rule": cr["color_rule"], "qac_color_master_row_id": cr["row_id"],
                    "qac_color_source_ref": cr["source_ref"],
                    "raw_line": x["raw_line"],
                    "source_ref": f"https://corpus.quran.com/wordmorphology.jsp?location=({surah}:{a}:{w})",
                })
        text = meh[a]["text"]
        toks = tokenize(text)
        if not reconstruct(toks, text):
            problems.append(f"ajet {a}: rekonstrukcija Mehanovića nije identična")
        for i, t in enumerate(toks, start=1):
            tokens.append({
                "surah_id": surah, "ayah_id": a, "bosnian_token_order": i, "bosnian_token_id": tok_id(surah, a, i),
                "bosnian_original_token": t["text"], "gap_before": t["gap_before"],
                "span_start": t["span_start"], "span_end": t["span_end"], "is_lexical": t["is_lexical"],
                "source_ref": f"https://quranenc.com/bs/browse/bosnian_mihanovich/{surah}-{a}",
            })

    if unknown_tags:
        problems.append(f"unknown_qac_tags: {unknown_tags}")
    snapshot = {
        "surah_id": surah, "surah_name": name, "created_at": now(),
        "qac_raw_lines": qac_raw, "qac_raw_hash": sha256_bytes("\n".join(qac_raw).encode("utf-8")),
        "uthmani": {str(a): uth[a] for a in ayahs},
        "uthmani_per_ayah_sha256": {str(a): sha256_bytes(uth[a]["ayah_text"].encode("utf-8")) for a in ayahs},
        "mehanovic": {str(a): meh[a] for a in ayahs},
        "mehanovic_per_ayah_sha256": {str(a): sha256_bytes(meh[a]["text"].encode("utf-8")) for a in ayahs},
        "words": words, "segments": segments, "tokens": tokens, "arabic_source_alignment": alignment,
        "color_master_hash": color_master["master_hash"],
    }
    snap_hash = atomic_write_json(os.path.join(run_dir, "cp1", "CP1_SOURCE_SNAPSHOT.json"), snapshot)

    seg_counts = [(a, sum(1 for s in segments if s["ayah"] == a)) for a in ayahs]
    plan = batch_plan(seg_counts)
    inventory = {
        "ayah_count": len(ayahs), "qac_word_count": len(words), "qac_segment_count": len(segments),
        "bosnian_token_count": len(tokens), "batches": [{"batch_id": f"B{i + 1:03d}", "ayahs": b} for i, b in enumerate(plan)],
        "tags_in_surah": sorted({s["tag"] for s in segments}),
        "pron_variants": sorted({str(s["pronoun_type"]) for s in segments if s["tag"] == "PRON"}),
        "unknown_qac_tag_count": len(unknown_tags), "problems": problems, "word_alignment_fixes": problems_fixed,
    }
    inv_hash = atomic_write_json(os.path.join(run_dir, "cp1", "INVENTORY_BATCH_PLAN.json"), inventory)

    # Ulazni paketi za Entry 1 / Entry 2 (isti snapshot, bez ikakvih odluka mapiranja).
    for b in inventory["batches"]:
        payload = {"surah_id": surah, "surah_name": name, "batch_id": b["batch_id"], "ayahs": []}
        for a in b["ayahs"]:
            payload["ayahs"].append({
                "ayah_id": a,
                "arabic_ayah_uthmani": uth[a]["ayah_text"],
                "mehanovic_text": meh[a]["text"],
                "words": [
                    {"qac_word_id": w["qac_word_id"], "arabic_word": w["arabic_word"], "qac_wbw_gloss_en": w["qac_wbw_gloss_en"],
                     "segments": [
                         {"qac_segment_id": s["qac_segment_id"], "arabic_segment": s["arabic_segment"], "tag": s["tag"],
                          "features": s["features"], "pronoun_type": s["pronoun_type"], "lemma": s["lemma"], "root": s["root"],
                          "qac_css_class": s["qac_css_class"]}
                         for s in segments if s["qac_word_id"] == w["qac_word_id"]]}
                    for w in words if w["ayah_id"] == a],
                "bosnian_tokens": [{"bosnian_token_id": t["bosnian_token_id"], "token": t["bosnian_original_token"]}
                                   for t in tokens if t["ayah_id"] == a],
            })
        atomic_write_json(os.path.join(run_dir, "cp1", "batch_inputs", f"{b['batch_id']}.json"), payload)

    manifest = {
        "protocol_version": "QAC DIRECT V13.1 (+53 LARGE-SURAH, +54 UTHMANI, +55 SEMANTIC)",
        "protocol_doc": PROTOCOL_DOC, "run_id": str(uuid.uuid4()), "surah_id": surah, "surah_name": name,
        **{k: preflight[k] for k in ("protocol_hash", "qac_morphology_master_hash", "qac_color_master_hash",
                                      "mehanovic_source_hash", "app_ready_schema_hash", "vizuelna_schema_hash")},
        "qac_color_source_commit": color_master["qac_commit"],
        "uthmani_text_source_name": "Tanzil Quran Text (Uthmani, Version 1.1)",
        "uthmani_text_source_provider": "Tanzil Project (tanzil.net)",
        "uthmani_text_source_version_or_revision": "1.1",
        "uthmani_text_source_ref": "sources/quran-uthmani.txt",
        "uthmani_text_master_hash": preflight["uthmani_text_master_hash"],
        "uthmani_expected_ayah_count": len(meh), "uthmani_actual_ayah_count": len(ayahs),
        **PROFILES,
        "high_volume_mode": "ON" if (len(ayahs) > 60 or len(segments) > 750 or len(tokens) > 800) else "OFF",
        "export_strategy": "SEGMENTED_CP8", "render_strategy": "CHUNKED_FULL_COVERAGE",
        "source_snapshot_hash": snap_hash, "inventory_hash": inv_hash,
        "preflight_status": preflight["preflight_status"],
        "current_checkpoint": "CP1", "current_batch": None, "last_valid_micro_checkpoint": "CP1",
        "checkpoint_seq": 2, "batch_retry_count": 0, "run_status": "RUNNING", "delivery_status": "NOT_READY",
        "expected": {k: inventory[k] for k in ("ayah_count", "qac_word_count", "qac_segment_count", "bosnian_token_count")},
        "unknown_qac_tag_count": len(unknown_tags), "missing_color_mapping_count": sum(1 for p in problems if p.startswith("nema color")),
        "checkpoints": [
            {"seq": 1, "checkpoint": "CP0", "batch": None, "artifact_path": "cp0/CP0_PREFLIGHT.json", "sha256": cp0_hash,
             "parent_checkpoint_hash": None, "status": "INSTRUCTION_LOCK_PASS", "timestamp": now(),
             "extra": {"QAC_COLOR_MASTER.json": cm_hash, "OUTPUT_SCHEMA.json": schema_file_hash}},
            {"seq": 2, "checkpoint": "CP1", "batch": None, "artifact_path": "cp1/CP1_SOURCE_SNAPSHOT.json", "sha256": snap_hash,
             "parent_checkpoint_hash": cp0_hash, "status": "SOURCE_SNAPSHOT_PASS" if not problems else "REVIEW_REQUIRED",
             "timestamp": now()},
        ],
        "technical_event_log": [],
    }
    atomic_write_json(manifest_path, manifest)
    print(canonical_json({k: inventory[k] for k in ("ayah_count", "qac_word_count", "qac_segment_count", "bosnian_token_count",
                                                     "tags_in_surah", "pron_variants", "unknown_qac_tag_count")}))
    print("batch-eva:", len(inventory["batches"]), "| problemi:", problems[:10])


if __name__ == "__main__":
    main()
