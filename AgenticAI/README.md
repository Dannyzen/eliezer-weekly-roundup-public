# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-24 Daily Scan

### Browser agents are becoming terminal-coded workspaces
Summary: Webwright makes a browser agent look more like a coding agent: write Playwright scripts, run disposable browser sessions, keep screenshots/logs/code as evidence, and finish with a rerunnable script instead of a brittle click transcript.

Analysis: [daily reasoning analysis](2026-05-24/reasoning.md#browser-agents-are-becoming-terminal-coded-workspaces)
Durable topic: [GUI-Tool Path Orchestration](gui-tool-path-orchestration/gui-tool-path-orchestration.md)
Core sources: [Microsoft Research Webwright](https://www.microsoft.com/en-us/research/articles/webwright-a-terminal-is-all-you-need-for-web-agents/), [microsoft/Webwright](https://github.com/microsoft/Webwright)
Implementable now:
- add a browser-task-as-script mode to local browser-agent evals;
- require rerunnable scripts, screenshots, logs, and final assertions;
- compare click-by-click control against Playwright-scripted control;
- promote repeated successful scripts into reviewed local tools.
Tools, repos, and methodologies worth exploring:
- Webwright, Playwright, fresh-run validation, screenshot/log evidence, ClawBench-style live browser tasks
Implementability score: 0.78

### Skills are becoming API and MCP compilation units
Summary: HarnessAPI, Unbrowse, and CodeGraph all compress recurring agent work into callable local infrastructure: typed skills compile into HTTP and MCP tools, browser workflows compile into reusable API paths, and codebases compile into queryable local graphs.

Analysis: [daily reasoning analysis](2026-05-24/reasoning.md#skills-are-becoming-api-and-mcp-compilation-units)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [HarnessAPI paper](https://arxiv.org/abs/2605.22733), [HarnessAPI repo](https://github.com/edwinjosechittilappilly/harnessapi), [Unbrowse](https://github.com/unbrowse-ai/unbrowse), [CodeGraph](https://github.com/colbymchenry/codegraph)
Implementable now:
- make typed schemas the source of truth for high-value skills;
- expose reviewed skills through HTTP and MCP where useful;
- capture recurring browser workflows as reviewed API contracts;
- add local code-graph indexes for large repos before repeated file scanning.
Tools, repos, and methodologies worth exploring:
- FastAPI, FastMCP, Pydantic, MCP servers, OpenAPI, local code graphs, skill-hash logging
Implementability score: 0.72

### Tool wait time is becoming schedulable compute
Summary: SpecHop and IdleSpec turn tool latency into a harness-scheduler problem. While an agent waits for search, retrieval, browser, or execution outputs, it can draft reversible branches, prefetch read-only evidence, and commit only after observations are verified.

Analysis: [daily reasoning analysis](2026-05-24/reasoning.md#tool-wait-time-is-becoming-schedulable-compute)
Durable topic: [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core sources: [SpecHop](https://arxiv.org/abs/2605.21965), [IdleSpec](https://arxiv.org/abs/2605.22154), [SpecHop repo](https://github.com/mehrdadsaberi/spechop)
Implementable now:
- measure tool-wait time by tool class;
- speculate only on reversible read-only branches first;
- keep speculative outputs out of memory until verified;
- log branch, commit, rollback, latency, and cost.
Tools, repos, and methodologies worth exploring:
- async tool execution, branch logs, cancellation tokens, speculative prefetch, trace-level cost accounting
Implementability score: 0.46

### Workflow eval is moving from final answers to stateful work products
Summary: SGR-Bench, WorkstreamBench, ClawBench, GBQA, Agentic CLEAR, and SynAE all push eval toward state, artifacts, process defects, and synthetic-data fidelity. A plausible answer is not enough if the agent used the wrong retrieval state or produced an unreviewable artifact.

Analysis: [daily reasoning analysis](2026-05-24/reasoning.md#workflow-eval-is-moving-from-final-answers-to-stateful-work-products)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core sources: [SGR-Bench](https://arxiv.org/abs/2605.22219), [WorkstreamBench](https://arxiv.org/abs/2605.22664), [Agentic CLEAR](https://arxiv.org/abs/2605.22608), [SynAE](https://arxiv.org/abs/2605.22564), [ClawBench](https://github.com/TIGER-AI-Lab/ClawBench), [GBQA](https://github.com/camel-ai/GBQA)
Implementable now:
- add retrieval-state checks to research/search agents;
- preserve browser, terminal, workspace, and spreadsheet artifacts;
- grade formulas, lineage, format, and modifiability;
- label failures at system, trace, and node levels;
- audit synthetic traces for validity, fidelity, diversity, and downstream ranking behavior.
Tools, repos, and methodologies worth exploring:
- SGR-Bench dataset, ClawBench, GBQA, SynAE, verifier-owned tests, state snapshots, trace schemas
Implementability score: 0.62

## Previous structured update

The prior daily scan for 2026-05-23 focused on source-level self-evolution, workflow placement, KV-cache boundaries, and stateful evasion/MCP-client telemetry: [2026-05-23 reasoning](2026-05-23/reasoning.md).
