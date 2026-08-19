# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-19

### Harness safety is a lifecycle, not a model score

Summary: A 128-case sandbox study of OpenClaw, Hermes, and Nanobot shows high task utility can coexist with 12.6% to 80.9% attack success. Configuration is the weakest phase, and detecting risk does not stop the action.

Analysis: [daily analysis](2026-08-19/reasoning.md#harness-safety-is-a-lifecycle-not-a-model-score)
Core sources: [HarnessRisk](https://arxiv.org/abs/2608.17597v1), [project page](https://baiyajing.github.io/harness-risk/), [implementation repository](https://github.com/Baiyajing/HarnessRisk)
Tools and methodologies worth exploring now: phase-scored harness fixtures, config-mutation cases, persistence and detection metrics, same-model cross-harness comparison
Implementability score: 0.86

### Skill code needs checked lowering before dispatch

Summary: Models turn skills into programs that request eager full-input access. SkillEffect rebuilds a bounded lowering from the program and immutable input before granting execution.

Analysis: [daily analysis](2026-08-19/reasoning.md#skill-code-needs-checked-lowering-before-dispatch)
Core source: [SkillEffect](https://arxiv.org/abs/2608.17007v1)
Tools and methodologies worth exploring now: source recognizers, bounded tool implementations, independent lowering checkers, fresh-cgroup replay, result-schema isolation
Implementability score: 0.62

## Current implication

Treat harnesses and generated skill programs as execution substrates. Score them by phase and physical resource shape, not by whether the task finished.
