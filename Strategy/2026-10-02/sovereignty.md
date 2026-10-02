# Daily Strategy Research: 2026-10-02

## Enforce provenance and authority at the final tool boundary

PACE argues that admission-time checks cannot contain a tool-using agent once retrieved pages, memory, skill text, and tool metadata jointly influence a call. Its control point is immediately before execution: trace represented influence paths, compile authority from the authenticated request, then verify the concrete tool effect against that authority.

Across eight executable security benchmarks and three model families, the evaluated configuration had the lowest attack success in 62 of 79 eligible attack columns and tied in 14. Native utility fell by at most three points. A 1,167-pair ablation attributed most security improvement to effect verification, and a reduced adaptive search succeeded on 0 of 30 out-of-authority targets.

### Why it matters

Trusted retrieval and approved tools do not make the final action authorized. A safe artifact and a leaking artifact can produce the same admission evidence. The system therefore needs a deterministic execution gate that sees authenticated principal, provenance, exact tool identity, typed arguments, target, and effect class at once.

### Fit in the strategy stack

PACE belongs in the gateway and context-to-execution control planes. Retrieval and ranking may propose an action. Only the final capability gate can release it. This separates evidence influence from authority and makes the realized effect the governed object.

### Practical methods worth exploring

- provenance labels for pages, memories, skills, tool metadata, and tool returns
- exact tool identity plus schema-defined effect classes
- capability manifests compiled from authenticated request scope
- path-confinement checks before dispatch
- refusal controls and declared repairs that preserve the certified boundary
- adversarial fixtures for prompt injection, poisoned tools, memory attacks, and cross-tool chains
- utility and blocked-effect reporting beside attack success

Artifact status: the paper says source code is included in its supplemental material. No paper-owned public repository was resolved, and external source code was not downloaded or executed in this cron.

Evidence caveat: the adaptive search has 30 out-of-authority targets, and the evaluated configuration can restore authorized calls after a proposed block. Production use needs independent tests of the repair path, false denials, concurrency, and effect receipts.

Implementability score: 0.54

Core source: [PACE: Provenance-Aware Capability Enforcement for Tool-Using LLM Agents](https://arxiv.org/abs/2610.01349v1)

## Working conclusion

Admission is an inventory control. Authorization is a use-time decision over the exact effect. Keep the final release gate outside model reasoning and bind it to authenticated scope, represented provenance, concrete arguments, and a verified outcome.
