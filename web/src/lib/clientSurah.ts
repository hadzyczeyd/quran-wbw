import { mergeSegmentsForDisplay } from "./segments";
import type { ClientSurah, SurahData } from "./types";

/** Pretvara punu suru iz baze u kompaktni oblik koji čitač u pregledniku stvarno koristi. */
export function toClientSurah(data: SurahData): ClientSurah {
  const segmentToWord = new Map<string, string>();
  for (const ayah of data.ayat) {
    for (const w of ayah.words) for (const s of w.segments) segmentToWord.set(s.segment_id, w.word_id);
  }

  return {
    surah_id: data.surah_id,
    ayat: data.ayat.map((ayah) => ({
      n: ayah.ayah_number,
      words: ayah.words.map((w) => {
        const tokens = new Set<string>();
        for (const s of w.segments) for (const t of s.linked_token_ids) tokens.add(t);
        return {
          id: w.word_id,
          pos: w.position,
          gloss: w.gloss,
          parts: mergeSegmentsForDisplay(w.segments).map((p) => ({ t: p.text, c: p.cssClass })),
          tokens: [...tokens],
        };
      }),
      tokens: ayah.bosnian_tokens.map((t) => {
        let word: string | null = null;
        for (const sid of t.linked_segment_ids) {
          const wid = segmentToWord.get(sid);
          if (wid) {
            word = wid;
            break;
          }
        }
        return {
          id: t.token_id,
          t: t.text,
          c: t.css_class,
          word,
          fused: t.fused_markers.map((m) => ({ c: m.css_class, tag: m.tag })),
        };
      }),
    })),
  };
}
