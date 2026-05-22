# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-22 Friday Synthesis

### Evidence-graph research agents need derivation and calibration audits
Summary: The week’s research-agent sources say the bottleneck is not just finding more pages. The stronger pattern is claim-evidence-derivation structure: lexical baselines, missing-evidence slots, evidence assembly, derivation audits, and calibration scoring.

Analysis: [weekly reasoning analysis](2026-05-22/reasoning.md#evidence-graph-research-agents-need-derivation-and-calibration-audits)
Durable topic: [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core sources: [Harness-shaped retrieval](https://arxiv.org/abs/2605.15184), [Argus](https://arxiv.org/abs/2605.16217), [DeepWeb-Bench](https://arxiv.org/abs/2605.21482v1)
Implementable now:
- run exact lexical retrieval beside vector search;
- store claims, evidence, derivation steps, contradictions, and missing slots as typed objects;
- dispatch search toward missing evidence slots, not duplicate whole-answer rollouts;
- score retrieval, derivation, and calibration separately.
Tools, repos, and methodologies worth exploring:
- evidence graphs, claim extraction, DeepWeb-Bench-style labels, Argus-style Searcher/Navigator separation, pgvector plus lexical search, trace-preserved research workflows
Implementability score: 0.83

### Trace-aware evaluation is an evidence pipeline, not a score
Summary: Open Agent Leaderboard, SpecBench, TerminalWorld, Agentic CLEAR, and SynAE point to eval as infrastructure: full-system traces, hidden composed tests, realistic terminal/workflow tasks, node-level failure analysis, and synthetic-data quality audits.

Analysis: [weekly reasoning analysis](2026-05-22/reasoning.md#trace-aware-evaluation-is-an-evidence-pipeline-not-a-scoreboard)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [Open Agent Leaderboard](https://huggingface.co/blog/ibm-research/open-agent-leaderboard), [SpecBench](https://arxiv.org/abs/2605.21384v1), [TerminalWorld](https://arxiv.org/abs/2605.22535), [Agentic CLEAR](https://arxiv.org/abs/2605.22608), [SynAE](https://arxiv.org/abs/2605.22564)
Implementable now:
- preserve full traces with model, scaffold, tool, dataset, and cost metadata;
- add hidden composed tests and real task-world subsets;
- label failures at system, trace, and node levels;
- audit synthetic tool-call traces for validity, fidelity, diversity, and rank preservation.
Tools, repos, and methodologies worth exploring:
- `Exgentic/exgentic`, `EuniAI/TerminalWorld`, `wsqwsq/SynAE`, OpenTelemetry/LangSmith traces, hidden integration tests, synthetic-data audits
Implementability score: 0.85

### Replayable state and memory gates should precede self-improvement loops
Summary: ActiveGraph makes the event log the source of truth. FORGE and Mem-pi show useful memory-improvement patterns. Faulty-memory and sleeper-memory work show the failure mode: unverified memory rewrites and persistent context can corrupt or poison future action.

Analysis: [weekly reasoning analysis](2026-05-22/reasoning.md#replayable-state-and-memory-gates-should-precede-self-improvement-loops)
Durable topics: [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Memory Systems](memory-systems/memory-systems.md)
Core sources: [The Log is the Agent](https://arxiv.org/abs/2605.21997), [ActiveGraph](https://activegraph.ai/), [Faulty memories](https://arxiv.org/abs/2605.12978), [FORGE](https://arxiv.org/abs/2605.16233), [Mem-pi](https://arxiv.org/abs/2605.21463v1)
Implementable now:
- store model calls, tool calls, object mutations, policy decisions, failures, and artifacts as append-only events;
- project tasks, evidence, artifacts, and policies from the log;
- promote memory only through provenance gates;
- test stale-premise, deletion, contradiction, and poisoning cases.
Tools, repos, and methodologies worth exploring:
- `yoheinakajima/activegraph`, event sourcing, replay/fork/diff, provenance graphs, typed memory schemas, writeback firewalls, memory taint labels
Implementability score: 0.71

### Harness contracts beat prompt folklore
Summary: Agent reliability work this week centered on the runtime boundary: stochastic/deterministic handoffs, skill admission, browser-plan compilation, and Life-Harness-style interface adaptation. The model is not the whole agent.

Analysis: [weekly reasoning analysis](2026-05-22/reasoning.md#harness-contracts-beat-prompt-folklore)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [runtime boundaries](https://arxiv.org/abs/2605.20173v1), [skill admission](https://arxiv.org/abs/2605.20023v1), [Agent JIT](https://arxiv.org/abs/2605.21470v1), [Life-Harness](https://arxiv.org/abs/2605.22166)
Implementable now:
- define propose/verify/commit/reject phases for side effects;
- measure skill load/no-load effects;
- compile browser or workflow plans before execution;
- mine failed traces into versioned harness patches;
- test interface fixes across multiple models.
Tools, repos, and methodologies worth exploring:
- `vasundras/agent-runtime-patterns`, `stanford-mast/blast`, harness patch manifests, replay suites, skill admission tests, deterministic task harnesses
Implementability score: 0.77

### Coding-agent productivity now includes operating-cost telemetry
Summary: Coding-agent quality now means more than pass rate. Code cleanliness affects token/file-revisit cost; hidden tests expose reward hacking; proof-carrying outputs remain promising but heavy; managed cloud agents need configuration audit.

Analysis: [weekly reasoning analysis](2026-05-22/reasoning.md#coding-agent-productivity-now-includes-operating-cost-telemetry)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [code cleanliness and cost](https://arxiv.org/abs/2605.20049v1), [SpecBench](https://arxiv.org/abs/2605.21384v1), [Viverra](https://arxiv.org/abs/2605.14972), [Copilot cloud-agent audit](https://github.blog/changelog/2026-05-18-audit-repository-copilot-cloud-agent-configuration-via-the-rest-api)
Implementable now:
- track token spend, file revisits, command count, retries, and elapsed time;
- run hidden composed tests;
- label claims as proved, tested, inspected, or unsupported;
- preserve command/test traces with patch diffs;
- audit cloud-agent configuration by repo.
Tools, repos, and methodologies worth exploring:
- static analysis, cognitive-complexity metrics, trace/cost dashboards, hidden tests, proof/non-proof labeling, GitHub Copilot cloud-agent audit APIs
Implementability score: 0.76

## Previous structured update

The prior daily scan for 2026-05-21 focused on deep-research derivation audits, browser-agent plan compilation, abstaining memory guidance, and hidden coding-agent tests: [2026-05-21 reasoning](2026-05-21/reasoning.md).
