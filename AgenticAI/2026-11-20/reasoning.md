# AgenticAI Weekly Analysis: 2026-11-20

## Scope

This synthesis covers primary sources captured from 14 through 20 November 2026. It compresses the week's daily notes into three implementation patterns. Public repositories and artifacts were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## 1. Evaluate changes prospectively against an incumbent

The week's evaluation papers converge on one rule: a candidate memory, agent update, or audit decision earns promotion only by improving the next task under controlled comparison.

[CoReMem](https://arxiv.org/abs/2611.17316v1) values memory by prospective utility in successive coding tasks instead of by compression quality or similarity. [Safe Personal RSI](https://arxiv.org/abs/2611.23651v1) evaluates personal-agent updates against the incumbent and repairs regressions before promotion. [DriftGuard](https://arxiv.org/abs/2611.25583v1) derives online memory-risk labels from repeated offline counterfactual replay. [ReA-Bench](https://arxiv.org/abs/2611.16493v1) reinforces the same methodological point for auditors: benign controls and paired evidence variants matter because an alarm alone cannot distinguish sensitivity from useful discrimination.

Why it matters: self-improvement and persistent memory create compounding state. Static quality scores miss downstream regressions, while direct promotion turns every user into the test environment. The safer loop is challenger versus incumbent, task-level acceptance, explicit regression budgets, and rollback.

Fits into the stack: evaluation harnesses, personal-agent updates, memory admission, audit calibration, and release gates.

Implementable now:
- retain an incumbent configuration and evaluate challengers against it;
- replay fixed task suites with paired seeds and state snapshots;
- score task success, policy violations, cost, and latency separately;
- use counterfactual memory neutralization offline to create causal labels;
- require bounded improvement with no unacceptable regression before promotion;
- retain the old state and promotion receipt for rollback.

Artifact status: papers verified from immutable v1 pages. DriftGuard exposes a read-only research snapshot. The full methods depend on benchmark-specific environments and repeated trajectory execution.

Evidence limit: the benchmarks and intervention policies are domain-specific. Counterfactual single-memory replay does not capture all multi-memory interactions, and personal-agent acceptance thresholds remain a product decision.

Implementability score: 0.72

Core sources: [CoReMem v1](https://arxiv.org/abs/2611.17316v1), [Safe Personal RSI v1](https://arxiv.org/abs/2611.23651v1), [DriftGuard v1](https://arxiv.org/abs/2611.25583v1), [ReA-Bench v1](https://arxiv.org/abs/2611.16493v1)

## 2. Make memory a visible, reversible, lineage-bearing object

Memory quality and memory governance are the same operational problem. [MemoSync](https://arxiv.org/abs/2611.24165v1) makes cross-session memory visible and co-managed by developers and agents. [Jetriever](https://arxiv.org/abs/2611.21478v1) ranks memory by expected usefulness rather than surface similarity. [Forget the Lineage](https://arxiv.org/abs/2611.18133v1) shows why deletion must cover derived summaries, embeddings, residues, and backups, not only the original message.

The combined design is stronger than another vector store. Each memory needs source identity, derivation edges, scope, validity, utility evidence, review state, and a reversible lifecycle. Retrieval can use utility, but the scoring surface itself needs evaluation because a learned utility model can become another unobserved authority source.

Why it matters: invisible memory creates silent behavior drift. Weak deletion leaves derived state behind. Similarity-only retrieval favors lexical resemblance over task value. A governed memory object lets the runtime explain why a memory was admitted, retrieved, changed, quarantined, or erased.

Fits into the stack: persistent memory, local-first workbenches, retrieval, provenance, user control, and erasure.

Implementable now:
- use [MemoSync](https://github.com/SLEEPYBQ/MemoSync) as a read-only design reference for visible cross-session memory;
- store immutable source IDs and explicit derivation edges;
- separate recall ranking from write authority;
- expose review, quarantine, supersession, and rollback states;
- evaluate utility ranking on downstream tasks rather than retrieval similarity alone;
- propagate erasure across the derivation closure and record an erasure receipt.

Artifact status: MemoSync has a populated TypeScript repository and tagged history. The erasure and utility-ranking papers describe more architecture than a drop-in production package.

Evidence limit: lineage-complete erasure requires coverage across storage systems and backups. Utility ranking needs domain data and can overfit its evaluator.

Implementability score: 0.66

Core sources: [MemoSync v1](https://arxiv.org/abs/2611.24165v1), [MemoSync repository](https://github.com/SLEEPYBQ/MemoSync), [Jetriever v1](https://arxiv.org/abs/2611.21478v1), [Forget the Lineage v1](https://arxiv.org/abs/2611.18133v1)

## 3. Treat sessions and harness steps as explicit runtime state

[Held While Waiting](https://arxiv.org/abs/2611.26480v1) shows that agent capacity can be dominated by environments reserved while models wait, even when framework computation lasts only milliseconds. [HerAgent](https://arxiv.org/abs/2611.18443v1) makes coding-agent environment setup recoverable through semantic checkpoints. [ModHarness-RL](https://arxiv.org/abs/2611.18533v1) treats the harness as an executable program that can itself evolve. [Metal Sandbox](https://arxiv.org/abs/2611.17294v1) moves scheduling below the agent to recover idle native GPU capacity safely.

These findings belong together. An agent runtime is a state machine with held resources, resumable checkpoints, scheduled commands, and terminal cleanup. Chat abstractions hide all four.

Why it matters: adding capacity before measuring held state wastes money. Retrying whole setup trajectories wastes time and obscures failure location. Letting each model independently schedule scarce resources creates contention and weak isolation.

Fits into the stack: serving, coding-agent harnesses, sandbox scheduling, recovery, and capacity planning.

Implementable now:
- close sessions explicitly on success, failure, cancellation, and timeout;
- measure held-environment seconds, model wait, tool wait, CPU, and idle retention separately;
- checkpoint setup at semantic block boundaries with verified outputs;
- resume from the last accepted checkpoint rather than replaying the entire trajectory;
- schedule scarce devices below the model through a deterministic runtime queue;
- version harness logic and evaluate harness changes like application changes.

Artifact status: [agent-runtime-capacity](https://github.com/MEKHALA/agent-runtime-capacity) and [pheragent](https://github.com/BeeuniLab/pheragent) have populated repositories inspected read-only. The broader multiplexing and learnable-harness claims still require architecture and replication.

Evidence limit: the capacity study is narrow and partly simulation-based. Evolving harnesses can optimize benchmarks without improving operational behavior unless the acceptance suite covers real failure modes.

Implementability score: 0.82

Core sources: [Held While Waiting v1](https://arxiv.org/abs/2611.26480v1), [HerAgent v1](https://arxiv.org/abs/2611.18443v1), [ModHarness-RL v1](https://arxiv.org/abs/2611.18533v1), [Metal Sandbox v1](https://arxiv.org/abs/2611.17294v1)

## Working conclusion

The implementable unit is the explicit runtime object: a candidate update with an incumbent, a memory with lineage, and a session with lifecycle state. Once those objects exist, promotion, retrieval, recovery, and capacity become measurable control problems.
