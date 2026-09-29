# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-29 Daily Scan

Tuesday's listing strengthens three runtime primitives: validated security harnesses, signed intervention ledgers, and typed execution-state memory.

### Prove payload delivery and score the exact effect

Summary: An indirect prompt-injection harness audit found silent payload non-delivery, identity-only scoring, environment mismatch, and missing audit trails. Corrected scoring changed attack success from 21.7% to 1.2%.

Analysis: [daily analysis](2026-09-29/reasoning.md#prove-payload-delivery-and-score-the-exact-effect)
Durable deep dives: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Incident Replay Testing](incident-replay-testing/incident-replay-testing.md)
Core source: [Silent Failures in Agentic Security Evaluation](https://arxiv.org/abs/2609.32691v1)
Tools and methodologies worth exploring now: payload-delivery receipts, argument-level effect predicates, environment conformance, replayable traces
Implementability score: 0.94

### Judge deterministic controls by signed intervention utility

Summary: Maat found 35 false alarms among 94 governed halts. DebateLedger found that a freeze prevented 29 harmful collapses while losing 108 useful corrections. Stop counts are insufficient.

Analysis: [daily analysis](2026-09-29/reasoning.md#judge-deterministic-controls-by-signed-intervention-utility)
Durable deep dives: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [Maat](https://arxiv.org/abs/2609.34017v1), [Measuring Collapse and Correction](https://arxiv.org/abs/2609.35279v1)
Tools and repositories worth exploring now: [Maat benchmarks](https://github.com/Lorelys/maat-benchmarks), [DebateLedger](https://github.com/LiXin97/DebateLedger), paired replay, signed intervention utility
Implementability score: 0.86

### Treat execution state as memory

Summary: FlowState stores typed state nodes and references to raw tool observations, then retrieves older evidence on demand. It reports higher task success with roughly 40% lower token use than full context.

Analysis: [daily analysis](2026-09-29/reasoning.md#treat-execution-state-as-memory)
Durable deep dives: [Memory Systems](memory-systems/memory-systems.md), [Context Economy](context-economy/context-economy.md)
Core source: [FlowState](https://arxiv.org/abs/2609.34565v1)
Tools and methodologies worth exploring now: typed state graphs, incremental state updates, progressive evidence access, immutable observation logs
Implementability score: 0.74

## Current implication

Prove that stimuli arrived, score the exact effect, and measure whether controls blocked more harm than recovery. Keep the resulting evidence available through typed execution state instead of replaying every token.

Friday synthesis remains the current week-level map: [2026-09-25 reasoning](2026-09-25/reasoning.md).
