import type { QacSegment } from "./types";

/**
 * Prikazni segment: jedan ili više QAC segmenata spojenih u jedan
 * obojeni raspon. Svaki QAC segment po pravilu ostaje svoj zaseban
 * obojeni raspon — NALOG-V13 poglavlje 24 zabranjuje spajanje segmenata
 * radi jednostavnijeg prikaza, i poglavlje 6 traži da svaki segment
 * zadrži vlastitu boju. Riječ i dalje ostaje jedan neprekinuti HTML
 * tekst (segmenti se ne razdvajaju razmakom).
 *
 * Jedini izuzetak je لله ligatura, empirijski potvrđena u Amiri Quran
 * fontu: kad se لِ (prijedlog/prefiks) i naredni segment koji počinje s
 * "الله" oboje odvojeno, font crta CIJELU ligaturu bojom DRUGOG spana —
 * boja prvog segmenta potpuno nestane. To nije stilski izbor nego
 * ograničenje text-shapinga (fonta/browsera), pa se ta dva segmenta
 * moraju spojiti u jedan raspon obojen bojom nosećeg (drugog) segmenta.
 */
export interface DisplaySegment {
  key: string;
  text: string;
  cssClass: string;
  hexColor: string;
  /** Svi qac_segment_id spojeni u ovaj prikazni raspon. */
  segmentIds: string[];
  /** Svi bosanski tokeni povezani sa spojenim segmentima. */
  linkedTokenIds: string[];
}

const ALIF_VARIANTS = /[إأآٱا]/g;
const DIACRITICS = /[ً-ٰٟ]/g;

function stripForBoundaryCheck(text: string): string {
  // Skida dijakritiku radi provjere suglasničkog kostura na granici
  // segmenata.
  return text.replace(DIACRITICS, "").replace(ALIF_VARIANTS, "ا");
}

/**
 * Da li segment nosi korijen Allahovog imena (ا ل ه). Ovo je pouzdanije
 * od provjere teksta "starts with الله" — kad se prijedlog direktno
 * nastavi na Allaha (npr. لِلَّهِ), elif iz "ٱل" ispadne, a šedda spaja
 * dva lama u JEDAN unicode znak s dijakritikom, pa tekst segmenta
 * nikad doslovno ne sadrži "لله" kao tri odvojena slova.
 */
function isAllahRoot(root: string | null): boolean {
  if (!root) return false;
  const normalized = root.replace(/\s+/g, "").replace(ALIF_VARIANTS, "ا");
  return normalized === "اله";
}

export function mergeSegmentsForDisplay(segments: QacSegment[]): DisplaySegment[] {
  const sorted = [...segments].sort((a, b) => a.order - b.order);
  const out: DisplaySegment[] = [];

  for (let i = 0; i < sorted.length; i++) {
    const seg = sorted[i];
    const next = sorted[i + 1];

    const endsInLam = stripForBoundaryCheck(seg.text).endsWith("ل");
    const isLillahLigature = next !== undefined && endsInLam && isAllahRoot(next.root);

    if (isLillahLigature) {
      out.push({
        key: `${seg.segment_id}+${next.segment_id}`,
        text: seg.text + next.text,
        cssClass: next.css_class,
        hexColor: next.hex_color,
        segmentIds: [seg.segment_id, next.segment_id],
        linkedTokenIds: [...seg.linked_token_ids, ...next.linked_token_ids],
      });
      i++; // preskoči next, već potrošen u spajanju
      continue;
    }

    out.push({
      key: seg.segment_id,
      text: seg.text,
      cssClass: seg.css_class,
      hexColor: seg.hex_color,
      segmentIds: [seg.segment_id],
      linkedTokenIds: [...seg.linked_token_ids],
    });
  }

  return out;
}
