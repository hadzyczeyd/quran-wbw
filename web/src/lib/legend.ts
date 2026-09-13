// Master QAC legenda — spojena iz Legenda listova svih 33 V13 APP_READY
// fajlova (Juz Amma). Svaka klasa je stvarna boja s corpus.quran.com,
// bez preklasifikacije (NALOG-V13 poglavlje 5).
export interface LegendEntry {
  cssClass: string;
  label: string;
  tags: string[];
}

export const QAC_LEGEND: LegendEntry[] = [
  { cssClass: "segSeagreen", label: "glagol", tags: ["V"] },
  { cssClass: "segSky", label: "imenica / vezana zamjenica", tags: ["N", "PRON"] },
  { cssClass: "segBlue", label: "vlastita imenica", tags: ["PN"] },
  { cssClass: "segPurple", label: "pridjev", tags: ["ADJ"] },
  { cssClass: "segGray", label: "određeni član", tags: ["DET"] },
  { cssClass: "segMetal", label: "lična/posvojna zamjenica", tags: ["PRON"] },
  { cssClass: "segRust", label: "prijedlog", tags: ["P"] },
  { cssClass: "segNavy", label: "veznik", tags: ["CIRC", "CONJ", "REM", "RSLT"] },
  { cssClass: "segRed", label: "negacija / zabrana", tags: ["NEG", "PRO"] },
  { cssClass: "segRose", label: "upitna čestica", tags: ["INTG"] },
  { cssClass: "segOrange", label: "uslovna / mjesna / vremenska", tags: ["COND", "LOC", "PREV", "T"] },
  { cssClass: "segGold", label: "namjera / odnosna zamjenica", tags: ["PRP", "REL", "SUB"] },
  { cssClass: "segBrown", label: "pokazna zamjenica", tags: ["DEM"] },
  { cssClass: "segGreen", label: "dozivna čestica", tags: ["VOC"] },
  { cssClass: "segPink", label: "ostale čestice", tags: ["ACC", "EMPH", "SUP", "FUT", "..."] },
  { cssClass: "inserted_no_arabic_segment", label: "bez arapskog para", tags: ["—"] },
];
