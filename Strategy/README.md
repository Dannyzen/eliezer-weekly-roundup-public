# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-16

### Skills and API routers now need tamper-resistant data paths

Summary: AEGIS frames LLM API routers as plaintext man-in-the-middle infrastructure unless the data path is sealed, while Dynamic Malicious Skills shows that writable skill files can be changed during execution. The strategy move is hardening below the prompt: sealed or tightly constrained routers, read-only skill mounts, source hashes, route logs, and trace-linked integrity evidence.

Analysis: [daily sovereignty analysis](2026-06-16/sovereignty.md#skills-and-api-routers-now-need-tamper-resistant-data-paths)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Model Router Governance](model-router-governance/model-router-governance.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core sources: [The Proxy Knows Too Much](https://arxiv.org/abs/2606.16358v1), [Dynamic Malicious Skills](https://arxiv.org/abs/2606.16287v1), [Agent trajectories as programs](https://arxiv.org/abs/2606.16988v1)
Implementable now:
- treat API routers and OpenAI/Anthropic-compatible proxies as privileged infrastructure
- pin router images, restrict upstream provider hosts, and log route decisions
- mount admitted skill directories read-only during execution
- include skill body hash, script hash, mount mode, and loaded-skill ID in traces
- run canary tests that try to mutate a skill at runtime and expect hard failure
Tools, repos, and methodologies worth exploring:
- read-only bind mounts, OverlayFS, container read-only filesystems, seccomp/AppArmor, signed router images, mTLS, provider host allowlists, LiteLLM or Portkey policy logs, remote attestation patterns, ProcGrep-style trace drift checks
Implementability score: 0.69

## Previous structured update: Daily scan, 2026-06-15

### Skill and guardrail defenses need cross-modal and resource-aware gates

Summary: SkillMutator shows that Agent Skills create a language-and-code attack surface, SkillAudit gives a paired-trajectory method for skill evolution, From Shield to Target shows LLM guardrails can be turned into denial-of-service targets, and NVIDIA SkillSpector shows practical scanner demand. Skills and guardrails now need manifests, probes, and budgets.

Analysis: [daily sovereignty analysis](2026-06-15/sovereignty.md#skill-and-guardrail-defenses-need-cross-modal-and-resource-aware-gates)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core sources: [SkillMutator](https://arxiv.org/abs/2606.14154v1), [SkillAudit](https://arxiv.org/abs/2606.14239v1), [From Shield to Target](https://arxiv.org/abs/2606.14517v1), [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector)
Implementability score: 0.78

## Previous structured update: Daily scan, 2026-06-14

### Five-plane reference architecture governs the agent runtime, not the data perimeter

Summary: The Five-Plane Reference Architecture maps production agent governance across substrate, control, data, agent, and policy planes. The governance unit is the workflow runtime, not only the data perimeter.

Analysis: [daily sovereignty analysis](2026-06-14/sovereignty.md#five-plane-reference-architecture-governs-the-agent-runtime-not-the-data-perimeter)
Core sources: [Five-Plane Architecture](https://arxiv.org/abs/2606.12320v1)
Implementability score: 0.65

### TRACE compiles user corrections into runtime enforcement for coding agents

Summary: TRACE mines user corrections into atomic rules and compiles them into deterministic task-completion checks, moving preference compliance out of passive memory and into runtime enforcement.

Analysis: [daily sovereignty analysis](2026-06-14/sovereignty.md#trace-compiles-user-corrections-into-runtime-enforcement-for-coding-agents)
Core sources: [TRACE](https://arxiv.org/abs/2606.13174v1)
Implementability score: 0.80
