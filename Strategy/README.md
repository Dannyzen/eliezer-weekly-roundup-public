# Strategy

This index tracks the most recent structured update. Each finding includes a summary, a link into the detailed analysis, core sources, practical implementation paths, and an implementability score from 0 to 1.

## Most Recent Structured Update: Thursday, 2026-07-23

### Privilege separation needs a bounded residual channel

Summary: Twin Agent separates untrusted exploration from privileged execution and passes only compact, state-conditioned hints. Reported utility stays high while attack success falls sharply, but compact text remains an attack channel and no public artifact URL resolved.

Analysis: [daily sovereignty analysis](2026-07-23/sovereignty.md#privilege-separation-needs-a-bounded-residual-channel)
Durable topic: [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md#july-23-update-privileged-agents-need-bounded-residual-input)
Core source: [paper](https://arxiv.org/abs/2607.19595v1)
Implementable now:
- split one workflow into untrusted explore and privileged execute principals;
- use a typed hint schema and strict size budget;
- bind privileged calls to goal, target, policy, and hint provenance;
- test adaptive attacks and deny raw-context requests.
Tools, repositories, and methodologies:
- dual-agent privilege separation, typed hint schemas, AgentDojo, SWE-bench injection, OPA or Cedar
Implementability score: 0.66

### Inter-agent channels need application-owned gates and attribution

Summary: ChannelGuard shows that safe outcomes can be borrowed from provider filters. Every planner, tool, memory, verifier, and synthesis handoff needs application-owned telemetry and replay, but the proposed embedding defense fails under adaptive paraphrase.

Analysis: [daily sovereignty analysis](2026-07-23/sovereignty.md#inter-agent-channels-need-application-owned-gates-and-attribution)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md#july-23-update-inter-agent-channels-need-attribution)
Core source: [paper](https://arxiv.org/abs/2607.19430v1)
Implementable now:
- add boundary spans for user, tool, memory, worker, verifier, and synthesis channels;
- attribute every safe stop to the exact layer and policy version;
- replay identical attacks across providers;
- retain exact-effect authorization below text filters.
Tools, repositories, and methodologies:
- OpenTelemetry, provider counterfactual replay, semantic gates, perturbation tests, policy receipts
Implementability score: 0.58

## Current implication

Treat every context crossing as a policy event. Minimize what crosses into privileged state, record which layer stopped unsafe behavior, and keep exact-effect enforcement below all text defenses.
