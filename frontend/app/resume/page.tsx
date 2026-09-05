"use client";

import { useEffect, useState } from "react";
import { api } from "@/lib/api";

type Resume = { id: string; file_type: string; uploaded_at: string };

export default function ResumePage() {
  const [resumes, setResumes] = useState<Resume[]>([]);
  const [error, setError] = useState<string | null>(null);

  function refresh() {
    api.listResumes().then(setResumes).catch((err) => setError(err.message));
  }

  useEffect(refresh, []);

  async function handleUpload(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    setError(null);
    try {
      await api.uploadResume(file);
      refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Upload failed");
    }
    e.target.value = "";
  }

  async function handleDelete(id: string) {
    try {
      await api.deleteResume(id);
      refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Delete failed");
    }
  }

  return (
    <main>
      <h1>Resume</h1>
      <input type="file" accept=".pdf,.docx" onChange={handleUpload} />
      {error && <p style={{ color: "crimson" }}>{error}</p>}
      <ul>
        {resumes.map((r) => (
          <li key={r.id}>
            {r.file_type.toUpperCase()} — uploaded {new Date(r.uploaded_at).toLocaleString()}{" "}
            <button onClick={() => handleDelete(r.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </main>
  );
}
