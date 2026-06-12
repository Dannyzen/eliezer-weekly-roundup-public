# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-12

### Privacy is a trajectory budget, not an output filter
Summary: OCELOT reframes agent privacy as cumulative posterior-risk control. The question is not whether one output contains a secret. It is how much a sink or colluding sinks can infer after a whole trajectory of observations, tool calls, and releases.

Analysis: [daily sovereignty analysis](2026-06-12/sovereignty.md#privacy-is-a-trajectory-budget-not-an-output-filter)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [OCELOT](https://arxiv.org/abs/2606.12341v1)
Implementable now:
- keep per-sink release ledgers;
- add release, redact, coarsen, defer, ask, and keep-local variants;
- charge disclosure decisions against trace-linked privacy budgets.
Tools, repos, and methodologies worth exploring:
- deterministic declassification checks, release ledgers, append-only disclosure records, cumulative-inference fixtures
Implementability score: 0.57

### Graph memory selection is a write-path security boundary
Summary: Selection Integrity shows that graph memory can be poisoned through structure rather than retrieved content. Final citations may all be authenticated while untrusted edges or merges influenced which facts were selected.

Analysis: [daily sovereignty analysis](2026-06-12/sovereignty.md#graph-memory-selection-is-a-write-path-security-boundary)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [Selection Integrity for LLM Graph Memory](https://arxiv.org/abs/2606.12290v1)
Implementable now:
- label graph edges and selection features by writer principal and trust tier;
- log graph-selection paths, not only final retrieved facts;
- prevent untrusted structure from steering authorization, policy, memory promotion, or external-send decisions.
Tools, repos, and methodologies worth exploring:
- graph provenance, taint-aware selection, policy-gated memory writes, poisoned-edge regression fixtures
Implementability score: 0.61

### Persistent cloud agents make stateful governance unavoidable
Summary: OpenAI's Ona acquisition announcement is market signal that coding agents are moving into secure, customer-controlled, persistent cloud environments for long-running work. That makes runtime state, checkpoint policy, and customer-visible evidence strategic boundaries.

Analysis: [daily sovereignty analysis](2026-06-12/sovereignty.md#persistent-cloud-agents-make-stateful-governance-unavoidable)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [OpenAI to acquire Ona](https://openai.com/index/openai-to-acquire-ona)
Implementable now:
- bind owner, tenant, project, model, policy, and checkpoint metadata to persistent workspaces;
- implement pause, resume, revoke, and handoff semantics;
- export customer-controlled traces and artifacts.
Tools, repos, and methodologies worth exploring:
- cloud/local parity tests, scoped credentials, workspace lineage, checkpoint audit, long-running task budgets
Implementability score: 0.66

## Previous structured update

The prior daily scan for 2026-06-11 focused on five-plane runtime governance and runtime evidence surfaces: [2026-06-11 roundup](../roundups/2026-06-11.md).
