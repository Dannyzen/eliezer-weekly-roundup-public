# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-08

### Kotlin SWE-bench makes language-specific coding-agent eval executable

Summary: JetBrains released a public Kotlin benchmark for coding agents with 105 repository-level tasks, Harbor task packaging, containerized validation, and a leaderboard. The value is not only Kotlin coverage. It is the repeatable task-pack shape for evaluating agents on a real language ecosystem.

Analysis: [daily reasoning analysis](2026-07-08/reasoning.md#kotlin-swe-bench-makes-language-specific-agent-eval-executable)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [JetBrains release post](https://blog.jetbrains.com/kotlin/2026/07/introducing-the-kotlin-benchmark-evaluate-ai-coding-agents-on-real-world-kotlin-tasks/), [Kotlin SWE-bench repo](https://github.com/Kotlin/kotlin-swe-bench), [Kotlin Benchmark leaderboard](https://kotlinlang.org/benchmark/)
Implementable now:
- copy the Harbor task-pack shape for one internal repository
- record base commit, issue instruction, hidden tests, validation command, agent/model config, cost, and wall time
- compare agents on domain-specific tasks instead of vendor demos
Tools, repos, and methodologies worth exploring:
- `Kotlin/kotlin-swe-bench`, Multi-SWE-bench, Harbor task format, per-language replay packs, leaderboard-style run metadata
Implementability score: 0.90

### StateFuse makes multi-agent memory conflict-preserving instead of last-write-wins

Summary: StateFuse gives multi-agent memory a deterministic, conflict-preserving contract. It stores immutable operations, explicit conflicts, evidence-linked claims, correction handles, and deterministic projections so disagreement remains inspectable.

Analysis: [daily reasoning analysis](2026-07-08/reasoning.md#statefuse-makes-multi-agent-memory-conflict-preserving-instead-of-last-write-wins)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md)
Core sources: [StateFuse paper](https://arxiv.org/abs/2607.05844v1), [StateFuse repo](https://github.com/nZiben/statefuse)
Implementable now:
- keep immutable memory operations instead of destructive overwrites
- represent conflicts as objects with provenance and evidence links
- use exact and semantic correction handles for repairs
- materialize workflow-specific views from the same canonical log
Tools, repos, and methodologies worth exploring:
- `nZiben/statefuse`, OpSet/CRDT merges, claim IDs, semantic claim references, conflict objects, deterministic materializers
Implementability score: 0.80

## Supporting recent AgenticAI context

The 2026-07-07 scan focused on untrusted boundary engineering. The 2026-07-08 scan adds two buildable substrates: executable domain-specific replay packs for coding agents, and conflict-preserving shared memory for multi-agent systems.
