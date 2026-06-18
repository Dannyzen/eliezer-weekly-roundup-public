# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-18

### Tool gates need contract integrity, not only hidden tools

Summary: ContractGuard shows that risk-aware tool gating moves the trust assumption into the tool contract layer. If declared effects can be forged, a dangerous tool can be routed into scope without persuading the agent. Tool manifests are now authority-bearing runtime artifacts.

Analysis: [daily reasoning analysis](2026-06-18/reasoning.md#tool-gates-need-contract-integrity-not-only-hidden-tools)
Durable topics: [Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core sources: [ContractGuard](https://arxiv.org/abs/2606.18550v1), [Runtime Compliance Verification for AI Agents](https://arxiv.org/abs/2606.19242v1)
Implementable now:
- sign tool manifests and store manifest hashes in every run trace
- validate declared effects against actual state writes before later gates read that state
- express tool policies over principal, scope, purpose, data class, and effects
- fuzz corrupted effects, scopes, and authorization fields, not only prompt text
Tools, repos, and methodologies worth exploring:
- OPA, Cedar, Sigstore, MCP gateway wrappers, pre/post state diffs, contract mutation tests
Implementability score: 0.76

### Shared memory needs governance scores, not only recall

Summary: GateMem evaluates multi-principal memory agents on utility, access-control violations, and active-forgetting failures. That is the right deployment frame for institutional assistants: a memory system that leaks across roles or reconstructs deleted data is not safe just because it recalls well.

Analysis: [daily reasoning analysis](2026-06-18/reasoning.md#shared-memory-needs-governance-scores-not-only-recall)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Shared-State Agents](../Strategy/shared-state-agents/shared-state-agents.md)
Core sources: [GateMem paper](https://arxiv.org/abs/2606.18829v1), [GateMem repository](https://github.com/rzhub/GateMem)
Implementable now:
- score utility, unauthorized leakage, and deleted-info reconstruction together
- tag memories by principal, role, scope, relationship, source event, and deletion state
- test long-context, naive RAG, policy-aware RAG, and external memory under the same checkpoints
- log memory read paths and policy verdicts before memories reach the model
Tools, repos, and methodologies worth exploring:
- GateMem, OpenFGA-style relationship graphs, deletion tombstones, policy-aware retrieval filters, memory replay tests
Implementability score: 0.71

### Grounding and web-agent verification need explicit evidence paths

Summary: Decoupled Search Grounding moves retrieval outside the model provider through an MCP-compatible gateway, while HANSEL extracts interactive breadcrumbs from web-agent trajectories. Search route, source rendering, cache behavior, page state, and final-claim linkage should be visible control-plane fields.

Analysis: [daily reasoning analysis](2026-06-18/reasoning.md#grounding-and-web-agent-verification-need-explicit-evidence-paths)
Durable topics: [Agentic Search and Retrieval](agentic-search/agentic-search.md), [Evidence Provenance Control Plane](../Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core sources: [Decoupled Search Grounding](https://arxiv.org/abs/2606.18947v1), [HANSEL](https://arxiv.org/abs/2606.18671v1)
Implementable now:
- route search through an explicit gateway instead of relying only on native model search
- record provider, retrieval depth, cache hit, selected sources, rendered context, and fallback path
- extract browser breadcrumbs with page, snippet, state snapshot, and final claim linkage
- fail strict-output tasks when grounding introduces uncontrolled verbosity
Tools, repos, and methodologies worth exploring:
- MCP-compatible search gateway wrappers, exact plus semantic caching, browser state snapshots, DOM snippets, claim-to-breadcrumb trace viewers
Implementability score: 0.84

## Previous structured update: Daily scan, 2026-06-17

### MCP factuality needs source ownership, not pooled support

Summary: ProvenanceGuard catches a failure mode that normal source-grounded scoring misses: a claim can be supported somewhere in pooled evidence while being attributed to the wrong source. MCP agents need stable tool IDs, source IDs, raw outputs, claim routing, and per-claim source verdicts.

Analysis: [daily reasoning analysis](2026-06-17/reasoning.md#mcp-factuality-needs-source-ownership-not-pooled-support)
Core sources: [ProvenanceGuard](https://arxiv.org/abs/2606.18037v1), [Zscaler agentic AI security platform](https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai)
Implementability score: 0.74

### Skill systems need compositional routing plus per-skill utility evals

Summary: SkillWeaver treats skill use as decompose, retrieve, and compose, not one-shot semantic lookup. The agentic skills evaluation framework supplies the missing promotion gate: test individual skills against realistic skill-derived tasks, rubrics, and no-skill baselines before they become default runtime authority.

Analysis: [daily reasoning analysis](2026-06-17/reasoning.md#skill-systems-need-compositional-routing-plus-per-skill-utility-evals)
Core sources: [Compositional Skill Routing](https://arxiv.org/abs/2606.18051v1), [A Framework for Evaluating Agentic Skills at Scale](https://arxiv.org/abs/2606.17819v1)
Implementability score: 0.76

### Evaluation needs trajectory preferences and oracle-aware test gates

Summary: Offline trajectory preferences reduce tied agent comparisons by using partial progress and time-to-return profiles, while All Smoke, No Alarm shows that most agent-authored test patches have weak or no explicit oracle signals.

Analysis: [daily reasoning analysis](2026-06-17/reasoning.md#evaluation-needs-trajectory-preferences-and-oracle-aware-test-gates)
Core sources: [Offline Preference-Based Trajectory Evaluation](https://arxiv.org/abs/2606.17541v1), [All Smoke, No Alarm](https://arxiv.org/abs/2606.18168v1)
Implementability score: 0.86
