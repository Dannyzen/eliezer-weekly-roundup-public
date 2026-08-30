# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-30

### Verify harness changes on behavior-relevant evidence

Summary: HarnessLens derives a candidate-specific verification set from trajectories, affected components, intended behavior, and regression risk. Across three harnesses and four benchmarks, it reports 7.6 to 13.6 percent average held-out improvement with less evaluation budget than fixed-set baselines.

Analysis: [daily analysis](2026-08-30/reasoning.md#verify-harness-changes-on-behavior-relevant-evidence)
Core sources: [paper](https://arxiv.org/abs/2608.27311v1), [repository](https://github.com/jhxu5214/HarnessLens)
Tools and methodologies worth exploring now: machine-readable change manifests, trajectory-derived impact sets, paired verification, attributable-evidence gates, bounded evaluation budgets, regression-risk task selection
Implementability score: 0.78

### Treat permission checks as resource-identity checks

Summary: Claude Code v2.1.251 closes symlink-swap, path-traversal, pre-permission-read, browser-permission, sandbox-output, and security-sensitive configuration gaps. It also adds model-switch hooks and prompt-cache telemetry, making check-and-use identity and runtime changes observable.

Analysis: [daily analysis](2026-08-30/reasoning.md#treat-permission-checks-as-resource-identity-checks)
Core source: [Claude Code v2.1.251](https://github.com/anthropics/claude-code/releases/tag/v2.1.251)
Tools and methodologies worth exploring now: check-and-use identity fixtures, model-switch hooks, managed-setting approval gates, prompt-cache telemetry, symlink and path-traversal regression tests, unified browser and file approval planes
Implementability score: 0.97

## Current implication

Harness change is an authority event, not a text edit. The runtime should name the modified component, derive the behaviors it can affect, run paired evidence, and reject unproven changes. Permission decisions must bind to the resource, model, route, and configuration actually used, not merely the name or state observed before execution.
