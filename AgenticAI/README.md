# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-07

### A model upgrade is a memory migration

Summary: In a controlled 48-history study, fixed-schema memory transferred almost unchanged, model-compressed notes moved by +9.91 or -13.28 percentage points depending on migration direction, and a 50/50 mixed embedding index recovered only 4.96 points of the 11.90-point full re-embedding gain.

Analysis: [daily analysis](2026-09-07/reasoning.md#memory-migrations-are-model-migrations)
Core source: [Memory Portability](https://arxiv.org/abs/2609.05339v1)
Tools and methodologies worth exploring now: writer-reader compatibility matrices, embedding-space isolation, raw-source retention, direction-specific migration tests
Implementability score: 0.77

### Skill evolution needs frozen snapshots and provenance

Summary: Skill-Evo4GUI executes each iteration against a frozen library, derives evidence from traces, and exposes accepted changes only in the next iteration. The released prompts and schemas are usable now, while full OSWorld replication still needs the environment and model services.

Analysis: [daily analysis](2026-09-07/reasoning.md#skill-evolution-needs-frozen-snapshots-and-provenance)
Core sources: [paper](https://arxiv.org/abs/2609.04869v1), [Skill-Evo4GUI](https://github.com/LongtaoHu/Skill-Evo4GUI)
Tools and methodologies worth exploring now: snapshot digests, provenance schemas, next-iteration mutation, empty-library controls, rollbackable skill versions
Implementability score: 0.72

### Multi-harness RL needs a held-out harness

Summary: Across 24,000 sealed evaluations, harness choice moved mean solve rate from 2.14% to 9.27%. Cross-harness versus within-harness reward grouping produced only +0.25 percentage points on the held-out harness, with a 95% confidence interval spanning zero.

Analysis: [daily analysis](2026-09-07/reasoning.md#harness-choice-dominates-multi-harness-rl-claims)
Core source: [Multi-Harness RL](https://arxiv.org/abs/2609.04518v1)
Tools and methodologies worth exploring now: held-out minimal harnesses, harness identity in trajectory schemas, reward-group disclosure, repeated-attempt evaluation
Implementability score: 0.58

## Current implication

Memory, skills, and RL policy do not transfer independently of their readers and harnesses. Freeze the representation and execution contract, test the migration direction, and require a held-out runtime before calling a capability portable.
