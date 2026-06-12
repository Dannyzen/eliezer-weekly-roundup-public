# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday synthesis, week ending 2026-06-12

### Tool execution should be raised from atomic calls to auditable macro-actions

Summary: The week’s context-economy signal is execution granularity. HyperTool, Less Context, ToolChoiceConfusion, skill rewriting, and Copilot CLI language-server integration all argue that deterministic tool workflows should move into typed executable blocks or state-aware tool frontiers instead of bloating the model trace.

Analysis: [weekly reasoning analysis](2026-06-12/reasoning.md#tool-execution-should-be-raised-from-atomic-calls-to-auditable-macro-actions)
Durable topics: [Context Economy](context-economy/context-economy.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [HyperTool](https://arxiv.org/abs/2606.13663v1), [Less Context, Better Agents](https://arxiv.org/abs/2606.10209v1), [ToolChoiceConfusion](https://arxiv.org/abs/2606.06284v1), [Copilot CLI language servers](https://github.blog/ai-and-ml/github-copilot/give-github-copilot-cli-real-code-intelligence-with-language-servers/)
Implementable now:
- build macro-tools for deterministic multi-step subroutines;
- preserve original tool schemas inside executable boundaries;
- return compact outputs with source IDs, intermediate-operation logs, and failure summaries.
Tools, repos, and methodologies worth exploring:
- MCP-style tool wrappers, language-server tools, state-frontier tool exposure, macro-actions, trace-length ablations
Implementability score: 0.84

### Harnesses should be delegated and evaluated as runtimes, not chats

Summary: Recursive Agent Harnesses, Layer-Isolated Evaluation, failed-trajectory repair, MASArena, OpenEnv, and AGENTSERVESIM all point at the same operating model: evaluate and delegate full harnesses with workspaces, budgets, tools, traces, and output contracts, not loose agent personas.

Analysis: [weekly reasoning analysis](2026-06-12/reasoning.md#harnesses-should-be-delegated-and-evaluated-as-runtimes-not-chats)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md)
Core sources: [Recursive Agent Harnesses](https://arxiv.org/abs/2606.13643v1), [Layer-Isolated Evaluation](https://arxiv.org/abs/2606.11686v1), [OpenEnv](https://huggingface.co/blog/openenv-agentic-rl), [AGENTSERVESIM](https://arxiv.org/abs/2606.09613v1)
Implementable now:
- create parent-child run manifests with depth, budget, workspace, tool scope, model, and output schema;
- run deterministic per-layer CI fixtures for routing, memory, escalation, decomposition, safety, and envelope logic;
- replay failed trajectories and promote layer-local repairs into regression fixtures.
Tools, repos, and methodologies worth exploring:
- recursive harness manifests, layer-isolated evals, OpenEnv sockets, program-level serving simulation, normalized multi-agent baselines
Implementability score: 0.76

### Memory should be evented, typed, and gated before it reaches the prompt

Summary: PROJECTMEM, Infini Memory, MemoryScale, bitemporal memory, and graph-memory selection integrity move memory from recall feature to state system. The useful design is typed events, staged topic memory, compact projections, and write-path gates before memory can influence high-authority actions.

Analysis: [weekly reasoning analysis](2026-06-12/reasoning.md#memory-should-be-evented-typed-and-gated-before-it-reaches-the-prompt)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Context Economy](context-economy/context-economy.md)
Core sources: [PROJECTMEM](https://arxiv.org/abs/2606.12329v1), [PROJECTMEM repo](https://github.com/riponcm/projectmem), [Infini Memory](https://arxiv.org/abs/2606.10677v1), [Selection Integrity](https://arxiv.org/abs/2606.12290v1)
Implementable now:
- log issues, attempts, fixes, decisions, fragile files, and failures as typed local events;
- project compact prompt summaries while preserving raw episodes outside the prompt;
- stage observations before promotion and attach evidence IDs, valid time, transaction time, and supersession.
Tools, repos, and methodologies worth exploring:
- event-sourced local memory, MCP summary projection, bitemporal fact stores, graph-selection path logs, memory write gates
Implementability score: 0.80

### Skills and user preferences should compile into verifiers

Summary: Trace shows that remembering a user correction is not the same as obeying it. This week’s skill work says corrections, skills, and AI guidance files need manifests, hashes, applicability predicates, runtime probes, context-rot checks, and final-state verifiers.

Analysis: [weekly reasoning analysis](2026-06-12/reasoning.md#skills-and-user-preferences-should-compile-into-verifiers)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Memory Systems](memory-systems/memory-systems.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [Getting Better at Working With You](https://arxiv.org/abs/2606.13174v1), [MalSkillBench](https://arxiv.org/abs/2606.07131v1), [Runtime Skill Audit](https://arxiv.org/abs/2606.11671v1), [Snyk Agent Scan](https://github.com/snyk/agent-scan)
Implementable now:
- extract corrections into atomic rules with examples and counterexamples;
- attach applicability predicates and final-state verifiers;
- require skill manifests, loaded-body hashes, static checks, sandbox probes, and repo-context rot tests.
Tools, repos, and methodologies worth exploring:
- correction-derived regression fixtures, executable skill checks, skill manifests, sandbox probes, guidance-file rot scanners
Implementability score: 0.83

## Previous structured update

The prior Friday synthesis for 2026-06-05 focused on evidence-bearing control planes: [week ending 2026-06-05 roundup](../roundups/2026-06-05.md).
