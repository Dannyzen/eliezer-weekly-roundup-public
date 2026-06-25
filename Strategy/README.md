# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-25

### Execution-time safety kernels move alignment below prompts

Summary: The Unfireable Safety Kernel argues that agent controls inside the agent runtime are reachable by the thing being controlled. Serious safety needs process separation, pre-action only-path enforcement, fail-closed behavior, and external evidence before privileged tools execute.

Analysis: [daily sovereignty analysis](2026-06-25/sovereignty.md#execution-time-safety-kernels-move-alignment-below-prompts)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core source: [The Unfireable Safety Kernel](https://arxiv.org/abs/2606.26057v1)
Supporting source: [Can Trustless Agents Be Trusted?](https://arxiv.org/abs/2606.26028v1)
Implementable now:
- wrap one high-risk tool with an external reference monitor
- force all side-effecting calls through the monitor, not the agent process
- fail closed on policy timeout, missing scope, parse failure, stale epoch, or missing approval
- preserve signed or tamper-evident policy verdicts in the trace
Tools, repos, and methodologies worth exploring:
- reference monitors, policy-as-code, broker-only mutation paths, signed policy verdicts, fail-closed tests, self-modification bypass fixtures
Implementability score: 0.54

## Supporting recent Strategy context

The 2026-06-24 Deep Dive Wednesday update remains the strongest durable Strategy addition this week: [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md).
