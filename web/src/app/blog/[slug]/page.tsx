import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import "@/styles/blog.css";
import { ShareMenu } from "@/components/ShareMenu";
import { firstImageUrl, formatBlogDate } from "@/lib/blog";
import { getPublishedPost } from "@/lib/blogQueries";

export const dynamic = "force-dynamic";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPublishedPost(slug);
  if (!post) return { title: "Članak nije pronađen — Kur'an riječ po riječ" };

  const image = firstImageUrl(post.content);
  return {
    title: `${post.title} — Kur'an riječ po riječ`,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      description: post.excerpt,
      type: "article",
      ...(image ? { images: [image] } : {}),
    },
  };
}

export default async function BlogPostPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = await getPublishedPost(slug);
  if (!post) notFound();

  return (
    <main className="page-shell">
      <article className="blog-post">
        <Link href="/blog" className="blog-back">
          ← Svi članci
        </Link>
        <h1 className="blog-post-title">{post.title}</h1>
        <div className="blog-post-meta">
          <span>{formatBlogDate(post.created_at)}</span>
          <div className="blog-share">
            <ShareMenu />
          </div>
        </div>
        {/* Sadržaj piše isključivo admin (RLS), i TipTap ga generiše iz svoje sheme. */}
        <div className="blog-content" dangerouslySetInnerHTML={{ __html: post.content }} />
      </article>
    </main>
  );
}
