# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-16

### Learn harness programs from typed trajectories

Summary: ModHarness-RL makes compression and steering executable programs over typed interaction state, then validates and replays candidate changes before promotion.

Analysis: [Daily analysis](2026-11-16/reasoning.md#1-learn-harness-programs-from-typed-trajectories)

Core source: [ModHarness-RL v1](https://arxiv.org/abs/2611.18533v1)

Implementable now:
- typed trajectory blocks
- deterministic compression and steering programs
- historical replay before admission
- score, context, latency, and regression gates

Implementability score: 0.62

### Checkpoint setup at semantic boundaries

Summary: HerAgent validates, checkpoints, repairs, and rolls back environment setup by functional block, then proves the accepted sequence in a fresh environment.

Analysis: [Daily analysis](2026-11-16/reasoning.md#2-checkpoint-coding-agent-setup-at-semantic-boundaries)

Core source: [HerAgent v1](https://arxiv.org/abs/2611.18443v1)

Implementable now:
- ordered setup blocks with validation commands
- clean checkpoints after passed blocks
- bounded repair and root-cause rollback
- clean-environment replay before acceptance

Implementability score: 0.84

## Current working model

1. Store agent work as typed trajectory state.
2. Express harness changes as executable programs.
3. Checkpoint at semantic validation boundaries.
4. Replay candidate changes and repaired setup from known-good state.
5. Promote only evidence-bearing artifacts.

## Browse

- [Daily roundup](../roundups/2026-11-16.md)
- [Daily analysis](2026-11-16/reasoning.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Sandbox-native agent workers](sandbox-native-agent-workers/sandbox-native-agent-workers.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
