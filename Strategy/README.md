# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-11

### Runtime governance needs a five-plane control plane
Summary: Production agents turn risk into stateful workflows. The five-plane reference architecture argues that governance needs a reasoning plane that adjudicates intent, then coordinated enforcement across network, identity, endpoint, and data planes.

Analysis: [daily sovereignty analysis](2026-06-11/sovereignty.md#runtime-governance-needs-a-five-plane-control-plane-not-per-tool-approvals)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/abs/2606.12320v1)
Implementable now:
- model composite principals for user, agent, subagent, tenant, and delegated authority;
- add stop-anywhere mediation before planning, retrieval, tool calls, effect commits, memory writes, and audit emission;
- preserve one composed evidence record per material action.
Tools, repos, and methodologies worth exploring:
- OPA, Cedar, OpenFGA, MCP gateways, identity providers, endpoint sandboxes, network egress controls, trace evidence records
Implementability score: 0.67

### Skill probes and deterministic layer tests are governance surfaces
Summary: Runtime Skill Audit and Layer-Isolated Evaluation make governance testable. Dynamic skill probes show what a skill-mediated agent actually does. Deterministic layer slices show where an agent scaffold regressed.

Analysis: [daily sovereignty analysis](2026-06-11/sovereignty.md#skill-probes-and-deterministic-layer-tests-are-governance-surfaces)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Runtime Skill Audit](https://arxiv.org/abs/2606.11671v1), [Layer-Isolated Evaluation](https://arxiv.org/abs/2606.11686v1), [snyk/agent-scan](https://github.com/snyk/agent-scan)
Implementable now:
- run risk-based skill probes before production admission;
- add no-LLM CI slices for routing, memory, safety, escalation, and tool boundaries;
- bind skill hash, probe result, policy verdict, and trace ID together.
Tools, repos, and methodologies worth exploring:
- Snyk Agent Scan, CodeQL, dependency advisory checks, secret scanning, sandbox probes, CI slice dashboards
Implementability score: 0.74

## Previous structured update

The prior daily scan for 2026-06-10 focused on executable security validation, platform-side scans, and trace-safe evidence release: [2026-06-10 roundup](../roundups/2026-06-10.md).
