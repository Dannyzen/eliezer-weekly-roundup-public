# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.


## Daily update: 2026-11-26

### Production failures should compile into replayable evolution gates

Summary: Sports Agent separates model evolution from harness evolution, then validates both through diagnosis, replay, independent audit, regression testing, and performance-tolerance gates.

Analysis: [Sports Agent turns production failures into bounded model and harness evolution](2026-11-26/reasoning.md#sports-agent-turns-production-failures-into-bounded-model-and-harness-evolution)

Core source: [Sports Agent v1](https://arxiv.org/abs/2611.33700v1)

Implementable now:
- retain failed trajectories with source evidence and failure labels;
- compile recurring failures into replay fixtures;
- version model, prompt, skill, and data changes separately;
- promote changes only after independent regression replay.

Implementability score: 0.72

### Context compaction should be a typed, observable runtime operation

Summary: Giving models context inspection and compaction operations improved accuracy or efficiency at tight budgets, while model-to-model variation shows why the harness still needs policy and fallback control.

Analysis: [Model-managed context is becoming a measurable runtime API](2026-11-26/reasoning.md#model-managed-context-is-becoming-a-measurable-runtime-api)

Core source: [Letting Models Manage Their Own Context v1](https://arxiv.org/abs/2611.34147v1)

Implementable now:
- explore [Mainplane](https://github.com/mainplane-ai/mainplane);
- expose typed context operations;
- log retained spans, edit timing, token deltas, cache reuse, and task outcome;
- compare policies across several context budgets.

Implementability score: 0.76

## Daily update: 2026-11-25

### Recover only the failed dependency branch

Summary: Durable orchestration should preserve completed siblings, reset a failed node and its descendants, and inject structured error context on retry.

Analysis: [Daily implementation analysis](2026-11-25/reasoning.md#1-recover-the-affected-subgraph-instead-of-replaying-the-whole-run)

Core source: [fork() for Agents](https://arxiv.org/abs/2611.31727v1)

Implementable now:
- persistent DAG node state
- selective descendant invalidation
- completed-artifact reuse
- schema-aware retry context
- duplicate-effect and recovery telemetry

Implementability score: 0.58

### Cross model, harness, and reasoning effort in evaluations

Summary: Agent evaluation should identify each model, harness, reasoning level, task, grader, and cost cell instead of collapsing them into one leaderboard score.

Analysis: [Daily implementation analysis](2026-11-25/reasoning.md#2-factor-model-harness-and-reasoning-effort-in-agent-evaluation)

Core sources: [ShellBench](https://arxiv.org/abs/2611.32946v1), [public dataset](https://huggingface.co/datasets/OpenClaw/ShellBench)

Implementable now:
- crossed evaluation designs
- pinned harness and model identities
- separate quality, safety, latency, token, and cost metrics
- held-out tasks
- hashed public evaluation subsets

Implementability score: 0.88

## Daily update: 2026-11-24

### Count serving failures in agent quality

Summary: Multi-agent benchmarks should replay identical work across load regimes and score useful results over every submitted job, not only the jobs that survive execution.

Analysis: [Daily implementation analysis](2026-11-24/reasoning.md#1-benchmark-multi-agent-systems-under-runtime-pressure)

Core sources: [MASSys paper](https://arxiv.org/abs/2611.28671v1), [repository](https://github.com/MAS-Sys-Bench/MAS-Sys), [trace dataset](https://huggingface.co/datasets/MAS-Sys/MAS-Sys-Traces)

Implementable now:
- fixed candidate-task replay
- explicit serving-cell identity
- submitted-versus-evaluated denominators
- queue, timeout, latency, and cache telemetry
- effective quality over all jobs

Implementability score: 0.62

### Test the evaluator before comparing agents

Summary: Agent evaluations need narrow claims, adversarial grader checks, repeated rollouts, trace review, and versioned evidence.

Analysis: [Daily implementation analysis](2026-11-24/reasoning.md#2-treat-the-evaluation-itself-as-a-maintained-system)

Core source: [How to build and maintain an agentic evaluation](https://huggingface.co/blog/agentic-evals)

Implementable now:
- reference, no-op, and shortcut probes
- repeated task trials
- successful-trace inspection
- uncertainty-aware reporting
- task, harness, verifier, and result identities

Implementability score: 0.92

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

- [Latest daily roundup](../roundups/2026-11-25.md)
- [Daily implementation analysis](2026-11-24/reasoning.md)
- [Friday synthesis](../roundups/2026-11-20.md)
- [Weekly analysis](2026-11-20/reasoning.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
