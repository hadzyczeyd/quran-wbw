"use client";

import { useEffect, useMemo, useState, useSyncExternalStore } from "react";
import { isTrackingExcluded, setTrackingExcluded, subscribeConsent } from "@/lib/consent";
import { supabase } from "@/lib/supabase";

interface Row {
  key: string;
  visitors?: number;
  sessions?: number;
  views?: number;
}

interface Summary {
  days: number;
  totals: { visitors: number; sessions: number; views: number };
  today: { visitors: number; views: number };
  daily: { day: string; visitors: number; views: number }[];
  countries: Row[];
  sources: Row[];
  apps: Row[];
  devices: Row[];
  browsers: Row[];
  os: Row[];
  pages: Row[];
}

const PERIODS = [7, 30, 90, 365];
const DEVICE_NAMES: Record<string, string> = { mobile: "Mobitel", tablet: "Tablet", desktop: "Računar" };

function countryName(code: string, names: Intl.DisplayNames | null): string {
  if (code === "??") return "Nepoznato";
  const flag = String.fromCodePoint(...[...code].map((c) => 0x1f1e6 + c.charCodeAt(0) - 65));
  let name = code;
  try {
    name = names?.of(code) ?? code;
  } catch {
    /* nepoznat kod */
  }
  return `${flag} ${name}`;
}

function Table({ title, rows, valueKey, label, format }: {
  title: string;
  rows: Row[];
  valueKey: "visitors" | "sessions" | "views";
  label: string;
  format?: (k: string) => string;
}) {
  const total = rows.reduce((s, r) => s + (r[valueKey] ?? 0), 0);
  return (
    <section className="stats-card">
      <h2>{title}</h2>
      {rows.length === 0 ? (
        <p className="admin-note">Još nema podataka.</p>
      ) : (
        <table className="stats-table">
          <thead>
            <tr>
              <th scope="col"></th>
              <th scope="col">{label}</th>
              <th scope="col">%</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r) => (
              <tr key={r.key}>
                <td>{format ? format(r.key) : r.key}</td>
                <td>{r[valueKey]}</td>
                <td>{total ? Math.round(((r[valueKey] ?? 0) / total) * 100) : 0}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </section>
  );
}

export function AdminStats() {
  const [days, setDays] = useState(30);
  const [data, setData] = useState<Summary | null>(null);
  const [error, setError] = useState<string | null>(null);
  const excluded = useSyncExternalStore(subscribeConsent, isTrackingExcluded, () => true);

  const countryNames = useMemo(() => {
    try {
      return new Intl.DisplayNames(["bs"], { type: "region" });
    } catch {
      return null;
    }
  }, []);

  useEffect(() => {
    let active = true;
    (async () => {
      const { data: res, error: rpcError } = await supabase.rpc("analytics_summary", { p_days: days });
      if (!active) return;
      if (rpcError) {
        setError(
          rpcError.message.includes("analytics_summary")
            ? "Statistika još nije podešena u bazi (nedostaje migracija 20261105000000_analytics.sql)."
            : "Učitavanje statistike nije uspjelo."
        );
        return;
      }
      setError(null);
      setData(res as Summary);
    })();
    return () => {
      active = false;
    };
  }, [days]);

  function toggleExcluded() {
    setTrackingExcluded(!excluded);
  }

  const maxDaily = Math.max(1, ...(data?.daily ?? []).map((d) => d.visitors));

  return (
    <div className="stats">
      <div className="stats-head">
        <h2>Statistika posjeta</h2>
        <div className="stats-periods" role="group" aria-label="Period">
          {PERIODS.map((p) => (
            <button
              key={p}
              type="button"
              className={`admin-btn ${p === days ? "" : "admin-btn-secondary"}`}
              onClick={() => setDays(p)}
            >
              {p === 365 ? "Godina" : `${p} dana`}
            </button>
          ))}
        </div>
      </div>

      <p className="admin-note">
        Bilježe se samo posjetioci koji su prihvatili statistiku. Ne broje se botovi, lokalni razvoj i ovaj
        uređaj dok je uključena opcija ispod.{" "}
        <label className="stats-exclude">
          <input type="checkbox" checked={excluded} onChange={toggleExcluded} /> Ne broji moje posjete s ovog
          uređaja
        </label>
      </p>

      {error && <p className="admin-error">{error}</p>}
      {!data && !error && <p className="admin-note">Učitavanje…</p>}

      {data && (
        <>
          <div className="stats-kpis">
            <div className="stats-kpi">
              <span className="stats-kpi-value">{data.totals.visitors}</span>
              <span className="stats-kpi-label">posjetilaca</span>
            </div>
            <div className="stats-kpi">
              <span className="stats-kpi-value">{data.totals.sessions}</span>
              <span className="stats-kpi-label">posjeta</span>
            </div>
            <div className="stats-kpi">
              <span className="stats-kpi-value">{data.totals.views}</span>
              <span className="stats-kpi-label">pregleda stranica</span>
            </div>
            <div className="stats-kpi">
              <span className="stats-kpi-value">{data.today.visitors}</span>
              <span className="stats-kpi-label">posjetilaca danas</span>
            </div>
          </div>

          <section className="stats-card">
            <h2>Posjetioci po danu</h2>
            {data.daily.length === 0 ? (
              <p className="admin-note">Još nema podataka.</p>
            ) : (
              <div className="stats-chart" role="img" aria-label="Broj posjetilaca po danu">
                {data.daily.map((d) => (
                  <div key={d.day} className="stats-bar" title={`${d.day}: ${d.visitors} posjetilaca, ${d.views} pregleda`}>
                    <span style={{ height: `${(d.visitors / maxDaily) * 100}%` }} />
                  </div>
                ))}
              </div>
            )}
          </section>

          <div className="stats-grid">
            <Table title="Države" rows={data.countries} valueKey="visitors" label="Posjetioci"
              format={(k) => countryName(k, countryNames)} />
            <Table title="Izvori dolaska" rows={data.sources} valueKey="sessions" label="Posjete" />
            <Table title="Aplikacija / preglednik" rows={data.apps} valueKey="visitors" label="Posjetioci" />
            <Table title="Uređaji" rows={data.devices} valueKey="visitors" label="Posjetioci"
              format={(k) => DEVICE_NAMES[k] ?? k} />
            <Table title="Preglednici" rows={data.browsers} valueKey="visitors" label="Posjetioci" />
            <Table title="Operativni sistemi" rows={data.os} valueKey="visitors" label="Posjetioci" />
          </div>
          <Table title="Najposjećenije stranice" rows={data.pages} valueKey="views" label="Pregledi" />
        </>
      )}
    </div>
  );
}
