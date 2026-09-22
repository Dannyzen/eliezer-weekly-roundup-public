# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-22

### Select regression tasks from prior trajectories

Summary: Historical trajectories can select a small deterministic regression set that better tracks full-benchmark behavior than convenient examples or random samples. A 10 percent subset cut measured token use by about 90 percent while holding median resolve-rate estimation error below 5 percent.

Analysis: [daily analysis](2026-09-22/reasoning.md#select-regression-tasks-from-prior-trajectories-not-convenient-examples)
Durable deep dive: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [paper](https://arxiv.org/abs/2609.24928v1), [repository](https://github.com/SAILResearch/swe-agent-subset-selection)
Tools and methodologies worth exploring now: normalized traces, outcome-leakage sanitization, outcome stratification, centroid selection, frozen small sets, periodic full-suite recalibration
Implementability score: 0.88

### Evaluate memory by future effects, cost, and latency

Summary: DolphinBench grades 600 future actions whose correctness depends on buried history, then reports accuracy, cost, and latency together. Memory rankings change across models and harnesses, so memory must be evaluated as a complete system configuration.

Analysis: [daily analysis](2026-09-22/reasoning.md#evaluate-memory-by-future-effects-cost-and-latency)
Durable deep dive: [Memory Systems](memory-systems/memory-systems.md)
Core sources: [paper](https://arxiv.org/abs/2609.24971v1), [repository](https://github.com/mem0ai/dolphinbench), [project](https://dolphinbench.ai/)
Tools and methodologies worth exploring now: future-action fixtures, oracle-history versus no-history certification, exact effect graders, pinned histories and app state, cost and latency accounting
Implementability score: 0.82

### Distill harness behavior before deployment

Summary: Harness-Zero uses a specialized harness as a training-time teacher, then deploys the student under one fixed minimal harness. Reported macro-average task success rose from 23.3 percent to 44.3 percent after distillation.

Analysis: [daily analysis](2026-09-22/reasoning.md#distill-harness-behavior-into-the-model-before-deployment)
Durable deep dive: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [paper](https://arxiv.org/abs/2609.24974v1), [repository](https://github.com/metaevo-ai/harness-zero)
Tools and methodologies worth exploring now: fixed target harnesses, teacher review at the student action boundary, filtered rollout collection, LoRA SFT, held-out pattern recovery tests
Implementability score: 0.52

## Current implication

Reuse execution evidence in three different ways: traces can choose cheaper regression sets, future actions can grade memory, and optimized harnesses can compile training data. Keep the full benchmark, raw history, and minimal deploy harness as calibration anchors.
