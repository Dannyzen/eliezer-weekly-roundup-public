# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-26 Daily Scan

### Personalized memory needs storage gates, not static retention
Summary: PerMemBench and Personalize-then-Store make memory write policy personal. Different users and tasks need different retention behavior, so the next practical memory primitive is session-level storage gating before durable writes.

Analysis: [daily reasoning analysis](2026-05-26/reasoning.md#personalized-memory-needs-storage-gates-not-static-retention)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [Personalize-then-Store](https://arxiv.org/abs/2605.25535)
Implementable now:
- classify sessions before durable memory writes;
- preserve raw episode evidence while storing derived memories with admission reasons;
- evaluate personalized retention under fixed token and retrieval budgets.
Tools, repos, and methodologies worth exploring:
- MemRouter-style write admission, MEMTIER-style tiers, SQLite/FTS, typed memory records, mem0/Qdrant/pgvector only after write policy exists, `fleet-memory` and `uncypher-context` as early watchlist repos
Implementability score: 0.72

### Skill libraries need selection discipline before self-evolution
Summary: CODESKILL shows how coding-agent trajectories can become reusable procedural skills; Skill Shadowing shows why bigger skill libraries can make agents worse. The bottleneck is selecting the right skill, not context length.

Analysis: [daily reasoning analysis](2026-05-26/reasoning.md#skill-libraries-need-selection-discipline-before-self-evolution)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [CODESKILL](https://arxiv.org/abs/2605.25430), [More Skills, Worse Agents?](https://arxiv.org/abs/2605.24050)
Implementable now:
- trace selected and rejected skills, loaded bodies, hashes, and task outcomes;
- compare no-skill, thin-skill, and full-skill baselines;
- accept generated or self-edited skills only after held-out improvement.
Tools, repos, and methodologies worth exploring:
- skill metadata indexes, reranking, load/no-load gates, held-out validation tasks, rejected-skill buffers, Git-backed review and rollback
Implementability score: 0.74

### Computer-use agents need verifiable environments, not more screenshots
Summary: CUA-Gym, MobileGym, and AgentHijack all move computer-use agents toward deterministic state checks, executable reward functions, parallel synthetic environments, and ordinary-corruption robustness tests.

Analysis: [daily reasoning analysis](2026-05-26/reasoning.md#computer-use-agents-need-verifiable-environments-not-more-screenshots)
Durable topic: [GUI-Tool Path Orchestration](gui-tool-path-orchestration/gui-tool-path-orchestration.md)
Core sources: [CUA-Gym](https://arxiv.org/abs/2605.25624), [MobileGym](https://arxiv.org/abs/2605.26114), [AgentHijack](https://arxiv.org/abs/2605.25707)
Implementable now:
- build small deterministic GUI/browser/mobile task fixtures;
- add popup, resolution, focus, stale-tab, and modal corruption cells;
- score final state, path length, verification, recovery, and side effects separately.
Tools, repos, and methodologies worth exploring:
- Playwright workspaces, OSWorld-style state snapshots, JSON state diffing, executable reward functions, OpenTelemetry/Langfuse/LangSmith or JSONL path traces
Implementability score: 0.60

## Previous structured update

The prior daily scan for 2026-05-25 focused on quantitative goal-persistence ledgers, operations-agent fault-injection harnesses, and skill validation/auditing: [2026-05-25 reasoning](2026-05-25/reasoning.md).
