"use client";

import { useEffect, useState } from "react";
import { api } from "@/lib/api";

type Job = { id: string; title: string; company?: string; description: string };

export default function JobsPage() {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [title, setTitle] = useState("");
  const [company, setCompany] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [status, setStatus] = useState<string | null>(null);

  function refresh() {
    api.listJobs().then(setJobs).catch((err) => setError(err.message));
  }

  useEffect(refresh, []);

  async function handleAdd(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    try {
      await api.createJob({ title, company, description });
      setTitle("");
      setCompany("");
      setDescription("");
      refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to add job");
    }
  }

  async function handleSave(id: string) {
    setStatus(null);
    setError(null);
    try {
      await api.saveJob(id);
      setStatus("Saved.");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to save job");
    }
  }

  return (
    <main>
      <h1>Jobs</h1>
      <h2>Add a job (manual input)</h2>
      <form onSubmit={handleAdd} style={{ display: "flex", flexDirection: "column", gap: 8, maxWidth: 480 }}>
        <input placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} required />
        <input placeholder="Company" value={company} onChange={(e) => setCompany(e.target.value)} />
        <textarea
          placeholder="Job description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          rows={6}
          required
        />
        <button type="submit">Add job</button>
      </form>
      {status && <p style={{ color: "green" }}>{status}</p>}
      {error && <p style={{ color: "crimson" }}>{error}</p>}

      <h2>All jobs</h2>
      <ul>
        {jobs.map((j) => (
          <li key={j.id} style={{ marginBottom: 12 }}>
            <strong>{j.title}</strong> {j.company && `— ${j.company}`}
            <br />
            <button onClick={() => handleSave(j.id)}>Save</button>
          </li>
        ))}
      </ul>
    </main>
  );
}
