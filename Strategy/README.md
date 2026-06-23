# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-23

### AgentRiskBOM makes agent authority a machine-readable artifact

Summary: AgentRiskBOM fills the gap left by SBOM, AIBOM, and MLBOM artifacts: deployed agents need a structured record of autonomy level, tools, memory, credentials, approval gates, audit signals, delegation, and external effects.

Analysis: [daily sovereignty analysis](2026-06-23/sovereignty.md#agentriskbom-makes-agent-authority-a-machine-readable-artifact)
Durable topics: [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [AgentRiskBOM](https://arxiv.org/abs/2606.21877v1)
Implementable now:
- define a compact authority manifest for each agent workflow
- diff manifests across deployments and block unreviewed authority expansion
- map high-risk capabilities to policy checks, approvals, sandboxes, rate limits, or logging requirements
Tools, repos, and methodologies worth exploring:
- JSON Schema authority manifests, CycloneDX/SPDX adjacency, OPA, Cedar, OpenFGA, OpenTelemetry authority spans, CI authority-drift checks
Implementability score: 0.82

### PORTICO closes the lingering-authority gap with revocable capabilities

Summary: Lingering Authority shows that coding agents often retain file, git, network, or write authority after the subgoal that justified it has closed. PORTICO uses task contracts, closure predicates, and epoch-bound handles to revoke temporary capabilities.

Analysis: [daily sovereignty analysis](2026-06-23/sovereignty.md#portico-closes-the-lingering-authority-gap-with-revocable-capabilities)
Durable topics: [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Lingering Authority](https://arxiv.org/abs/2606.22504v1)
Implementable now:
- issue opaque capability handles instead of exposing broad credentials or ambient tool access
- bind grants to principal, workflow, tool, resource, effect, and epoch
- remove closed handles from the next planner context and reject stale replay before execution
Tools, repos, and methodologies worth exploring:
- reference monitors, typed tool catalogs, task contracts, OPA/Cedar policies over task stage and capability epoch, scoped git/filesystem/network grants, OpenTelemetry grant and closure events
Implementability score: 0.76
