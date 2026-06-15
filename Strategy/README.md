# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-15

### Skill and guardrail defenses need cross-modal and resource-aware gates

Summary: SkillMutator shows that Agent Skills create a language-and-code attack surface, SkillAudit gives a paired-trajectory method for skill evolution, From Shield to Target shows LLM guardrails can be turned into denial-of-service targets, and NVIDIA SkillSpector shows practical scanner demand. Skills and guardrails now need manifests, probes, and budgets.

Analysis: [daily sovereignty analysis](2026-06-15/sovereignty.md#skill-and-guardrail-defenses-need-cross-modal-and-resource-aware-gates)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core sources: [SkillMutator](https://arxiv.org/abs/2606.14154v1), [SkillAudit](https://arxiv.org/abs/2606.14239v1), [From Shield to Target](https://arxiv.org/abs/2606.14517v1), [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector)
Implementable now:
- require skill manifests with body hash, script hash, tool scope, file scope, network scope, memory-write scope, and approval points
- scan skill prose and code jointly before installation
- run targeted sandbox probes for high-risk skills
- compare with-skill and without-skill trajectories for recurring workflows
- put timeout, token, recursion, and wall-clock budgets around LLM guardrails
Tools, repos, and methodologies worth exploring:
- NVIDIA SkillSpector, Snyk agent-scan, SARIF outputs, paired trajectory auditing, guardrail budget tests, circuit breakers, fail-closed policy verdicts
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
