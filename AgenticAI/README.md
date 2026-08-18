# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-18

### Edit-time fact coverage is the real coding context budget

Summary: Controlled migrations show that coding success depends on whether required versioned facts are available when an edit is proposed. Read volume alone cannot distinguish parametric recall, eviction, staleness, or contradiction.

Analysis: [daily analysis](2026-08-18/reasoning.md#edit-time-fact-coverage-is-the-real-coding-context-budget)
Core source: [The Working Set of a Coding Agent](https://arxiv.org/abs/2608.16630v1)
Tools and methodologies worth exploring now: coupled-fact graphs, edit-intent events, versioned fact ledgers, renamed-API tests, contradictory-source tests
Implementability score: 0.90

### Coordination should be measured as a temporal network

Summary: A 1,902-run study models agents and files as nodes and messages, reads, and writes as cost-bearing edges. The instrument exposes topology and channel substitution that task success and aggregate tokens miss.

Analysis: [daily analysis](2026-08-18/reasoning.md#coordination-should-be-measured-as-a-temporal-network)
Core sources: [When Agents Coordinate](https://arxiv.org/abs/2608.16801v1), [replication repository](https://github.com/giuseppedestefanis/when-agents-coordinate)
Tools and methodologies worth exploring now: temporal run graphs, repeated configuration cells, file-versus-message ablations, containment checks, coordination-cost metrics
Implementability score: 0.88

### OpenAI Agents SDK ships stronger run boundaries

Summary: v0.21.1 adds model-call timeouts, per-run sandbox directories, optional network-off Docker sandboxes, resource controls, and fixes for exact approvals and failure cleanup.

Analysis: [daily analysis](2026-08-18/reasoning.md#openai-agents-sdk-ships-stronger-run-boundaries)
Core source: [OpenAI Agents SDK v0.21.1](https://github.com/openai/openai-agents-python/releases/tag/v0.21.1)
Tools and methodologies worth exploring now: pinned SDK branch, model-call deadlines, run-scoped workdirs, default-deny sandbox networking, approval and cleanup regression tests
Implementability score: 0.95

## Current implication

Treat facts, coordination, and run resources as first-class runtime state. Explicit representations make coding agents and agent teams measurable, testable, and containable.
