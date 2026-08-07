# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-07

### Temporal policy and rate limits belong at the gateway

Summary: Amazon Bedrock AgentCore posts from 2026-08-06 make stateful temporal authorization and per-user or per-tool rate limits concrete gateway controls, and package Automated Reasoning policy work as Agent Skills. The portable pattern is stateful policy plus metered mediation with enforcement receipts outside the prompt.

Analysis: [daily analysis](2026-08-07/sovereignty.md#agentcore-makes-temporal-policy-and-rate-limits-first-class-gateway-controls)
Core sources: [temporal policies](https://aws.amazon.com/blogs/machine-learning/securing-ai-agents-with-temporal-policies-in-amazon-bedrock-agentcore/), [rate limits](https://aws.amazon.com/blogs/machine-learning/configure-rate-limits-for-ai-traffic-on-agentcore-gateway/), [behavior and cost controls](https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/), [policy skills](https://aws.amazon.com/blogs/machine-learning/agent-skills-for-automated-reasoning-policies-in-amazon-bedrock/)
Implementable now:
- encode stateful allow or deny rules over recent tool and principal history;
- rate-limit by user, tool, target, and model dimensions;
- separate policy authoring from enforcement receipts;
- deny by default when temporal context is missing for high-risk tools.
Tools and methodologies:
- AgentCore Gateway, temporal policy docs, gateway rate-limit configs, OAuth or IAM principal binding, OpenTelemetry spans
Implementability score: 0.84

### Skill writeback is an authority transition

Summary: When Self-Evolution Backfires shows self-distilled skills can contaminate capability past a critical pool size, and post-hoc rollback recovers little. Verifier-as-Gatekeeper admits skills only before they become executable runtime memory.

Analysis: [daily analysis](2026-08-07/sovereignty.md#skill-writeback-is-an-authority-transition-and-needs-a-pre-commit-gate)
Core source: [paper](https://arxiv.org/abs/2608.05810v1)
Implementable now:
- split draft, admitted, and revoked skill states;
- require replay or held-out verification before admission;
- block progressive disclosure of rejected skills;
- measure pool growth against task regression.
Tools and methodologies:
- skill registries, replay harnesses, held-out suites, progressive disclosure loaders
Implementability score: 0.69

### Multi-turn tool history is an untrusted authority surface

Summary: When History Lies shows structurally valid tool history can flip actions a model already knows under oracle state. On Qwen3-1.7B, polluted history flips about 32.1 percent of otherwise correct decisions.

Analysis: [daily analysis](2026-08-07/sovereignty.md#multi-turn-tool-history-is-an-untrusted-authority-surface)
Core source: [paper](https://arxiv.org/abs/2608.06057v1)
Implementable now:
- label tool-trace authority before reuse;
- evaluate polluted-history and oracle-state fixtures;
- require fresh state validation before high-impact calls that depend on history.
Tools and methodologies:
- session state ledgers, tool-trace authority labels, multi-turn fixtures
Implementability score: 0.64

## Previous Structured Update: 2026-08-06

### Side effects need certificates over retained memory worlds

Summary: SafeCommit permits external actions only when a conformal certificate shows the action is safe in every retained world. Otherwise it probes or falls back. In the authors' synthetic study, unsafe commitment falls from about 41.2 percent to about 2.6 percent.

Analysis: [daily analysis](2026-08-06/sovereignty.md#safecommit-certifies-side-effects-against-memory-uncertainty)
Core sources: [paper](https://arxiv.org/abs/2608.04289v1), [repo](https://github.com/akewarmayur/SafeCommit)
Implementability score: 0.71

### Frontier spend should wait for verified scout evidence

Summary: SuperScout refuses to route coding work from issue text alone. A smaller searcher must produce a verified handoff before frontier fixers are unlocked, matching best solo solve rate at about one fifth matched cost.

Analysis: [daily analysis](2026-08-06/sovereignty.md#superscout-makes-routing-a-governed-spend-decision-after-local-verification)
Core sources: [paper](https://arxiv.org/abs/2608.04804v1), [repo](https://github.com/TransformerOptimus/superscout)
Implementability score: 0.80

### Tool catalogs need canary audits before trust

Summary: Canary tool families test whether description text can mint unintended capability. Capability mirages and missing prerequisites remain especially important against strong models.

Analysis: [daily analysis](2026-08-06/sovereignty.md#canary-tool-catalogs-are-an-authority-plane-audit-not-just-an-eval-trick)
Core source: [paper](https://arxiv.org/abs/2608.04719v1)
Implementability score: 0.60

## Previous deep dive: 2026-08-05

### Stateful effect governance puts authority at commit

Summary: Request-time policy is stale when another agent can change the state behind the decision. Provenact's policy-state serializability binds authorization, certified policy state, and the governed effect at commit. In a 256-operation conflict test, request-local baselines produced 30 to 31 stale allows, while scoped transactional modes committed exactly the 50 valid effects with zero stale allows.

Analysis: [Deep Dive Wednesday](2026-08-05/sovereignty.md#deep-dive-wednesday-stateful-effect-governance)
Durable topic: [Stateful Effect Governance](stateful-effect-governance/stateful-effect-governance.md)
Core source: [Stateful Governance for Concurrent Agentic Systems](https://arxiv.org/abs/2608.02764v1)
Implementability score: 0.67

## Current implication

Authority should be earned at write time and re-checked at use time. Skills need admission before they load. Gateway traffic needs temporal and rate policy. Session history needs authority labels before it can decide the next effect.
