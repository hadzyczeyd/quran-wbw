"use client";

import {
  type ReactNode,
  startTransition,
  useEffect,
  useMemo,
  useRef,
  useState,
  useSyncExternalStore,
} from "react";
import type { BosnianToken, QacWord, SurahData } from "@/lib/types";
import { ayahAudioUrl, wordAudioUrl } from "@/lib/audio";
import type { RootPanelIndex } from "@/lib/rootPanel";
import { setLastRead } from "@/lib/lastRead";
import { AyahRow } from "./AyahRow";
import { ColorLegend } from "./ColorLegend";
import { ReaderToolbar } from "./ReaderToolbar";
import { RootPanel } from "./RootPanel";

interface SuraReaderProps {
  data: SurahData;
  /** Panel korijena (desna kolona na širem ekranu); postoji samo za sure s ROOT_PANEL podacima. */
  rootPanel?: RootPanelIndex | null;
  /** Otvarajući blok sure iznad prvog ajeta (server komponenta). */
  header?: ReactNode;
  /** Ajeti ove sure na kojima počinje džuz: ajet → broj džuza. */
  juzStarts?: Record<number, number>;
  /** Bosanski naziv sure (traka čitača). */
  surahName: string;
  /** Blok ispod zadnjeg ajeta (prethodna/sljedeća sura). */
  footer?: ReactNode;
}

/** Koliko ajeta se iscrta odmah pri prelasku na suru; ostatak dolazi u dijelovima. */
const FIRST_CHUNK = 12;
const CHUNK = 24;

const noopSubscribe = () => () => {};

type PlayingState =
  | { kind: "ayah"; ayahNumber: number }
  | { kind: "word"; wordId: string }
  | null;

/**
 * Isticanje je GLOBALNO za cijelu suru — u svakom trenutku može biti
 * istaknuta samo jedna riječ (i njen bosanski par), nikad više ajeta
 * odjednom. Isto važi za zvuk: jedan zajednički <audio> element, klik
 * na bilo šta prekida prethodnu reprodukciju prije nove.
 */
export function SuraReader({
  data,
  rootPanel,
  header,
  juzStarts,
  surahName,
  footer,
}: SuraReaderProps) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [activeWordId, setActiveWordId] = useState<string | null>(null);
  const [activeTokenIds, setActiveTokenIds] = useState<Set<string>>(new Set());
  const [playing, setPlaying] = useState<PlayingState>(null);

  // Pri direktnom otvaranju (hidratacija) server je već iscrtao sve ajete.
  // Pri kliku na suru unutar aplikacije prvo se odmah prikažu prvi ajeti,
  // a ostatak se dodaje u pozadini — klik je trenutan i kod dugih sura.
  const isClientNavigation = useSyncExternalStore(noopSubscribe, () => true, () => false);
  const total = data.ayat.length;
  const [renderCount, setRenderCount] = useState(() =>
    isClientNavigation ? Math.min(FIRST_CHUNK, total) : total,
  );

  useEffect(() => {
    if (renderCount >= total) return;
    const id = setTimeout(() => {
      startTransition(() => setRenderCount((c) => Math.min(total, c + CHUNK)));
    }, 0);
    return () => clearTimeout(id);
  }, [renderCount, total]);

  // word_id -> { ayahNumber, word } — za povratnu vezu token -> riječ i audio.
  const wordIndex = useMemo(() => {
    const map = new Map<string, { ayahNumber: number; word: QacWord }>();
    for (const ayah of data.ayat) {
      for (const w of ayah.words) {
        map.set(w.word_id, { ayahNumber: ayah.ayah_number, word: w });
      }
    }
    return map;
  }, [data.ayat]);

  const segmentToWord = useMemo(() => {
    const map = new Map<string, string>();
    for (const ayah of data.ayat) {
      for (const w of ayah.words) {
        for (const s of w.segments) map.set(s.segment_id, w.word_id);
      }
    }
    return map;
  }, [data.ayat]);

  // Skok na ajet (link #ajet-N, "Nastavi čitati" ili traka): ajet mora biti
  // iscrtan, pa se po potrebi odmah iscrtaju svi do njega.
  const pendingJump = useRef<number | null>(null);
  const renderCountRef = useRef(renderCount);
  useEffect(() => {
    renderCountRef.current = renderCount;
    if (pendingJump.current !== null && renderCount >= pendingJump.current) {
      document.getElementById(`ajet-${pendingJump.current}`)?.scrollIntoView({ block: "start" });
      pendingJump.current = null;
    }
  }, [renderCount]);

  function jumpTo(ayah: number, updateHash = true) {
    if (updateHash) history.replaceState(null, "", `#ajet-${ayah}`);
    if (renderCountRef.current >= ayah) {
      document.getElementById(`ajet-${ayah}`)?.scrollIntoView({ block: "start" });
    } else {
      pendingJump.current = ayah;
      setRenderCount(Math.min(total, ayah + CHUNK));
    }
  }

  useEffect(() => {
    const id = setTimeout(() => {
      const m = /^#ajet-(\d+)$/.exec(window.location.hash);
      if (m) jumpTo(Number(m[1]), false);
    }, 0);
    return () => clearTimeout(id);
    // Samo pri otvaranju sure.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Trenutni ajet = onaj koji prelazi gornju trećinu ekrana. Pamti se kao
  // "zadnje čitanje" (localStorage) za karticu "Nastavi čitati" na početnoj.
  const [currentAyah, setCurrentAyah] = useState(1);
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        for (const e of entries) {
          if (e.isIntersecting) {
            const n = Number((e.target as HTMLElement).dataset.ayah);
            if (n) setCurrentAyah(n);
          }
        }
      },
      { rootMargin: "-25% 0px -70% 0px" },
    );
    document.querySelectorAll<HTMLElement>(".ayah[data-ayah]").forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, [renderCount]);
  useEffect(() => {
    const id = setTimeout(() => setLastRead({ surah: data.surah_id, ayah: currentAyah }), 800);
    return () => clearTimeout(id);
  }, [currentAyah, data.surah_id]);

  function getAudio(): HTMLAudioElement {
    if (audioRef.current === null) {
      audioRef.current = new Audio();
      audioRef.current.addEventListener("ended", () => setPlaying(null));
    }
    return audioRef.current;
  }

  function playWord(word: QacWord, ayahNumber: number) {
    const audio = getAudio();
    audio.pause();
    audio.src = wordAudioUrl(data.surah_id, ayahNumber, word.position);
    audio.play().catch(() => setPlaying(null));
    setPlaying({ kind: "word", wordId: word.word_id });
  }

  function clearHighlight() {
    setActiveWordId(null);
    setActiveTokenIds(new Set());
  }

  function handleWordClick(word: QacWord, ayahNumber: number) {
    if (activeWordId === word.word_id) {
      // Ponovni klik na već istaknutu riječ gasi isticanje.
      clearHighlight();
      return;
    }

    const tokenIds = new Set<string>();
    for (const seg of word.segments) {
      for (const tid of seg.linked_token_ids) tokenIds.add(tid);
    }
    setActiveTokenIds(tokenIds);
    setActiveWordId(word.word_id);
    playWord(word, ayahNumber);
    revealAboveSheet(word, ayahNumber);
  }

  // Na uskom ekranu traka korijena stoji pri dnu — ako bi prekrila
  // kliknutu riječ, riječ se pomjeri u gornju trećinu ekrana.
  function revealAboveSheet(word: QacWord, ayahNumber: number) {
    if (!rootPanel || !rootPanel.words[`${ayahNumber}:${word.position}`]) return;
    if (!window.matchMedia("(max-width: 71.99rem)").matches) return;
    if (document.documentElement.getAttribute("data-roots") === "off") return;
    const el = document.querySelector(`[data-word-id="${word.word_id}"]`);
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const covered = rect.bottom > window.innerHeight - 150;
    if (covered) {
      window.scrollBy({ top: rect.top - window.innerHeight * 0.35, behavior: "smooth" });
    }
  }

  function handleTokenClick(token: BosnianToken) {
    if (activeTokenIds.has(token.token_id) && activeTokenIds.size === 1) {
      clearHighlight();
      return;
    }

    // Bosanska riječ nema svoju boju niti audio — vodi na svoj arapski
    // segment i odatle na cijelu riječ (i njen izgovor).
    let firstWordId: string | null = null;
    for (const segId of token.linked_segment_ids) {
      const wid = segmentToWord.get(segId);
      if (wid) {
        firstWordId = wid;
        break;
      }
    }
    setActiveTokenIds(new Set([token.token_id]));
    setActiveWordId(firstWordId);

    if (firstWordId) {
      const entry = wordIndex.get(firstWordId);
      if (entry) playWord(entry.word, entry.ayahNumber);
    }
  }

  function handlePlayAyah(ayahNumber: number) {
    const audio = getAudio();

    if (playing?.kind === "ayah" && playing.ayahNumber === ayahNumber) {
      audio.pause();
      audio.currentTime = 0;
      setPlaying(null);
      return;
    }

    audio.pause();
    audio.src = ayahAudioUrl(data.surah_id, ayahNumber);
    audio.play().catch(() => setPlaying(null));
    setPlaying({ kind: "ayah", ayahNumber });
  }

  const activeEntry = activeWordId ? wordIndex.get(activeWordId) : undefined;
  const rootSelection = activeEntry
    ? {
        ayahNumber: activeEntry.ayahNumber,
        position: activeEntry.word.position,
      }
    : null;

  return (
    <>
      <ReaderToolbar
        surahId={data.surah_id}
        surahName={surahName}
        ayahCount={total}
        currentAyah={currentAyah}
        onJump={jumpTo}
      />
      <div className="reader-columns">
      {/* Široki ekran: legenda boja stalno lijevo od teksta (na mobitelu je u traci čitača). */}
      <aside className="reader-legend" aria-labelledby="legenda-lijevo">
        <h2 id="legenda-lijevo" className="reader-legend-title">
          Legenda boja
        </h2>
        <ColorLegend />
      </aside>
      <div className="reader-main">
        {header}
        <div className="sura-reader" onClick={clearHighlight}>
          {data.ayat.slice(0, renderCount).map((ayah) => (
            <AyahRow
              key={ayah.ayah_number}
              surahId={data.surah_id}
              ayah={ayah}
              activeWordId={activeWordId}
              activeTokenIds={activeTokenIds}
              onWordClick={(word) => handleWordClick(word, ayah.ayah_number)}
              onTokenClick={handleTokenClick}
              onPlayAyah={handlePlayAyah}
              isAyahPlaying={
                playing?.kind === "ayah" &&
                playing.ayahNumber === ayah.ayah_number
              }
              juzStart={juzStarts?.[ayah.ayah_number]}
            />
          ))}
        </div>
        {renderCount >= total && footer}
      </div>
      <RootPanel panel={rootPanel ?? null} selection={rootSelection} onClose={clearHighlight} />
      </div>
    </>
  );
}
