# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-28

### Knowledge-based pull requests make external code evidence, not authority

Summary: External agent work should cross project boundaries as a provenance-bearing knowledge package, not as the default merge candidate. KPR separates knowledge acceptance from code acceptance, then lets a project-owned inner agent regenerate code inside the receiving repository's policy, tests, and conventions.

Analysis: [daily reasoning analysis](2026-06-28/reasoning.md#knowledge-based-pull-requests-make-external-code-evidence-not-authority)
Durable topics: [Ticket-Native Agent Orchestration](ticket-native-agent-orchestration/ticket-native-agent-orchestration.md), [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md)
Core source: [Knowledge-Based Pull Requests](https://arxiv.org/abs/2606.26721v1)
Implementable now:
- define a KPR package schema with claim, evidence, tests, risk, constraints, uncertainty, and trace fields
- accept external diffs as evidence, not direct merge candidates, for high-context contributions
- run an internal coding agent in a clean checkout after human knowledge acceptance
- compare regenerated code against the accepted knowledge package and project-side tests
Tools, repos, and methodologies worth exploring:
- GitHub Issues or Linear state machines, structured reviewer briefs, risk checklists, clean worktrees, branch protection, CODEOWNERS, CI, secret scanning, dependency scanning
Implementability score: 0.72

### Temporal validity turns memory updates into ledger operations

Summary: Stale facts are write-path failures. MemStrata shows vector similarity cannot reliably separate contradictions from duplicates, then uses deterministic subject-relation-object supersession in a bi-temporal ledger to retire stale values before retrieval.

Analysis: [daily reasoning analysis](2026-06-28/reasoning.md#temporal-validity-turns-memory-updates-into-ledger-operations)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Context Economy for Agents](context-economy/context-economy.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [Temporal Validity in Retrieval Memory](https://arxiv.org/abs/2606.26511v1)
Implementable now:
- add valid-from, valid-until, superseded-by, source event, and writer principal fields to structured memories
- apply deterministic supersession for typed project facts, preferences, config values, and API metadata
- preserve retired values as lineage rather than deleting them
- add marker-free stale-fact tests to memory evals
Tools, repos, and methodologies worth exploring:
- SQLite or Postgres bi-temporal ledgers, append-only memory events, active fact projections, write-path contradiction checks, stale-fact benchmarks
Implementability score: 0.83

## Supporting recent AgenticAI context

The 2026-06-26 weekly synthesis remains the broadest current map: [weekly reasoning analysis](2026-06-26/reasoning.md). The 2026-06-27 daily scan tightened loop economics and workflow harnesses. The new 2026-06-28 scan tightens boundary objects: external code becomes evidence packages, and memory updates become ledger mutations.
