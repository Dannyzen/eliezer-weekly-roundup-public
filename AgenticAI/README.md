# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-22 Daily Scan

### Event-sourced runtimes make agent state replayable
Summary: ActiveGraph makes the append-only event log the source of truth and projects working graph state from it. That gives agents replay, fork/diff, and end-to-end lineage that transcript-plus-memory systems cannot provide.

Analysis: [reasoning analysis](2026-05-22/reasoning.md#activegraph-makes-the-event-log-the-agent-state)
Durable topic: [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md)
Core source: [The Log is the Agent](https://arxiv.org/abs/2605.21997)
Implementable now:
- store model calls, tool calls, object mutations, relation changes, policy decisions, failures, and final artifacts as append-only events;
- project claims, evidence, tasks, and artifacts into a graph from the log;
- cache model/tool responses where possible so runs can replay;
- add fork-and-diff to one narrow workflow before generalizing.
Tools, repos, and methodologies worth exploring:
- `yoheinakajima/activegraph`, event sourcing, graph projections, deterministic replay caches, structural diffs, lineage graphs, OpenTelemetry trace IDs
Implementability score: 0.84

### Harness fixes should target runtime interfaces before model weights
Summary: Life-Harness argues that deterministic-agent failures often come from environment contracts, action realization, procedural skills, and trajectory regulation. Those are harness-interface problems, not only model-weight problems.

Analysis: [reasoning analysis](2026-05-22/reasoning.md#life-harness-says-fix-the-interface-before-the-model)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [Adapting the Interface, Not the Model](https://arxiv.org/abs/2605.22166)
Implementable now:
- mine failed traces for recurring environment-contract and action-realization failures;
- convert those failures into versioned harness interventions;
- test harness patches across multiple models;
- log loop-control and termination fixes as runtime components, not prompt folklore.
Tools, repos, and methodologies worth exploring:
- trace clustering, harness patch manifests, replay suites, `tau-bench`, `tau^2-bench`, AgentBench-style deterministic tasks, model-agnostic A/B tests
Implementability score: 0.66

### Agent eval needs real task worlds and synthetic-data audits
Summary: TerminalWorld derives terminal-agent tasks from in-the-wild recordings, Agentic CLEAR analyzes agents at system/trace/node levels, and SynAE measures whether synthetic tool-calling traces preserve validity, fidelity, diversity, and downstream utility.

Analysis: [reasoning analysis](2026-05-22/reasoning.md#terminalworld-agentic-clear-and-synae-turn-eval-into-a-trace-and-data-quality-stack)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [TerminalWorld](https://arxiv.org/abs/2605.22535), [Agentic CLEAR](https://arxiv.org/abs/2605.22608), [SynAE](https://arxiv.org/abs/2605.22564)
Implementable now:
- build a small verified subset of real terminal or workflow tasks;
- preserve full traces and label failures at node, trace, and system levels;
- audit synthetic tool-call trajectories for format validity, semantic fidelity, diversity, and downstream ranking preservation;
- store scaffold, model, dataset version, cost, and failure taxonomy with every run.
Tools, repos, and methodologies worth exploring:
- `EuniAI/TerminalWorld`, TerminalWorld dataset, `wsqwsq/SynAE`, Agentic CLEAR-style multi-level eval, OpenTelemetry/LangSmith traces, synthetic-data quality checks
Implementability score: 0.78

## Previous structured update

The prior daily scan for 2026-05-21 focused on deep-research derivation audits, browser-agent plan compilation, abstaining memory guidance, and hidden coding-agent tests: [2026-05-21 reasoning](2026-05-21/reasoning.md).
