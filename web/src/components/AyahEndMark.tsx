import { toEasternArabicDigits } from "@/lib/arabicNumerals";

interface AyahEndMarkProps {
  number: number;
}

/**
 * Ukrasni broj kraja ajeta, kao u mushafu. Koristi standardne Unicode
 * ornamentalne zagrade ﴿ ﴾ (U+FD3E/FD3F, Arabic Presentation Forms-A)
 * oko istočnoarapske cifre — isti pristup kao Tanzil.net (provjereno
 * na tanzil.net/#1:1). Amiri Quran ih iscrtava kao elegantan
 * medaljon-oblik; nema potrebe za posebnim fontom niti ručno crtanim
 * SVG-om.
 */
export function AyahEndMark({ number }: AyahEndMarkProps) {
  return (
    <span className="ayah-end-mark" aria-hidden="true">
      {"﴿"}
      {toEasternArabicDigits(number)}
      {"﴾"}
    </span>
  );
}
