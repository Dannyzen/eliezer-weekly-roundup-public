# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-20

### Structured ledgers make tool state first-class

Summary: LedgerAgent turns task state into an explicit ledger of facts, identifiers, constraints, and conditions, then uses that ledger both for prompt context and pre-execution policy checks on environment-changing tools.

Analysis: [daily reasoning analysis](2026-06-20/reasoning.md#structured-ledgers-make-tool-state-first-class)
Durable topics: [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Memory Systems](memory-systems/memory-systems.md), [Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core source: [LedgerAgent](https://arxiv.org/abs/2606.20529)
Implementable now:
- define a typed task ledger with source-event IDs and validity fields
- render compact ledger state into prompts instead of replaying transcript fragments
- run deterministic policy checks before write/refund/delete/send/deploy tools
Tools, repos, and methodologies worth exploring:
- Pydantic or JSON Schema, OPA/Cedar, SQLite/Postgres projections, OpenTelemetry policy spans
Implementability score: 0.82

### Skill mining is useful as diagnosis, not autonomous skill promotion

Summary: SKILL.md trajectory mining produces readable candidate skill clusters, but weak transfer. The right use is candidate discovery and diagnostics, not automatic promotion into a default skill library.

Analysis: [daily reasoning analysis](2026-06-20/reasoning.md#skill-mining-is-useful-as-diagnosis-not-autonomous-skill-promotion)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [Automating SKILL.md Generation](https://arxiv.org/abs/2606.20363)
Implementable now:
- mine GUI traces for candidate skills and missing docs
- require held-out replay gains before promotion
- compare no-skill, frequency-prior, mined-skill, and reviewed-skill baselines
Tools, repos, and methodologies worth exploring:
- trajectory segmentation, clustering, InteraSkill-style labels, SkillSpector/static scans, held-out task replay
Implementability score: 0.61

### Multi-agent transactive memory treats trajectories as reusable infrastructure

Summary: MATM stores agent-generated trajectories for population-level reuse. Producer agents contribute completed traces; consumer agents retrieve relevant traces to reduce rediscovery in interactive environments.

Analysis: [daily reasoning analysis](2026-06-20/reasoning.md#multi-agent-transactive-memory-treats-trajectories-as-reusable-infrastructure)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [Multi-Agent Transactive Memory](https://arxiv.org/abs/2606.19911)
Implementable now:
- store completed trajectories with task, environment, tool sequence, state deltas, outcome, and source-agent metadata
- retrieve trajectories as examples and warnings, not blind instructions
- gate cross-agent memory by principal, tenant, data class, and deletion state
Tools, repos, and methodologies worth exploring:
- event stores, hybrid retrieval, WebArena/ALFWorld-style replay tasks, retrieval ablation tests
Implementability score: 0.68

### Enterprise multi-agent orchestration fails first on discovery noise

Summary: A production-derived enterprise orchestration study reports that scale, not task complexity, dominates performance. Agent discovery noise becomes the bottleneck, and a Task Manager with priority, merge, and preemption logic improves high-priority latency and related-event correctness.

Analysis: [daily reasoning analysis](2026-06-20/reasoning.md#enterprise-multi-agent-orchestration-fails-first-on-discovery-noise)
Durable topics: [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md)
Core source: [Autonomous Event-Driven Multi-Agent Orchestration](https://arxiv.org/abs/2606.20058)
Implementable now:
- add capability metadata and reliability scores before exposing agents to planners
- route events through priority, dedupe, merge, and preemption logic
- track queue latency, discovery failure, assignment retries, and abandoned work
Tools, repos, and methodologies worth exploring:
- Temporal, Inngest, Prefect, service-catalog patterns, OpenTelemetry routing spans
Implementability score: 0.57
