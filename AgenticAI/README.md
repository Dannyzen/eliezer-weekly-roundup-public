# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-08

### Harness evolution needs held-out tests and causal debugging

Summary: HarnessOpt-Bench evaluates five optimizer models on four tasks over 111 runs, while TRAJDEBUG adds 486 manually annotated failed trajectories for earliest decisive-error localization.

Analysis: [daily analysis](2026-08-08/reasoning.md#harness-evolution-needs-held-out-evaluation-and-causal-failure-localization)
Core sources: [HarnessOpt-Bench](https://arxiv.org/abs/2608.06301v1), [TRAJDEBUG](https://arxiv.org/abs/2608.06346v1)
Tools and methodologies worth exploring now: immutable candidate commits, hidden tests, isolated sandboxes, token budgets, causal failure labels, replay fixtures
Implementability score: 0.62

### Reusable skills need relation-aware replay gates

Summary: GSE models dependency, co-usage, and conflict across a skill bank, consolidates related updates, and replays historical cases before promotion. Evaluation covers 108 real bugs and 500 industrial reports.

Analysis: [daily analysis](2026-08-08/reasoning.md#global-skill-evolution-needs-relation-graphs-and-replay-gates)
Core source: [paper](https://arxiv.org/abs/2608.06153v1)
Tools and methodologies worth exploring now: skill relation graphs, typed change proposals, project-held-out evaluation, historical replay, provenance-preserving patches
Implementability score: 0.64

## Current implication

Ship receipts first. Force coding agents to earn mutations with local evidence. Treat skills, tool catalogs, and session history as admitted control surfaces. Retained state is useful only after a boundary decides it is still authoritative.
