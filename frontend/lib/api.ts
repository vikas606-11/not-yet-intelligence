const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export function getToken(): string | null {
  if (typeof window === "undefined") return null;
  return window.localStorage.getItem("access_token");
}

export function setToken(token: string) {
  window.localStorage.setItem("access_token", token);
}

export function clearToken() {
  window.localStorage.removeItem("access_token");
}

async function request(path: string, options: RequestInit = {}) {
  const token = getToken();
  const headers: Record<string, string> = {
    ...(options.headers as Record<string, string>),
  };
  if (token) headers["Authorization"] = `Bearer ${token}`;
  if (!(options.body instanceof FormData)) {
    headers["Content-Type"] = "application/json";
  }

  const res = await fetch(`${API_BASE}/api/v1${path}`, { ...options, headers });

  if (!res.ok) {
    let detail = res.statusText;
    try {
      const body = await res.json();
      detail = body.detail || detail;
    } catch {
      /* no json body */
    }
    throw new Error(typeof detail === "string" ? detail : JSON.stringify(detail));
  }

  if (res.status === 204) return null;
  return res.json();
}

export const api = {
  register: (email: string, password: string) =>
    request("/auth/register", { method: "POST", body: JSON.stringify({ email, password }) }),
  login: (email: string, password: string) =>
    request("/auth/login", { method: "POST", body: JSON.stringify({ email, password }) }),
  me: () => request("/auth/me"),

  getProfile: () => request("/profile"),
  updateProfile: (data: Record<string, unknown>) =>
    request("/profile", { method: "PUT", body: JSON.stringify(data) }),

  uploadResume: (file: File) => {
    const formData = new FormData();
    formData.append("file", file);
    return request("/resumes", { method: "POST", body: formData });
  },
  listResumes: () => request("/resumes"),
  deleteResume: (id: string) => request(`/resumes/${id}`, { method: "DELETE" }),

  createJob: (data: Record<string, unknown>) =>
    request("/jobs", { method: "POST", body: JSON.stringify(data) }),
  listJobs: () => request("/jobs"),
  saveJob: (id: string) => request(`/jobs/${id}/save`, { method: "POST" }),
  listSavedJobs: () => request("/jobs/saved"),
};
