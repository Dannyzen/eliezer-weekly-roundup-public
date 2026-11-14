# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-14

### Value memory by future work

Summary: CoReMem measures whether a trajectory segment helps the next coding task, then builds compact memory around repository locations and executable checks.

Analysis: [Daily analysis](2026-11-14/reasoning.md#1-value-memory-by-future-work-not-retrieval-relevance)

Core source: [CoReMem v1](https://arxiv.org/abs/2611.17316v1)

Implementable now:
- matched next-task trials with and without candidate memory
- source-linked file, command, and check anchors
- joint resolution, step, token, and memory-cost scoring

Implementability score: 0.78

### Give structural coordination its own optimization objective

Summary: MultiLoop improved task accuracy through prompts and a new tool while delegation failures persisted. Harness optimization must score coordination structure separately.

Analysis: [Daily analysis](2026-11-14/reasoning.md#2-optimize-harness-structure-not-only-prompts-and-tools)

Core source: [MultiLoop v1](https://arxiv.org/abs/2611.15754v1)

Implementable now:
- versioned harness diffs and rollout receipts
- structural failure labels
- equal-budget single-agent baselines
- held-out regression tasks

Implementability score: 0.72

### Calibrate trajectory auditors against benign controls

Summary: ReA-Bench pairs risky traces with authorized benign behavior and evidence variants, exposing the recall versus false-positive tradeoff hidden by aggregate scores.

Analysis: [Daily analysis](2026-11-14/reasoning.md#3-audit-trajectory-risks-with-paired-evidence-conditions)

Core source: [ReA-Bench v1](https://arxiv.org/abs/2611.16493v1)

Implementable now:
- risky and benign trace pairs
- shortened and evidence-completed variants
- recall at fixed false-positive budgets
- failure-tier diagnostics

Implementability score: 0.81

## Current working model

1. Preserve canonical evidence before deriving memory or conclusions.
2. Measure memory on future work, not retrieval similarity alone.
3. Optimize task outcomes and coordination structure separately.
4. Audit risk with benign controls and evidence-conditioned variants.
5. Promote only changes with held-out proof and rollback.

## Browse

- [Daily roundup](../roundups/2026-11-14.md)
- [Daily analysis](2026-11-14/reasoning.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
