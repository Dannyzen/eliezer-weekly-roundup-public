# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-17

### Govern the composed execution, not only each step

Summary: Step-scoped guardrails cannot detect authority creep, threshold laundering, cumulative violations, or context collapse when every individual action is locally acceptable. Recompute policy state from raw provenance over the complete execution before admitting the next effect.

Analysis: [dated strategy analysis](2026-09-17/sovereignty.md#govern-the-composed-execution-not-only-each-step)
Durable deep dive: [Context-to-Execution Integrity](context-to-execution-integrity/context-to-execution-integrity.md)
Core source: [compositional policy violations paper](https://arxiv.org/abs/2609.18820v1)
Tools and methodologies worth exploring now: append-only event ledgers, Rego, Cedar, SQL assertions, deterministic state machines, cumulative-policy fixtures, versioned trace schemas
Implementability score: 0.64

## Supporting daily signal: task evidence is an authority boundary

Summary: AgentLSD shows that fake results, decoy endpoints, and misleading validation cues can alter agent behavior without explicit injected instructions. Tool identity is not evidence validity. Consequential effects need lineage and independent validation at the effect gate.

Analysis: [dated strategy analysis](2026-09-17/sovereignty.md#supporting-signal-task-evidence-itself-is-an-authority-boundary)
Durable deep dive: [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
Core source: [AgentLSD paper](https://arxiv.org/abs/2609.19140v1)
Tools and methodologies worth exploring now: [AgentLSD](https://github.com/Golim/agent-lsd), evidence lineage, paired contaminated fixtures, independent validation, trajectory-level policy checks
Implementability score: 0.88

## Current implication

Per-turn safety is necessary but insufficient. The runtime must know where evidence came from and whether the accumulated execution still satisfies the governing policy.
