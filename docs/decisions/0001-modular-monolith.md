# ADR 0001: Start as a Modular Monolith

## Status

Accepted

## Context

The full product vision includes separate User, Job, Resume, Matching, AI, and Notification services. Building microservices from day one adds operational complexity (service discovery, distributed transactions, multiple deployments, network overhead) before there's a real scaling or team-boundary reason for it.

## Decision

Phase 1–4 backend is a single FastAPI application organized into clearly separated internal modules: `authentication`, `users`, `profiles`, `resumes`, `jobs`, `matching`, `ai`, `applications`. Each module owns its own routes, schemas, and service logic, and does not reach into another module's internals directly.

## Consequences

- Faster to build and deploy in early phases; one process, one deployment
- Module boundaries are enforced by convention/code organization now, so extraction later is a refactor, not a rewrite
- Microservice split only happens when there's a concrete reason (independent scaling need, team ownership split, or a module — e.g. AI — needing a different deployment cadence/resources)
- The AI module in particular is designed as a swappable internal service from the start (see `architecture.md`), even while it lives inside the monolith
