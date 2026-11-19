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
  /** Za fused token: QAC klasa svakog povezanog segmenta, redom (V13.1 pravilo 8.4). */
  fused_markers: { segment_id: string; css_class: string; tag: string }[];
}

export interface Ayah {
  ayah_number: number;
  text_uthmani: string;
  mehanovic_text: string | null;
  words: QacWord[];
  bosnian_tokens: BosnianToken[];
}

/*
 * Kompaktni oblik za preglednik (čitač). Server unaprijed spaja segmente za
 * prikaz i računa veze riječ↔token, pa se ne šalju opisi, leme, hex boje,
 * ID-ovi segmenata ni drugi podaci koje čitač ne iscrtava (sura 2 je
 * inače bila ~9 MB HTML-a).
 */
export interface ClientPart {
  /** Tekst prikaznog raspona (jedan QAC segment ili لله ligatura). */
  t: string;
  /** QAC CSS klasa. */
  c: string;
}

export interface ClientWord {
  id: string;
  pos: number;
  gloss: string | null;
  parts: ClientPart[];
  /** Bosanski tokeni povezani s bilo kojim segmentom riječi. */
  tokens: string[];
}

export interface ClientToken {
  id: string;
  t: string;
  c: string;
  /** Prva arapska riječ na koju token vodi (klik → isticanje + izgovor), null = bez arapskog para. */
  word: string | null;
  /** Spojeni token: boje (i oznake) svih povezanih segmenata, redom. */
  fused: { c: string; tag: string }[];
}

export interface ClientAyah {
  n: number;
  words: ClientWord[];
  tokens: ClientToken[];
}

export interface ClientSurah {
  surah_id: number;
  ayat: ClientAyah[];
}

export interface SurahData {
  surah_id: number;
  ayah_count: number;
  source: string;
  qa: Record<string, unknown>;
  ayat: Ayah[];
}
