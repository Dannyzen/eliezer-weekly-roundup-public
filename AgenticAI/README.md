# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-13

### Preserve evidence across delegation boundaries

Summary: Lost in Delegation found no consistent accuracy gain from forced delegated search and larger failures on post-cutoff facts. Orchestrators distorted queries, lost retrieval failures, and overrode executor evidence with stale priors.

Analysis: [Daily analysis](2026-11-13/reasoning.md#1-delegate-only-when-the-orchestrator-can-preserve-the-evidence-contract)

Durable topic: [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)

Core source: [Lost in Delegation paper v1](https://arxiv.org/abs/2611.16526v1)

Implementable now:
- lossless source-question handoffs
- returned sources, failures, and uncertainty
- direct-tool baselines under equal budgets
- parent-owned evidence integration

Implementability score: 0.83

### Test tool decisions against explicit state

Summary: StateAlign pairs near-identical states that require different actions, then trains with outcome and state-contrastive rewards. The cheaper transferable pattern is to grade call, ask, retrieve, decline, continue, and stop decisions separately from task success.

Analysis: [Daily analysis](2026-11-13/reasoning.md#2-train-and-test-tool-decisions-against-explicit-task-state)

Durable topic: [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)

Core sources: [StateAlign paper v1](https://arxiv.org/abs/2611.16304v1), [repository](https://github.com/ZhexiLu/StateAlign)

Implementable now:
- one-condition state contrasts
- action-appropriateness grading
- tool-error recovery fixtures
- deterministic runtime guards

Implementability score: 0.63

### Turn memory hazards into deterministic scenarios

Summary: AstroMemBench maps operational challenges to 2,240 history-dependent tests with deterministic scores for completion, state, safety, and resources. This is a reusable memory-evaluation design method rather than a generic recall leaderboard.

Analysis: [Daily analysis](2026-11-13/reasoning.md#3-turn-memory-requirements-into-deterministic-scenario-tests)

Durable topic: [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)

Core sources: [AstroMemBench paper v1](https://arxiv.org/abs/2611.16590v1), [repository](https://github.com/flyingView/AstroMemBench-v1)

Implementable now:
- Scenario-Challenge-Capability test design
- matched clean, noisy, compacted, and restarted histories
- separate completion, state, safety, and resource scores
- deterministic regression receipts

Implementability score: 0.82

### Search memory designs under accuracy and cost

Summary: MAPE evolves complete memory programs through stable lifecycle interfaces. It reports up to 12 points of absolute accuracy gain at 35 percent of baseline serving cost and repeatedly discovers raw-evidence retention plus query-specific composition.

Analysis: [Daily analysis](2026-11-13/reasoning.md#4-evolve-memory-programs-under-an-accuracy-cost-objective)

Durable topic: [Memory systems](memory-systems/memory-systems.md)

Core sources: [MAPE paper v1](https://arxiv.org/abs/2611.17068v1), [repository](https://github.com/ash-ding/MAPE)

Implementable now:
- stable build, retrieve, compose, and answer interfaces
- raw evidence beside derived memory
- fixed evaluation conditions
- joint accuracy and serving-cost objectives
- candidate lineage and failure attribution

Implementability score: 0.58

## Current working model

1. Preserve the source question, evidence, failures, and uncertainty across delegation boundaries.
2. Grade tool actions against explicit state before grading final success.
3. Convert operational memory hazards into deterministic history-dependent tests.
4. Keep raw evidence canonical and derived memory reversible.
5. Optimize memory and orchestration programs for quality and lifecycle cost together.

## Browse

- [Latest roundup](../roundups/2026-11-13.md)
- [Latest dated analysis](2026-11-13/reasoning.md)
- [Friday synthesis](2026-11-06/reasoning.md)
- [Decision-state compilation](decision-state-compilation/decision-state-compilation.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Evidence-linked memory](evidence-linked-memory/evidence-linked-memory.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Skills as control](skills-as-control/skills-as-control.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
