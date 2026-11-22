# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Daily update: 2026-11-22

### Grade compaction by completed work

Summary: Context compaction should be tested by resuming from a fixed environment boundary and grading task completion, repeated work, and false completion claims.

Analysis: [Daily implementation analysis](2026-11-22/reasoning.md#1-test-context-compaction-by-resuming-the-task)

Core source: [CompAct-Bench](https://arxiv.org/abs/2611.25673v1)

Implementable now:
- fixed-boundary continuation replay
- one executor and action budget across compactors
- typed unresolved goals, completed effects, and evidence pointers
- separate omission and false-completion analysis

Implementability score: 0.72

### Tune memory dosage per model

Summary: Procedural memory needs model-specific dose curves, conserved provenance, and held-out selection. More guidance can help a strong model while overloading a weaker one.

Analysis: [Daily implementation analysis](2026-11-22/reasoning.md#2-tune-memory-dosage-per-model-and-conserve-provenance)

Core sources: [deployment lessons paper](https://arxiv.org/abs/2611.26361v1), [altk-evolve](https://github.com/AgentToolkit/altk-evolve)

Implementable now:
- source-linked support counts
- memory subset bakeoffs against a fixed scaffold
- separate development and held-out evaluation
- explicit task and tool error propagation

Implementability score: 0.86

### Persist waits instead of holding invocations

Summary: Human approvals, deadlines, and subagent waits should be persisted as resumable runtime objects so the active invocation and Durable Object can sleep.

Analysis: [Daily implementation analysis](2026-11-22/reasoning.md#3-park-durable-waits-instead-of-holding-an-agent-invocation)

Core source: [Cloudflare Agents SDK v0.34.0](https://developers.cloudflare.com/changelog/post/2026-11-20-pi-harness-pi-1-6/)

Implementable now:
- persisted park records
- idempotent signal delivery
- durable history resume
- timeout, cancellation, and reauthorization tests

Implementability score: 0.85

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

1. Test state transformations by resuming the real task.
2. Promote memory only after model-specific dose evaluation.
3. Store waits as durable runtime state.
4. Keep memory source identity and derivation through consolidation.
5. Measure the deployed trajectory rather than the chat turn.

## Browse

- [Latest daily roundup](../roundups/2026-11-22.md)
- [Daily implementation analysis](2026-11-22/reasoning.md)
- [Friday synthesis](../roundups/2026-11-20.md)
- [Weekly analysis](2026-11-20/reasoning.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
