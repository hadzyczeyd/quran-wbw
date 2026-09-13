// Tipovi za privremeni JSON izlaz iz data-pipeline/scripts/export_sura_json.py
// (dok Supabase baza iz OPIS poglavlja 6 ne bude spremna).

export interface QacSegment {
  segment_id: string;
  order: number;
  text: string;
  tag: string;
  description: string;
  css_class: string;
  hex_color: string;
  lemma: string | null;
  root: string | null;
  expression_status: string;
  linked_token_ids: string[];
}

export interface QacWord {
  word_id: string;
  position: number;
  text_uthmani: string;
  transliteration: string | null;
  gloss: string | null;
  segments: QacSegment[];
}

export interface BosnianToken {
  token_id: string;
  position: number;
  text: string;
  css_class: string;
  hex_color: string;
  mapping_status: string;
  linked_segment_ids: string[];
}

export interface Ayah {
  ayah_number: number;
  text_uthmani: string;
  mehanovic_text: string | null;
  words: QacWord[];
  bosnian_tokens: BosnianToken[];
}

export interface SurahData {
  surah_id: number;
  ayah_count: number;
  source: string;
  qa: Record<string, unknown>;
  ayat: Ayah[];
}
