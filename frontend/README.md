# Frontend — not-yet-intelligence

Next.js (App Router) + TypeScript. Phase 1 (MVP) scope: register, login, profile, resume upload, manual job input + save.

## Setup

```bash
cd frontend
npm install
cp .env.example .env.local   # set NEXT_PUBLIC_API_BASE_URL if backend isn't on localhost:8000
```

## Run

```bash
npm run dev
```

http://localhost:3000 — requires the backend running (see `../backend/README.md`).

## Build

```bash
npm run build
```

## Structure

```
app/
├── layout.tsx     shared nav + shell
├── page.tsx       home
├── register/      registration form
├── login/         login form, stores JWT
├── profile/       profile create/update
├── resume/        resume upload/list/delete
└── jobs/          manual job input, list, save
lib/api.ts         typed fetch client for backend /api/v1
```

## Notes

- Auth token stored in `localStorage` for this MVP — no refresh-token flow yet, matches Phase 1 scope (single access token, `/auth/login`).
- No design system / styling library — deliberately minimal, matches MVP boundary. Visual design is not a Phase 1 requirement.
