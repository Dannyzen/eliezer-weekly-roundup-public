# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-06

### Memory has become a costed systems workload, not a recall feature
Summary: Long-horizon memory now needs systems profiling. The useful unit is not only whether an agent remembered a fact, but which construction, retrieval, update, compression, and generation costs the memory design shifted into the run.

Analysis: [daily reasoning analysis](2026-06-06/reasoning.md#memory-has-become-a-costed-systems-workload-not-a-recall-feature)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Context Economy](context-economy/context-economy.md)
Core sources: [Agent Memory](https://arxiv.org/abs/2606.06448v1), [TokenMizer](https://arxiv.org/abs/2606.06337v1), [TokenMizer repo](https://github.com/Shweta-Mishra-ai/tokenmizer)
Implementable now:
- profile memory construction, retrieval, update, and generation as separate phases;
- preserve graph or event structure for decisions, files, transitions, and rationale;
- test resume blocks for decision recall, not just token compression.
Tools, repos, and methodologies worth exploring:
- phase-aware memory profiling, typed session graphs, resume-block regression tests, source-span IDs, OpenTelemetry memory spans, TokenMizer-style compact checkpoints
Implementability score: 0.78

### Tool exposure should be a causal frontier, not a semantic search result
Summary: Tool filtering should expose the minimal next-step frontier implied by current state and goal. Relevance search over tool descriptions is too loose because it can show tools that are related, premature, or actively distracting.

Analysis: [daily reasoning analysis](2026-06-06/reasoning.md#tool-exposure-should-be-a-causal-frontier-not-a-semantic-search-result)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [ToolChoiceConfusion](https://arxiv.org/abs/2606.06284v1)
Implementable now:
- attach lightweight precondition and effect contracts to tools;
- compute the visible tool frontier from state transitions, not keyword overlap;
- log visible tool count, rejected tools, wrong-tool calls, premature actions, and token cost.
Tools, repos, and methodologies worth exploring:
- precondition-effect schemas, state machines, causal-path filtering, Pydantic tool contracts, gateway candidate logs, tool-call confusion tests
Implementability score: 0.84

## Previous structured update

The prior Friday synthesis for week ending 2026-06-05 focused on governed skills, evidence-bearing evals, memory/context evidence preservation, and dependency-wave orchestration: [2026-06-05 roundup](../roundups/2026-06-05.md).
