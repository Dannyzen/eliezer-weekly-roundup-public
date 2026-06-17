# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-17

### Evidence provenance is becoming the control-plane primitive

Summary: ProvenanceGuard and All Smoke, No Alarm show the same governance defect on different surfaces: sourced answers and agent-written tests can look verified while lacking claim-to-source or oracle-strength evidence. Zscaler and Salesforce reinforce the market direction: agent identity, access graphs, MCP/A2A brokers, multi-agent routing, observability, and policy controls are becoming control-plane features.

Analysis: [daily sovereignty analysis](2026-06-17/sovereignty.md#evidence-provenance-is-becoming-the-control-plane-primitive)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md), [Trajectory-Aware Evaluation](../AgenticAI/trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [ProvenanceGuard](https://arxiv.org/abs/2606.18037v1), [All Smoke, No Alarm](https://arxiv.org/abs/2606.18168v1), [Zscaler agentic AI security platform](https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai), [Salesforce Agentforce Multi-Agent Orchestration](https://www.salesforce.com/agentforce/multi-agent-orchestration/)
Implementable now:
- require high-risk answers to carry claim-to-source evidence, not only citations
- make MCP source IDs stable enough for replay and audit
- run oracle-aware checks on agent-authored tests before merge
- log agent identity, selected specialist, delegated task, tool surface, policy verdict, and output evidence for multi-agent handoffs
Tools, repos, and methodologies worth exploring:
- MCP trace schemas, source-aware factuality checks, claim decomposition, test-oracle linters, mutation testing, CodeQL or AST rules, OpenTelemetry spans, OPA/Cedar policy, OpenFGA-style relationship graphs, agent registries, access graphs
Implementability score: 0.78

## Previous structured update: Daily scan, 2026-06-16

### Skills and API routers now need tamper-resistant data paths

Summary: AEGIS frames LLM API routers as plaintext man-in-the-middle infrastructure unless the data path is sealed, while Dynamic Malicious Skills shows that writable skill files can be changed during execution. The strategy move is hardening below the prompt: sealed or tightly constrained routers, read-only skill mounts, source hashes, route logs, and trace-linked integrity evidence.

Analysis: [daily sovereignty analysis](2026-06-16/sovereignty.md#skills-and-api-routers-now-need-tamper-resistant-data-paths)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Model Router Governance](model-router-governance/model-router-governance.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core sources: [The Proxy Knows Too Much](https://arxiv.org/abs/2606.16358v1), [Dynamic Malicious Skills](https://arxiv.org/abs/2606.16287v1), [Agent trajectories as programs](https://arxiv.org/abs/2606.16988v1)
Implementability score: 0.69

## Previous structured update: Daily scan, 2026-06-15

### Skill and guardrail defenses need cross-modal and resource-aware gates

Summary: SkillMutator shows that Agent Skills create a language-and-code attack surface, SkillAudit gives a paired-trajectory method for skill evolution, From Shield to Target shows LLM guardrails can be turned into denial-of-service targets, and NVIDIA SkillSpector shows practical scanner demand. Skills and guardrails now need manifests, probes, and budgets.

Analysis: [daily sovereignty analysis](2026-06-15/sovereignty.md#skill-and-guardrail-defenses-need-cross-modal-and-resource-aware-gates)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core sources: [SkillMutator](https://arxiv.org/abs/2606.14154v1), [SkillAudit](https://arxiv.org/abs/2606.14239v1), [From Shield to Target](https://arxiv.org/abs/2606.14517v1), [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector)
Implementability score: 0.78
