# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-13

### Tool architecture is part of the agent policy surface

Summary: Six equivalent-capability tool architectures, three actors, and 11,700 coding trajectories changed repeat-run consistency, repository exploration, steps, and tokens. CodeAct-style interfaces reached similar performance with 41.6 percent fewer steps and 56.3 percent fewer tokens.

Analysis: [daily analysis](2026-08-13/reasoning.md#tool-architecture-is-part-of-the-agent-policy-surface)
Core source: [The Devil Is in the Interface](https://arxiv.org/abs/2608.11386v1)
Tools and methodologies worth exploring now: interface schema identity, equivalent-capability A/B tests, repeated-run variance, relevant-file coverage, step and token ledgers
Implementability score: 0.72

### Memory systems need a serving-cost break-even test

Summary: Three memory systems, two baselines, two backbones, conversations up to 400 turns, and 665 LoCoMo questions show that internal memory pipelines make simple cost estimates miss by 18 to 69 percent. Some systems never beat full-transcript cost within 400 turns.

Analysis: [daily analysis](2026-08-13/reasoning.md#memory-systems-need-a-serving-cost-break-even-test)
Core source: [Total Recall at What Cost?](https://arxiv.org/abs/2608.11879v1)
Tools and methodologies worth exploring now: per-stage model-call ledgers, matched cost-accuracy curves, rolling-window baseline, full-transcript baseline, break-even by session depth
Implementability score: 0.82

### Adversarial tool environments should be executable and stateful

Summary: ToolHazard generates stateful environments, attack points, payloads, and long-horizon tasks with deterministic checks. Its benchmark spans 28 domains and exposes richer task and tool graphs than fixed prompt-injection suites.

Analysis: [daily analysis](2026-08-13/reasoning.md#adversarial-tool-environments-should-be-executable-and-stateful)
Core sources: [paper](https://arxiv.org/abs/2608.11878v1), [public MIT repository](https://github.com/MurrayTom/ToolHazard)
Tools and repositories worth exploring now: ToolHazard environment/task schemas, isolated service doubles, final-state diffs, attack-placement coverage, trajectory receipts
Implementability score: 0.78

### Agent Plugins 1.0 is ready for a bounded portability pilot

Summary: GitHub now supports one package containing portable skills and MCP configuration across VS Code, Copilot CLI, the Copilot SDK, and the Copilot app, while client-specific features remain namespaced.

Analysis: [daily analysis](2026-08-13/reasoning.md#portable-agent-plugins-make-packaging-easy-enough-to-standardize-now)
Core sources: [GitHub release](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/), [1.0.0 specification](https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md)
Tools and repositories worth exploring now: `agent-plugins-spec`, manifest JSON schema, MCP component schema, CI linting, one read-only cross-client pilot
Implementability score: 0.96

## Current implication

Package capabilities once, but evaluate each interface, memory pipeline, environment, and client admission separately.
