# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-15 Friday Synthesis

### Runtime compilation turns tool schemas, capability routers, workflow profiles, and async calls into control surfaces
Summary: The agent harness is becoming a compiler, router, scheduler, and profiler. TSCG, DADL, QVeris, GitHub token-efficiency work, and AsyncFC all point toward versioned tool schemas, routed capabilities, workflow cost profiles, and future-based scheduling as first-class runtime artifacts.

Analysis: [reasoning analysis](2026-05-15/reasoning.md#runtime-compilation-turns-tool-schemas-capability-routers-workflow-profiles-and-async-calls-into-control-surfaces)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources:
- [TSCG](https://arxiv.org/abs/2605.04107)
- [SKZL-AI/tscg](https://github.com/SKZL-AI/tscg)
- [DADL](https://arxiv.org/abs/2605.05247)
- [QVeris agent toolkit](https://github.com/QVerisAI/qveris-agent-toolkit)
- [AsyncFC](https://arxiv.org/abs/2605.15077v1)
- [GitHub token-efficiency practices](https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/)
Implementable now:
- compile tool schemas into deterministic, model-readable bundles
- route tools through capability discovery and audit surfaces instead of exposing entire catalogs
- run token-usage audits for unused tools, fallback loops, and oversized prompts
- add future IDs, `await_future`, resource labels, and latency/accuracy traces for slow tools
Tools, repos, and methodologies worth exploring:
- TSCG, QVeris, AsyncFC, LiteLLM, Temporal, Prefect, OpenTelemetry, model-router audit logs, deterministic schema snapshots
Implementability score: 0.80

### Evaluation moved from final answers to trajectory and process evidence
Summary: PrefixGuard, TEBench, EvalMonkey, SREGym, AgentEscapeBench, AgentLens, SWE-Cycle, and BenchJack show that final pass/fail hides brittle trajectories. Agents need prefix warnings, chaos tests, full-cycle coding evals, lucky-pass detection, and replayable evidence.

Analysis: [reasoning analysis](2026-05-15/reasoning.md#evaluation-moved-from-final-answers-to-trajectory-and-process-evidence)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources:
- [PrefixGuard](https://arxiv.org/abs/2605.06455)
- [TEBench](https://arxiv.org/abs/2605.06125)
- [EvalMonkey](https://github.com/Corbell-AI/evalmonkey)
- [SREGym](https://arxiv.org/abs/2605.07161)
- [AgentLens](https://arxiv.org/abs/2605.12925)
- [SWE-Cycle](https://arxiv.org/abs/2605.13139)
- [BenchJack](https://arxiv.org/abs/2605.12673)
Implementable now:
- store observations, tool calls, edits, tests, errors, retries, and terminal states per run
- run prefix monitors and chaos tests before relying on final answer checks
- grade setup, test evolution, patch quality, review response, and merge readiness
- preserve replay artifacts for regression testing
Tools, repos, and methodologies worth exploring:
- PrefixGuard, TEBench, EvalMonkey, SREGym, OpenTelemetry, pytest/JUnit artifacts, replay harnesses, CI failure classifiers
Implementability score: 0.80

### Memory and context became governed state with provenance
Summary: Memory is no longer transcript recall. Memori, Statewave, MemReranker, MEME, and Agentic GraphRAG provenance all push toward typed memory admission, retrieval budgets, deletion and absence tests, and traversal-path evidence.

Analysis: [reasoning analysis](2026-05-15/reasoning.md#memory-and-context-became-governed-state-with-provenance)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Context Economy for Agents](context-economy/context-economy.md)
Core sources:
- [Memori](https://github.com/MemoriLabs/Memori)
- [Statewave](https://github.com/smaramwbc/statewave)
- [MemReranker](https://arxiv.org/abs/2605.06132)
- [MEME](https://arxiv.org/abs/2605.12477v1)
- [Why Neighborhoods Matter](https://arxiv.org/abs/2605.15109v1)
Implementable now:
- store raw events separately from promoted memories
- add typed memory schemas with source, timestamp, validity, supersession, confidence, and deletion state
- log retrieval paths, graph traversal nodes, discarded candidates, and final citations separately
- test deletion, absence, conflict, stale premise, and dependency reasoning
Tools, repos, and methodologies worth exploring:
- Memori, Statewave, Postgres, pgvector, Qdrant, graph tables, append-only event logs, OpenTelemetry retrieval spans, citation-faithfulness ablations
Implementability score: 0.77

### Skills are becoming a semantic supply chain
Summary: Skills are executable context, not prompt snippets. Anthropic’s skills repository is the demand signal, while SkillOps and semantic fuzzing show why skills need contracts, validators, permissions, side-effect declarations, dependency graphs, and lifecycle maintenance.

Analysis: [reasoning analysis](2026-05-15/reasoning.md#skills-are-becoming-a-semantic-supply-chain)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources:
- [Anthropic skills](https://github.com/anthropics/skills)
- [SkillOps](https://arxiv.org/abs/2605.13716)
- [Hik289/SkillOps](https://github.com/Hik289/SkillOps)
- [Semantic fuzzing for skill spec violations](https://arxiv.org/abs/2605.13044)
Implementable now:
- declare purpose, prerequisites, permissions, side effects, inputs, outputs, and safety constraints in skill metadata
- run semantic fuzz tests against routine-but-risky task variants
- maintain a skill dependency graph and deprecation workflow
- log skill version, permission claims, and side effects in agent traces
Tools, repos, and methodologies worth exploring:
- Anthropic skills, SkillOps, skill manifests, schema validation, regression fixtures, permission metadata, OPA/Cedar policy, preflight side-effect checks
Implementability score: 0.75

### Computer-use agents need GUI tool path supervision
Summary: ToolCUA and ComplexMCP make the GUI-agent problem path-level: agents need to choose and justify routes across clicks, tools, screenshots, files, verification, and recovery. The action path matters as much as the final state.

Analysis: [reasoning analysis](2026-05-15/reasoning.md#computer-use-agents-need-gui-tool-path-supervision)
Durable topic: [GUI-Tool Path Orchestration](gui-tool-path-orchestration/gui-tool-path-orchestration.md)
Core sources:
- [ToolCUA](https://arxiv.org/abs/2605.12481v1)
- [ToolCUA project](https://x-plug.github.io/ToolCUA/)
- [X-PLUG/ToolCUA](https://github.com/X-PLUG/ToolCUA)
- [OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)
- [ComplexMCP](https://arxiv.org/abs/2605.10787v1)
- [trycua/cua](https://github.com/trycua/cua)
Implementable now:
- record screenshots, UI targets, tool calls, file operations, confirmations, and recovery steps in one trace
- compare GUI-only, tool-only, and hybrid routes on the same task
- require explicit verification after state-changing GUI actions
- use deterministic tools when they reduce risk and preserve auditability
Tools, repos, and methodologies worth exploring:
- ToolCUA, OSWorld-MCP, CUA, Playwright, VNC/desktop sandboxes, visual state snapshots, path-level traces, task-level verifiers
Implementability score: 0.64

### Environment and trajectory substrates are the next training layer
Summary: Orchard reframes agent improvement around reusable environment services and trajectory corpora. It is strategically important but operationally heavier than instrumentation work, and its Hugging Face dataset page currently warns that the release is temporarily on hold for re-upload.

Analysis: [reasoning analysis](2026-05-15/reasoning.md#environment-and-trajectory-substrates-are-the-next-training-layer)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources:
- [Orchard](https://arxiv.org/abs/2605.15040v1)
- [microsoft/Orchard dataset](https://huggingface.co/datasets/microsoft/Orchard)
Implementable now:
- define an internal environment API for reset, observe, act, snapshot, verify, and teardown
- store trajectories with messages, tool calls, state snapshots, screenshots, terminal output, verification results, and failure labels
- label productive unresolved segments separately from resolved rollouts
- treat the Orchard dataset as a watch item until the re-upload warning disappears
Tools, repos, and methodologies worth exploring:
- Orchard Env, SWE-bench Verified, WebVoyager, Online-Mind2Web, DeepShop, trajectory schemas, sandbox lifecycle APIs, credit-assignment SFT, Balanced Adaptive Rollout-style RL
Implementability score: 0.62
