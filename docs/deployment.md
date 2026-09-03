# Deployment

## Current state (Phase 0)

No deployment yet. This document will be filled in incrementally as each relevant phase is built — not written in full now, to avoid documenting infrastructure that doesn't exist yet.

## Planned deployment stages

| Phase | Deployment target |
|---|---|
| 1 (MVP) | Local processes: `next dev`, `uvicorn`, local Postgres |
| 5 | Docker Compose (frontend, backend, Postgres, Redis) |
| 6 | Local Kubernetes (Kind/Minikube) via Helm |
| 7 | GitHub Actions CI → image push → ArgoCD sync |
| 8 | AWS: EKS, RDS, S3, ECR, ALB, via Terraform-provisioned infra |

## Local development setup (Phase 1 target)

To be documented once Phase 1 scaffolding exists (backend `.env`, `alembic upgrade`, frontend `npm run dev`, etc.). Placeholder — will be updated in the Phase 1 implementation task, not now.
