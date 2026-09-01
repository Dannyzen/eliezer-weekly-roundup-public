# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-01

### Measure working memory at four distinct layers

Summary: A 55-trajectory coding-agent study separates stored state, delivered context, management work, and task outcome. It shows that equal token budgets can hide different delivered context, serving limits, and management costs.

Analysis: [daily analysis](2026-09-01/reasoning.md#measure-working-memory-at-four-distinct-layers)
Core source: [paper](https://arxiv.org/abs/2608.31057v1)
Tools and methodologies worth exploring now: typed memory objects, delivery accounting, management-cost accounting, held-out replay, recoverable pointers, task-level outcome gates
Implementability score: 0.68

### Make hidden dependency breakage a first-class coding-agent gate

Summary: DEPBENCH isolates 203 real dependency-upgrade repair tasks with a four-state causal oracle. The best completed agent configuration solved 104 tasks, or 51.2 percent, with incomplete repository-wide migration as the dominant failure.

Analysis: [daily analysis](2026-09-01/reasoning.md#make-hidden-dependency-breakage-a-first-class-coding-agent-gate)
Core source: [paper](https://arxiv.org/abs/2608.30300v1)
Tools and methodologies worth exploring now: Dependabot and Renovate task mining, patch decomposition, held-out tests, four-state causal oracles, Harbor, repository-wide migration failure classes
Implementability score: 0.62

### Ship runtime continuity as explicit, inspectable state

Summary: Hermes Agent v0.21.0 turns cron continuity, durable notepads, live subagent steering, bot handoffs, MCP health, instruction protection, compaction recall, and repository-native verification into explicit runtime surfaces.

Analysis: [daily analysis](2026-09-01/reasoning.md#ship-runtime-continuity-as-explicit-inspectable-state)
Core source: [release](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31)
Tools and methodologies worth exploring now: `continuity=true`, monitor-mode suppression, live delegation control, protected instruction writes, compaction recall evaluation, verify-command detection
Implementability score: 0.95

## Current implication

Memory, maintenance, and orchestration should be evaluated through typed runtime objects and executable gates. Nominal token budgets, plausible patches, and successful process startup are not durable proof.
