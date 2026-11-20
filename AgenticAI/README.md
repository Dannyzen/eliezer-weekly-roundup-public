# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-20

### Stop reserving one environment per waiting session

Summary: Agent sessions spend seconds waiting on models and milliseconds computing, yet many runtimes reserve one environment for the whole conversation and idle-retention window. Explicit close is the first capacity fix.

Analysis: [Daily analysis](2026-11-20/reasoning.md#1-stop-reserving-one-environment-per-waiting-session)

Core sources: [Held While Waiting v1](https://arxiv.org/abs/2611.26480v1), [agent-runtime-capacity artifact](https://github.com/MEKHALA/agent-runtime-capacity)

Implementable now:
- explicit close on success, failure, and cancellation
- held-environment and idle-retention metrics
- real-wait capacity tests
- workload-driven capacity simulation

Implementability score: 0.82

### Train memory guards from counterfactual trajectory evidence

Summary: DriftGuard learns which retrieved memory changes downstream behavior by running repeated single-memory counterfactual replays offline, then predicts that causal risk online.

Analysis: [Daily analysis](2026-11-20/reasoning.md#2-train-memory-guards-from-counterfactual-trajectory-evidence)

Core sources: [DriftGuard v1](https://arxiv.org/abs/2611.25583v1), [DriftGuard artifact](https://anonymous.4open.science/r/DriftGuard-7F0B)

Implementable now:
- source-linked memory lineage
- pre-action trajectory checkpoints
- repeated single-memory neutralization
- causal labels for action, attack, violation, and task effects
- validation-calibrated intervention thresholds

Implementability score: 0.63

## Current working model

1. Measure held runtime state, not only billed CPU or tokens.
2. Close terminal sessions explicitly before changing infrastructure.
3. Preserve trajectory checkpoints and memory lineage.
4. Build causal memory labels offline through controlled replay.
5. Keep serving-time guards bounded and auditable.

## Browse

- [Daily roundup](../roundups/2026-11-20.md)
- [Daily analysis](2026-11-20/reasoning.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
