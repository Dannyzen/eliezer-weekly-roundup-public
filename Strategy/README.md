# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-29

### Purpose-bound privacy makes tool arguments part of the security boundary

Summary: ToolPrivacyBench shows that task success and privacy success are different metrics. An agent can complete a workflow while over-disclosing private fields through intermediate tool arguments or backend writes. Privacy has to be audited across the trajectory.

Analysis: [daily sovereignty analysis](2026-06-29/sovereignty.md#purpose-bound-privacy-makes-tool-arguments-part-of-the-security-boundary)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core source: [ToolPrivacyBench](https://arxiv.org/abs/2606.28061v1)
Implementable now:
- label sensitive fields as task-private atoms
- define authorized tools and sinks per workflow purpose
- record field-level disclosure in tool arguments and backend audit logs
- score task completion separately from privacy over-disclosure
Tools, repos, and methodologies worth exploring:
- policy knowledge bases, mock backends, OPA or Cedar, ABAC, OpenTelemetry spans, field-level privacy regression tests
Implementability score: 0.78

### Prompt injection is a control-data separation problem

Summary: The prompt-injection impossibility argument says shared-embedding architectures without enforced control-data separation cannot provide perfect protection for control-authoritative actions. Tool authorization, policy routing, refusal decisions, and memory writes need external enforcement.

Analysis: [daily sovereignty analysis](2026-06-29/sovereignty.md#prompt-injection-is-a-control-data-separation-problem-not-a-better-prompt-problem)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md)
Core source: [On the Inseparability of Instructions and Data](https://arxiv.org/abs/2606.27567v1)
Implementable now:
- preserve immutable provenance labels for untrusted content and tool output
- route authority-bearing actions through policy outside the model
- block untrusted content from directly authorizing memory writes or tool grants
- test prompt injection as a control-plane bypass attempt
Tools, repos, and methodologies worth exploring:
- reference monitors, taint tracking, capability handles, policy brokers, memory-write gates, typed provenance traces
Implementability score: 0.44

## Supporting recent Strategy context

The 2026-06-26 weekly synthesis remains the broad current governance map: [weekly sovereignty analysis](2026-06-26/sovereignty.md). The 2026-06-28 daily scan focused on runtime monitors and adaptive gateway tests. The new 2026-06-29 scan says the same boundary has to cover field-level privacy and control-data separation.
