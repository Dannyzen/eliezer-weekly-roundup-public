# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the daily analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-12

### Instrument the reward-relevant lifecycle, not only the transcript

Summary: BenchShield treats evaluation as an executable lifecycle. Static phase-aware taint analysis and runtime evidence distinguish exposure, agent use, verifier input, and reward realization. The reported runtime detector reaches 96 percent accuracy on a 456-trajectory adjudicated corpus drawn from more than 31,000 public runs.

Analysis: [daily analysis](2026-09-12/reasoning.md#instrument-the-reward-relevant-lifecycle-not-only-the-transcript)
Core sources: [BenchShield](https://arxiv.org/abs/2609.11028v1), [BenchFlow](https://github.com/benchflow-ai/benchflow), [ClawsBench trajectories](https://huggingface.co/datasets/benchflow/ClawsBench)
Tools and methodologies worth exploring now: lifecycle models, phase-aware taint analysis, infrastructure-side evidence, reward source and sink inventories, evidence pinning, explicit inconclusive outcomes
Implementability score: 0.72

### Evaluate freshness against event time, not cache age

Summary: ChurnBench computes gold state from an append-only event ledger at both retrieval and evaluation time. Its ablation shows that refresh scheduling and entity churn, not cache age alone, determine staleness.

Analysis: [daily analysis](2026-09-12/reasoning.md#evaluate-freshness-against-event-time-not-cache-age)
Core sources: [ChurnBench](https://arxiv.org/abs/2609.11515v1), [repository](https://github.com/vsingh45/churnbench)
Tools and methodologies worth exploring now: event ledgers, timestamped gold-state folds, per-entity TTL tiers, freshness-versus-reasoning labels, replayable run provenance
Implementability score: 0.84

## Current implication

Before optimizing models, make evaluation lifecycle and source time first-class runtime objects. A score without reward provenance and an answer without temporal validity are both incomplete evidence.
