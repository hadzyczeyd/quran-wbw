"use client";

import { type ReactNode, useEffect, useMemo, useRef, useState } from "react";
import type { BosnianToken, QacWord, SurahData } from "@/lib/types";
import { ayahAudioUrl, wordAudioUrl } from "@/lib/audio";
import type { RootFamilies } from "@/lib/rootFamilies";
import type { RootPanelData } from "@/lib/rootPanel";
import { AyahRow } from "./AyahRow";
import { RootPanel } from "./RootPanel";

interface SuraReaderProps {
  data: SurahData;
  rootFamilies?: RootFamilies | null;
  /** Panel korijena (desna kolona na širem ekranu); postoji samo za sure s ROOT_PANEL podacima. */
  rootPanel?: RootPanelData | null;
  /** Otvarajući blok sure iznad prvog ajeta (server komponenta). */
  header?: ReactNode;
  /** Ajeti ove sure na kojima počinje džuz: ajet → broj džuza. */
  juzStarts?: Record<number, number>;
}

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
  rootFamilies,
  rootPanel,
  header,
  juzStarts,
}: SuraReaderProps) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [activeWordId, setActiveWordId] = useState<string | null>(null);
  const [activeTokenIds, setActiveTokenIds] = useState<Set<string>>(new Set());
  const [playing, setPlaying] = useState<PlayingState>(null);

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

  // Link na ajet (#ajet-N, npr. iz navigacije po džuzevima): skrol nakon što je čitač iscrtan.
  useEffect(() => {
    const m = /^#ajet-(\d+)$/.exec(window.location.hash);
    if (m) document.getElementById(`ajet-${m[1]}`)?.scrollIntoView({ block: "start" });
  }, []);

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

  // Na uskom ekranu ploča korijena prekriva donju polovinu — kliknuta
  // riječ se pomjeri u gornju četvrtinu ekrana da ostane vidljiva.
  function revealAboveSheet(word: QacWord, ayahNumber: number) {
    if (!rootPanel || !rootPanel.words[`${ayahNumber}:${word.position}`])
      return;
    if (!window.matchMedia("(max-width: 74.99rem)").matches) return;
    const el = document.querySelector(`[data-word-id="${word.word_id}"]`);
    if (!el) return;
    const top = el.getBoundingClientRect().top;
    if (top > window.innerHeight * 0.4 || top < 70) {
      window.scrollBy({
        top: top - window.innerHeight * 0.22,
        behavior: "smooth",
      });
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
      <div className={`sura-main-column${rootPanel ? " has-root-panel" : ""}`}>
        {header}
        <div className="sura-reader" onClick={clearHighlight}>
          {data.ayat.map((ayah) => (
            <AyahRow
              key={ayah.ayah_number}
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
              rootFamilies={rootPanel ? null : rootFamilies}
              juzStart={juzStarts?.[ayah.ayah_number]}
            />
          ))}
        </div>
      </div>
      {rootPanel && (
        <RootPanel
          panel={rootPanel}
          selection={rootSelection}
          onClose={clearHighlight}
        />
      )}
    </>
  );
}
