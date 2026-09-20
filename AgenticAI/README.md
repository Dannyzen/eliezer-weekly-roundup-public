# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-20

### Use correlated task sets for cheap coding-agent A/B tests

Summary: Ad hoc smoke tasks do not reliably stand in for a full coding-agent benchmark. DeltaSelect chooses a fixed, budgeted set whose historical results track the larger suite and preserves the evidence needed for repeated baseline-versus-candidate decisions.

Analysis: [daily analysis](2026-09-20/reasoning.md#use-correlated-task-sets-for-cheap-coding-agent-ab-tests)
Durable deep dive: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [DeltaSelect paper](https://arxiv.org/abs/2609.19607v1), [tool](https://agent-layer.dev/deltaselect), [repository](https://github.com/conn-castle/agent-layer)
Tools and methodologies worth exploring now: fixed task sets, task weights, cost budgets, verifier normalization, provenance receipts, periodic full-suite recalibration
Implementability score: 0.88

### Treat token efficiency as a measured harness outcome

Summary: SoL-Pi reports comparable 51-task performance while cutting recorded token traffic by 44.7% to 49.0%. Promote harness changes only when useful work, token traffic, cost, latency, and held-out regressions are measured together.

Analysis: [daily analysis](2026-09-20/reasoning.md#treat-token-efficiency-as-a-measured-harness-outcome)
Durable deep dive: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [SoL-Pi paper](https://arxiv.org/abs/2609.20519v1), [repository](https://github.com/NVlabs/SoL-Pi), [project page](https://nvlabs.github.io/SoL-Pi/)
Tools and methodologies worth exploring now: native and minimal harness controls, component ablations, EdgeBench-style executable tasks, utility-per-token reporting, held-out environment gates
Implementability score: 0.80

### Audit compressed memory against future updates

Summary: Current-answer accuracy can hide that compression erased a distinction needed by a later update. Use paired histories, shared updates, identifier renaming, tombstones, and late-reference replay to test update sufficiency.

Analysis: [daily analysis](2026-09-20/reasoning.md#audit-compressed-memory-against-future-updates)
Durable deep dive: [Memory Systems](memory-systems/memory-systems.md)
Core source: [Correct Now, Insufficient Later](https://arxiv.org/abs/2609.20045v1)
Tools and methodologies worth exploring now: paired-history fixtures, raw-history controls, metamorphic identifier tests, tombstone replay, retained-state versus delivery classification
Implementability score: 0.66

## Current implication

Cheap evaluation is useful only when it preserves what the decision needs. Calibrate the task subset, measure harness utility per token, and reject memory compression that cannot survive a future update.
