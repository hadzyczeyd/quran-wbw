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

/** Podaci panela za suru, ako postoje (web/src/data/rootPanel/S<NNN>.json, scripts/roots/build_app_root_panel.py). */
export async function getRootPanel(surahId: number): Promise<RootPanelData | null> {
  if (!Number.isInteger(surahId) || surahId < 1 || surahId > 114) return null;
  try {
    const mod = await import(`@/data/rootPanel/S${String(surahId).padStart(3, "0")}.json`);
    return mod.default as RootPanelData;
  } catch {
    return null;
  }
}
