# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday synthesis, week ending 2026-06-19

### Sessioned state replaces scattered memory, context, and handoff logs

Summary: The week’s memory, harness, collaboration, and OpenRath findings converge on a single runtime object: Session. Agent systems need branchable run-state that binds memory events, tool evidence, workspace placement, lineage, token use, pending work, and replay pointers instead of reconstructing them from scattered logs.

Analysis: [weekly reasoning analysis](2026-06-19/reasoning.md#sessioned-state-replaces-scattered-memory-context-and-handoff-logs)
Durable topics: [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Memory Systems](memory-systems/memory-systems.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [OpenRath paper](https://arxiv.org/abs/2606.19409v1), [OpenRath repository](https://github.com/Rath-Team/OpenRath), [GateMem](https://arxiv.org/abs/2606.18829v1), [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)
Implementable now:
- define a Session or run-state schema with branch ID, parent ID, workspace ID, sandbox placement, memory references, tool evidence, token accounting, and replay pointers
- keep raw events append-only, then project compact prompt views from them
- add memory governance checks for cross-principal leakage, forgetting, and reconstruction risk
Tools, repos, and methodologies worth exploring:
- OpenRath, TencentDB Agent Memory, SQLite or Postgres event tables, OpenTelemetry spans, Temporal or Prefect, git-style branch/diff models
Implementability score: 0.77

### Tool surfaces become discovered, compiled, and cache-aware

Summary: ToolPro, HyperTool, Agentic Resource Discovery, and context-selection work reject giant static tool catalogs. The practical tool layer searches capabilities before prompt construction, then compiles repeated multi-step service intent into effect-typed execution objects when the workflow is stable.

Analysis: [weekly reasoning analysis](2026-06-19/reasoning.md#tool-surfaces-become-discovered-compiled-and-cache-aware)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md), [Context Economy](context-economy/context-economy.md), [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core sources: [ToolPro](https://arxiv.org/abs/2606.19992v1), [Agentic Resource Discovery](https://huggingface.co/blog/agentic-resource-discovery-launch), [hf-discover](https://github.com/huggingface/hf-discover), [HyperTool](https://arxiv.org/abs/2606.13663v1)
Implementable now:
- put scoped search in front of Skills, MCP servers, A2A agents, and internal tools
- split compact tool summaries from full schemas and load full contracts only after selection
- compile repeated endpoint workflows into deterministic functions or service-side tool programs
- log discovery query, selected capability, manifest hash, compiled program hash, effect type, execution result, and fallback path
Tools, repos, and methodologies worth exploring:
- hf-discover, ARD-style manifests, MCP gateways, Wasm execution, policy checks over READ/WRITE effects, context-cache telemetry
Implementability score: 0.82

### Skills become admitted and measured behavior modules

Summary: The skill layer is now part of the agent supply chain. Skill-Juror, SkillSpector, SkillWeaver, learned-skill work, and immutable skill mounts all point at one lifecycle: scan, route, benchmark, freeze, and regression-test skills before they influence a run.

Analysis: [weekly reasoning analysis](2026-06-19/reasoning.md#skills-become-admitted-and-measured-behavior-modules)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core sources: [Skill-Juror](https://arxiv.org/abs/2606.11543v1), [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector), [Compositional Skill Routing](https://arxiv.org/abs/2606.18051v1), [large-scale skill utility evaluation](https://arxiv.org/abs/2606.17819v1)
Implementable now:
- require owner, version, hash, declared capabilities, allowed tools, data scope, and review status for every skill
- scan prose, scripts, templates, references, and embedded commands together
- benchmark no-skill, wrong-skill, and full-skill variants before promotion
- route skills through dependency-aware DAGs and mount admitted skills read-only
Tools, repos, and methodologies worth exploring:
- NVIDIA SkillSpector, Skill-Juror style evals, dependency DAG routing, static scans plus sandboxed probes, content-addressed skill stores
Implementability score: 0.75

### Evaluation shifts from final outcome to trajectory, oracle, harm, and effort telemetry

Summary: SafeClawBench, All Smoke No Alarm, offline trajectory preferences, HANSEL, and Hugging Face’s tooling benchmark all say the same thing: pass/fail is too lossy. Agent evaluation needs oracle strength, state deltas, harmful endpoint layers, evidence breadcrumbs, effort metrics, and route quality.

Analysis: [weekly reasoning analysis](2026-06-19/reasoning.md#evaluation-shifts-from-final-outcome-to-trajectory-oracle-harm-and-effort-telemetry)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Sandboxing](../Strategy/agent-sandboxing/agent-sandboxing.md), [Evidence Provenance Control Plane](../Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core sources: [SafeClawBench](https://arxiv.org/abs/2606.18356v1), [Is it agentic enough?](https://huggingface.co/blog/is-it-agentic-enough), [OpenAI Deployment Simulation](https://openai.com/index/deployment-simulation), [All Smoke, No Alarm](https://arxiv.org/abs/2606.18168v1)
Implementable now:
- normalize traces into action alphabets or procedure fingerprints
- lint agent-authored tests for explicit oracle strength before merge
- score semantic failure, audit-visible harm, and sandbox-observed harm separately
- track turns, tokens, time, errors, intended API path adoption, deprecated path use, and environment state deltas
Tools, repos, and methodologies worth exploring:
- SafeClawBench, Hugging Face Jobs and Buckets, OpenTelemetry marker extraction, deployment simulation, deterministic task suites, test-oracle linting
Implementability score: 0.85
