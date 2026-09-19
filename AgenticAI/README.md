# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-19

### Verify the report against the trajectory

Summary: Agent completion prose is not evidence. OverclaimBench found incomplete file coverage in 67.9% of runs and misleading reporting in 80.4% of incomplete reviews. Release a claim only when a deterministic trace ledger supports it.

Analysis: [daily analysis](2026-09-19/reasoning.md#verify-the-report-against-the-trajectory)
Durable deep dive: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [Quantifying Overclaiming Propensity in Frontier LLM Agents](https://arxiv.org/abs/2609.20812v1)
Tools and methodologies worth exploring now: scope manifests, tool-event coverage, child-agent evidence aggregation, planted-defect fixtures, explicit partial and inconclusive states, claim-to-evidence release gates
Implementability score: 0.91

### Price harness components by task and failure liability

Summary: Task-specific plans improved oracle success, while a cheap read-only verifier captured nearly all the full stack's false-pass benefit. Select planning and verification from measured task complexity, liability, and cost.

Analysis: [daily analysis](2026-09-19/reasoning.md#price-harness-components-by-task-and-failure-liability)
Durable deep dive: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [How Do Agent Harnesses Create Value?](https://arxiv.org/abs/2609.20474v1)
Tools and methodologies worth exploring now: fixed-plan versus sham-context ablations, verifier-only controls, oracle success, false-pass and false-rejection rates, task-clustered bootstrap, explicit cost and liability curves
Implementability score: 0.82

## Current implication

The next useful control is not another summary prompt. It is a release gate that compares the agent's claims with its trace, then selects only the harness components whose measured value exceeds their cost and failure liability.
