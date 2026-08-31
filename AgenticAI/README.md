# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-31

### Evaluate the controller separately from the worker

Summary: LoopArena fixes the coding Worker and evaluates a separate runtime Controller through typed Loop Contracts across 90 contract-selection questions, 27 condensed tasks, and 27 full tasks. The best full-task Strict Success Rate is 24.69 percent.

Analysis: [daily analysis](2026-08-31/reasoning.md#evaluate-the-controller-separately-from-the-worker)
Core sources: [paper](https://arxiv.org/abs/2608.28281v1), [repository](https://github.com/AMAP-ML/LoopArena)
Tools and methodologies worth exploring now: typed Loop Contracts, fixed-worker controller comparisons, Evidence Packets, paired starting states, cheap contract-selection fixtures, full-task anchors, terminal evaluator receipts
Implementability score: 0.86

### Score trajectory evidence, not only terminal success

Summary: GCPC instantiates human-governed task checklists, judges only cited execution evidence, abstains when evidence is absent, and applies the official verifier in a separate scripted step. It exposes improvement and regression hidden inside unchanged pass/fail outcomes.

Analysis: [daily analysis](2026-08-31/reasoning.md#score-trajectory-evidence-not-only-terminal-success)
Core source: [paper](https://arxiv.org/abs/2608.27487v1)
Tools and methodologies worth exploring now: reusable human rules, task-specific grounded checklists, evidence-span scoring, abstention, matched with-skill and without-skill trajectories, deterministic verifier overrides
Implementability score: 0.79

## Current implication

Long-running agent work needs a separately testable controller and an evidence-bearing progress measure below terminal success. Cheap fixtures can guide controller selection, but full-task outcomes and deterministic evaluator receipts remain the acceptance anchor.
