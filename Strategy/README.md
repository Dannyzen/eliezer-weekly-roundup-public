# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-24

### Origin-bound memory authority closes laundering attacks

Summary: Memory poisoning is not only a prompt problem. A hostile memory can be laundered through summarization, trusted-tool echo, or manufactured corroboration. The fix is write-time, origin-bound authority that survives summaries, embeddings, retrieval, and future action.

Analysis: [daily sovereignty analysis](2026-06-24/sovereignty.md#origin-bound-memory-authority-closes-laundering-attacks)
Durable topics: [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core source: [Securing LLM-Agent Long-Term Memory Against Poisoning](https://arxiv.org/abs/2606.24322)
Implementable now:
- attach origin principal, source event, authority tier, scope, and elevation rule to durable memories
- block memory records from authorizing actions outside their declared scope
- test laundering through summarization, tool echo, and repeated corroboration
Tools, repos, and methodologies worth exploring:
- memory authority schemas, policy-as-code, source-event IDs, elevation gates, TLA+-style threat modeling, memory-laundering regression fixtures
Implementability score: 0.66

### Governed shared memory makes fleet memory a policy service

Summary: Governed Shared Memory frames multi-agent memory as a policy service with scoped retrieval, temporal supersession, provenance tracking, and policy-governed propagation. Its MemClaw and ArgusFleet live-service evaluation found real enforcement and pipeline-ordering failures.

Analysis: [daily sovereignty analysis](2026-06-24/sovereignty.md#governed-shared-memory-makes-fleet-memory-a-policy-service)
Durable topics: [Shared-State Agents](shared-state-agents/shared-state-agents.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Governed Shared Memory](https://arxiv.org/abs/2606.24535)
Implementable now:
- enforce the same scope checks for memory search and direct object reads
- add temporal supersession and contradiction handling before prompt retrieval
- test provenance reconstruction, propagation, stale visibility, and leakage through a live API harness
Tools, repos, and methodologies worth exploring:
- scoped retrieval gateways, direct-read policy tests, supersession graphs, writer identity fields, ArgusFleet-style memory governance probes, OpenTelemetry memory spans
Implementability score: 0.72
