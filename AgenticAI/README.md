# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-11 Daily Scan

Today's implementation signal is timing as a control surface. Adaptive agents need explicit rules for when to inspect a trajectory, when to spend another reasoning step, and when generated tests have enough evidence to support release.

### Adapt monitoring pressure to trajectory health

Summary: Cadence uses advisory and replacement interventions to tighten or relax inspection intervals. Across 300 SWE-bench Lite tasks, it resolves 76 more mini-swe-agent tasks and 47 more Moatless tasks than vanilla agents.

Analysis: [daily analysis](2026-10-11/reasoning.md#cadence-adapt-monitoring-pressure-to-execution-health)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.12269v1), [public MIT repository](https://github.com/LogAnalysisTech/Cadence), [results dataset](https://huggingface.co/datasets/dengdan1999/Cadence-Experiment-Results)
Tools and methodologies worth exploring now: severity-coded interventions, adaptive inspection intervals, shadow monitoring, false-intervention metrics, source-bound run artifacts
Implementability score: 0.72

### Grade tests against implementation sets

Summary: TestPrism's Joint Success Function requires generated tests to fail the initial program, accept every valid candidate, and reject every invalid candidate. Fourteen configurations score 59.67% against one reference and 28.00% against the full implementation set.

Analysis: [daily analysis](2026-10-11/reasoning.md#testprism-validate-tests-against-an-implementation-set)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [TestPrism paper v1](https://arxiv.org/abs/2610.12289v1)
Tools and methodologies worth exploring now: valid-implementation corpora, invalid behavioral mutants, Joint Success Function, oracle provenance, single-reference comparison
Implementability score: 0.64

### Route reasoning at the turn boundary

Summary: RACE learns when earlier reasoning still supports subsequent actions. Across four benchmarks, it stays within 1.40 performance points of standard SFT plus GRPO while reducing reasoning tokens by 32.3% to 80.2%.

Analysis: [daily analysis](2026-10-11/reasoning.md#race-route-reasoning-at-the-turn-boundary)
Durable topic: [Model Router Governance](../Strategy/model-router-governance/model-router-governance.md)
Core sources: [RACE paper v1](https://arxiv.org/abs/2610.12061v1), [currently empty repository](https://github.com/HututuAI/RACE)
Tools and methodologies worth exploring now: per-turn token accounting, forced-reasoning events, fixed-think and fixed-skip baselines, shadow skip policies, held-out quality-cost gates
Implementability score: 0.42

## Current implication

Replace fixed schedules with evidence-triggered timing, then preserve the trigger, intervention, cost, and outcome in the trajectory.

Latest roundup: [2026-10-11 daily scan](../roundups/2026-10-11.md).
