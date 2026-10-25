import s001 from "@/data/rootPanel/S001.json";
import s114 from "@/data/rootPanel/S114.json";

/** Kartica jednog oblika (nalog ROOT_PANEL V7): oblik, kratko značenje i jedan provjeren primjer. */
export interface RootPanelCard {
  id: string;
  form: string;
  meaning: string;
  /** Referenca primjera "sura:ajet". */
  ref: string;
  /** QAC indeks cijele riječi primjera u ajetu. */
  w: number;
  /** Prikazani arapski tekst (cijeli ajet ili kontinuirani izvod), 1:1 Uthmani. */
  ar: string;
  /** Prikazani Mehanovićev prijevod (cijeli ili kontinuirani izvod), 1:1. */
  bs: string;
  /** Raspon ciljne riječi u `ar`, [start, end). */
  hl: number[];
  /** Izostavljanje: [arapski ispred, arapski iza, bosanski ispred, bosanski iza]. */
  ell: boolean[];
}

export interface RootPanelRoot {
  display: string;
  nouns: RootPanelCard[];
  verbs: RootPanelCard[];
}

export interface RootPanelData {
  surah: number;
  roots: Record<string, RootPanelRoot>;
  /** "ajet:riječ" → ROOT_BW, samo za riječi s dozvoljenim klikom (nosivi segment N/V s korijenom). */
  words: Record<string, string>;
}

const BY_SURAH: Record<number, RootPanelData> = {
  1: s001 as RootPanelData,
  114: s114 as RootPanelData,
};

export function getRootPanel(surahId: number): RootPanelData | null {
  return BY_SURAH[surahId] ?? null;
}
