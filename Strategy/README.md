# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-30

### Separate persona drift from audited execution

Summary: Persona-Execution Separation puts mutable tone, instructions, and self-presentation in a permissive domain while execution identity, credentials, state, and audit remain stable. A typed contract bridge returns status summaries and gates data-body egress.

Analysis: [daily strategy](2026-08-30/sovereignty.md#separate-persona-drift-from-audited-execution)
Core source: [paper](https://arxiv.org/abs/2608.27427v1)
Tools and methodologies worth exploring now: separate persona and execution configuration, stable service identity, typed bridge requests, summary-versus-body egress classes, DLP gates, persona-versioned execution receipts
Implementability score: 0.61

### Secure persistent state with plan-first information-flow control

Summary: SPA commits to a declarative plan before reading untrusted outputs, carries confidentiality and integrity labels through execution and storage, and exposes semantic metadata instead of raw payloads to later planners. It reports 0 percent and 0.2 percent attack success on single- and multi-query benchmarks.

Analysis: [daily strategy](2026-08-30/sovereignty.md#secure-persistent-state-with-plan-first-information-flow-control)
Core source: [paper](https://arxiv.org/abs/2608.27234v1)
Tools and methodologies worth exploring now: plan-first DSLs, dual-lattice IFC, label-preserving artifacts, metadata/value separation, delayed-attack fixtures, security-versus-reuse measurement
Implementability score: 0.68

## Current implication

Sovereign agents need separate trust domains for mutable presentation and audited work, then label-preserving state between queries. Context may describe a task or artifact, but it does not acquire authority to alter execution identity, reveal data bodies, or drive higher-integrity effects.
