# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-06

### Side effects need certificates over retained memory worlds

Summary: SafeCommit permits external actions only when a conformal certificate shows the action is safe in every retained world. Otherwise it probes or falls back. In the authors' synthetic study, unsafe commitment falls from about 41.2 percent to about 2.6 percent.

Analysis: [daily analysis](2026-08-06/sovereignty.md#safecommit-certifies-side-effects-against-memory-uncertainty)
Core sources: [paper](https://arxiv.org/abs/2608.04289v1), [repo](https://github.com/akewarmayur/SafeCommit)
Implementable now:
- build candidate-world sets before high-impact actions;
- require certificates over retained worlds;
- prefer targeted probes over generic confirmation prompts.
Tools and methodologies:
- conformal risk control, probe planners, commit or fallback controllers, provenance ledgers
Implementability score: 0.71

### Frontier spend should wait for verified scout evidence

Summary: SuperScout refuses to route coding work from issue text alone. A smaller searcher must produce a verified handoff before frontier fixers are unlocked, matching best solo solve rate at about one fifth matched cost.

Analysis: [daily analysis](2026-08-06/sovereignty.md#superscout-makes-routing-a-governed-spend-decision-after-local-verification)
Core sources: [paper](https://arxiv.org/abs/2608.04804v1), [repo](https://github.com/TransformerOptimus/superscout)
Implementable now:
- separate scout authority from fixer authority;
- strip failed reproduction claims before dispatch;
- deny spend below verified-claim thresholds.
Tools and methodologies:
- scout or fix lanes, verify-then-strip gates, frozen routers, budget-tier policies
Implementability score: 0.80

### Tool catalogs need canary audits before trust

Summary: Canary tool families test whether description text can mint unintended capability. Capability mirages and missing prerequisites remain especially important against strong models.

Analysis: [daily analysis](2026-08-06/sovereignty.md#canary-tool-catalogs-are-an-authority-plane-audit-not-just-an-eval-trick)
Core source: [paper](https://arxiv.org/abs/2608.04719v1)
Implementable now:
- keep shadow canaries beside high-risk tools;
- score selection susceptibility separately from task success;
- move prerequisite checks outside model-visible prose.
Tools and methodologies:
- MCP or gateway catalog audits, schema-derived decoys, description linting
Implementability score: 0.60

## Previous deep dive: 2026-08-05

### Stateful effect governance puts authority at commit

Summary: Request-time policy is stale when another agent can change the state behind the decision. Provenact's policy-state serializability binds authorization, certified policy state, and the governed effect at commit. In a 256-operation conflict test, request-local baselines produced 30 to 31 stale allows, while scoped transactional modes committed exactly the 50 valid effects with zero stale allows.

Analysis: [Deep Dive Wednesday](2026-08-05/sovereignty.md#deep-dive-wednesday-stateful-effect-governance)
Durable topic: [Stateful Effect Governance](stateful-effect-governance/stateful-effect-governance.md)
Core source: [Stateful Governance for Concurrent Agentic Systems](https://arxiv.org/abs/2608.02764v1)
Implementability score: 0.67

## Current implication

Authority should narrow while uncertainty remains. Unresolved memory worlds block commitment. Tool descriptions cannot invent prerequisites. Expensive backends should wait for verified local evidence. Commit-time policy still owns concurrent shared state.
