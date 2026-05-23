# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-23 Daily Scan

### Source-level self-evolution needs replay-gated code promotion
Summary: MOSS pushes self-improving agents below prompt, skill, memory, and workflow mutation into source-level harness rewriting. The useful pattern is not autonomous self-editing; it is failure-batch replay, isolated candidate images, predicted-effect manifests, consent gates, health probes, and rollback.

Analysis: [daily reasoning analysis](2026-05-23/reasoning.md#source-level-self-evolution-has-to-be-a-replay-gated-code-promotion-loop)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [MOSS](https://arxiv.org/abs/2605.22794v1)
Implementable now:
- turn recurring failures into replay suites;
- version harness/source components in git;
- require patch manifests with predicted fixes and regression risks;
- test candidate patches in ephemeral trial workers or containers;
- gate promotion through CI, consent, health probes, and rollback.
Tools, repos, and methodologies worth exploring:
- replay harnesses, git-backed harness components, isolated candidate containers, OpenTelemetry/LangSmith traces, CI promotion gates, health-probe rollbacks
Implementability score: 0.58

### Workflow control is becoming a placement decision
Summary: GraphFlow and workflow-compilation point to the same design rule from different sides: workflow logic should live where evidence says it belongs. Volatile, audited, tool-heavy workflows want graphs/gateways. Stable procedures may justify prompt-only baselines or small-model fine-tuning.

Analysis: [daily reasoning analysis](2026-05-23/reasoning.md#workflow-control-is-splitting-between-graph-serving-and-weight-compilation)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [GraphFlow](https://arxiv.org/abs/2605.22566v1), [Compiling Agentic Workflows into LLM Weights](https://arxiv.org/abs/2605.22502v1)
Implementable now:
- compare prompt-only, graph-orchestrated, and fine-tuned variants for one procedural workflow;
- record cost, latency, memory, quality, failure modes, and auditability;
- keep volatile policy and approval logic outside weights;
- compile only stable, well-instrumented procedures with clean trajectory data.
Tools, repos, and methodologies worth exploring:
- workflow graphs, KV-cache-aware serving, prompt baselines, fine-tuning pipelines, cost/latency dashboards, workflow-placement scorecards
Implementability score: 0.54

## Previous structured update

The prior Friday synthesis for 2026-05-22 focused on evidence-graph research agents, trace-aware evaluation, replayable state/memory gates, harness contracts, and coding-agent cost telemetry: [2026-05-22 reasoning](2026-05-22/reasoning.md).
