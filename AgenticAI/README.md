# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-17

### Compile tool calls from request-bound choices

Summary: System 1 Agents turns schemas and request values into finite decisions, then lets deterministic code assemble and replay the call.

Analysis: [Daily analysis](2026-11-17/reasoning.md#1-compile-tool-calls-from-request-bound-choices)

Core source: [System 1 Agents v1](https://arxiv.org/abs/2611.21053v1)

Implementable now:
- typed choices from JSON Schema
- request-bound value extraction
- explicit decline and clarification thresholds
- compiler-oracle and replay regression tests

Implementability score: 0.84

### Put deterministic acceptance around agent search

Summary: Agent-guided cvc5 tuning lets models propose bounded changes while a fixed harness measures, validates, and promotes per-workload incumbents.

Analysis: [Daily analysis](2026-11-17/reasoning.md#2-let-agents-propose-then-let-the-harness-accept)

Core source: [SMT solver tuning v1](https://arxiv.org/abs/2611.20484v1)

Implementable now:
- typed proposal surfaces
- persistent experiment records
- full-group semantic validation
- immutable promotion receipts

Implementability score: 0.68

### Retrieve memory by downstream utility

Summary: Jetriever scores whether each memory helps answer the current query, catching implicit associations that similarity search misses.

Analysis: [Daily analysis](2026-11-17/reasoning.md#3-retrieve-memory-by-downstream-utility-with-a-scale-gate)

Core source: [Jetriever v1](https://arxiv.org/abs/2611.21478v1)

Implementable now:
- stable raw-memory IDs
- calibrated utility scoring
- cheap candidate filtering before reranking
- cost, latency, and answer-effect traces

Implementability score: 0.60

## Current working model

1. Let models judge finite choices and propose bounded changes.
2. Keep action assembly and promotion in deterministic code.
3. Validate semantic effects over the complete target group.
4. Preserve experiment and decision receipts for replay.
5. Use utility reranking only over a bounded memory candidate set.

## Browse

- [Daily roundup](../roundups/2026-11-17.md)
- [Daily analysis](2026-11-17/reasoning.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
