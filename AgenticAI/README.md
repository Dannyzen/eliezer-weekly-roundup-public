# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-29 Friday Synthesis

### Agent evaluation is moving from answers to evidence packages
Summary: Spec review, goal persistence, fault injection, search freshness, incident response, and sabotage audits all point to one rule: serious agent eval needs traces, artifacts, state snapshots, and verifier evidence, not just final answers.

Analysis: [weekly reasoning analysis](2026-05-29/reasoning.md#agent-evaluation-is-moving-from-answers-to-evidence-packages)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [Goal-persistence metrics](https://arxiv.org/abs/2605.23574), [Agent-breakage](https://arxiv.org/abs/2605.23058), [LiveBrowseComp](https://arxiv.org/abs/2605.28721), [ITBench-AA](https://huggingface.co/blog/ibm-research/itbench-aa), [RAMPART](https://github.com/microsoft/RAMPART), [SpecBench](https://arxiv.org/abs/2605.30314)
Implementable now:
- require spec critique before code edits;
- preserve traces, state snapshots, artifacts, verifier outputs, and failure labels;
- run fault-injection and freshness/feasibility fixtures before expanding agent scope.
Tools, repos, and methodologies worth exploring:
- RFC/ADR review gates, SWE-Bench-style replay, OpenTelemetry, LangSmith/Langfuse, pytest, RAMPART, ITBench-AA, internal incident/postmortem replay
Implementability score: 0.82

### Routing is now workflow, retrieval, wait-time, and team-topology control
Summary: Routing now covers graph/prompt/gateway/code/weight placement, per-query retrieval settings, tool-wait budgets, and confidence-gated multi-agent communication. Static RAG and all-agent chat are weak defaults.

Analysis: [weekly reasoning analysis](2026-05-29/reasoning.md#routing-is-now-workflow-retrieval-wait-time-and-team-topology-control)
Durable topics: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core sources: [workflow placement](https://arxiv.org/abs/2605.22566v1), [workflow compilation](https://arxiv.org/abs/2605.22502v1), [per-query retrieval](https://arxiv.org/abs/2605.27361), [CONCAT](https://arxiv.org/abs/2605.29612), [DynaGraph](https://arxiv.org/abs/2605.29511), [Meta-Team](https://arxiv.org/abs/2605.29790)
Implementable now:
- expose retrieval policy as a traceable per-query decision;
- collect first-pass confidence before multi-agent discussion;
- log topology changes, tool-wait decisions, and routing choices as first-class events.
Tools, repos, and methodologies worth exploring:
- LangGraph, AutoGen, CrewAI, Temporal, Pydantic state machines, LiteLLM, OpenTelemetry, confidence calibration, retrieval-policy classifiers
Implementability score: 0.74

### Skills, tools, and memory need lifecycle governance, not bigger libraries
Summary: Larger skill libraries, generated tool catalogs, and memory stores are liabilities unless they are validated, versioned, traced, promoted, quarantined, and rollbackable.

Analysis: [weekly reasoning analysis](2026-05-29/reasoning.md#skills-tools-and-memory-need-lifecycle-governance-not-bigger-libraries)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Memory Systems](memory-systems/memory-systems.md)
Core sources: [skills as API/MCP units](https://arxiv.org/abs/2605.22733), [OpenSkillEval](https://arxiv.org/abs/2605.23904), [personalized memory gates](https://arxiv.org/abs/2605.25535), [MemTrace](https://arxiv.org/abs/2605.28732), [zjunlp/MemTrace](https://github.com/zjunlp/MemTrace), [Tool Forge](https://github.com/nextmoca/tool-forge)
Implementable now:
- attach schemas, tests, owners, and hashes to skills/tools;
- trace loaded skill/tool/memory versions in every run;
- promote generated tools only after sandbox validation and catalog review.
Tools, repos, and methodologies worth exploring:
- pytest fixtures, Pydantic/OpenAPI schemas, Tool Forge, MemTrace, OPA/Cedar, MCP Inspector, OpenTelemetry, promotion/quarantine dashboards
Implementability score: 0.72

### Computer-use agents need executable workspaces and verifiable environments
Summary: Browser and desktop agents should leave runnable scripts, logs, artifacts, checksums, screenshots, and assertions. Screenshot-only automation is not a serious reliability story.

Analysis: [weekly reasoning analysis](2026-05-29/reasoning.md#computer-use-agents-need-executable-workspaces-and-verifiable-environments)
Durable topics: [GUI-Tool Path Orchestration](gui-tool-path-orchestration/gui-tool-path-orchestration.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [Webwright article](https://www.microsoft.com/en-us/research/articles/webwright-a-terminal-is-all-you-need-for-web-agents/), [microsoft/Webwright](https://github.com/microsoft/Webwright), [computer-use verification](https://arxiv.org/abs/2605.25624), [reward validation](https://arxiv.org/abs/2605.26114), [Sandlock](https://github.com/multikernel/sandlock)
Implementable now:
- require browser agents to emit scripts, logs, screenshots, downloads, and assertions;
- verify final state with DOM/file/API checks;
- run risky local execution in a process, container, or VM sandbox.
Tools, repos, and methodologies worth exploring:
- Webwright, Playwright, pytest, browser workflow manifests, file checksums, OpenTelemetry, Sandlock, container/VM fallbacks
Implementability score: 0.76

## Previous structured update

The prior Friday synthesis for 2026-05-22 focused on replayable agent infrastructure, evidence graphs, trace-aware eval, harness contracts, and MCP gateway governance: [2026-05-22 synthesis](../roundups/2026-05-22.md).
