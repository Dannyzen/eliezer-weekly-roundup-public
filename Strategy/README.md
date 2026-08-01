# Strategy

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-01

### A governed router needs both receipts and a hard budget boundary

Summary: Vercel AI Gateway now exposes request-level routing logs and enforceable budgets at team, project, and API-key scopes. The logs show every provider attempt, cost, token breakdown, latency, region, and retention controls. The budgets can stop requests when any applicable scope is exhausted.

Analysis: [daily sovereignty](2026-08-01/sovereignty.md#vercel-turns-model-routing-into-a-budgeted-inspectable-gateway)
Core sources: [AI Gateway Logs](https://vercel.com/changelog/ai-gateway-logs), [AI Gateway Budgets](https://vercel.com/changelog/ai-gateway-spend-budgets-and-alerts)
Implementable now:
- bind requests to team, project, key, run, policy, and fallback budget;
- export receipts for independent retention;
- test retry, cache, fallback, and BYOK accounting;
- verify region and retention policy per provider attempt.
Tools, repositories, and methodologies:
- Vercel AI Gateway, budgets CLI, OpenTelemetry, budget-bypass fixtures
Implementability score: 0.92

### Model access policy is moving toward user and role scope

Summary: GitHub's Enterprise Teams preview allows an enterprise baseline plus team grants for Optional models. This is a meaningful move from organization-level settings toward identity-aware model governance, but its least-restrictive union semantics can still overgrant access.

Analysis: [daily sovereignty](2026-08-01/sovereignty.md#github-moves-model-access-from-organization-settings-to-team-policy)
Core source: [GitHub changelog](https://github.blog/changelog/2026-07-31-enterprise-teams-model-policy-targeting-in-public-preview)
Implementable now:
- grant experimental models through explicit teams;
- attach data class, budget, training, expiry, and review;
- diff effective user permissions before migration;
- preserve a rollback snapshot.
Tools, repositories, and methodologies:
- GitHub Enterprise Teams, model-access manifests, permission diffing, expiry reviews
Implementability score: 0.68

## Current implication

Put routing evidence, spend enforcement, and model access at operator-owned boundaries. A model selector is not governance unless effective access and every fallback attempt are inspectable and budgeted.
