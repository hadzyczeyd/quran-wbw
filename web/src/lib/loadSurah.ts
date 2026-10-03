import { supabase } from "./supabase";
import type { Ayah, BosnianToken, QacSegment, QacWord, SurahData } from "./types";

const PAGE = 1000;

/** PostgREST vraća najviše 1000 redova po upitu — duže sure se čitaju u dijelovima. */
async function fetchAll<T>(
  query: (from: number, to: number) => PromiseLike<{ data: T[] | null; error: unknown }>
): Promise<T[]> {
  const rows: T[] = [];
  for (let from = 0; ; from += PAGE) {
    const { data, error } = await query(from, from + PAGE - 1);
    if (error) throw error;
    rows.push(...(data ?? []));
    if (!data || data.length < PAGE) return rows;
  }
}

/**
 * Učitava kompletnu suru iz Supabase baze i slaže je u isti oblik
 * (SurahData) koji su komponente ranije dobijale iz JSON fixture-a.
 * Nekoliko upita paralelno umjesto jednog velikog joina — sure imaju
 * najviše ~250 riječi, pa je ovo brzo i čitljivo.
 */
export async function loadSurahFromSupabase(surahId: number): Promise<SurahData | null> {
  const { data: ayahRows, error: ayahError } = await supabase
    .from("ayahs")
    .select("ayah_number, text_uthmani, mehanovic_text")
    .eq("surah_id", surahId)
    .order("ayah_number");

  if (ayahError || !ayahRows || ayahRows.length === 0) {
    return null;
  }

  // ID-ovi svih redova sure počinju s "S057-" — filter po prefiksu umjesto
  // dugačke .in() liste.
  const idPrefix = `S${String(surahId).padStart(3, "0")}-%`;

  const [wordRows, tokenRows, segmentRows, linkRows] = await Promise.all([
    fetchAll((from, to) =>
      supabase
        .from("words")
        .select("word_id, ayah_number, position, text_uthmani, transliteration, gloss")
        .eq("surah_id", surahId)
        .order("ayah_number")
        .order("position")
        .range(from, to)
    ),
    fetchAll((from, to) =>
      supabase
        .from("bosnian_tokens")
        .select("token_id, ayah_number, position, display_text, qac_css_class, qac_hex_color, mapping_status")
        .eq("surah_id", surahId)
        .order("ayah_number")
        .order("position")
        .range(from, to)
    ),
    fetchAll((from, to) =>
      supabase
        .from("word_segments")
        .select(
          "segment_id, word_id, segment_order, segment_text, qac_tag, qac_full_description, qac_css_class, qac_hex_color, lemma, root, expression_status"
        )
        .like("segment_id", idPrefix)
        .order("segment_id")
        .range(from, to)
    ),
    fetchAll((from, to) =>
      supabase
        .from("token_segment_links")
        .select("segment_id, token_id")
        .like("token_id", idPrefix)
        .order("segment_id")
        .order("token_id")
        .range(from, to)
    ),
  ]);

  const segToTokens = new Map<string, string[]>();
  const tokenToSegs = new Map<string, string[]>();
  for (const link of linkRows ?? []) {
    if (!segToTokens.has(link.segment_id)) segToTokens.set(link.segment_id, []);
    segToTokens.get(link.segment_id)!.push(link.token_id);
    if (!tokenToSegs.has(link.token_id)) tokenToSegs.set(link.token_id, []);
    tokenToSegs.get(link.token_id)!.push(link.segment_id);
  }

  const segmentsByWord = new Map<string, QacSegment[]>();
  const segmentById = new Map<string, { css_class: string; tag: string }>();
  for (const s of segmentRows ?? []) {
    segmentById.set(s.segment_id, { css_class: s.qac_css_class, tag: s.qac_tag });
    const seg: QacSegment = {
      segment_id: s.segment_id,
      order: s.segment_order,
      text: s.segment_text,
      tag: s.qac_tag,
      description: s.qac_full_description ?? "",
      css_class: s.qac_css_class,
      hex_color: s.qac_hex_color,
      lemma: s.lemma,
      root: s.root,
      expression_status: s.expression_status,
      linked_token_ids: segToTokens.get(s.segment_id) ?? [],
    };
    if (!segmentsByWord.has(s.word_id)) segmentsByWord.set(s.word_id, []);
    segmentsByWord.get(s.word_id)!.push(seg);
  }

  const wordsByAyah = new Map<number, QacWord[]>();
  for (const w of wordRows ?? []) {
    const word: QacWord = {
      word_id: w.word_id,
      position: w.position,
      text_uthmani: w.text_uthmani,
      transliteration: w.transliteration,
      gloss: w.gloss,
      segments: segmentsByWord.get(w.word_id) ?? [],
    };
    if (!wordsByAyah.has(w.ayah_number)) wordsByAyah.set(w.ayah_number, []);
    wordsByAyah.get(w.ayah_number)!.push(word);
  }

  const tokensByAyah = new Map<number, BosnianToken[]>();
  for (const t of tokenRows ?? []) {
    const linked = tokenToSegs.get(t.token_id) ?? [];
    const token: BosnianToken = {
      token_id: t.token_id,
      position: t.position,
      text: t.display_text,
      css_class: t.qac_css_class,
      hex_color: t.qac_hex_color,
      mapping_status: t.mapping_status,
      linked_segment_ids: linked,
      fused_markers:
        t.mapping_status === "MAPPED_FUSED_MULTI_SEGMENT"
          ? [...linked].sort().flatMap((id) => {
              const seg = segmentById.get(id);
              return seg ? [{ segment_id: id, ...seg }] : [];
            })
          : [],
    };
    if (!tokensByAyah.has(t.ayah_number)) tokensByAyah.set(t.ayah_number, []);
    tokensByAyah.get(t.ayah_number)!.push(token);
  }

  const ayat: Ayah[] = ayahRows.map((a) => ({
    ayah_number: a.ayah_number,
    text_uthmani: a.text_uthmani,
    mehanovic_text: a.mehanovic_text,
    words: wordsByAyah.get(a.ayah_number) ?? [],
    bosnian_tokens: tokensByAyah.get(a.ayah_number) ?? [],
  }));

  return {
    surah_id: surahId,
    ayah_count: ayat.length,
    source: "Supabase",
    qa: {},
    ayat,
  };
}
