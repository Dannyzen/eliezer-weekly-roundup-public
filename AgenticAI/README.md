# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-20 Daily Scan

### Stochastic-deterministic boundaries turn agent reliability into architecture
Summary: A production agent needs an explicit boundary where stochastic model proposals become deterministic system actions. The useful contract is proposer -> verifier -> commit -> reject signal.

Analysis: [reasoning analysis](2026-05-20/reasoning.md#stochastic-deterministic-boundaries-turn-agent-reliability-into-architecture)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents](https://arxiv.org/abs/2605.20173v1)
Implementable now:
- define every side-effecting action as propose -> verify -> commit -> reject;
- bind validators, tests, policy gates, and human approvals to commit paths;
- preserve reject signals in traces for replay and retry;
- choose orchestration patterns by task horizon and state persistence needs.
Tools, repos, and methodologies worth exploring:
- LangGraph, Google ADK, Temporal, Prefect, OpenTelemetry, Pydantic/JSON Schema, Open Policy Agent, state machines, saga compensation, `vasundras/agent-runtime-patterns`
Implementability score: 0.78

### Skills need admission control when tool feedback is already strong
Summary: A negative result on procedural skills argues that skills can become redundant overhead when tools already return strict, low-latency, schema-validated correction feedback.

Analysis: [reasoning analysis](2026-05-20/reasoning.md#skills-can-become-redundant-overhead-when-tools-give-high-bandwidth-feedback)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [When Skills Don't Help](https://arxiv.org/abs/2605.20023v1)
Implementable now:
- add skill load/no-load gates;
- A/B test skill value against no-skill and thinner-skill baselines;
- improve tool error messages and validators before adding more procedural text;
- quarantine skills that increase retries, context cost, or policy violations.
Tools, repos, and methodologies worth exploring:
- skill admission gates, skill A/B tests, schema-validated tool outputs, structured tool errors, OpenTelemetry traces, SkillOps-style contracts, semantic fuzzing
Implementability score: 0.86

### Code cleanliness changes agent cost even when pass rate stays flat
Summary: A controlled minimal-pair study reports that cleaner repositories did not change coding-agent pass rate, but did reduce token usage by 7-8% and file revisits by 34%.

Analysis: [reasoning analysis](2026-05-20/reasoning.md#code-cleanliness-changes-agent-cost-even-when-pass-rate-stays-flat)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [Does Code Cleanliness Affect Coding Agents?](https://arxiv.org/abs/2605.20049v1)
Implementable now:
- add static-analysis and cognitive-complexity metrics to coding-agent evals;
- track tokens, file revisits, tool calls, latency, and retries per task;
- build minimal-pair repository tests before claiming harness gains;
- prioritize refactors that reduce agent navigation waste.
Tools, repos, and methodologies worth exploring:
- SonarQube/SonarCloud, ESLint, Ruff, cognitive-complexity budgets, OpenTelemetry traces, file-revisit metrics, cost-per-task dashboards
Implementability score: 0.92

## Previous structured update

The prior daily scan for 2026-05-19 focused on full-system agent evals, executable environment supply, and persistent rubric memory: [2026-05-19 reasoning](2026-05-19/reasoning.md).
