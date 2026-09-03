# Requirements

## Functional requirements (full product vision)

1. User registration & authentication
2. User profile management (experience, location, target roles, skills, education, goals, work preference, salary preference)
3. Resume upload (PDF/DOCX) and parsing into a structured profile
4. Job aggregation from multiple authorized sources
5. Job normalization into a standard schema
6. Duplicate job detection across sources
7. AI-based job analysis (role, seniority, required/preferred skills, experience, responsibilities)
8. Resume-vs-job matching with a hybrid (deterministic + AI) scoring engine
9. Explainable match output (strong/partial/missing matches, experience gap, recommendation)
10. Job prioritization (ranked, actionable list)
11. Market skill intelligence (aggregate skill demand across analyzed jobs)
12. Career action engine (skill-gap-driven learning priorities)
13. Application tracking (saved/applied/interview/rejected/offer + dashboard)
14. (Future) Browser extension for in-page job analysis

## Non-functional requirements

- **Security:** no secrets in git/images, least-privilege IAM, HTTPS, input validation, rate limiting
- **Replaceability:** AI provider must be swappable behind an internal AI service interface
- **Cost control:** local-first development; AWS resources are temporary/on-demand, never left running idle
- **Modularity:** backend starts as a modular monolith; source adapters and AI provider are pluggable
- **Auditability:** explainable outputs, not black-box scores
- **Scalability path:** architecture must support an eventual move to event-driven microservices without a rewrite

## MVP boundary (Phase 1 target)

The MVP is complete when a user can:

1. Register
2. Create a profile
3. Upload a resume
4. Enter a job description manually
5. Analyze the job (AI, Phase 2 — noted here as the MVP's logical endpoint, not built in Phase 1)
6. Receive a match score
7. See matching skills
8. See missing skills
9. Receive an explanation
10. Save the job

> Note: steps 5–9 depend on AI capability, which belongs to Phase 2. Phase 1 itself delivers steps 1–4 and 10, plus the data model and API surface that Phase 2 will build on. This is intentional — see `development-roadmap.md`.

**Explicitly out of scope for MVP:**

- Multiple job sources / scraping / adapters
- Duplicate detection
- Market intelligence
- Application tracker dashboard
- Kubernetes, Terraform, AWS, CI/CD, monitoring

## Assumptions

- Initial job domain limited to technology roles (see `product-overview.md`)
- Single-region, single-environment (local) target for MVP
- AI provider for Phase 2 is Amazon Bedrock, accessed only when that phase begins
