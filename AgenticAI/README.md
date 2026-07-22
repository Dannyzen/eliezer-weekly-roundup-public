# AgenticAI

This index tracks the most recent structured update. Each finding includes a summary, a link into the detailed analysis, core sources, practical implementation paths, and an implementability score from 0 to 1.

## Most Recent Structured Update: Wednesday, 2026-07-22

### Stable harnesses make the default runtime a product surface

Summary: Microsoft Agent Framework graduated its harness to stable in Python and .NET. Planning state, per-service-call persistence, compaction, file memory, skills, approvals, web search, and OpenTelemetry now have one versioned open-source composition.

Analysis: [daily reasoning analysis](2026-07-22/reasoning.md#stable-harnesses-make-the-default-runtime-a-product-surface)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md#july-22-update-stable-harnesses-make-the-default-runtime-a-versioned-product-surface)
Core sources: [announcement](https://devblogs.microsoft.com/agent-framework/the-microsoft-agent-framework-harness-is-now-released/), [Python 1.12.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.12.0), [.NET 1.14.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.14.0)
Implementable now:
- build one reference agent on the stable core;
- export tool, compaction, approval, todo, and history events through OpenTelemetry;
- keep file, shell, loop, and background authority outside the default profile;
- run crash, resume, compaction, approval-replay, and tool-collision fixtures.
Tools, repositories, and methodologies:
- `microsoft/agent-framework`, Python 1.12.0, .NET 1.14.0, OpenTelemetry, differential harness evaluation
Implementability score: 0.90

### Debugging needs exact attribution and rerun closure

Summary: AgentDebugX improves strict agent-and-step attribution from 21.7% to 28.8% and repairs 13 of 73 GAIA failures in one rerun. The absolute attribution rate shows the hard part: plausible diagnosis is not reliable causal localization.

Analysis: [daily reasoning analysis](2026-07-22/reasoning.md#debugging-needs-exact-attribution-and-rerun-closure)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md#july-22-update-debugging-needs-exact-attribution-and-rerun-closure)
Core sources: [paper](https://arxiv.org/abs/2607.18754v1), [repository](https://github.com/AgentDebugX/AgentDebugX), [project site](https://www.agentdebugx.com/)
Implementable now:
- normalize one framework trace into a portable event schema;
- label symptom, causal step, responsible agent, and repair point;
- rerun from a checkpoint and score the resulting state;
- keep incident sharing opt-in and scrubbed.
Tools, repositories, and methodologies:
- AgentDebugX 0.3.1, OpenTelemetry, causal trace slices, checkpointed reruns, local incident bundles
Implementability score: 0.82

### Failed coding attempts need budget-calibrated recovery routing

Summary: a failed cheap-model attempt should not always escalate. CodeRescue routes among reflection, replanning, and escalation, then calibrates the expected-cost frontier without retraining.

Analysis: [daily reasoning analysis](2026-07-22/reasoning.md#failed-coding-attempts-need-budget-calibrated-recovery-routing)
Durable topic: [Model Router Governance](../Strategy/model-router-governance/model-router-governance.md#july-22-update-recovery-routing-needs-a-budgeted-action-frontier)
Core sources: [paper](https://arxiv.org/abs/2607.19338v1), [repository](https://github.com/Qijia-He/agent-budget-control)
Implementable now:
- replay failures against reflect, replan, and escalate actions;
- log failure class, action, solve result, latency, and cost;
- start with auditable rules, then calibrate and shadow a learned policy;
- treat the repository as methodology-only until it has explicit reuse terms.
Tools, repositories, and methodologies:
- conformal risk control, offline trajectory replay, cost frontiers, shadow routing
Implementability score: 0.64

## Current implication

The harness, debugger, and router should share one run identity. Preserve state and approvals, localize the causal failure, choose a bounded recovery action, rerun, and attach the result to the original trace.
