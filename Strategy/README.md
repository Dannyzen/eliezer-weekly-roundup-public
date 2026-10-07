# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-07

The governance signal is economic and operational: make agent resource ownership checkable, then decide whether repeated work belongs in a reusable artifact or repeated general-model calls.

### Make agent-fleet resource ownership checkable

Summary: MemMux attributes process trees, checks descendant cleanup, detects escaped children, and enforces a memory admission budget. Under a 7.5 GiB limit it reported zero swap, complete tested cleanup, and detection of all ten injected escapes.

Analysis: [daily strategy analysis](2026-10-07/sovereignty.md#make-agent-fleet-resource-ownership-checkable-at-runtime)
Durable topic: [Agent Fleet Monitoring Control Plane](agent-fleet-monitoring-control-plane/agent-fleet-monitoring-control-plane.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.07257v1), [MemMux repository](https://github.com/sumanyumuku98/MemMux)
Tools and methodologies worth exploring now: cgroup-based ownership, per-agent memory attribution, admission control, cleanup receipts, escaped-process detection, host-stamped runtime benchmarks
Implementability score: 0.84

### Bottle repeated cognition before routing millions of calls

Summary: BOTTLED tests whether an agent can spend a fixed budget to build a reusable program or small model. Most runs underperformed direct or distillation controls, but one task retained about 82 percent of zero-shot quality at roughly 657 times lower reported cost.

Analysis: [daily strategy analysis](2026-10-07/sovereignty.md#bottle-repeated-cognition-before-routing-millions-of-calls)
Durable topic: [Model Router Governance](model-router-governance/model-router-governance.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.08775v1), [BOTTLED repository](https://github.com/aktsonthalia/bottled)
Tools and methodologies worth exploring now: build-versus-call routing, fixed artifact budgets, zero-shot and distillation controls, workload-level cost accounting, drift-triggered rebuilds
Implementability score: 0.61

## Current implication

Fleet governance should account for both host resources and inference economics. Bind each agent to a verifiable runtime envelope, and route repetitive work through reusable artifacts only after held-out quality and cost gates pass.

Latest roundup: [2026-10-07](../roundups/2026-10-07.md).
