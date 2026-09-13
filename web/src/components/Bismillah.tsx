import { mergeSegmentsForDisplay } from "@/lib/segments";
import type { QacSegment } from "@/lib/types";

// Ručno uneseni QAC segmenti za بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
// (stvarna corpus.quran.com segmentacija/boje, sura 1:1 — provjereno u
// V12 Fatiha fajlu, iste HEX vrijednosti kao objedinjena V13 paleta).
function seg(
  id: string,
  order: number,
  text: string,
  tag: string,
  cssClass: string,
  hexColor: string
): QacSegment {
  return {
    segment_id: id,
    order,
    text,
    tag,
    description: "",
    css_class: cssClass,
    hex_color: hexColor,
    lemma: null,
    root: null,
    expression_status: "EXPRESSED_IN_BOSNIAN",
    linked_token_ids: [],
  };
}

const WORDS: QacSegment[][] = [
  [seg("bi", 1, "بِ", "P", "segRust", "#AD2323"), seg("sm", 2, "سْمِ", "N", "segSky", "#548DD4")],
  [seg("allah", 1, "ٱللَّهِ", "PN", "segBlue", "#257E9C")],
  [
    seg("det1", 1, "ٱل", "DET", "segGray", "#575757"),
    seg("rahman", 2, "رَّحْمَٰنِ", "ADJ", "segPurple", "#8126C0"),
  ],
  [
    seg("det2", 1, "ٱل", "DET", "segGray", "#575757"),
    seg("rahim", 2, "رَّحِيمِ", "ADJ", "segPurple", "#8126C0"),
  ],
];

export function Bismillah() {
  return (
    <p className="home-bismillah">
      {WORDS.map((wordSegments, i) => (
        <span key={i}>
          {mergeSegmentsForDisplay(wordSegments).map((s) => (
            <span key={s.key} data-qac-class={s.cssClass}>
              {s.text}
            </span>
          ))}
          {i < WORDS.length - 1 ? " " : ""}
        </span>
      ))}
    </p>
  );
}
