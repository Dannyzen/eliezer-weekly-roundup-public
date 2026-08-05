# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-05

### Stateful policy must be revalidated at commit time

Summary: Provenact binds policy state and governed effects together. In a full-conflict budget test, request-local baselines commit 79.4 to 80.8 transfers against a limit of 50, while transactional modes commit exactly 50 with zero stale allows.

Analysis: [daily analysis](2026-08-05/sovereignty.md#stateful-governance-moves-policy-enforcement-to-the-commit-boundary)
Core source: [paper](https://arxiv.org/abs/2608.02764v1)
Implementable now:
- declare policy-state scopes per effect;
- protect authorization and effect in one transaction;
- reserve and revalidate delayed approvals;
- preserve commit receipts.
Tools and methodologies:
- PostgreSQL serializable transactions, scoped reservations, Cedar, OPA, concurrency fixtures
Implementability score: 0.67

## Current implication

Request-time policy checks are advisory when shared state can change. Consequential authority belongs at the commit boundary that owns the relevant state and effect.
