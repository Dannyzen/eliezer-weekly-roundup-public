# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-19

### Mutation authority belongs in brokers, not agents

Summary: Sovereign Execution Brokers moves the authority boundary from agent-held credentials to a broker that verifies signed action certificates at mutation time. DeepMind's AI Control Roadmap supplies the operating metrics: coverage, recall, and time-to-response.

Analysis: [daily sovereignty analysis](2026-06-19/sovereignty.md#mutation-authority-belongs-in-brokers-not-agents)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Sovereign Execution Brokers](https://arxiv.org/abs/2606.20520v1), [Google DeepMind AI Control Roadmap](https://deepmind.google/blog/securing-the-future-of-ai-agents/)
Implementable now:
- remove standing write credentials from agent runtimes where possible
- require broker validation before production mutation APIs accept an action
- verify action contract, principal, resource scope, policy epoch, revocation epoch, and live-state hash
- mint short-lived scoped credentials only after validation
Tools, repos, and methodologies worth exploring:
- AWS STS, Kubernetes TokenRequest, workload identity, OPA, Cedar, signed certificates, OpenTelemetry traces
Implementability score: 0.68

### Capability discovery is becoming a governed supply chain

Summary: Agentic Resource Discovery turns capability lookup into a registry/search problem, and ToolPro turns multi-step execution into an effect-typed program problem. Discovery and execution are now gateway-owned authority surfaces, not convenience features.

Analysis: [daily sovereignty analysis](2026-06-19/sovereignty.md#capability-discovery-is-becoming-a-governed-supply-chain)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core sources: [Agentic Resource Discovery](https://huggingface.co/blog/agentic-resource-discovery-launch), [hf-discover](https://github.com/huggingface/hf-discover), [ToolPro](https://arxiv.org/abs/2606.19992v1)
Implementable now:
- make capability discovery permissioned by principal, tenant, workflow, and data class
- require source metadata and manifest hashes for tools, skills, and MCP cards
- log registry query, selected capability, generated artifact, and compiled program hash
- gate WRITE effects and service-side program execution through policy
Tools, repos, and methodologies worth exploring:
- hf-discover, ARD-style registries, MCP gateways, signed manifests, effect-typed workflow DSLs, policy-as-code
Implementability score: 0.73

### Safety claims need deployment-shaped evidence

Summary: SafeClawBench, OpenAI Deployment Simulation, and DeepMind AI Control converge on the same rule: match evidence to the deployment claim. Refusal rates, benchmark scores, and red-team anecdotes are not enough for tool agents with real side effects.

Analysis: [daily sovereignty analysis](2026-06-19/sovereignty.md#safety-claims-need-deployment-shaped-evidence)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md), [Trajectory-Aware Evaluation](../AgenticAI/trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [SafeClawBench](https://arxiv.org/abs/2606.18356v1), [OpenAI Deployment Simulation](https://openai.com/index/deployment-simulation), [Google DeepMind AI Control Roadmap](https://deepmind.google/blog/securing-the-future-of-ai-agents/)
Implementable now:
- separate refusal, audit evidence, sandbox state mutation, and deployment-like incidence estimates
- sample representative historical workflows before release
- tag eval results with traffic slice, tool set, scaffold, model, policy, and environment state
- report monitor coverage, recall, false positives, and time-to-response
Tools, repos, and methodologies worth exploring:
- SafeClawBench, deployment simulation, AI control metrics, sandbox state oracles, release gates with representative-distribution checks
Implementability score: 0.75

## Previous structured update: Daily scan, 2026-06-18

### Contract-mediated tool control is the strategic runtime boundary

Summary: ContractGuard, C-Trace, and WitnessAI all point to the same operating model: put control at the tool boundary, bind policies to trace events, and block non-compliant execution before the external system observes the action.

Analysis: [daily sovereignty analysis](2026-06-18/sovereignty.md#contract-mediated-tool-control-is-the-strategic-runtime-boundary)
Core sources: [ContractGuard](https://arxiv.org/abs/2606.18550v1), [Runtime Compliance Verification for AI Agents](https://arxiv.org/abs/2606.19242v1), [WitnessAI Agentic Control](https://witness.ai/blog/introducing-witnessai-agentic-control-one-control-plane-for-every-agent-tool-and-mcp-server/)
Implementability score: 0.74

### Memory and sandbox claims need bounded governance evidence

Summary: GateMem and AI Sandboxes both reject vague safety claims. A shared-memory system is not safe if it recalls well but leaks protected data. A sandbox does not prove deployment readiness unless each required evidence dimension is measured.

Analysis: [daily sovereignty analysis](2026-06-18/sovereignty.md#memory-and-sandbox-claims-need-bounded-governance-evidence)
Core sources: [GateMem](https://arxiv.org/abs/2606.18829v1), [AI Sandboxes](https://arxiv.org/abs/2606.18532v1), [GateMem repository](https://github.com/rzhub/GateMem)
Implementability score: 0.66

### Search grounding should be owned outside the model provider

Summary: Decoupled Search Grounding separates retrieval from model-native generation through an MCP-compatible gateway, and HANSEL turns web-agent traces into user-checkable evidence breadcrumbs. Owning the evidence path is now a sovereignty move.

Analysis: [daily sovereignty analysis](2026-06-18/sovereignty.md#search-grounding-should-be-owned-outside-the-model-provider)
Core sources: [Decoupled Search Grounding](https://arxiv.org/abs/2606.18947v1), [HANSEL](https://arxiv.org/abs/2606.18671v1)
Implementability score: 0.82
