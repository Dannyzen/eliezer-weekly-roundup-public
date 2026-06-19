# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-19

### Session should be the runtime primitive, not a scattered trace

Summary: OpenRath makes Session the branchable, inspectable, replayable value passed through multi-agent workflows. That is the right abstraction for systems where transcripts, tool effects, memory events, workspace placement, and branch provenance cannot stay in separate side channels.

Analysis: [daily reasoning analysis](2026-06-19/reasoning.md#session-should-be-the-runtime-primitive-not-a-scattered-trace)
Durable topics: [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [OpenRath paper](https://arxiv.org/abs/2606.19409v1), [OpenRath repository](https://github.com/Rath-Team/OpenRath)
Implementable now:
- define a Session or run-state object as the value agents transform
- preserve branch ID, parent session, sandbox placement, tool evidence, memory references, token usage, and replay pointers
- make fork, merge, compression, and selector decisions explicit runtime operations
- link final artifacts back to session lineage and tool evidence
Tools, repos, and methodologies worth exploring:
- OpenRath, append-only event tables, OpenTelemetry spans, Temporal or Prefect, git-style branch/diff mental models
Implementability score: 0.83

### Tool surfaces need discovery and executable intent, not static catalogs

Summary: ToolPro and Agentic Resource Discovery point to a better tool layer. First, search and scope capabilities instead of exposing huge catalogs. Then compile repeated multi-step service interactions into effect-typed programs instead of making the model babysit endpoint calls.

Analysis: [daily reasoning analysis](2026-06-19/reasoning.md#tool-surfaces-need-discovery-and-executable-intent-not-static-catalogs)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md)
Core sources: [ToolPro](https://arxiv.org/abs/2606.19992v1), [Agentic Resource Discovery](https://huggingface.co/blog/agentic-resource-discovery-launch), [hf-discover](https://github.com/huggingface/hf-discover)
Implementable now:
- put scoped search in front of Skills, MCP servers, A2A agents, and internal tools
- require source metadata, publisher identity, manifest hash, representative queries, tags, and compliance signals
- compile repeated multi-endpoint workflows into effect-typed tool programs or deterministic workflow functions
- log discovery query, selected capability, generated artifact, compiled program hash, effect type, and fallback path
Tools, repos, and methodologies worth exploring:
- hf-discover, MCP gateways, ARD-style manifests, Wasm service-side execution, policy checks over READ/WRITE effects
Implementability score: 0.78

### Agent evaluation needs staged harm and effort telemetry

Summary: SafeClawBench separates semantic acceptance, audit-visible harm, and sandbox-observed harm. Hugging Face's tool-specific benchmark adds effort metrics and marker adoption, which is how tool authors can tell whether docs, APIs, CLIs, and Skills actually make agents better.

Analysis: [daily reasoning analysis](2026-06-19/reasoning.md#agent-evaluation-needs-staged-harm-and-effort-telemetry)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Sandboxing](../Strategy/agent-sandboxing/agent-sandboxing.md), [Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core sources: [SafeClawBench](https://arxiv.org/abs/2606.18356v1), [SafeClawBench dataset](https://huggingface.co/datasets/sairights/safeclawbench), [Is it agentic enough?](https://huggingface.co/blog/is-it-agentic-enough), [OpenAI Deployment Simulation](https://openai.com/index/deployment-simulation)
Implementable now:
- score semantic, audit-evidence, and sandbox-state harm separately
- preserve pre/post environment state and tool effects
- add trace markers for intended API/CLI/tool-path adoption and deprecated path use
- compare bare install, cloned source, and packaged Skill tiers
- replay representative historical workflows before rollout
Tools, repos, and methodologies worth exploring:
- SafeClawBench, Hugging Face Jobs and Buckets, marker extraction, OpenTelemetry traces, privacy-preserved deployment simulation
Implementability score: 0.88

## Previous structured update: Daily scan, 2026-06-18

### Tool gates need contract integrity, not only hidden tools

Summary: ContractGuard shows that risk-aware tool gating moves the trust assumption into the tool contract layer. If declared effects can be forged, a dangerous tool can be routed into scope without persuading the agent. Tool manifests are now authority-bearing runtime artifacts.

Analysis: [daily reasoning analysis](2026-06-18/reasoning.md#tool-gates-need-contract-integrity-not-only-hidden-tools)
Core sources: [ContractGuard](https://arxiv.org/abs/2606.18550v1), [Runtime Compliance Verification for AI Agents](https://arxiv.org/abs/2606.19242v1)
Implementability score: 0.76

### Shared memory needs governance scores, not only recall

Summary: GateMem evaluates multi-principal memory agents on utility, access-control violations, and active-forgetting failures. That is the right deployment frame for institutional assistants: a memory system that leaks across roles or reconstructs deleted data is not safe just because it recalls well.

Analysis: [daily reasoning analysis](2026-06-18/reasoning.md#shared-memory-needs-governance-scores-not-only-recall)
Core sources: [GateMem paper](https://arxiv.org/abs/2606.18829v1), [GateMem repository](https://github.com/rzhub/GateMem)
Implementability score: 0.71

### Grounding and web-agent verification need explicit evidence paths

Summary: Decoupled Search Grounding moves retrieval outside the model provider through an MCP-compatible gateway, while HANSEL extracts interactive breadcrumbs from web-agent trajectories. Search route, source rendering, cache behavior, page state, and final-claim linkage should be visible control-plane fields.

Analysis: [daily reasoning analysis](2026-06-18/reasoning.md#grounding-and-web-agent-verification-need-explicit-evidence-paths)
Core sources: [Decoupled Search Grounding](https://arxiv.org/abs/2606.18947v1), [HANSEL](https://arxiv.org/abs/2606.18671v1)
Implementability score: 0.84
