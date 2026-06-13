# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-13

### Memory systems need evolutionary state, compression, and poisoning gates

Summary: EvoArena, MemRefine, and SMSR turn durable memory into a runtime state system. Agents need memory update histories, budgeted compression, writer provenance, and poisoning-resistance gates before recalled memory can steer action.

Analysis: [daily reasoning analysis](2026-06-13/reasoning.md#memory-systems-need-evolutionary-state-compression-and-poisoning-gates)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Context Economy](context-economy/context-economy.md)
Core sources: [EvoArena](https://arxiv.org/abs/2606.13681v1), [MemRefine](https://arxiv.org/abs/2606.13177v1), [SMSR](https://arxiv.org/abs/2606.12703v1)
Implementable now:
- record patch-like memory update histories instead of overwriting state;
- budget memory stores and log delete, merge, preserve, and abstain decisions;
- bind memory writes to writer principal, source hash, signature or trust tier;
- test authenticated and unauthenticated memory poisoning separately.
Tools, repos, and methodologies worth exploring:
- evolving-environment memory fixtures, storage-budgeted memory management, signed memory writes, randomized retrieval ablations, memory-poisoning red teams
Implementability score: 0.70

### Skills need topology, probes, and scanner-backed admission

Summary: SkillJuror and SkillCAT show that skill organization and topology change runtime behavior, while SkillSpector and large installable skill catalogs make skill admission a practical dependency-management problem.

Analysis: [daily reasoning analysis](2026-06-13/reasoning.md#skills-need-topology-probes-and-scanner-backed-admission)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [SkillJuror](https://arxiv.org/abs/2606.11543v1), [skill-juror repo](https://github.com/zhiyuchen-ai/skill-juror), [SkillCAT](https://arxiv.org/abs/2606.13317v1), [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector), [Agent Skills](https://github.com/addyosmani/agent-skills), [Superpowers](https://github.com/obra/superpowers)
Implementable now:
- compare progressive-disclosure skills against flat baselines;
- measure resource touches, effective uptake, retries, verifier passes, and wrong-skill loads;
- replay candidate skill patches before promotion;
- scan prose, scripts, MCP permissions, memory poisoning, and tool misuse before installing community skills.
Tools, repos, and methodologies worth exploring:
- SkillJuror-style trajectory evidence, SkillCAT-style topology-aware execution, SkillSpector scans, SARIF reports, runtime skill probes, production-admitted skill catalogs
Implementability score: 0.86

## Previous structured update

The Friday synthesis for 2026-06-12 focused on trace-governed operational units: [week ending 2026-06-12 roundup](../roundups/2026-06-12.md).
