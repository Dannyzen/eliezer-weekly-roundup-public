# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the daily analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-15

### Search unread evidence before accepting a root cause

Summary: Continual Search turns long-trace root-cause attribution into iterative evidence retrieval. On 50 MegaRCA-Mix failures with 286K-token median records, Opus-4.8 evidence coverage rose from 70.8 to 97.4 percent and F1 from 0.478 to 0.620, while short traces showed no reliable benefit.

Analysis: [daily analysis](2026-09-15/reasoning.md#search-beyond-the-first-plausible-root-cause)
Core source: [Continual Search paper](https://arxiv.org/abs/2609.13463v1)
Tools and methodologies worth exploring now: unread-evidence ledgers, challenge prompts, artifact-coverage metrics, source-bound root-cause labels, one-pass controls, coverage-gain stopping rules
Implementability score: 0.82

### Route collaboration per task and compare at equal spend

Summary: Across 614 code problems, hierarchical collaboration's advantage grows from 2.4 pass@1 points on easy tasks to 21.1 on hard tasks while costing about 9.95 times more tokens. A difficulty-aware selector reaches 77.7 percent pass@1 at 40 percent of always-hierarchical spend.

Analysis: [daily analysis](2026-09-15/reasoning.md#route-collaboration-per-problem-and-compare-at-equal-spend)
Core source: [difficulty-aware topology paper](https://arxiv.org/abs/2609.13890v1)
Tools and methodologies worth exploring now: per-task topology routing, interpretable difficulty features, cached route outcomes, equal-spend calibration, single-agent defaults, route receipts
Implementability score: 0.76

## Current implication

Do not buy more context or more agents by default. Long failures need controlled evidence expansion; collaboration needs a per-task route whose quality is compared at equal realized spend.
