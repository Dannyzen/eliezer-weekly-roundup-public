# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-07-03

### AgenticSTS turns memory into an ablatable contract

Summary: AgenticSTS frames long-horizon agent memory as a visibility contract. Each decision is assembled from typed retrieval into a fresh prompt rather than by appending the raw cross-decision transcript, which makes memory layers bounded, auditable, and ablation-ready.

Analysis: [daily reasoning analysis](2026-07-03/reasoning.md#agenticsts-turns-memory-into-an-ablatable-contract)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Context Economy](context-economy/context-economy.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [AgenticSTS](https://arxiv.org/abs/2607.02255v1)
Implementable now:
- define memory visibility as a per-decision contract
- store prompt records, retrieved item IDs, memory layer IDs, and skill snapshot IDs
- run no-store, full-history, typed-retrieval, and skill-triggered ablations on the same long-horizon task
- score memory by downstream decision quality, not only retrieval relevance
Tools, repos, and methodologies worth exploring:
- typed retrieval layers, condition-tagged trajectories, frozen memory snapshots, prompt records, memory-layer ablations
Implementability score: 0.72

## Supporting recent AgenticAI context

The 2026-06-26 weekly synthesis remains the broad current implementation map: [weekly reasoning analysis](2026-06-26/reasoning.md). The 2026-07-02 scan made proof-bearing artifacts explicit with memory actions, source-only patches, benchmark replays, and skill dependency graphs. The 2026-07-03 scan narrows the memory lesson: useful long-horizon memory needs per-decision visibility contracts and ablation-ready traces, not unbounded transcript stuffing.
