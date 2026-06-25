# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-25

### ToolBench-X turns tool-use eval into recovery testing

Summary: ToolBench-X injects recoverable hazards into multi-step tool tasks: specification drift, invocation error, execution failure, output drift, and cross-source conflict. The useful metric is no longer function-call accuracy alone. It is whether the agent diagnoses the hazard and recovers.

Analysis: [daily reasoning analysis](2026-06-25/reasoning.md#toolbench-x-turns-tool-use-eval-into-recovery-testing)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [ToolBench-X paper](https://arxiv.org/abs/2606.25819v1)
Implementation artifact: [Foreverskyou/ToolBench-X](https://github.com/Foreverskyou/ToolBench-X)
Implementable now:
- create deterministic tool doubles for high-value internal workflows
- inject specification drift, invocation errors, execution failures, output drift, and cross-source conflict
- score diagnosis, retry, fallback, verification, and cross-checking separately from final answers
Tools, repos, and methodologies worth exploring:
- ToolBench-X design, pytest fixtures, OpenTelemetry recovery spans, golden answers, targeted recovery-hint ablations
Implementability score: 0.68

### Constraint Tax shows tool calling and JSON Schema can interfere

Summary: Constraint Tax reports Tool Suppression when open-weight models run tool calling and JSON Schema constrained decoding together. The mitigation is Transparent Two-Pass Execution: let the agent use tools first, then serialize the verified result under a strict schema.

Analysis: [daily reasoning analysis](2026-06-25/reasoning.md#constraint-tax-shows-tool-calling-and-json-schema-can-interfere)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Context Economy](context-economy/context-economy.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [Constraint Tax](https://arxiv.org/abs/2606.25605v1)
Implementable now:
- add joint tests for tool calling plus structured output, not only separate tests
- split action selection from schema serialization when tools disappear under constraints
- log allowed tools, schema mode, serving backend, selected tool path, and final serializer mode
Tools, repos, and methodologies worth exploring:
- two-pass execution scaffolds, structured-output regression fixtures, serving-backend comparison matrices, decoder-mode telemetry
Implementability score: 0.78

### DESIGN.md makes agent UI context a validated artifact

Summary: DESIGN.md defines a small, lintable format for giving coding agents persistent visual-identity context: YAML design tokens plus Markdown rationale. The broader lesson is that agent context files should be versioned, validated, and diffed like code.

Analysis: [daily reasoning analysis](2026-06-25/reasoning.md#designmd-makes-agent-ui-context-a-validated-artifact)
Durable topics: [Context Economy](context-economy/context-economy.md), [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [google-labs-code/design.md](https://github.com/google-labs-code/design.md)
Package metadata: [@google/design.md](https://registry.npmjs.org/%40google%2Fdesign.md)
Implementable now:
- add `DESIGN.md` to UI-heavy repos
- require agents to read it before UI edits
- lint and diff design-token changes in CI
Tools, repos, and methodologies worth exploring:
- `@google/design.md`, design-token CI, context-file linting, context diff review, agent-readable contracts for security and runbooks
Implementability score: 0.92
