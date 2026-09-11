# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-11

### Evolve harnesses from recurring failures, not isolated episodes

Summary: Ecdysis clusters failures across tasks before proposing runtime-harness changes. It reports up to a 1.84x training speedup, 18.56% higher reasoning accuracy, and full-data-comparable performance from one-quarter of the training data.

Analysis: [daily analysis](2026-09-11/reasoning.md#evolve-harnesses-from-recurring-failures-not-isolated-episodes)
Core sources: [paper](https://arxiv.org/abs/2609.11677v1), [cuiyu-ai/Ecdysis](https://github.com/cuiyu-ai/Ecdysis)
Tools and methodologies worth exploring now: failure clustering by interaction structure, model-accommodation labels, machine-readable harness changes, held-out task gates, cross-model acceptance, token and regression budgets
Implementability score: 0.61

### Let memory curators ask the environment before they write

Summary: A read-only environment-probing curator raised CLBench pass rate from 39% to 73%, reduced queries from 8.8 to 4.7 per question, and cut task-agent cost from $3.38 to $1.68 without retraining the model or changing production write authority.

Analysis: [daily analysis](2026-09-11/reasoning.md#let-memory-curators-ask-the-environment-before-they-write)
Core source: [Grounding Agent Memory](https://arxiv.org/abs/2609.11060v1)
Tools and methodologies worth exploring now: read-only curator principals, MCP probe subsets, typed memory admission states, probe receipts, paired no-memory evaluations, separate production write gates
Implementability score: 0.78

## Current implication

Do not let a single failed episode rewrite the harness or a completed trajectory become memory truth. Aggregate failures across tasks, probe the current environment, and promote changes only through held-out or downstream admission gates.
