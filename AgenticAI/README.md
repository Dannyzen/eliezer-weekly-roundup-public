# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-14

### HyperTool folds deterministic tool workflows into executable MCP-style blocks

Summary: HyperTool replaces step-wise atomic tool calls with executable code blocks that call existing tools through their original schemas, manipulate returned values, and pass intermediate results locally. The model reasons at the subroutine level; HyperTool handles the internal dataflow.

Analysis: [daily reasoning analysis](2026-06-14/reasoning.md#hypertool-folds-deterministic-tool-workflows-into-executable-mcp-style-blocks)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Skills as Control](skills-as-control/skills-as-control.md), [MCP Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md)
Core sources: [HyperTool](https://arxiv.org/abs/2606.13663v1)
Implementable now:
- adopt an MCP-style executable tool interface for any deterministic multi-step tool workflow
- keep model-visible tool schemas minimal; push dataflow logic into the tool runtime
- use HyperTool's training approach (tool-use trajectory distillation) to teach models the folded-call pattern
- trace folded tool executions as single admission events with internal span detail
Tools, repos, and methodologies worth exploring:
- MCP-style executable tool runtimes, trajectory distillation for tool-use, folded-call admission tracing
Implementability score: 0.85

### Recursive Agent Harnesses make the harness itself the recursive unit

Summary: Recursive Agent Harnesses (RAH) name the pattern where a parent agent generates and runs an executable script that spawns subagent harnesses in parallel for fine-grained workloads and uses structured function calls for small subtasks. The harness — not the model call — is the recursive unit.

Analysis: [daily reasoning analysis](2026-06-14/reasoning.md#recursive-agent-harnesses-make-the-harness-itself-the-recursive-unit)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [Recursive Agent Harnesses](https://arxiv.org/abs/2606.13643v1)
Implementable now:
- design agent runtimes where spawning a child harness is a first-class runtime operation with explicit resource bounds
- use executable scripts as the parent agent's "thought" artifact, not hidden prompt chains
- separate parallel subagent spawning (for independent workloads) from structured function calls (for dependent subtasks)
- trace the full harness recursion tree for debugging and governance
Tools, repos, and methodologies worth exploring:
- harness-spawning runtimes, executable-script thought artifacts, recursion-tree tracing, resource-bounded parallelism
Implementability score: 0.75

### Brick routes by capability geometry, not keywords

Summary: Brick presents a multimodal router that scores each model on six capability dimensions, combines this with a per-query difficulty estimate, and dispatches via a cost-penalized geometric rule. A continuous preference knob lets operators slide between max-quality and max-saving profiles at deploy time. On 5,504 queries, max-quality reaches 76.98% accuracy while reducing cost by 47.3% versus always using the strongest model.

Analysis: [daily reasoning analysis](2026-06-14/reasoning.md#brick-routes-by-capability-geometry-not-keywords)
Durable topics: [Model Router Governance](../Strategy/model-router-governance/model-router-governance.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md), [Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core sources: [Brick](https://arxiv.org/abs/2606.13241v1)
Implementable now:
- profile candidate models on a fixed capability benchmark suite across six dimensions (reasoning, coding, tool use, long context, multimodal, instruction following)
- estimate per-query difficulty with a lightweight classifier or proxy model
- dispatch via cost-penalized geometric rule: select argmax(score - lambda * cost)
- expose the quality/savings trade-off as a runtime knob (lambda) for operators
Tools, repos, and methodologies worth exploring:
- capability-profiling benchmarks, difficulty classifiers, geometric dispatch logic, continuous quality/savings knobs
Implementability score: 0.70

## Previous structured update: Daily scan, 2026-06-13

### Memory systems need evolutionary state, compression, and poisoning gates

Summary: EvoArena, MemRefine, and SMSR turn durable memory into a runtime state system. Agents need memory update histories, budgeted compression, writer provenance, and poisoning-resistance gates before recalled memory can steer action.

Analysis: [daily reasoning analysis](2026-06-13/reasoning.md#memory-systems-need-evolutionary-state-compression-and-poisoning-gates)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Context Economy](context-economy/context-economy.md)
Core sources: [EvoArena](https://arxiv.org/abs/2606.13681v1), [MemRefine](https://arxiv.org/abs/2606.13177v1), [SMSR](https://arxiv.org/abs/2606.12703v1)
Implementable now:
- record patch-like memory update histories instead of overwriting state
- budget memory stores and log delete, merge, preserve, and abstain decisions
- bind memory writes to writer principal, source hash, signature or trust tier
- test authenticated and unauthenticated memory poisoning separately
Tools, repos, and methodologies worth exploring:
- evolving-environment memory fixtures, storage-budgeted memory management, signed memory writes, randomized retrieval ablations, memory-poisoning red teams
Implementability score: 0.70

### Skills need topology, probes, and scanner-backed admission

Summary: SkillJuror and SkillCAT show that skill organization and topology change runtime behavior, while SkillSpector and large installable skill catalogs make skill admission a practical dependency-management problem.

Analysis: [daily reasoning analysis](2026-06-13/reasoning.md#skills-need-topology-probes-and-scanner-backed-admission)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [SkillJuror](https://arxiv.org/abs/2606.11543v1), [skill-juror repo](https://github.com/zhiyuchen-ai/skill-juror), [SkillCAT](https://arxiv.org/abs/2606.13317v1), [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector), [Agent Skills](https://github.com/addyosmani/agent-skills), [Superpowers](https://github.com/obra/superpowers)
Implementable now:
- compare progressive-disclosure skills against flat baselines
- measure resource touches, effective uptake, retries, verifier passes, and wrong-skill loads
- replay candidate skill patches before promotion
- scan prose, scripts, MCP permissions, memory poisoning, and tool misuse before installing community skills
Tools, repos, and methodologies worth exploring:
- SkillJuror-style trajectory evidence, SkillCAT-style topology-aware execution, SkillSpector scans, SARIF reports, runtime skill probes, production-admitted skill catalogs
Implementability score: 0.86

## Previous structured update

The Friday synthesis for 2026-06-12 focused on trace-governed operational units: [week ending 2026-06-12 roundup](../roundups/2026-06-12.md).