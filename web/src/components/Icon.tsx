/** Jednostavne linijske ikone (24×24, currentColor). Uvijek dekorativne — tekst ili aria-label nosi značenje. */
const PATHS: Record<string, React.ReactNode> = {
  home: (
    <>
      <path d="M4 10.5 12 4l8 6.5" />
      <path d="M6 9.5V20h12V9.5" />
      <path d="M10 20v-5h4v5" />
    </>
  ),
  book: (
    <>
      <path d="M12 6.5C10 5 7.5 4.5 4 4.5v14c3.5 0 6 .5 8 2 2-1.5 4.5-2 8-2v-14c-3.5 0-6 .5-8 2Z" />
      <path d="M12 6.5v14" />
    </>
  ),
  article: (
    <>
      <rect x="4" y="4" width="16" height="16" rx="2" />
      <path d="M8 9h8M8 12.5h8M8 16h5" />
    </>
  ),
  more: (
    <>
      <circle cx="6" cy="12" r="1.3" fill="currentColor" stroke="none" />
      <circle cx="12" cy="12" r="1.3" fill="currentColor" stroke="none" />
      <circle cx="18" cy="12" r="1.3" fill="currentColor" stroke="none" />
    </>
  ),
  search: (
    <>
      <circle cx="11" cy="11" r="6" />
      <path d="m20 20-4.5-4.5" />
    </>
  ),
  play: <path d="M8 5.5v13l10.5-6.5Z" fill="currentColor" stroke="none" />,
  pause: (
    <>
      <rect x="7" y="5.5" width="3.5" height="13" rx="0.8" fill="currentColor" stroke="none" />
      <rect x="13.5" y="5.5" width="3.5" height="13" rx="0.8" fill="currentColor" stroke="none" />
    </>
  ),
  type: (
    <>
      <path d="M4 18 8.5 6h1L14 18" />
      <path d="M5.7 14h6.6" />
      <path d="M15.5 18l2.75-7h.5L21.5 18" />
      <path d="M16.4 15.6h4.2" />
    </>
  ),
  palette: (
    <>
      <circle cx="12" cy="12" r="8" />
      <circle cx="8.5" cy="10" r="1.2" fill="currentColor" stroke="none" />
      <circle cx="12" cy="7.5" r="1.2" fill="currentColor" stroke="none" />
      <circle cx="15.5" cy="10" r="1.2" fill="currentColor" stroke="none" />
      <path d="M12 20c-1.5 0-2-1-2-2s1-2 2.5-2H15" />
    </>
  ),
  share: (
    <>
      <path d="M12 15V4" />
      <path d="M7.5 8.5 12 4l4.5 4.5" />
      <path d="M5 13v5a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-5" />
    </>
  ),
  link: (
    <>
      <path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1" />
      <path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1" />
    </>
  ),
  check: <path d="m5 12.5 4.5 4.5L19 7.5" />,
  chevronLeft: <path d="m14.5 6-6 6 6 6" />,
  chevronUp: <path d="m6 14.5 6-6 6 6" />,
  chevronDown: <path d="m6 9.5 6 6 6-6" />,
  chevronRight: <path d="m9.5 6 6 6-6 6" />,
  close: <path d="M6 6l12 12M18 6 6 18" />,
  sun: (
    <>
      <circle cx="12" cy="12" r="4" />
      <path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4" />
    </>
  ),
  moon: <path d="M19.5 14.5A8 8 0 0 1 9.5 4.5a8 8 0 1 0 10 10Z" />,
  download: (
    <>
      <path d="M12 4v11" />
      <path d="M7.5 10.5 12 15l4.5-4.5" />
      <path d="M5 19h14" />
    </>
  ),
  info: (
    <>
      <circle cx="12" cy="12" r="8.5" />
      <path d="M12 11v5.5" />
      <circle cx="12" cy="7.8" r="0.6" fill="currentColor" />
    </>
  ),
  mail: (
    <>
      <rect x="3.5" y="5.5" width="17" height="13" rx="2" />
      <path d="m4.5 7 7.5 6 7.5-6" />
    </>
  ),
  sources: (
    <>
      <path d="M6 4h9l3 3v13H6Z" />
      <path d="M9 10h6M9 13.5h6M9 17h4" />
    </>
  ),
  shield: <path d="M12 3.5 5 6v5.5c0 4.2 3 7.7 7 9 4-1.3 7-4.8 7-9V6Z" />,
};

export type IconName = keyof typeof PATHS;

export function Icon({ name, size = 20 }: { name: IconName; size?: number }) {
  return (
    <svg
      viewBox="0 0 24 24"
      width={size}
      height={size}
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      focusable="false"
    >
      {PATHS[name]}
    </svg>
  );
}
