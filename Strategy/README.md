# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday synthesis, week ending 2026-06-19

### Governance moves to evidence provenance and runtime contracts

Summary: ProvenanceGuard, ContractGuard, C-Trace, StakeBench, TRACE, and Five-Plane Runtime Governance all turn governance into trace-time evidence. The strategic primitive is no longer a trusted final answer. It is a proof packet with source IDs, raw outputs, contract hashes, policy verdicts, correction-derived checks, and stakeholder harm labels.

Analysis: [weekly sovereignty analysis](2026-06-19/sovereignty.md#governance-moves-to-evidence-provenance-and-runtime-contracts)
Durable topics: [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [ProvenanceGuard](https://arxiv.org/abs/2606.18037v1), [ContractGuard](https://arxiv.org/abs/2606.18550v1), [Runtime Compliance Verification for AI Agents](https://arxiv.org/abs/2606.19242v1), [StakeBench](https://arxiv.org/abs/2606.13385v1)
Implementable now:
- add source_id, tool_id, raw_output_ref, contract_hash, policy_id, and policy_verdict fields to tool traces
- require claim-to-source evidence for high-risk answers and generated artifacts
- sign and hash tool contracts and verify declared effects at runtime
- compile recurring user corrections into deterministic checks
Tools, repos, and methodologies worth exploring:
- MCP trace schemas, OPA or Cedar, signed tool manifests, OpenTelemetry policy spans, immutable evidence stores, CI gates for correction-derived checks
Implementability score: 0.76

### Capability discovery and skills are now supply-chain authority surfaces

Summary: Agentic Resource Discovery, ToolPro, SkillSpector, SkillWeaver, and GitHub Agentic Workflows make capability supply chains explicit. Registries, skills, MCP cards, tool programs, and workflow resources decide what the agent can find, load, execute, and mutate.

Analysis: [weekly sovereignty analysis](2026-06-19/sovereignty.md#capability-discovery-and-skills-are-now-supply-chain-authority-surfaces)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [Agentic Resource Discovery](https://huggingface.co/blog/agentic-resource-discovery-launch), [hf-discover](https://github.com/huggingface/hf-discover), [ToolPro](https://arxiv.org/abs/2606.19992v1), [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector)
Implementable now:
- make capability discovery permissioned by principal, tenant, workflow, and data class
- require source metadata, publisher identity, manifest hash, and compliance tags for tools, skills, MCP cards, and workflow resources
- scan skills and workflow definitions before admission
- log registry query, selected result, generated artifact, loaded resource, and compiled program hash
Tools, repos, and methodologies worth exploring:
- hf-discover, ARD-style registries, MCP gateways, SkillSpector, GitHub Actions governance, signed skill stores, policy-as-code over discovery and execution
Implementability score: 0.74

### Mutation authority leaves agents for brokers and tamper-resistant paths

Summary: Sovereign Execution Brokers and DeepMind AI Control define the production boundary: agents propose, brokers verify, scoped credentials mutate, and monitors measure coverage, recall, and time-to-response. API-router and sandbox work add the enforcement caveat: if the mutation path can bypass the broker, the safety evidence is advisory.

Analysis: [weekly sovereignty analysis](2026-06-19/sovereignty.md#mutation-authority-leaves-agents-for-brokers-and-tamper-resistant-paths)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agent Network Containment](agent-network-containment/agent-network-containment.md), [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core sources: [Sovereign Execution Brokers](https://arxiv.org/abs/2606.20520v1), [Google DeepMind AI Control Roadmap](https://deepmind.google/blog/securing-the-future-of-ai-agents/), [API router tamper-resistant data paths](https://arxiv.org/abs/2606.16358v1), [OpenAI Deployment Simulation](https://openai.com/index/deployment-simulation)
Implementable now:
- remove standing write credentials from agent runtimes where possible
- route production mutations through a broker that validates signed action certificates
- bind certificate checks to action contract, principal, resource scope, policy epoch, revocation epoch, and live-state hash
- reject non-broker mutation identities at the target system
- measure monitor coverage, recall, false positives, time-to-response, and escalation outcomes
Tools, repos, and methodologies worth exploring:
- AWS STS, Kubernetes TokenRequest, workload identity, OPA, Cedar, signed admission artifacts, OpenTelemetry broker spans, deployment simulation, sandbox state oracles
Implementability score: 0.71
