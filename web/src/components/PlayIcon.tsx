interface PlayIconProps {
  playing: boolean;
}

/**
 * SVG umjesto ▶/⏸ Unicode znakova — glifovi iz fonta imaju neravnomjeran
 * optički razmak (▶ posebno) i nikad ne ispadnu tačno centrirani u
 * okruglom dugmetu bez obzira na flex centriranje.
 */
export function PlayIcon({ playing }: PlayIconProps) {
  if (playing) {
    return (
      <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor" aria-hidden="true">
        <rect x="6" y="5" width="4" height="14" rx="0.5" />
        <rect x="14" y="5" width="4" height="14" rx="0.5" />
      </svg>
    );
  }

  return (
    <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor" aria-hidden="true">
      <path d="M7 4.7c0-.9 1-1.5 1.8-1L18 9.1c.8.5.8 1.7 0 2.2L8.8 16.7c-.8.5-1.8-.1-1.8-1Z" />
    </svg>
  );
}
