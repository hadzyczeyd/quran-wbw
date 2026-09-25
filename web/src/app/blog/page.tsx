import type { Metadata } from "next";
import Link from "next/link";
import "@/styles/blog.css";
import { formatBlogDate } from "@/lib/blog";
import { getPublishedPosts } from "@/lib/blogQueries";

// Novi članci moraju biti vidljivi odmah, bez novog deploya.
export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Blog — Kur'an riječ po riječ",
  description: "Članci i obavijesti uz aplikaciju Kur'an riječ po riječ.",
};

export default async function BlogPage() {
  const posts = await getPublishedPosts();

  return (
    <main className="page-shell">
      <section className="blog-hero">
        <h1>Blog</h1>
        <p>Članci i obavijesti uz aplikaciju.</p>
      </section>

      {posts.length === 0 ? (
        <p className="blog-empty">Uskoro — još nema objavljenih članaka.</p>
      ) : (
        <div className="blog-grid">
          {posts.map((post) => (
            <Link key={post.id} href={`/blog/${post.slug}`} className="blog-card">
              <span className="blog-card-date">{formatBlogDate(post.created_at)}</span>
              <h2 className="blog-card-title">{post.title}</h2>
              {post.excerpt && <p className="blog-card-excerpt">{post.excerpt}</p>}
              <span className="blog-card-more">Pročitaj →</span>
            </Link>
          ))}
        </div>
      )}
    </main>
  );
}
