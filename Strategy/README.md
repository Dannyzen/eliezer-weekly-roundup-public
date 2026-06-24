# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Deep Dive Wednesday, 2026-06-24

### Memory authority control plane

Summary: Persistent memory has become an authority surface. A stored memory can steer future actions, so serious agent systems need write-time origin authority, non-malleable propagation through summaries and embeddings, scoped retrieval, elevation rules, and action-time enforcement.

Deep dive: [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md)
Dated analysis: [2026-06-24 sovereignty analysis](2026-06-24/sovereignty.md#deep-dive-wednesday-memory-authority-control-plane)
Durable topics: [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [Shared-State Agents](shared-state-agents/shared-state-agents.md)
Core source: [Securing LLM-Agent Long-Term Memory Against Poisoning](https://arxiv.org/abs/2606.24322v1)
Implementation artifact: [MEM-INV-Bench / TMA-NM](https://github.com/yedidel/mem-inv-bench)

Why it won the week: Handoff logs, GUI skill coverage, and shared-memory policy are useful implementation moves. Origin-bound memory authority changes the trust model underneath all of them, because memory can carry compromised authority across sessions after the original prompt context disappears.

Implementable now:
- attach origin principal, source event, authority tier, scope, derivation, expiration, and elevation rule to durable memories
- route semantic memory search and direct memory reads through the same policy gate
- preserve authority metadata through summaries, embeddings, handoff files, and tool echoes
- test laundering through self-summarization, trusted-tool echo, manufactured corroboration, stale recall, and direct read bypass

Tools, repos, and methodologies worth exploring:
- [MEM-INV-Bench](https://github.com/yedidel/mem-inv-bench), [MEM-INV-Bench dataset](https://huggingface.co/datasets/anonymos-2321135/MEM-INV-Bench), TLA+ authority invariants, policy-as-code memory gateways, OpenTelemetry memory-authority spans, memory-laundering regression fixtures

Implementability score: 0.66

## Daily scan, 2026-06-24 supporting signals

### Origin-bound memory authority closes laundering attacks

Summary: Memory poisoning is not only a prompt problem. A hostile memory can be laundered through summarization, trusted-tool echo, or manufactured corroboration. The fix is write-time, origin-bound authority that survives summaries, embeddings, retrieval, and future action.

Analysis: [daily sovereignty analysis](2026-06-24/sovereignty.md#origin-bound-memory-authority-closes-laundering-attacks)
Durable topics: [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
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
Durable topics: [Shared-State Agents](shared-state-agents/shared-state-agents.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md)
Core source: [Governed Shared Memory](https://arxiv.org/abs/2606.24535)
Implementable now:
- enforce the same scope checks for memory search and direct object reads
- add temporal supersession and contradiction handling before prompt retrieval
- test provenance reconstruction, propagation, stale visibility, and leakage through a live API harness
Tools, repos, and methodologies worth exploring:
- scoped retrieval gateways, direct-read policy tests, supersession graphs, writer identity fields, ArgusFleet-style memory governance probes, OpenTelemetry memory spans
Implementability score: 0.72
