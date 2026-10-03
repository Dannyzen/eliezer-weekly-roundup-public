# Strategy Weekly Sovereignty: 2026-10-02

The week’s strategic lesson is that evidence, approval, and identity are inputs to authority, not substitutes for it. A sovereign agent stack binds authorization to the complete effect path, checks provenance and capability at the last responsible moment, and treats persistent memory as a scoped authority object.

## Bind approval to the transitive effect closure

Agent Approval Laundering identifies the gap between the invocation a human approves and the downstream effects that actually execute through package hooks, generated files, network calls, or nested tools. Across 111 approval-object pairs, decision-time metadata reduced residual records from 40 to 13; source-backed predictions on 17 holdout workflows reached 0.926 recall and 0.941 precision. GitHub’s proof-of-presence feature supplies a complementary product control by requiring a live identity-provider challenge for high-impact enterprise actions.

### Why it matters

An approval is weak when it describes only the visible command. The approved object must include the transitive effect closure or the runtime must stop and obtain a new approval when the effect set expands.

### Fit in the stack

This belongs between orchestration and execution. The runtime needs a frozen action manifest, dependency and hook expansion, network and filesystem effect classes, and a receipt that compares predicted with realized effects.

### Practical tools and methodologies worth exploring

- canonical action manifests with resolved tool identity, arguments, targets, and effect classes
- dependency, hook, subprocess, network, and generated-file expansion before approval
- proof of presence for high-impact actions
- approval invalidation when the action manifest or dependency closure changes
- realized-effect receipts and residual-effect alerts

Implementability score: 0.78

Core sources: [Agent Approval Laundering](https://arxiv.org/abs/2609.28586v1), [GitHub proof of presence](https://github.blog/changelog/2026-09-24-require-proof-of-presence-for-high-impact-actions)

## Enforce provenance and authority at the final tool boundary

PACE combines influence-path confinement with capability and effect verification immediately before tool execution. Across eight security benchmarks and three model families, the evaluated configuration recorded the lowest attack success in 62 of 79 eligible columns and tied in 14, while native utility fell by at most three points.

### Why it matters

Earlier checks can become stale after retrieval, planning, memory, or another tool modifies the action. Final-dispatch enforcement sees the concrete tool identity, arguments, target, provenance, and requested effect.

### Fit in the stack

The gateway or execution broker is the last responsible authority plane. Artifact admission, model intent, and prior approval can inform the decision, but only the final gate releases the side effect.

### Practical tools and methodologies worth exploring

- provenance labels on every argument and derived value
- authenticated capability manifests bound to tool identity and effect class
- path-confinement checks from untrusted inputs to sensitive sinks
- argument validation against current-session values
- refusal controls and adversarial cross-tool fixtures
- post-effect receipts that verify the realized state change

Implementability score: 0.54

Core source: [PACE](https://arxiv.org/abs/2610.01349v1)

## Treat persistent memory as a scoped authority object

The shared-memory admission benchmark shows that repetition is not corroboration: uncontested false beliefs were repeated in 0.97 to 0.99 of probes, while a declared-source-type gate reduced false adoption to 0.06 to 0.09. PrivDrift shows why scope must survive context change: across three models and 1,000 dialogues, hybrid secret leakage remained between 38.7 and 54.6 percent, and extra topic drift did not reliably erase the risk.

### Why it matters

Persistent memory can influence later decisions, cross user or task boundaries, and carry secrets long after the original context has disappeared. The system needs source lineage, audience scope, contest state, and explicit widening grants.

### Fit in the stack

Memory governance belongs beside identity and gateway policy. Capture, derivation, retrieval, and consolidation must preserve the authority envelope attached to the original evidence.

### Practical tools and methodologies worth exploring

- provenance-root collapse before independent-support counts
- source classes, contest state, supersession, and expiry
- audience labels that survive derivation and consolidation
- object-specific grants for any scope widening
- secret redaction and deletion below the prompt layer
- delivered-context receipts keyed to viewer and purpose

Implementability score: 0.72

Core sources: [Epistemic Admission in Shared Agent Memory](https://arxiv.org/abs/2609.30813v1), [PrivDrift](https://arxiv.org/abs/2609.30094v1)

## Weekly implication

Authority should narrow as an action approaches execution. The user approves a complete effect object, the gateway rechecks provenance and capability against concrete arguments, and memory contributes evidence only inside its original scope. If any layer can bypass that chain, the approval surface is interface theater rather than control.
