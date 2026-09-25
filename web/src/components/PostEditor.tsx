"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState, type ChangeEvent } from "react";
import Image from "@tiptap/extension-image";
import Placeholder from "@tiptap/extension-placeholder";
import { TableKit } from "@tiptap/extension-table";
import { EditorContent, useEditor, useEditorState, type Editor } from "@tiptap/react";
import StarterKit from "@tiptap/starter-kit";
import "@/styles/blog.css";
import { slugify } from "@/lib/blog";
import { supabase } from "@/lib/supabase";

const IMAGE_TYPES = ["image/jpeg", "image/png", "image/webp", "image/gif"];
const MAX_IMAGE_BYTES = 5 * 1024 * 1024;

interface ToolButtonProps {
  label: React.ReactNode;
  title: string;
  onClick: () => void;
  active?: boolean;
  disabled?: boolean;
  danger?: boolean;
}

function ToolButton({ label, title, onClick, active, disabled, danger }: ToolButtonProps) {
  return (
    <button
      type="button"
      className={`editor-btn${active ? " is-active" : ""}${danger ? " editor-btn-danger" : ""}`}
      title={title}
      aria-label={title}
      aria-pressed={active}
      disabled={disabled}
      // Sprječava da klik na dugme oduzme fokus/selekciju editoru.
      onMouseDown={(e) => e.preventDefault()}
      onClick={onClick}
    >
      {label}
    </button>
  );
}

function EditorToolbar({
  editor,
  onError,
}: {
  editor: Editor;
  onError: (message: string | null) => void;
}) {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [uploading, setUploading] = useState(false);

  const s = useEditorState({
    editor,
    selector: ({ editor: e }) => ({
      bold: e.isActive("bold"),
      italic: e.isActive("italic"),
      underline: e.isActive("underline"),
      h2: e.isActive("heading", { level: 2 }),
      h3: e.isActive("heading", { level: 3 }),
      bullet: e.isActive("bulletList"),
      ordered: e.isActive("orderedList"),
      quote: e.isActive("blockquote"),
      link: e.isActive("link"),
      inTable: e.isActive("table"),
      canUndo: e.can().undo(),
      canRedo: e.can().redo(),
    }),
  });

  function setLink() {
    const previous = editor.getAttributes("link").href as string | undefined;
    const input = window.prompt("Adresa linka (npr. https://primjer.ba):", previous ?? "https://");
    if (input === null) return;
    const url = input.trim();
    if (url === "" || url === "https://") {
      editor.chain().focus().extendMarkRange("link").unsetLink().run();
      return;
    }
    const href = /^(https?:\/\/|mailto:)/i.test(url) ? url : `https://${url}`;
    editor.chain().focus().extendMarkRange("link").setLink({ href }).run();
  }

  async function onFileChosen(e: ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    e.target.value = "";
    if (!file) return;

    if (!IMAGE_TYPES.includes(file.type)) {
      onError("Dozvoljene su slike u formatu JPG, PNG, WEBP ili GIF.");
      return;
    }
    if (file.size > MAX_IMAGE_BYTES) {
      onError("Slika je prevelika (najviše 5 MB).");
      return;
    }

    onError(null);
    setUploading(true);
    const ext = file.type === "image/jpeg" ? "jpg" : file.type.split("/")[1];
    const path = `${crypto.randomUUID()}.${ext}`;
    const { error } = await supabase.storage
      .from("blog-images")
      .upload(path, file, { contentType: file.type, cacheControl: "31536000" });
    setUploading(false);

    if (error) {
      onError(`Otpremanje slike nije uspjelo: ${error.message}`);
      return;
    }
    const { data } = supabase.storage.from("blog-images").getPublicUrl(path);
    editor
      .chain()
      .focus()
      .setImage({ src: data.publicUrl, alt: file.name.replace(/\.[^.]+$/, "") })
      .run();
  }

  const run = () => editor.chain().focus();

  return (
    <>
      <div className="editor-toolbar" role="toolbar" aria-label="Formatiranje teksta">
        <div className="editor-toolbar-group">
          <ToolButton label={<strong>B</strong>} title="Podebljano" active={s.bold} onClick={() => run().toggleBold().run()} />
          <ToolButton label={<em>I</em>} title="Kurziv" active={s.italic} onClick={() => run().toggleItalic().run()} />
          <ToolButton label={<u>U</u>} title="Podvučeno" active={s.underline} onClick={() => run().toggleUnderline().run()} />
        </div>
        <div className="editor-toolbar-group">
          <ToolButton label="Naslov" title="Veliki naslov" active={s.h2} onClick={() => run().toggleHeading({ level: 2 }).run()} />
          <ToolButton label="Podnaslov" title="Manji naslov" active={s.h3} onClick={() => run().toggleHeading({ level: 3 }).run()} />
        </div>
        <div className="editor-toolbar-group">
          <ToolButton label="• Lista" title="Lista s tačkama" active={s.bullet} onClick={() => run().toggleBulletList().run()} />
          <ToolButton label="1. Lista" title="Numerisana lista" active={s.ordered} onClick={() => run().toggleOrderedList().run()} />
          <ToolButton label="❝ Citat" title="Citat" active={s.quote} onClick={() => run().toggleBlockquote().run()} />
        </div>
        <div className="editor-toolbar-group">
          <ToolButton label="Link" title="Dodaj ili uredi link" active={s.link} onClick={setLink} />
          <ToolButton
            label={uploading ? "Otprema…" : "Slika"}
            title="Otpremi sliku"
            disabled={uploading}
            onClick={() => fileInputRef.current?.click()}
          />
          <ToolButton
            label="Tabela"
            title="Umetni tabelu (3×3)"
            onClick={() => run().insertTable({ rows: 3, cols: 3, withHeaderRow: true }).run()}
          />
        </div>
        <div className="editor-toolbar-group">
          <ToolButton label="↶" title="Poništi" disabled={!s.canUndo} onClick={() => run().undo().run()} />
          <ToolButton label="↷" title="Ponovi" disabled={!s.canRedo} onClick={() => run().redo().run()} />
        </div>
        <input
          ref={fileInputRef}
          type="file"
          accept={IMAGE_TYPES.join(",")}
          hidden
          onChange={onFileChosen}
        />
      </div>

      {s.inTable && (
        <div className="editor-table-tools" role="toolbar" aria-label="Uređivanje tabele">
          <span>Tabela:</span>
          <ToolButton label="+ Red" title="Dodaj red ispod" onClick={() => run().addRowAfter().run()} />
          <ToolButton label="− Red" title="Obriši red" onClick={() => run().deleteRow().run()} />
          <ToolButton label="+ Kolona" title="Dodaj kolonu desno" onClick={() => run().addColumnAfter().run()} />
          <ToolButton label="− Kolona" title="Obriši kolonu" onClick={() => run().deleteColumn().run()} />
          <ToolButton label="Obriši tabelu" title="Obriši cijelu tabelu" danger onClick={() => run().deleteTable().run()} />
        </div>
      )}
    </>
  );
}

export function PostEditor({ postId }: { postId?: string }) {
  const router = useRouter();
  const [title, setTitle] = useState("");
  const [published, setPublished] = useState(true);
  const [loading, setLoading] = useState(Boolean(postId));
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const editor = useEditor({
    immediatelyRender: false,
    extensions: [
      StarterKit.configure({
        heading: { levels: [2, 3] },
        link: {
          openOnClick: false,
          autolink: true,
          HTMLAttributes: { rel: "noopener noreferrer nofollow", target: "_blank" },
        },
      }),
      TableKit.configure({ table: { resizable: false } }),
      Image.configure({ HTMLAttributes: { loading: "lazy" } }),
      Placeholder.configure({ placeholder: "Počnite pisati članak…" }),
    ],
    content: "",
    editorProps: { attributes: { class: "blog-content" } },
  });

  useEffect(() => {
    if (!postId || !editor) return;
    let active = true;

    (async () => {
      const { data, error: loadError } = await supabase
        .from("blog_posts")
        .select("*")
        .eq("id", postId)
        .maybeSingle();
      if (!active) return;
      if (loadError || !data) {
        setError("Članak nije pronađen.");
      } else {
        setTitle(data.title);
        setPublished(data.published);
        editor.commands.setContent(data.content);
      }
      setLoading(false);
    })();

    return () => {
      active = false;
    };
  }, [postId, editor]);

  async function save() {
    if (!editor) return;
    setError(null);

    const cleanTitle = title.trim();
    if (!cleanTitle) {
      setError("Unesite naslov članka.");
      return;
    }
    if (editor.isEmpty) {
      setError("Članak nema teksta.");
      return;
    }

    setSaving(true);
    const content = editor.getHTML();
    const text = editor.getText({ blockSeparator: " " }).replace(/\s+/g, " ").trim();
    const excerpt = text.length > 200 ? `${text.slice(0, 200).trimEnd()}…` : text;

    if (postId) {
      const { data, error: updateError } = await supabase
        .from("blog_posts")
        .update({ title: cleanTitle, content, excerpt, published })
        .eq("id", postId)
        .select("id");
      if (updateError || !data || data.length === 0) {
        setError("Spremanje nije uspjelo. Provjerite prijavu i pokušajte ponovo.");
        setSaving(false);
        return;
      }
    } else {
      const base = slugify(cleanTitle);
      let saved = false;
      for (let attempt = 0; attempt < 4 && !saved; attempt++) {
        const slug = attempt === 0 ? base : `${base}-${Math.random().toString(36).slice(2, 6)}`;
        const { error: insertError } = await supabase
          .from("blog_posts")
          .insert({ slug, title: cleanTitle, content, excerpt, published });
        if (!insertError) {
          saved = true;
        } else if (insertError.code !== "23505") {
          // 23505 = adresa već postoji, pokušavamo s drugim nastavkom.
          setError("Spremanje nije uspjelo. Provjerite prijavu i pokušajte ponovo.");
          setSaving(false);
          return;
        }
      }
      if (!saved) {
        setError("Nije moguće napraviti jedinstvenu adresu članka. Promijenite naslov.");
        setSaving(false);
        return;
      }
    }

    router.push("/admin");
  }

  async function remove() {
    if (!postId) return;
    if (!window.confirm("Obrisati ovaj članak? Ovo se ne može poništiti.")) return;
    const { error: deleteError } = await supabase.from("blog_posts").delete().eq("id", postId);
    if (deleteError) {
      setError("Brisanje nije uspjelo.");
      return;
    }
    router.push("/admin");
  }

  if (loading) return <p className="admin-note">Učitavanje…</p>;

  return (
    <section className="editor-card">
      <h2>{postId ? "Uređivanje članka" : "Novi članak"}</h2>

      <div className="admin-field">
        <label htmlFor="post-title">Naslov</label>
        <input
          id="post-title"
          className="admin-input editor-title-input"
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Naslov članka"
          maxLength={200}
        />
      </div>

      <div className="admin-field">
        <label>Tekst</label>
        <div>
          {editor && <EditorToolbar editor={editor} onError={setError} />}
          <div className="editor-surface">
            <EditorContent editor={editor} />
          </div>
        </div>
      </div>

      {error && <p className="admin-error">{error}</p>}

      <div className="editor-footer">
        <label className="editor-publish">
          <input type="checkbox" checked={published} onChange={(e) => setPublished(e.target.checked)} />
          Objavi (vidljivo posjetiocima)
        </label>

        <div className="editor-footer-actions">
          {postId && (
            <button type="button" className="admin-btn admin-btn-danger" onClick={remove} disabled={saving}>
              Obriši
            </button>
          )}
          <Link href="/admin" className="admin-btn admin-btn-secondary">
            Odustani
          </Link>
          <button type="button" className="admin-btn" onClick={save} disabled={saving}>
            {saving ? "Spremanje…" : published ? "Spremi i objavi" : "Spremi kao skicu"}
          </button>
        </div>
      </div>
    </section>
  );
}
