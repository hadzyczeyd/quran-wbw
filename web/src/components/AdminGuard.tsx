"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";

type GuardState = "loading" | "ok" | "no-access" | "setup-error";

/**
 * Pušta dalje samo prijavljenog admina. Ovo je samo UI zaštita — stvarnu
 * sigurnost daju RLS pravila u bazi (is_blog_admin), pa bez admin naloga
 * nijedan upis ne prolazi čak ni mimo ove stranice.
 */
export function AdminGuard({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const [state, setState] = useState<GuardState>("loading");

  useEffect(() => {
    let active = true;

    async function check() {
      const {
        data: { session },
      } = await supabase.auth.getSession();
      if (!session) {
        router.replace("/login");
        return;
      }
      const { data, error } = await supabase.rpc("is_blog_admin");
      if (!active) return;
      if (error) setState("setup-error");
      else setState(data === true ? "ok" : "no-access");
    }

    check();
    const { data: sub } = supabase.auth.onAuthStateChange((_event, session) => {
      if (!session) router.replace("/login");
    });

    return () => {
      active = false;
      sub.subscription.unsubscribe();
    };
  }, [router]);

  async function logout() {
    await supabase.auth.signOut();
    router.replace("/login");
  }

  if (state === "loading") {
    return (
      <main className="page-shell admin-shell">
        <p className="admin-note">Učitavanje…</p>
      </main>
    );
  }

  if (state === "no-access" || state === "setup-error") {
    return (
      <main className="page-shell admin-shell">
        <p className="admin-error">
          {state === "no-access"
            ? "Ovaj nalog nema pristup uređivanju bloga."
            : "Uređivanje bloga još nije podešeno u bazi (nedostaje migracija)."}
        </p>
        <p>
          <button type="button" className="admin-btn admin-btn-secondary" onClick={logout}>
            Odjava
          </button>
        </p>
      </main>
    );
  }

  return (
    <main className="page-shell admin-shell">
      <div className="admin-bar">
        <h1 className="admin-bar-title">Uređivanje bloga</h1>
        <nav className="admin-bar-links">
          <Link href="/admin">Članci</Link>
          <Link href="/admin/novi">Novi članak</Link>
          <Link href="/blog">Pogledaj blog</Link>
          <button type="button" className="admin-link-btn" onClick={logout}>
            Odjava
          </button>
        </nav>
      </div>
      {children}
    </main>
  );
}
