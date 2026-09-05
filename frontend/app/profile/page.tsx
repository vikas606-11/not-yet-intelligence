"use client";

import { useEffect, useState } from "react";
import { api } from "@/lib/api";

type Profile = {
  name?: string;
  experience_years?: number;
  location?: string;
  skills?: string[];
  education?: string;
  career_goals?: string;
  work_preference?: string;
  salary_preference?: string;
};

export default function ProfilePage() {
  const [profile, setProfile] = useState<Profile>({});
  const [skillsInput, setSkillsInput] = useState("");
  const [status, setStatus] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api
      .getProfile()
      .then((p) => {
        if (p) {
          setProfile(p);
          setSkillsInput((p.skills || []).join(", "));
        }
      })
      .catch((err) => setError(err.message));
  }, []);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setStatus(null);
    try {
      const skills = skillsInput
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean);
      const updated = await api.updateProfile({ ...profile, skills });
      setProfile(updated);
      setStatus("Saved.");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to save profile");
    }
  }

  return (
    <main>
      <h1>Profile</h1>
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 8, maxWidth: 400 }}>
        <input
          placeholder="Name"
          value={profile.name || ""}
          onChange={(e) => setProfile({ ...profile, name: e.target.value })}
        />
        <input
          type="number"
          placeholder="Experience (years)"
          value={profile.experience_years ?? ""}
          onChange={(e) => setProfile({ ...profile, experience_years: Number(e.target.value) })}
        />
        <input
          placeholder="Location"
          value={profile.location || ""}
          onChange={(e) => setProfile({ ...profile, location: e.target.value })}
        />
        <input placeholder="Skills (comma-separated)" value={skillsInput} onChange={(e) => setSkillsInput(e.target.value)} />
        <input
          placeholder="Education"
          value={profile.education || ""}
          onChange={(e) => setProfile({ ...profile, education: e.target.value })}
        />
        <input
          placeholder="Career goals"
          value={profile.career_goals || ""}
          onChange={(e) => setProfile({ ...profile, career_goals: e.target.value })}
        />
        <button type="submit">Save profile</button>
      </form>
      {status && <p style={{ color: "green" }}>{status}</p>}
      {error && <p style={{ color: "crimson" }}>{error}</p>}
    </main>
  );
}
