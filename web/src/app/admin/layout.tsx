import type { Metadata } from "next";
import "@/styles/admin.css";
import { AdminGuard } from "@/components/AdminGuard";

export const metadata: Metadata = {
  title: "Uređivanje bloga — Kur'an riječ po riječ",
  robots: { index: false, follow: false },
};

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  return <AdminGuard>{children}</AdminGuard>;
}
