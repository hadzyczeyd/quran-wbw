import s001 from "@/data/roots/S001.json";
import s112 from "@/data/roots/S112.json";
import s113 from "@/data/roots/S113.json";
import s114 from "@/data/roots/S114.json";

export interface RootFamily {
  root: string;
  imenice: string[];
  glagoli: string[];
  pridjevi: string[];
}

export type RootFamilies = Record<string, RootFamily>;

// Test funkcija: porodice korijena postoje samo za sure iz priloženih tabela.
const BY_SURAH: Record<number, RootFamilies> = { 1: s001, 112: s112, 113: s113, 114: s114 };

export function getRootFamilies(surahId: number): RootFamilies | null {
  return BY_SURAH[surahId] ?? null;
}

/** Isti ključ kao u build_root_families.py: bez razmaka i harakata, elif varijante → ا. */
export function normRoot(root: string): string {
  return root.replace(/[\sً-ْٰ]/g, "").replace(/[أإآٱ]/g, "ا");
}
