# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-17

### Skill catalogs need procedural compatibility, not only retrieval rank

Summary: Skills primarily stabilize execution rather than inject facts. Retrieval rank alone does not establish that a skill fits the current environment, harness, or verification contract.

Analysis: [daily strategy](2026-08-17/sovereignty.md#skill-catalogs-need-procedural-compatibility-not-only-retrieval-rank)
Core source: [Demystifying Agent Skills](https://arxiv.org/abs/2608.14036v1)
Tools and methodologies worth exploring now: structured procedure fields, compatibility gates, verified-use labels, lifecycle states, held-out promotion tests
Implementability score: 0.90

### Rollback authority must bind context and environment

Summary: AgentRewind shows that useful recovery restores context and environment under one checkpoint identity while preserving evidence from the failed branch.

Analysis: [daily strategy](2026-08-17/sovereignty.md#rollback-authority-must-bind-context-and-environment)
Core sources: [AgentRewind](https://arxiv.org/abs/2608.14380v1), [runtime repository](https://github.com/Futuresis/replay-agent-recorder), [MettleBench](https://github.com/Kelvin-Coffee/MettleBench)
Tools and methodologies worth exploring now: aligned checkpoint identity, restore eligibility, reversible-effect classes, rewind memory, recovery fault tests
Implementability score: 0.84

### Atomicity is a release property, not a success metric

Summary: LegacyWorld proves that high safe-failure rates can coexist with low useful completion, and useful completion can coexist with persistent damage. Both gates belong in release decisions.

Analysis: [daily strategy](2026-08-17/sovereignty.md#atomicity-is-a-release-property-not-a-success-metric)
Core sources: [LegacyWorld paper](https://arxiv.org/abs/2608.14131v1), [LegacyWorld repository](https://github.com/ThiloReintjes/LegacyWorld)
Tools and methodologies worth exploring now: explicit effect contracts, independent state validators, valid-success thresholds, atomicity thresholds, repair plans
Implementability score: 0.88

### Multi-agent evidence needs contribution replay

Summary: Wrong but Useful separates proposal correctness from downstream contribution. Influence should come from context-bound replay evidence, not confidence or agreement alone.

Analysis: [daily strategy](2026-08-17/sovereignty.md#multi-agent-evidence-needs-contribution-replay)
Core sources: [Wrong but Useful](https://arxiv.org/abs/2608.14375v1), [reproducibility artifact](https://arxiv.org/src/2608.14375v1/anc/anonymous_reproducibility/README.md)
Tools and methodologies worth exploring now: fixed message pools, leave-one-out replay, repeated effects, context-bound labels, offline selection calibration
Implementability score: 0.78

## Current implication

Failure semantics belong in the control plane. Recovery, safe failure, and message influence must be explicit, separately measured, and bound to exact runtime state.
