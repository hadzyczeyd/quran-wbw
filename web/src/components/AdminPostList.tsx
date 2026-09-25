"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { formatBlogDate, type BlogPostSummary } from "@/lib/blog";
import { supabase } from "@/lib/supabase";

export function AdminPostList() {
  const [posts, setPosts] = useState<BlogPostSummary[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  const [reloadKey, setReloadKey] = useState(0);

  useEffect(() => {
    let active = true;

    (async () => {
      const { data, error: loadError } = await supabase
        .from("blog_posts")
        .select("id, slug, title, excerpt, published, created_at")
        .order("created_at", { ascending: false });
      if (!active) return;
      if (loadError) {
        setError("Učitavanje članaka nije uspjelo.");
        return;
      }
      setPosts(data ?? []);
    })();

    return () => {
      active = false;
    };
  }, [reloadKey]);

  async function remove(post: BlogPostSummary) {
    if (!window.confirm(`Obrisati članak „${post.title}“? Ovo se ne može poništiti.`)) return;
    const { error: deleteError } = await supabase.from("blog_posts").delete().eq("id", post.id);
    if (deleteError) {
      setError("Brisanje nije uspjelo.");
      return;
    }
    setError(null);
    setReloadKey((k) => k + 1);
  }

  return (
    <section>
      <div className="admin-list-head">
        <h2>Članci</h2>
        <Link href="/admin/novi" className="admin-btn">
          + Novi članak
        </Link>
      </div>

      {error && <p className="admin-error">{error}</p>}

      {posts === null && !error && <p className="admin-note">Učitavanje…</p>}

      {posts !== null && posts.length === 0 && (
        <p className="admin-note">Još nema članaka. Napravite prvi klikom na „Novi članak“.</p>
      )}

      {posts !== null && posts.length > 0 && (
        <ul className="admin-list">
          {posts.map((post) => (
            <li key={post.id} className="admin-list-item">
              <div>
                <span className="admin-list-title">
                  {post.title}
                  {!post.published && <span className="admin-badge">Skica</span>}
                </span>
                <span className="admin-list-meta">{formatBlogDate(post.created_at)}</span>
              </div>
              <div className="admin-list-actions">
                {post.published && (
                  <Link href={`/blog/${post.slug}`} className="admin-btn admin-btn-secondary">
                    Pogledaj
                  </Link>
                )}
                <Link href={`/admin/uredi/${post.id}`} className="admin-btn admin-btn-secondary">
                  Uredi
                </Link>
                <button type="button" className="admin-btn admin-btn-danger" onClick={() => remove(post)}>
                  Obriši
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
