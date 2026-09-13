const EASTERN_ARABIC_DIGITS = ["٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"];

/** Pretvara broj u istočnoarapske (indijsko-arapske) cifre, npr. 12 -> "١٢". */
export function toEasternArabicDigits(n: number): string {
  return String(n)
    .split("")
    .map((ch) => (/[0-9]/.test(ch) ? EASTERN_ARABIC_DIGITS[Number(ch)] : ch))
    .join("");
}
