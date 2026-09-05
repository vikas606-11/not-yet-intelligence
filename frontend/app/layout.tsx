import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "not-yet-intelligence",
  description: "AI-powered career intelligence engine",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ fontFamily: "system-ui, sans-serif", maxWidth: 640, margin: "0 auto", padding: 24 }}>
        <nav style={{ display: "flex", gap: 16, marginBottom: 24 }}>
          <Link href="/">Home</Link>
          <Link href="/register">Register</Link>
          <Link href="/login">Login</Link>
          <Link href="/profile">Profile</Link>
          <Link href="/resume">Resume</Link>
          <Link href="/jobs">Jobs</Link>
        </nav>
        {children}
      </body>
    </html>
  );
}
