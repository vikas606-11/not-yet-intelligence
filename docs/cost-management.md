# Cost Management

AWS credits are limited and must not be consumed unnecessarily.

## Principle

Develop locally by default. Touch AWS only when the current phase specifically requires it.

```
Local PC → Docker → Local PostgreSQL → Local Kubernetes (Kind/Minikube)
```

AWS is used for: Bedrock (Phase 2, pay-per-call, low ongoing cost), S3/ECR/RDS/EKS (Phase 8 only).

## Before creating any AWS resource

1. Explain what will be created
2. Explain why it's required for the current phase
3. Estimate likely cost
4. State how to monitor cost (CloudWatch billing alarms / Cost Explorer)
5. State how to destroy it
6. Avoid always-on resources unless justified

## Rules

- No EKS cluster, RDS instance, or NAT Gateway running idle between work sessions
- Prefer on-demand / destroy-after-use for anything with hourly cost (EKS, RDS, NAT Gateway, ALB)
- Bedrock usage stays pay-per-call — no provisioned throughput unless explicitly needed and approved
- Set a billing alarm before Phase 8 begins

## Teardown

See `docs/aws-destruction.md`. No AWS resource is left running "just in case" once a work session or phase concludes.
