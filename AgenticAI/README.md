# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-08

### Separate hard issues, weak models, and bad runs

Summary: current coding-agent failure predictors can score well by rediscovering issue difficulty and model ability. On public SWE-bench Verified trajectories, an issue-only baseline reached 0.92 AUROC versus about 0.62 for tested trajectory predictors.

Analysis: [Daily analysis](2026-11-08/reasoning.md#1-separate-hard-issues-weak-models-and-bad-runs)

Core source: [Hard Issue, Weak Model, or Bad Run?](https://arxiv.org/abs/2611.08285v1)

Implementable now:
- repeated attempts for each issue-model pair
- issue-only and model-only baselines
- causal failure labels before stop, retry, or switch decisions
- equal-budget closed-loop intervention tests

Implementability score: 0.84

### Derive migration tests from changed contracts

Summary: typical-input checks released 41.0 percent of wrong repairs across 73 migration tasks. One edge input derived from the release note cut the wrong-release rate to 6.5 percent.

Analysis: [Daily analysis](2026-11-08/reasoning.md#2-derive-migration-tests-from-changed-contracts)

Core source: [Accepted but Wrong](https://arxiv.org/abs/2611.08269v1)

Implementable now:
- before-and-after contracts from release notes
- edge inputs targeted at changed semantics
- hidden checks independent from the repair model
- runtime, input, expected-effect, and verdict receipts

Implementability score: 0.87

## Current working model

1. Version the measurement instrument before comparing models.
2. Separate issue difficulty, model ability, and run variance.
3. Derive migration gates from changed contracts.
4. Preserve typed events before compressing evidence.
5. Keep release oracles deterministic and independent from the acting model.

## Browse

- [Latest roundup](../roundups/2026-11-08.md)
- [Latest dated analysis](2026-11-08/reasoning.md)
- [Friday synthesis](2026-11-06/reasoning.md)
- [Decision-state compilation](decision-state-compilation/decision-state-compilation.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Skills as control](skills-as-control/skills-as-control.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
