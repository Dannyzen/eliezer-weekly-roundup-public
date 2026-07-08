# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-08

### MCP approval dialogs need byte-level fidelity checks

Summary: Unicode TAG-block concealment exposes a gateway failure where the approval view and model-visible tool metadata can diverge. Approval only means something if the user approves the same canonical bytes the model later receives.

Analysis: [daily sovereignty analysis](2026-07-08/sovereignty.md#mcp-approval-dialogs-need-byte-level-fidelity-checks)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Unicode TAG-Block Concealment of Tool-Metadata Payloads in MCP](https://arxiv.org/abs/2607.05744v1)
Implementable now:
- scan MCP tool metadata for invisible Unicode, TAG-block payloads, bidi controls, zero-width characters, and control bytes
- compare raw bytes, canonical text, rendered approval text, and model-context text
- hash approved metadata and require re-approval on drift
- treat tool descriptions as untrusted evidence, not authority
Tools, repos, and methodologies worth exploring:
- Unicode category scanners, MCP admission fixtures, metadata hashing, approval-view diffing, tool-description taint labels
Implementability score: 0.86

### Context-to-Execution Integrity turns writable context into typed releases

Summary: CXI separates writable context from protected execution sinks. Context can provide evidence, but protected tool fields need typed releases, opaque data slots, destination binding, and deterministic admission gates before side effects happen.

Analysis: [daily sovereignty analysis](2026-07-08/sovereignty.md#context-to-execution-integrity-turns-writable-context-into-typed-releases)
Durable topics: [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core source: [Context-to-Execution Integrity for LLM Agents](https://arxiv.org/abs/2607.06000v1)
Implementable now:
- mark protected sink fields on privileged tools
- keep untrusted values in opaque slots until validators release them
- bind releases to destination, principal, task, and expiry
- emit allow and deny traces for release decisions
Tools, repos, and methodologies worth exploring:
- protected-field schemas, typed release validators, OPA or Cedar policy, evidence-object IDs, release-gate regression fixtures
Implementability score: 0.68

## Supporting recent Strategy context

The 2026-07-01 Deep Dive established that connection is not authority. The 2026-07-07 scan showed observation is not authority. The 2026-07-08 scan adds representation fidelity: approval views and writable context must not silently become execution authority.
