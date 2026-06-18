# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-18

### Contract-mediated tool control is the strategic runtime boundary

Summary: ContractGuard, C-Trace, and WitnessAI all point to the same operating model: put control at the tool boundary, bind policies to trace events, and block non-compliant execution before the external system observes the action.

Analysis: [daily sovereignty analysis](2026-06-18/sovereignty.md#contract-mediated-tool-control-is-the-strategic-runtime-boundary)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core sources: [ContractGuard](https://arxiv.org/abs/2606.18550v1), [Runtime Compliance Verification for AI Agents](https://arxiv.org/abs/2606.19242v1), [WitnessAI Agentic Control](https://witness.ai/blog/introducing-witnessai-agentic-control-one-control-plane-for-every-agent-tool-and-mcp-server/)
Implementable now:
- inventory agents, MCP servers, tools, and downstream systems
- sign or pin tool contracts and log manifest hashes in traces
- express policy over principal, scope, purpose, data class, and declared effects
- intercept tool calls and model outputs before external mutation
Tools, repos, and methodologies worth exploring:
- OPA, Cedar, signed tool registries, MCP gateways, OpenTelemetry spans, attack-dialogue replay, contract-mutation fixtures
Implementability score: 0.74

### Memory and sandbox claims need bounded governance evidence

Summary: GateMem and AI Sandboxes both reject vague safety claims. A shared-memory system is not safe if it recalls well but leaks protected data. A sandbox does not prove deployment readiness unless each required evidence dimension is measured.

Analysis: [daily sovereignty analysis](2026-06-18/sovereignty.md#memory-and-sandbox-claims-need-bounded-governance-evidence)
Durable topics: [Shared-State Agents](shared-state-agents/shared-state-agents.md), [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Memory Systems](../AgenticAI/memory-systems/memory-systems.md)
Core sources: [GateMem](https://arxiv.org/abs/2606.18829v1), [AI Sandboxes](https://arxiv.org/abs/2606.18532v1), [GateMem repository](https://github.com/rzhub/GateMem)
Implementable now:
- define bounded claims before deployment
- score memory on utility, leakage, and deleted-info reconstruction
- score sandboxes by fidelity, containment, observability, reproducibility, and governance artifacts
- block promotion when a required dimension has weak or missing evidence
Tools, repos, and methodologies worth exploring:
- GateMem, sandbox threat models, weakest-link evidence reviews, red-team fixtures, claim-dimension evidence registers
Implementability score: 0.66

### Search grounding should be owned outside the model provider

Summary: Decoupled Search Grounding separates retrieval from model-native generation through an MCP-compatible gateway, and HANSEL turns web-agent traces into user-checkable evidence breadcrumbs. Owning the evidence path is now a sovereignty move.

Analysis: [daily sovereignty analysis](2026-06-18/sovereignty.md#search-grounding-should-be-owned-outside-the-model-provider)
Durable topics: [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agentic Search and Retrieval](../AgenticAI/agentic-search/agentic-search.md)
Core sources: [Decoupled Search Grounding](https://arxiv.org/abs/2606.18947v1), [HANSEL](https://arxiv.org/abs/2606.18671v1)
Implementable now:
- put search behind a gateway and make routing explicit
- keep provider, query, cache, retrieval-depth, rendered context, and source IDs in traces
- create answer artifacts with claim-to-source or claim-to-breadcrumb links
- preserve web-agent page state for high-risk decisions
Tools, repos, and methodologies worth exploring:
- MCP search gateway wrappers, exact plus semantic caching, browser trace snapshots, cost-quality Pareto tests
Implementability score: 0.82

## Previous structured update: Deep Dive Wednesday, 2026-06-17

### Evidence provenance is becoming the control-plane primitive

Summary: ProvenanceGuard won the week because it names the primitive underneath the week's best findings: source-owned evidence. Sourced answers, agent-written tests, skill routing, trajectory scoring, and multi-agent delegation all need replayable proof of which source, oracle, skill, policy, route, or trace segment carried the claim.

Analysis: [daily sovereignty analysis](2026-06-17/sovereignty.md#evidence-provenance-is-becoming-the-control-plane-primitive)
Core sources: [ProvenanceGuard](https://arxiv.org/abs/2606.18037v1), [All Smoke, No Alarm](https://arxiv.org/abs/2606.18168v1), [Zscaler agentic AI security platform](https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai), [Salesforce Agentforce Multi-Agent Orchestration](https://www.salesforce.com/agentforce/multi-agent-orchestration/)
Implementability score: 0.76

## Previous structured update: Daily scan, 2026-06-16

### Skills and API routers now need tamper-resistant data paths

Summary: AEGIS frames LLM API routers as plaintext man-in-the-middle infrastructure unless the data path is sealed, while Dynamic Malicious Skills shows that writable skill files can be changed during execution. The strategy move is hardening below the prompt: sealed or tightly constrained routers, read-only skill mounts, source hashes, route logs, and trace-linked integrity evidence.

Analysis: [daily sovereignty analysis](2026-06-16/sovereignty.md#skills-and-api-routers-now-need-tamper-resistant-data-paths)
Core sources: [The Proxy Knows Too Much](https://arxiv.org/abs/2606.16358v1), [Dynamic Malicious Skills](https://arxiv.org/abs/2606.16287v1), [Agent trajectories as programs](https://arxiv.org/abs/2606.16988v1)
Implementability score: 0.69
