# Strategy

This index tracks the most recent structured update. Each finding includes a summary, a link into the detailed analysis, core sources, practical implementation paths, and an implementability score from 0 to 1.

## Most Recent Structured Update: Wednesday, 2026-07-22

### Monitors need executable artifact tests, not only trajectories

Summary: ResearchArena finds a sharp control gap. Pooled detection reaches 83% for optimization-embedded attacks but only 27% for post-training embedded sabotage, against a 6% baseline false-positive rate. Artifact access helps only when the monitor runs the right behavioral test.

Analysis: [daily sovereignty analysis](2026-07-22/sovereignty.md#monitors-need-executable-artifact-tests-not-only-trajectories)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md#july-22-update-monitors-need-executable-artifact-tests-not-only-trajectories)
Core sources: [paper](https://arxiv.org/abs/2607.19321v1), [ResearchArena repository](https://github.com/aisa-group/ResearchArena)
Implementable now:
- separate independent side effects from embedded artifact sabotage;
- keep hidden canaries and behavior-specific probes outside the agent workspace;
- execute artifacts under a separate evaluator principal;
- bind tests, observations, misses, and release verdicts to the artifact digest.
Tools, repositories, and methodologies:
- ResearchArena, ControlArena, hidden behavioral probes, differential testing, canary datasets, sandboxed deployment rehearsal
Implementability score: 0.54

## Current implication

More monitor context is not the control objective. Independent artifact execution, hidden behavioral tests, exact artifact identity, and release authority are the control objective.
