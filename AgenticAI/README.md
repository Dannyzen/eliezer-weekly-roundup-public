# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-15 Daily Scan

The current implementation signal is that task success and user-visible reporting need separate gates. Retain the execution record, test what the report preserves, and connect runtime monitors through explicit effect boundaries.

### Measure task-state recoverability from reports

Summary: Across 37 coding tasks and 4,799 valid probes, CTXGAP reports 92.7% task-state recovery from full execution context and 52.0% from accumulated reports. Full terminal scrollback reaches 73.6%, so more visible logs help without closing the gap.

Analysis: [dated analysis](2026-10-15/reasoning.md#ctxgap-grade-report-recoverability-as-its-own-dimension)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md#october-15-2026-grade-what-reports-preserve-not-only-whether-the-task-succeeds)
Core sources: [paper v1](https://arxiv.org/abs/2610.20003v1), [public benchmark repository](https://github.com/Kaguraaaaaa/Ctxgap)
Tools and methodologies worth exploring now: task-state atoms, paired report and trajectory probes, frozen judge prompts, terminal-view ablations, privacy audits, report-rewrite gates
Implementability score: 0.82

### Put heterogeneous monitors behind one event and reaction contract

Summary: AgenticRV normalizes LangGraph, MCP, and A2A events, gives each monitor an authorized projection, normalizes native verdicts, and applies reactions only where the adapter can actually interpose. The public alpha includes 179 passing repository tests.

Analysis: [dated analysis](2026-10-15/reasoning.md#agenticrv-separate-event-collection-from-monitor-logic)
Durable topic: [Runtime Governance](../Strategy/runtime-governance/runtime-governance.md#october-15-2026-normalize-observations-then-interpose-at-effect-boundaries)
Core sources: [paper v1](https://arxiv.org/abs/2610.19818v1), [MIT-licensed implementation](https://github.com/AngeloFerrando/agentic-rv)
Tools and methodologies worth exploring now: versioned event envelopes, monitor-specific projections, normalized verdicts, deny-overrides arbitration, blocked-effect tests, recovery-after-rejection tests
Implementability score: 0.76

## Current implication

Treat the report as a derived view and the event stream as the operational record. Test both: one for recoverable supervision state, the other for authority over realized effects.

Latest roundup: [2026-10-15 daily scan](../roundups/2026-10-15.md).
