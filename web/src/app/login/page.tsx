import type { Metadata } from "next";
import "@/styles/admin.css";
import { LoginForm } from "@/components/LoginForm";

export const metadata: Metadata = {
  title: "Prijava — Kur'an riječ po riječ",
  robots: { index: false, follow: false },
};

export default function LoginPage() {
  return <LoginForm />;
}
