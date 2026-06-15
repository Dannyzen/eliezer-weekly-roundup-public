# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-15

### Typed agent harnesses are becoming the runtime control surface

Summary: HarnessX and AgentSpec push agent scaffolds toward typed, swappable runtime components. Prompts, tools, memory, reflection, and action execution should be versioned and measured as harness parts, not hidden in one prompt loop.

Analysis: [daily reasoning analysis](2026-06-15/reasoning.md#typed-agent-harnesses-are-becoming-the-runtime-control-surface)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core sources: [HarnessX](https://arxiv.org/abs/2606.14249v1), [AgentSpec](https://arxiv.org/abs/2606.14674v1)
Implementable now:
- define typed internal interfaces for perception, memory, tool selection, action, verifier, and answer phases
- log harness component versions with every run
- replay one component swap at a time before adopting autonomous harness evolution
- require harness patches to name failed trace evidence and regression risk
Tools, repos, and methodologies worth exploring:
- LangGraph, Temporal, OpenTelemetry, Langfuse, LangSmith, Pydantic component schemas, replay fixtures
Implementability score: 0.74

### Reasoning memory should be replayable, diffable, and local-first

Summary: GitOfThoughts proposes storing reasoning trees in git, while TencentDB Agent Memory shows demand for local long-term memory infrastructure. The durable memory substrate should support replay, diff, merge, rollback, provenance, and local retention before memory steers future action.

Analysis: [daily reasoning analysis](2026-06-15/reasoning.md#reasoning-memory-should-be-replayable-diffable-and-local-first)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Local-First Agents](../Strategy/local-first-agents/local-first-agents.md)
Core sources: [GitOfThoughts](https://arxiv.org/abs/2606.14470v1), [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)
Implementable now:
- store high-value memory writes as append-only events with stable IDs
- make diff and rollback first-class for memory changes
- keep private project memory local by default
- preserve source episode, writer, timestamp, and outcome with promoted memories
Tools, repos, and methodologies worth exploring:
- git-backed memory logs, SQLite event stores, local vector indexes, TencentDB Agent Memory, replayable memory tests
Implementability score: 0.82

### Heterogeneous agent collaboration needs file protocols before shared runtimes

Summary: tap uses a file-based protocol so Claude and Codex can collaborate without one shared runtime, while agentsview supplies local observability across many coding agents. The practical move is to coordinate through structured artifacts first, then add richer orchestration only when the traces prove it is needed.

Analysis: [daily reasoning analysis](2026-06-15/reasoning.md#heterogeneous-agent-collaboration-needs-file-protocols-before-shared-runtimes)
Durable topics: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Local-First Agents](../Strategy/local-first-agents/local-first-agents.md)
Core sources: [tap](https://arxiv.org/abs/2606.14445v1), [agentsview](https://github.com/kenn-io/agentsview)
Implementable now:
- define an `agents/` workspace convention for requests, claims, evidence, reviews, and handoffs
- require structured status and evidence files from each agent
- normalize local logs across agents into one trace view
- compare single-agent, handoff, and parallel-agent runs by quality, cost, and latency
Tools, repos, and methodologies worth exploring:
- tap-style file protocols, agentsview, git worktrees, Pydantic handoff schemas, local token/cost dashboards
Implementability score: 0.88

## Previous structured update: Daily scan, 2026-06-14

### HyperTool folds deterministic tool workflows into executable MCP-style blocks

Summary: HyperTool replaces step-wise atomic tool calls with executable code blocks that call existing tools through their original schemas, manipulate returned values, and pass intermediate results locally.

Analysis: [daily reasoning analysis](2026-06-14/reasoning.md#hypertool-folds-deterministic-tool-workflows-into-executable-mcp-style-blocks)
Core sources: [HyperTool](https://arxiv.org/abs/2606.13663v1)
Implementability score: 0.85

### Recursive Agent Harnesses make the harness itself the recursive unit

Summary: Recursive Agent Harnesses make spawning child harnesses a first-class runtime operation with workspace, tools, context, and typed output contracts.

Analysis: [daily reasoning analysis](2026-06-14/reasoning.md#recursive-agent-harnesses-make-the-harness-itself-the-recursive-unit)
Core sources: [Recursive Agent Harnesses](https://arxiv.org/abs/2606.13643v1)
Implementability score: 0.75

### Brick routes by capability geometry, not keywords

Summary: Brick scores models on capability dimensions and routes with a cost-penalized geometric rule plus an operator-controlled quality/savings knob.

Analysis: [daily reasoning analysis](2026-06-14/reasoning.md#brick-routes-by-capability-geometry-not-keywords)
Core sources: [Brick](https://arxiv.org/abs/2606.13241v1)
Implementability score: 0.70
