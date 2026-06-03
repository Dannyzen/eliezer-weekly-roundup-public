# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-03 Daily Scan

### SkillGuard turns skills into permission-bearing runtime artifacts
Summary: SkillGuard adds the missing runtime-control layer for agent skills: context influence and action side effects should both be governed by a skill-specific manifest, authorization policy, and trace evidence.

Analysis: [daily reasoning analysis](2026-06-03/reasoning.md#skillguard-turns-skills-into-permission-bearing-runtime-artifacts)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [SkillGuard](https://arxiv.org/abs/2606.03024v1)
Implementable now:
- add skill manifests with context, tool, file, network, memory-write, and approval scopes;
- record loaded body and manifest hashes;
- bind tool calls, file writes, memory writes, and external observations to the skill that influenced them;
- deny runtime behavior that exceeds declared skill authority.
Tools, repos, and methodologies worth exploring:
- skill manifests, signed skill cards, OPA/Cedar, capability labels, OpenTelemetry trace fields, static skill scanners, semantic fuzzing, deny-by-default monitors
Implementability score: 0.78

### Deterministic memory should make pruning decisions auditable
Summary: DMF argues that memory admission, retention, decay, and pruning should be deterministic, CPU-first, and replayable instead of hidden inside write-time LLM summarization.

Analysis: [daily reasoning analysis](2026-06-03/reasoning.md#deterministic-memory-should-make-pruning-decisions-auditable)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [DMF](https://arxiv.org/abs/2606.03463v1)
Implementable now:
- preserve raw episodes and treat summaries as derived artifacts;
- compute deterministic retention scores from source, salience, recency, role, entity, action, and outcome signals;
- attach score components and provenance to each memory;
- make decay, pruning, and supersession replayable from stored events.
Tools, repos, and methodologies worth exploring:
- SQLite/Postgres event logs, pgvector/local embedding stores, deterministic feature extractors, temporal decay, provenance IDs, memory replay tests, belief-state fixtures
Implementability score: 0.80

### SPOQ makes multi-agent coding orchestration look like dependency queues, not chat
Summary: SPOQ uses dependency-wave dispatch, planning validation, code validation, human-as-agent participation, and tiered model roles. AgentLens reinforces the eval side: passing tests can still hide low-quality lucky-pass trajectories.

Analysis: [daily reasoning analysis](2026-06-03/reasoning.md#spoq-makes-multi-agent-coding-orchestration-look-like-dependency-queues-not-chat)
Durable topic: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [SPOQ](https://arxiv.org/abs/2606.03115v1), [AgentLens](https://arxiv.org/abs/2605.12925v3)
Implementable now:
- decompose coding work into typed tasks with dependency edges;
- dispatch only ready execution waves;
- add planning validation before work and artifact validation before merge;
- label process defects such as blind retry, missing verification, wasted exploration, and validation bypass.
Tools, repos, and methodologies worth exploring:
- LangGraph, Temporal, issue DAGs, typed task contracts, Pydantic task/result schemas, reviewer agents, OpenTelemetry spans, process-defect labels
Implementability score: 0.66

## Previous structured update

The prior daily scan for 2026-06-02 focused on skill lifecycle attacks, controlled transfer eval, and process/outcome separation: [2026-06-02 roundup](../roundups/2026-06-02.md).
