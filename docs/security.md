# Security Baseline

## Never

- Commit credentials, API keys, AWS access keys
- Hardcode secrets in source or Docker images
- Expose database credentials
- Disable security controls for developer convenience

## Always

- Secrets via `.env` locally (never committed — see `.gitignore`), AWS Secrets Manager / Kubernetes Secrets in deployed environments
- `.env.example` kept in sync with required variables, no real values
- Passwords hashed (bcrypt/argon2), never stored plaintext
- JWT-based auth with expiry; refresh flow for long sessions
- Input validation on every endpoint (Pydantic models)
- Rate limiting on auth endpoints at minimum (added when infra supports it — Redis, Phase 2+)
- HTTPS enforced in any non-local environment
- Least-privilege IAM policies when AWS resources are created (Phase 8)
- File upload validation: type/size checks on resume uploads (PDF/DOCX only, size cap)

## Scanning (introduced when relevant phase begins)

- **Trivy** — container image scanning (Phase 5+)
- **SonarQube** — static analysis (introduced in CI, Phase 7)
- Dependency scanning via GitHub Actions (Phase 7)

## Phase-specific notes

- **Phase 1 (MVP):** auth, input validation, hashed passwords, `.env`-based config, S3 (or local disk in dev) for resume files with type/size validation
- **Phase 8 (AWS):** IAM least privilege, Secrets Manager, security groups, no public RDS
- **Phase 10:** full security review before considering the project production-hardened
