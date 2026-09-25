"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { usernameToEmail } from "@/lib/blog";
import { supabase } from "@/lib/supabase";

export function LoginForm() {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => {
      if (data.session) router.replace("/admin");
    });
  }, [router]);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError(null);

    const { error: signInError } = await supabase.auth.signInWithPassword({
      email: usernameToEmail(username),
      password,
    });

    if (signInError) {
      setError("Pogrešno korisničko ime ili šifra.");
      setBusy(false);
      return;
    }
    router.replace("/admin");
  }

  return (
    <main className="page-shell login-shell">
      <form className="login-card" onSubmit={onSubmit}>
        <h1>Prijava</h1>

        <div className="admin-field">
          <label htmlFor="login-username">Korisničko ime</label>
          <input
            id="login-username"
            className="admin-input"
            type="text"
            autoComplete="username"
            autoCapitalize="none"
            spellCheck={false}
            required
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>

        <div className="admin-field">
          <label htmlFor="login-password">Šifra</label>
          <input
            id="login-password"
            className="admin-input"
            type="password"
            autoComplete="current-password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        {error && <p className="admin-error">{error}</p>}

        <button type="submit" className="admin-btn" disabled={busy}>
          {busy ? "Prijava…" : "Prijavi se"}
        </button>
      </form>
    </main>
  );
}
