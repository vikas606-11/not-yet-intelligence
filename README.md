# not-yet-intelligence

An AI-powered career intelligence engine that turns resumes, job requirements, and market signals into actionable career decisions.

## What this is

`not-yet-intelligence` is an intelligence layer above job platforms (LinkedIn, Naukri, Indeed, company career pages) — not a replacement for them. It collects authorized/public job opportunities, normalizes and deduplicates them, analyzes them with AI, and helps a candidate understand:

- Which jobs are relevant to them
- Why a job is a good or poor match
- What skills they are missing
- Which jobs to prioritize
- What the market currently demands
- What to do next

Core idea: **Don't just find jobs. Understand which opportunities are worth applying to.**

## Status

See [`PROJECT_STATUS.md`](./PROJECT_STATUS.md) for current phase and progress.

## Documentation

| Doc | Purpose |
|---|---|
| [`docs/product-overview.md`](./docs/product-overview.md) | Problem, solution, users |
| [`docs/requirements.md`](./docs/requirements.md) | Requirements & MVP boundary |
| [`docs/architecture.md`](./docs/architecture.md) | System architecture |
| [`docs/database.md`](./docs/database.md) | Database design |
| [`docs/api.md`](./docs/api.md) | API design |
| [`docs/development-roadmap.md`](./docs/development-roadmap.md) | Phased roadmap |
| [`docs/security.md`](./docs/security.md) | Security baseline |
| [`docs/testing.md`](./docs/testing.md) | Testing strategy |
| [`docs/cost-management.md`](./docs/cost-management.md) | AWS cost strategy |
| [`docs/deployment.md`](./docs/deployment.md) | Local & cloud deployment |
| [`docs/aws-destruction.md`](./docs/aws-destruction.md) | Cloud teardown procedure |
| [`docs/future-work.md`](./docs/future-work.md) | Deferred items |
| [`docs/decisions/`](./docs/decisions/) | Architecture decision records |

## Engineering principle

```
REAL PROBLEM → PRODUCT → APPLICATION → AI → CLOUD → DEVOPS → SCALE
```

Technologies exist to support the product. Never the other way around.

## Tech stack (planned)

- **Frontend:** Next.js, TypeScript
- **Backend:** Python, FastAPI (modular monolith)
- **Database:** PostgreSQL, Redis
- **AI:** Amazon Bedrock, isolated behind an internal AI service
- **Cloud/DevOps (later phases):** Docker, Kubernetes, Helm, ArgoCD, Terraform, AWS

## License

TBD.
