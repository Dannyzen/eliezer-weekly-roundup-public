# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-19 Daily Scan

### Open Agent Leaderboard makes the full agent system the eval unit
Summary: IBM Research’s Open Agent Leaderboard evaluates complete agent systems rather than base models alone. It treats the wrapper, tools, planning, memory, recovery behavior, and cost as part of the measured object.

Analysis: [reasoning analysis](2026-05-19/reasoning.md#open-agent-leaderboard-makes-the-full-agent-system-the-eval-unit)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [The Open Agent Leaderboard](https://huggingface.co/blog/ibm-research/open-agent-leaderboard)
Implementable now:
- normalize tasks into task/context/action;
- compare model x scaffold x tool-shortlist variants;
- track success, cost, retries, failed-run premium, and tool-selection errors together;
- preserve result artifacts and traces for replay.
Tools, repos, and methodologies worth exploring:
- Exgentic, Open Agent Leaderboard Space, Open Agent Leaderboard results dataset, OpenTelemetry traces, cost-per-task dashboards, scaffold A/B tests
Implementability score: 0.86

### EnvFactory turns tool-use RL into executable environment supply
Summary: EnvFactory frames stateful tool environments as the bottleneck for agentic RL. It synthesizes verified executable environments and natural multi-turn trajectories so tool-use agents can train and evaluate against realistic hidden intents.

Analysis: [reasoning analysis](2026-05-19/reasoning.md#envfactory-turns-tool-use-rl-into-executable-environment-supply)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [EnvFactory](https://arxiv.org/abs/2605.18703v1)
Implementable now:
- build verified mock environments for a few high-value internal workflows;
- generate natural intents instead of scripted step-by-step instructions;
- score state transitions, payload correctness, recovery, and final outcome;
- reuse the environments for SFT data, RL experiments, and CI regression.
Tools, repos, and methodologies worth exploring:
- tau2-Bench, BFCL, MCP-Atlas-style evals, AppWorld-style simulated apps, LangGraph/custom state machines, Schemathesis, OpenAPI specs, deterministic mock services
Implementability score: 0.55

### AMARIS treats rubric updates as memory, not per-step improvisation
Summary: AMARIS stores rollout diagnostics and historical rubric failures so RL reward rubrics improve from persistent evaluation memory instead of re-deriving criteria from the current step alone.

Analysis: [reasoning analysis](2026-05-19/reasoning.md#amaris-treats-rubric-updates-as-memory-not-per-step-improvisation)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [AMARIS](https://arxiv.org/abs/2605.18592v1)
Implementable now:
- store rubric-level diagnostics from eval runs;
- retrieve recent and semantically similar historical failures when updating rubrics;
- version rubric changes with provenance and rollback;
- keep rubric refinement asynchronous.
Tools, repos, and methodologies worth exploring:
- structured rubrics, SQLite/Postgres evaluation memory, BM25/vector retrieval, W&B or MLflow experiment history, TRL-style RL loops, OpenTelemetry traces
Implementability score: 0.58

## Previous structured update

The prior daily scan for 2026-05-18 focused on population-broadcast memory and evidence-graph research orchestration: [2026-05-18 reasoning](2026-05-18/reasoning.md).
