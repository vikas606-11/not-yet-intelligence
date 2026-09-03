# Development Roadmap

Principle: `REAL PROBLEM → PRODUCT → APPLICATION → AI → CLOUD → DEVOPS → SCALE`

Each phase must be fully complete (implementation, tests, docs, security review, proof, git tag) before the next begins. See `PROJECT_STATUS.md` for current phase.

| Phase | Name | Key deliverables |
|---|---|---|
| 0 | Planning & Documentation | Requirements, architecture, DB/API design, repo, this roadmap |
| 1 | MVP | Next.js + FastAPI + Postgres, register, profile, resume upload, manual job input |
| 2 | AI | Bedrock integration, job analysis, resume analysis, match score, explanation |
| 3 | Job Intelligence | Multi-source ingestion, normalization, dedup, ranking, skill gap, market intel |
| 4 | Application Management | Save/apply/interview/reject/offer tracking, dashboard, notifications |
| 5 | Containerization | Dockerfiles, Docker Compose |
| 6 | Kubernetes | Kind/Minikube, manifests, Helm (local) |
| 7 | GitOps | GitHub Actions CI, ArgoCD |
| 8 | AWS | Terraform: VPC, IAM, ECR, RDS, S3, EKS, SQS, ALB, CloudWatch |
| 9 | Observability | Prometheus, Grafana, Loki/CloudWatch, alerts |
| 10 | Production Hardening | Security review, autoscaling, retries, DR, perf testing, cost optimization |

Tags: `v0.1-phase-0`, `v0.2-mvp`, `v0.3-ai`, `v0.4-job-intelligence`, ... one per completed phase.

Full feature-level detail per phase is in the project specification; this file is the concise, living reference.
