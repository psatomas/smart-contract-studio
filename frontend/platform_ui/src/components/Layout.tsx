import type { ReactNode } from "react";

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <div className="layout">
      <header><h1>Blockchain Platform</h1></header>
      <main>{children}</main>
    </div>
  );
}