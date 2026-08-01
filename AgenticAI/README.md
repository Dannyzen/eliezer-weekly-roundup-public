# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-01

### Replayable runtime state is now a released harness contract

Summary: Microsoft Agent Framework Python 1.13.0 combines reusable session stores, complete Responses-session persistence, replayable checkpoints, approval continuity, bounded MCP skill discovery, and token observability. The useful unit is no longer a chat transcript. It is a replayable run state with approvals and tool evidence attached.

Analysis: [daily analysis](2026-08-01/reasoning.md#microsoft-agent-framework-makes-replayable-state-a-released-runtime-contract)
Core sources: [Python 1.13.0 release](https://github.com/microsoft/agent-framework/releases/tag/python-1.13.0), [repository](https://github.com/microsoft/agent-framework)
Implementable now:
- pin the harness and provider adapters as one profile;
- persist input, human responses, approvals, tools, and checkpoints together;
- run crash, resume, compaction, approval replay, and migration fixtures.
Tools, repositories, and methodologies:
- Microsoft Agent Framework, OpenTelemetry, replayable checkpoint tests, bounded MCP archives
Implementability score: 0.90

### Offline tests and production traces need one metric registry

Summary: Google Agent Platform evaluations are generally available with more than 20 metrics, versioned custom metrics, adaptive rubrics, local and server-side experiments, production monitors, drift alerts, user simulation, and environment fault simulation.

Analysis: [daily analysis](2026-08-01/reasoning.md#google-unifies-pre-release-and-production-evaluation-on-one-metric-registry)
Core sources: [GA announcement](https://developers.googleblog.com/agent-and-model-evaluations-in-gemini-enterprise-agent-platform-are-now-ga/), [agents-cli](https://github.com/google/agents-cli)
Implementable now:
- keep deterministic checks load-bearing;
- version metrics, datasets, simulators, models, and trace schemas;
- run the same metric offline and on sampled production traces;
- turn failure clusters into regression cases.
Tools, repositories, and methodologies:
- Gemini Enterprise Agent Platform, ADK eval, agents-cli, Cloud Trace, environment simulation
Implementability score: 0.82

## Current implication

Treat session state and evaluation policy as versioned runtime artifacts. A checkpoint must replay the exact approval and tool history, and a production score must name the same metric definition used before release.
