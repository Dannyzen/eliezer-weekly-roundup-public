# Strategy Weekly Sovereignty: Week ending 2026-06-19

This week’s strategic signal is that sovereignty is moving from model ownership to runtime boundary ownership. The durable control points are evidence provenance, tool contracts, capability supply chains, brokered credentials, and deployment-shaped safety evidence.

## Executive summary

1. **Governance moves to evidence provenance and runtime contracts.** Source ownership, contract integrity, compliance predicates, stakeholder harm, and correction-to-check pipelines are becoming trace fields.
2. **Capability discovery and skills are now supply-chain authority surfaces.** Registries, tool programs, skill stores, and agentic workflows decide what the agent can find, load, execute, and mutate.
3. **Mutation authority leaves agents for brokers and tamper-resistant paths.** Agents should propose. Brokers, monitors, routers, and sandbox evidence should decide whether production state changes.

## Governance moves to evidence provenance and runtime contracts

ProvenanceGuard won the Wednesday deep dive because it names the control-plane primitive under the week’s governance work: source-owned evidence. It decomposes final answers into claims, routes them to source-specific evidence, and separates support from attribution. That matters because pooled evidence can make a generated claim look supported while hiding cross-source conflation.

ContractGuard supplies the tool-boundary version of the same argument. A risk-aware tool gate is only as trustworthy as the contract it reads. If a tool can forge declared effects, the agent can route dangerous behavior through an apparently safe path. C-Trace adds trace-time policy enforcement: compliance should be checked against runtime behavior, not only written into policies. StakeBench adds the harm model: prompt-injection risk needs stakeholder and source-locality labels, not only generic attack success. TRACE adds a practical loop: recurring user corrections should become deterministic runtime checks.

Why it matters: governance cannot live in system prompts once tools, memory, retrieval, subagents, and SaaS APIs all affect the run. The runtime must preserve which source, contract, policy, correction, and trace segment carried each decision.

How it fits into the strategy stack: this is the audit substrate for agent gateways, MCP, enterprise orchestration, regulated deployment, and local-first agent networks. The evidence packet becomes the governable unit.

Implementable now:
- add source_id, tool_id, raw_output_ref, contract_hash, policy_id, and policy_verdict fields to tool traces
- require claim-to-source evidence for high-risk answers and generated artifacts
- sign and hash tool contracts and verify declared effects at runtime
- express policies over trace fields instead of natural-language-only instructions
- compile recurring user corrections into deterministic checks before allowing similar actions
- label prompt-injection evals by harmed stakeholder and source locality

Tools, repos, and methodologies worth exploring:
- MCP trace schemas with source IDs and raw output references
- OPA or Cedar over trace fields
- signed tool manifests and contract attestation
- OpenTelemetry spans for policy and evidence packets
- CI gates for correction-derived checks
- evidence stores with immutable raw output handles

Core sources:
- ProvenanceGuard: https://arxiv.org/abs/2606.18037v1
- ContractGuard: https://arxiv.org/abs/2606.18550v1
- Runtime Compliance Verification for AI Agents: https://arxiv.org/abs/2606.19242v1
- StakeBench: https://arxiv.org/abs/2606.13385v1
- TRACE: https://arxiv.org/abs/2606.13174v1
- Five-Plane Runtime Governance: https://arxiv.org/abs/2606.12320v1

Implementability score: 0.76

## Capability discovery and skills are now supply-chain authority surfaces

Capability discovery is no longer a UX feature. Agentic Resource Discovery makes discoverability explicit through catalogs, manifests, search endpoints, and resource cards. ToolPro turns selected service interactions into effect-typed executable programs. SkillSpector scans AI-agent skills as supply-chain artifacts. SkillWeaver composes real MCP-server skills through a dependency-aware DAG. GitHub Agentic Workflows turns natural-language automation into governed Actions resources.

The strategic point is that every one of these surfaces decides what the agent can find, load, run, or mutate. A registry can omit or prioritize capabilities. A generated skill can smuggle behavior. A tool program can collapse many state changes into one call. A workflow resource can turn prose into CI execution. That is authority, not convenience.

Why it matters: organizations will not manage agent risk by reviewing chat prompts alone. They need governed catalogs, signed manifests, scanner results, admission gates, workflow firewalls, and audit records for every agent-visible capability.

How it fits into the strategy stack: capability supply chains sit between identity, policy, model routing, and tool execution. Owning that layer is a sovereignty move because it lets the operator decide what the agent can discover and under which policy context it can execute.

Implementable now:
- make capability discovery permissioned by principal, tenant, workflow, and data class
- require source metadata, publisher identity, manifest hash, and compliance tags for tools, skills, MCP cards, and workflow resources
- scan skills and workflow definitions before admission
- benchmark skills against no-skill and wrong-skill baselines before promotion
- log registry query, selected result, generated artifact, installed or loaded resource, and compiled program hash
- block or require review when publisher identity, effect typing, or provenance is weak

Tools, repos, and methodologies worth exploring:
- `huggingface/hf-discover`: https://github.com/huggingface/hf-discover
- ARD-style manifests and catalog search
- NVIDIA SkillSpector: https://github.com/NVIDIA/SkillSpector
- GitHub Actions governance and Agent Workflow Firewall patterns
- signed skill stores and content-addressed catalogs
- policy-as-code over discovery and execution

Core sources:
- Agentic Resource Discovery: https://huggingface.co/blog/agentic-resource-discovery-launch
- hf-discover repository: https://github.com/huggingface/hf-discover
- ToolPro: https://arxiv.org/abs/2606.19992v1
- NVIDIA SkillSpector: https://github.com/NVIDIA/SkillSpector
- Compositional Skill Routing for LLM Agents: https://arxiv.org/abs/2606.18051v1
- GitHub Agentic Workflows public preview: https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview

Implementability score: 0.74

## Mutation authority leaves agents for brokers and tamper-resistant paths

Sovereign Execution Brokers is the clearest sovereignty paper of the week. Its core claim is that production mutation authority should not sit inside a non-deterministic reasoning process. The agent can propose an action, and an admission boundary can certify it, but the infrastructure mutation path itself must require a broker to verify the certificate at execution time.

DeepMind’s AI Control Roadmap supplies the operating model around that enforcement boundary: threat-model capable internal agents, monitor trajectories, deploy mitigations, and measure coverage, recall, and time-to-response. API-router hardening and AI-sandbox evidence work add the implementation warning: if provider routes, sandbox boundaries, or live mutation paths can be bypassed or misrepresented, governance evidence is weak. SafeClawBench and OpenAI Deployment Simulation add the release discipline: safety claims need evidence at the same layer and distribution as the deployment claim.

Why it matters: a credentialed agent with direct mutation access can bypass most governance. Policies, monitors, certificates, and evals only become binding when the external system refuses side effects that did not pass the broker path.

How it fits into the strategy stack: mutation brokers should sit at the boundary between agent proposals and real systems: cloud APIs, GitHub, Kubernetes, CRM, email, payments, local files, and customer data. The agent’s output is an intent artifact. Authority is minted outside the model.

Implementable now:
- remove standing write credentials from agent runtimes where possible
- route production mutations through a broker that validates signed action certificates
- bind certificate checks to action contract, principal, resource scope, policy epoch, revocation epoch, and live-state hash
- mint short-lived scoped credentials only after validation
- reject non-broker mutation identities at the target system
- pin router images, provider hosts, and allowed egress paths for model/API routing
- attach evidence dimensions to sandbox and deployment-safety claims
- measure monitoring coverage, recall, false positives, time-to-response, and escalation outcomes

Tools, repos, and methodologies worth exploring:
- AWS STS, Kubernetes TokenRequest, workload identity, and short-lived credentials
- OPA or Cedar for certificate and policy predicates
- signed admission artifacts with revocation epochs
- OpenTelemetry spans for proposal, admission, broker decision, scoped credential mint, mutation, and outcome
- DeepMind-style AI control threat taxonomies and monitor metrics
- release gates that combine representative-distribution simulation with tail-risk red-team tasks

Core sources:
- Sovereign Execution Brokers: https://arxiv.org/abs/2606.20520v1
- Google DeepMind AI Control Roadmap: https://deepmind.google/blog/securing-the-future-of-ai-agents/
- API router tamper-resistant data paths: https://arxiv.org/abs/2606.16358v1
- AI Sandboxes: https://arxiv.org/abs/2606.18532v1
- SafeClawBench: https://arxiv.org/abs/2606.18356v1
- OpenAI Deployment Simulation: https://openai.com/index/deployment-simulation

Implementability score: 0.71

## Strategic read

The sovereignty move is not owning every model. It is owning the runtime boundaries where state, capability, evidence, and authority become real. Let the model propose. Make the platform decide which state is valid, which capabilities are discoverable, which contracts can be trusted, which evidence supports a claim, and which broker is allowed to mutate production.

## References

- ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents: https://arxiv.org/abs/2606.18037v1
- ContractGuard: Open Tool Risk Management for Context-Aware AI Agents: https://arxiv.org/abs/2606.18550v1
- Runtime Compliance Verification for AI Agents: https://arxiv.org/abs/2606.19242v1
- StakeBench: A Benchmark for Stakeholder-Centric Prompt Injection Risk: https://arxiv.org/abs/2606.13385v1
- TRACE: https://arxiv.org/abs/2606.13174v1
- Five-Plane Runtime Governance: https://arxiv.org/abs/2606.12320v1
- Agentic Resource Discovery: Let agents search: https://huggingface.co/blog/agentic-resource-discovery-launch
- hf-discover repository: https://github.com/huggingface/hf-discover
- ToolPro: https://arxiv.org/abs/2606.19992v1
- NVIDIA SkillSpector: https://github.com/NVIDIA/SkillSpector
- Compositional Skill Routing for LLM Agents: https://arxiv.org/abs/2606.18051v1
- GitHub Agentic Workflows public preview: https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview
- Sovereign Execution Brokers: https://arxiv.org/abs/2606.20520v1
- Google DeepMind AI Control Roadmap: https://deepmind.google/blog/securing-the-future-of-ai-agents/
- API router tamper-resistant data paths: https://arxiv.org/abs/2606.16358v1
- AI Sandboxes: https://arxiv.org/abs/2606.18532v1
- SafeClawBench: https://arxiv.org/abs/2606.18356v1
- OpenAI Deployment Simulation: https://openai.com/index/deployment-simulation
