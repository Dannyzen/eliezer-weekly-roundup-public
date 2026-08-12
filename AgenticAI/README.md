# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-12

### Self-evolving harnesses need typed edits and transfer gates

Summary: A fixed evolution recipe across eight languages and three models improved most cells, but Python and GPT-5-mini were null regions. Twenty to 40 percent of each evolved harness remained ecosystem-specific.

Analysis: [daily analysis](2026-08-12/reasoning.md#self-evolving-harnesses-should-produce-typed-transferable-contracts)
Core source: [One Recipe, Many Harnesses](https://arxiv.org/abs/2608.10178v1)
Tools and methodologies worth exploring now: typed failure signals, falsifiable edit contracts, held-out gates, transfer tests, native ecosystem adapters
Implementability score: 0.78

### Agent safety scores need realized-state evidence

Summary: REDAgentBench separates exposure, execution, observation, and adjudication across 1,661 executable cases. Almost one in five state-confirmed violations in a diagnostic cohort followed explicit risk recognition by the agent.

Analysis: [daily analysis](2026-08-12/reasoning.md#agent-red-teaming-should-separate-exposure-execution-observation-and-adjudication)
Core source: [REDAgentBench](https://arxiv.org/abs/2608.10669v1)
Tools and methodologies worth exploring now: isolated service doubles, constraint-derived attacks, final-state diffs, evidence-view receipts, action-boundary reminders
Implementability score: 0.72

### Prompt-injection detectors need attack-family coverage maps

Summary: Quadrat-IPI measures nine detectors across 92 attack cells, 16,800 injections, and 63,000 clean documents at fixed false-positive budgets. One recall number hides 4 to 76 point spreads between a detector's weakest and strongest cells.

Analysis: [daily analysis](2026-08-12/reasoning.md#prompt-injection-detectors-need-attack-family-maps-at-fixed-false-positive-budgets)
Core sources: [article](https://huggingface.co/blog/mihailgribov/compare-prompt-injection-detectors), [dataset](https://huggingface.co/datasets/mihailgribov/quadrat-ipi), [evaluation harness](https://github.com/mihail-gribov/quadrat-ipi-eval)
Tools and repositories worth exploring now: Quadrat-IPI 1.0.1, `quadrat-ipi-eval`, per-carrier false-positive budgets, attack-cell coverage thresholds
Implementability score: 0.95

## Current implication

Use typed transfer gates for harness evolution, state receipts for safety evaluation, and attack-family coverage at fixed false-positive budgets for detector admission.
