# AWS Destruction Procedure

No AWS resources exist yet (Phase 0). This document defines the structure that will be filled in as Phase 8 creates real infrastructure, and is the checklist used at project end (or after any AWS work session) to confirm nothing is left running.

## Destruction checklist (to be executed via `terraform destroy` + manual verification once populated)

- [ ] Terraform destroy run and confirmed clean (`terraform plan` shows no resources)
- [ ] EKS cluster and node groups removed
- [ ] RDS instance(s) removed (snapshot policy decided beforehand)
- [ ] S3 buckets emptied and removed (or explicitly retained with justification)
- [ ] ECR repositories removed or images pruned
- [ ] Load Balancers (ALB/NLB) removed
- [ ] IAM roles/policies created for this project removed (where not needed for teardown itself)
- [ ] CloudWatch log groups/alarms removed or retained with justification
- [ ] Security groups removed
- [ ] Orphan resource check: manually review VPC, EIPs, NAT Gateways, volumes for anything Terraform didn't track
- [ ] Final AWS Cost Explorer check confirming no unexpected ongoing spend

## Rule

Nothing is destroyed automatically. Every destructive command requires explicit confirmation before execution, and this checklist is walked through before the project (or a given cloud work session) is considered closed.
