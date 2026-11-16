"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { LOGO_HALF_PATHS, LOGO_MIRROR } from "@/lib/logo";
import { Icon, type IconName } from "./Icon";
import { ShareMenu } from "./ShareMenu";
import { ThemeToggle } from "./ThemeToggle";

const DESKTOP_LINKS = [
  { href: "/sure", label: "Sure" },
  { href: "/blog", label: "Blog" },
  { href: "/o-aplikaciji", label: "O aplikaciji" },
  { href: "/izvori", label: "Izvori" },
  { href: "/contact", label: "Kontakt" },
];

const TABS: { href: string; label: string; icon: IconName; match: (p: string) => boolean }[] = [
  { href: "/", label: "Početna", icon: "home", match: (p) => p === "/" },
  { href: "/sure", label: "Sure", icon: "book", match: (p) => p.startsWith("/sur") },
  { href: "/blog", label: "Blog", icon: "article", match: (p) => p.startsWith("/blog") },
  {
    href: "/vise",
    label: "Više",
    icon: "more",
    match: (p) => ["/vise", "/o-aplikaciji", "/izvori", "/contact", "/privatnost"].some((x) => p.startsWith(x)),
  },
];

function Brand() {
  return (
    <Link href="/" className="brand">
      <svg viewBox="16 22 96 84" width="34" height="30" aria-hidden="true" className="brand-mark">
        <g fill="var(--logo)">
          {LOGO_HALF_PATHS.map((d) => (
            <path key={d} d={d} />
          ))}
          <g transform={LOGO_MIRROR}>
            {LOGO_HALF_PATHS.map((d) => (
              <path key={d} d={d} />
            ))}
          </g>
        </g>
      </svg>
      <span>Kur&apos;an riječ po riječ</span>
    </Link>
  );
}

/** Gornje zaglavlje: na širem ekranu puna navigacija, na mobitelu samo naziv i brze radnje. */
export function SiteHeader() {
  const pathname = usePathname() ?? "/";
  return (
    <header className="site-header">
      <div className="shell site-header-inner">
        <Brand />
        <nav className="header-nav" aria-label="Glavna navigacija">
          {DESKTOP_LINKS.map((l) => (
            <Link
              key={l.href}
              href={l.href}
              aria-current={pathname.startsWith(l.href) ? "page" : undefined}
            >
              {l.label}
            </Link>
          ))}
        </nav>
        <div className="header-actions">
          <ThemeToggle />
          <ShareMenu />
        </div>
      </div>
    </header>
  );
}

/** Donja traka s karticama — samo na uskom ekranu (kao u mobilnoj aplikaciji). */
export function TabBar() {
  const pathname = usePathname() ?? "/";
  return (
    <nav className="tabbar" aria-label="Glavna navigacija">
      {TABS.map((t) => {
        const active = t.match(pathname);
        return (
          <Link key={t.href} href={t.href} className="tab" aria-current={active ? "page" : undefined}>
            <Icon name={t.icon} size={22} />
            <span>{t.label}</span>
          </Link>
        );
      })}
    </nav>
  );
}
