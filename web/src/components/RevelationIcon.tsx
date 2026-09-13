import type { RevelationType } from "@/lib/surahs";

interface RevelationIconProps {
  type: RevelationType;
}

/**
 * Mali simbol mjesta objave — Kaba za mekkanske sure, Poslanikova
 * džamija (zelena kupola) za medinske, po uzoru na praksu sajtova kao
 * quranwbw.com da svaka sura nosi prepoznatljivu ilustraciju mjesta
 * objave. Originalna ilustracija, ne kopija njihovog SVG-a.
 */
export function RevelationIcon({ type }: RevelationIconProps) {
  if (type === "meccan") {
    return (
      <svg viewBox="0 0 24 24" width="15" height="15" aria-label="Mekkanska sura" role="img">
        <title>Mekkanska sura — Kaba</title>
        {/* Kaba: crna kocka sa zlatnim pojasom (kiswa) i vratima */}
        <path d="M5 8.5 L12 5 L19 8.5 L19 19 L5 19 Z" fill="#1c1c1c" />
        <path d="M5 8.5 L12 5 L19 8.5 L12 12 Z" fill="#2e2e2e" />
        <rect x="5" y="12.5" width="14" height="2" fill="#c9a13b" />
        <rect x="10.3" y="15" width="3.4" height="4" fill="#c9a13b" opacity="0.9" />
      </svg>
    );
  }

  return (
    <svg viewBox="0 0 24 24" width="15" height="15" aria-label="Medinska sura" role="img">
      <title>Medinska sura — Poslanikova džamija</title>
      {/* Zelena kupola Poslanikove džamije, s dva minareta */}
      <rect x="2.6" y="15" width="1.6" height="5" fill="#7a7264" />
      <rect x="19.8" y="15" width="1.6" height="5" fill="#7a7264" />
      <path d="M3.4 15 L2.6 12.5 L4.2 12.5 Z" fill="#2f8f5b" />
      <path d="M20.6 15 L19.8 12.5 L21.4 12.5 Z" fill="#2f8f5b" />
      <rect x="6" y="17" width="12" height="3" fill="#efe6d3" />
      <path d="M6 17c0-3.5 2.7-6.3 6-6.3s6 2.8 6 6.3Z" fill="#2f8f5b" />
      <rect x="11.4" y="8" width="1.2" height="3" fill="#2f8f5b" />
      <circle cx="12" cy="7.3" r="0.9" fill="#c9a13b" />
    </svg>
  );
}
