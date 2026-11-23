# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Daily update: 2026-11-23

### Isolate verdict authority

Summary: Candidate code should run in a disposable environment that exports bounded observations to a separate trusted grader holding expected values.

Analysis: [Daily implementation analysis](2026-11-23/reasoning.md#1-isolate-the-grader-from-the-agent-controlled-test-environment)

Core source: [Who Grades the Agent?](https://arxiv.org/abs/2611.27860v1)

Implementable now:
- separate candidate and Oracle processes
- schema-validated observations
- hidden expected values
- native-versus-separated replay
- verdict receipts

Implementability score: 0.68

### Grade recovery from exercised incidents

Summary: Recovery maturity should be based on fault-injected and operator-attributable outcomes, with full, partial, failed, and unclear recovery separated.

Analysis: [Daily implementation analysis](2026-11-23/reasoning.md#2-grade-recovery-by-exercised-outcomes-not-feature-labels)

Core sources: [Exercised, Rarely Recovered](https://arxiv.org/abs/2611.27090v1), [replication package](https://doi.org/10.5281/zenodo.24122560)

Implementable now:
- crash and partial-write fixtures
- recovery evidence ladder
- explicit outcome labels
- operator-attributable receipts
- separate compensation gate

Implementability score: 0.92

## Weekly baseline: week ending 2026-11-20

### Evaluate changes prospectively against an incumbent

Summary: Memory, personal-agent updates, and audit decisions should be promoted only after controlled comparison against the current state on downstream tasks.

Analysis: [Weekly analysis](2026-11-20/reasoning.md#1-evaluate-changes-prospectively-against-an-incumbent)

Core sources: [CoReMem](https://arxiv.org/abs/2611.17316v1), [Safe Personal RSI](https://arxiv.org/abs/2611.23651v1), [DriftGuard](https://arxiv.org/abs/2611.25583v1), [ReA-Bench](https://arxiv.org/abs/2611.16493v1)

Implementable now:
- incumbent-versus-challenger replay
- paired task suites and state snapshots
- separate success, policy, cost, and latency metrics
- bounded promotion and rollback receipts

Implementability score: 0.72

### Make memory visible, reversible, and lineage-bearing

Summary: A useful memory system needs source identity, derivation edges, scope, utility evidence, review state, and erasure across derived state.

Analysis: [Weekly analysis](2026-11-20/reasoning.md#2-make-memory-a-visible-reversible-lineage-bearing-object)

Core sources: [MemoSync](https://arxiv.org/abs/2611.24165v1), [MemoSync repository](https://github.com/SLEEPYBQ/MemoSync), [Jetriever](https://arxiv.org/abs/2611.21478v1), [Forget the Lineage](https://arxiv.org/abs/2611.18133v1)

Implementable now:
- immutable source IDs and derivation edges
- review, quarantine, supersession, and rollback states
- utility evaluation on downstream tasks
- erasure closure and receipts

Implementability score: 0.66

### Treat sessions and harness steps as explicit runtime state

Summary: Capacity, recovery, and device scheduling improve when the runtime exposes held environments, semantic checkpoints, terminal conditions, and deterministic queues.

Analysis: [Weekly analysis](2026-11-20/reasoning.md#3-treat-sessions-and-harness-steps-as-explicit-runtime-state)

Core sources: [Held While Waiting](https://arxiv.org/abs/2611.26480v1), [HerAgent](https://arxiv.org/abs/2611.18443v1), [ModHarness-RL](https://arxiv.org/abs/2611.18533v1), [Metal Sandbox](https://arxiv.org/abs/2611.17294v1)

Implementable now:
- terminal-path session close
- held-resource and idle-retention telemetry
- semantic checkpoints and bounded resume
- deterministic queues for scarce devices
- versioned harness logic

Implementability score: 0.82

## Current working model

1. Keep verdict authority outside candidate-controlled environments.
2. Grade recovery from exercised incidents and explicit outcomes.
3. Promote memory only after model-specific dose evaluation.
4. Store waits and session boundaries as durable runtime state.
5. Measure the deployed trajectory rather than the chat turn.

## Browse

- [Latest daily roundup](../roundups/2026-11-23.md)
- [Daily implementation analysis](2026-11-23/reasoning.md)
- [Friday synthesis](../roundups/2026-11-20.md)
- [Weekly analysis](2026-11-20/reasoning.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
