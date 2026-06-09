# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-09

### Artifact provenance gaps are now an agent attack surface
Summary: Tool-using agents persist files, logs, memories, summaries, plans, and other artifacts that later steps may treat as neutral context. If the runtime does not preserve artifact lineage, cross-context jailbreak fragments can become dangerous only when recomposed by the workflow.

Analysis: [daily sovereignty analysis](2026-06-09/sovereignty.md#artifact-provenance-gaps-are-now-an-agent-attack-surface)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Context-Fractured Decomposition Attacks](https://arxiv.org/abs/2606.09084v1)
Implementable now:
- attach origin, author, tool, session, task, trust level, and transformation lineage to durable artifacts;
- keep user data, tool outputs, generated plans, memories, scripts, and logs in separate trust classes;
- propagate taint labels into later reads, summaries, code/config generation, and privileged tool arguments.
Tools, repos, and methodologies worth exploring:
- provenance graphs, artifact taint, trace-linked artifact reads/writes, trust-class validators, policy gates before artifact-to-instruction promotion, cross-step attack fixtures
Implementability score: 0.72

## Previous structured update

The prior daily scan for 2026-06-08 focused on malicious skill supply-chain admission and cross-step sabotage evidence accumulation: [2026-06-08 roundup](../roundups/2026-06-08.md).
