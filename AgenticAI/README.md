# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Daily update: 2026-11-21

### Evolve harnesses through requirements and deployed-loop evidence

Summary: Harness changes should enter through evidence-backed user requirements, train or evaluate inside the exact deployed loop, and carry verifier controls that reject known-wrong solutions.

Analysis: [Daily implementation analysis](2026-11-21/reasoning.md)

Core sources: [AHE-Beta](https://arxiv.org/abs/2611.24924v1), [AHE-Beta repository](https://github.com/Curry09/AHE-Beta), [Hugging Face harness adapters](https://huggingface.co/blog/harness-adapters-at-scale), [adapter collection](https://huggingface.co/collections/harness-hub/qwen38-27b-harness-adapters)

Implementable now:
- evidence-backed harness requirement issues
- root-cause consolidation and requirement-specific merge proof
- exact production-harness replay in evaluation
- known-wrong and valid-alternative verifier controls
- separate in-distribution and transfer metrics

Implementability scores: 0.65 for requirement-centered evolution; 0.45 for harness-specific RL adapters

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

1. Promote candidate state only after it beats an incumbent.
2. Store memory as a governed object with lineage and lifecycle.
3. Represent sessions as held resources with explicit terminal transitions.
4. Checkpoint harness work at semantic proof boundaries.
5. Measure the deployed trajectory rather than the chat turn.

## Browse

- [Latest daily roundup](../roundups/2026-11-21.md)
- [Daily implementation analysis](2026-11-21/reasoning.md)
- [Friday synthesis](../roundups/2026-11-20.md)
- [Weekly analysis](2026-11-20/reasoning.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
