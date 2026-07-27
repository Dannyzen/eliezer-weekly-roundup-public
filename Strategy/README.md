# Strategy

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Monday, 2026-07-27

### Model routing should learn from terminal task outcomes

Summary: TRACE-ROUTER assigns one backend at task admission and learns from terminal accuracy-latency reward. It reports strong benchmark deltas, but we found no paper-owned public implementation artifact as of 2026-07-27, and it does not solve sparse or gameable production rewards.

Analysis: [daily sovereignty analysis](2026-07-27/sovereignty.md#model-routing-should-learn-from-terminal-task-outcomes)
Core source: [paper](https://arxiv.org/abs/2607.22465v1)
Implementable now:
- emit task-level routing receipts;
- shadow task pinning against static, per-call, cascade, and stage-aware baselines;
- keep explicit failover and escalation paths;
- require trustworthy terminal outcome and latency signals before online updates.
Tools, repositories, and methodologies:
- LiteLLM, contextual bandits, OpenTelemetry, task manifests, shadow routing, Pareto analysis
Implementability score: 0.45

## Current implication

Match the routing decision to the outcome boundary, but treat model pinning as a shadowed policy until reward quality, escalation, and failover are proven.
