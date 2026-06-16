# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-16

### Procedure fingerprints turn traces into routing and monitoring signals

Summary: Agent trajectories as programs and ProcGrep make the agent trace a procedural artifact. Instead of only scoring pass/fail, teams can fingerprint how an agent searches, reads, edits, tests, retries, and fails, then use those fingerprints for routing, monitoring, and regression detection.

Analysis: [daily reasoning analysis](2026-06-16/reasoning.md#procedure-fingerprints-turn-traces-into-routing-and-monitoring-signals)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Model Router Governance](../Strategy/model-router-governance/model-router-governance.md)
Core sources: [Agent trajectories as programs](https://arxiv.org/abs/2606.16988v1), [ProcGrep](https://github.com/hamidahoderinwale/procgrep), [PACT](https://arxiv.org/abs/2606.16215v1)
Implementable now:
- normalize traces into action atoms such as search, read, edit, test, tool-call, error, and submit
- store procedural fingerprints next to success, cost, latency, and human-correction outcomes
- detect known bad action prefixes before a long run burns budget or mutates state
- route coding agents by procedural fit for task class, not only headline benchmark score
Tools, repos, and methodologies worth exploring:
- ProcGrep, trace JSONL, OpenTelemetry spans, SWE-Bench style task corpora, LangSmith/Langfuse exports, prefix-risk monitors
Implementability score: 0.80

### Tool and context selection must preserve intention fit and cache continuity

Summary: SING retrieves tools through an intention-tool graph instead of schema stuffing, while TokenPilot and LightMem2 show that context pruning must preserve prompt-prefix cache continuity. Context economy now has two constraints: admit only plausible tools, and do not invalidate the expensive stable prefix unnecessarily.

Analysis: [daily reasoning analysis](2026-06-16/reasoning.md#tool-and-context-selection-must-preserve-intention-fit-and-cache-continuity)
Durable topics: [Context Economy](context-economy/context-economy.md), [Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md)
Core sources: [SING](https://arxiv.org/abs/2606.16591v1), [TokenPilot](https://arxiv.org/abs/2606.17016v1), [LightMem2](https://github.com/zjunlp/LightMem2)
Implementable now:
- keep compact tool summaries separate from full schemas
- build an intention graph from observed task types, subgoals, tools used together, and successful traces
- load full schemas only for the small candidate set that current intent, state, and policy justify
- preserve stable prompt prefixes and log when context segments are compacted or evicted
Tools, repos, and methodologies worth exploring:
- LightMem2, MCP tool registries, graph-backed tool indexes, LangGraph or Temporal, prompt-category token metrics, cache telemetry
Implementability score: 0.83

### Skills are moving from runtime text toward searched and learned behavior modules

Summary: OpenClaw-Skill uses collective skill tree search, while Skill-to-LoRA uses skill documents offline to train dynamically loadable behavior adapters. The direction is powerful but not free: compiled or learned skills still need body hashes, evaluation, admission, rollback, and runtime immutability.

Analysis: [daily reasoning analysis](2026-06-16/reasoning.md#skills-are-moving-from-runtime-text-toward-searched-and-learned-behavior-modules)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Runtime Governance](../Strategy/runtime-governance/runtime-governance.md), [Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md)
Core sources: [OpenClaw-Skill](https://arxiv.org/abs/2606.16774v1), [Skill-to-LoRA](https://arxiv.org/abs/2606.16769v1), [Dynamic Malicious Skills](https://arxiv.org/abs/2606.16287v1)
Implementable now:
- measure high-use skills against no-skill and full-skill baselines before compiling anything
- preserve the markdown skill body as the audited source of truth
- tie any demonstration set or adapter to body hash, source commit, test corpus, and evaluation result
- mount admitted skill directories read-only during execution
Tools, repos, and methodologies worth exploring:
- skill manifests, paired trajectory audits, LoRA/QLoRA lab experiments, read-only bind mounts, sandbox probes, skill-body hash logging
Implementability score: 0.58

## Previous structured update: Daily scan, 2026-06-15

### Typed agent harnesses are becoming the runtime control surface

Summary: HarnessX and AgentSpec push agent scaffolds toward typed, swappable runtime components. Prompts, tools, memory, reflection, and action execution should be versioned and measured as harness parts, not hidden in one prompt loop.

Analysis: [daily reasoning analysis](2026-06-15/reasoning.md#typed-agent-harnesses-are-becoming-the-runtime-control-surface)
Core sources: [HarnessX](https://arxiv.org/abs/2606.14249v1), [AgentSpec](https://arxiv.org/abs/2606.14674v1)
Implementability score: 0.74

### Reasoning memory should be replayable, diffable, and local-first

Summary: GitOfThoughts proposes storing reasoning trees in git, while TencentDB Agent Memory shows demand for local long-term memory infrastructure. The durable memory substrate should support replay, diff, merge, rollback, provenance, and local retention before memory steers future action.

Analysis: [daily reasoning analysis](2026-06-15/reasoning.md#reasoning-memory-should-be-replayable-diffable-and-local-first)
Core sources: [GitOfThoughts](https://arxiv.org/abs/2606.14470v1), [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)
Implementability score: 0.82

### Heterogeneous agent collaboration needs file protocols before shared runtimes

Summary: tap uses a file-based protocol so Claude and Codex can collaborate without one shared runtime, while agentsview supplies local observability across many coding agents. The practical move is to coordinate through structured artifacts first, then add richer orchestration only when the traces prove it is needed.

Analysis: [daily reasoning analysis](2026-06-15/reasoning.md#heterogeneous-agent-collaboration-needs-file-protocols-before-shared-runtimes)
Core sources: [tap](https://arxiv.org/abs/2606.14445v1), [agentsview](https://github.com/kenn-io/agentsview)
Implementability score: 0.88
