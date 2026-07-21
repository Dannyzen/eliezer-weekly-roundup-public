# AgenticAI Daily Analysis - 2026-07-18

## Daily thesis

The strongest implementation signal is not a new planner. It is an execution substrate that makes agent actions safe to inspect.

Two papers first listed by arXiv on Friday, July 17 make that concrete. Copy-on-Write Scoring isolates database writes inside the real application shape and grades the resulting state. Tactile turns desktop interaction into semantic targets, executable affordances, provenance, and post-action verification. Both move reliability out of prompt prose and into runtime objects.

## Copy-on-Write scoring brings evaluation into the application data plane

[Copy-on-Write Scoring](https://arxiv.org/abs/2607.14336v1) evaluates an agent against representative workflows without giving it direct write access to base PostgreSQL data. Each original table becomes a base table, a per-session changes table, and a view. Session and operation IDs bind writes to an isolated branch of database state. A human ground-truth session and an agent session can then be compared at the row, field, session, and operation level.

This is more useful than a generic benchmark when the question is whether an agent can operate one real application safely. The Plane study used 20 workflows and five models. Two initial trials per model and workflow produced 200 sessions, and a third run after tool-surface changes brought the total to 300. The scoring exposed vocabulary mismatch, unsupported argument guesses, and extra writes. It also gave the authors a direct way to measure whether tool-surface fixes improved the affected models.

Why it matters:

- replica benchmarks drift away from the deployed application;
- final-answer grading misses extra, missing, or malformed writes;
- copy-on-write isolation preserves realistic reads while containing mutations;
- operation-level utility shows which tool call moved state toward or away from the target.

Practical tools and methods:

- [trail-ml/agent-cow-python](https://github.com/trail-ml/agent-cow-python)
- PostgreSQL views, triggers, session IDs, operation IDs, and per-session changes tables
- human-recorded ground-truth workflows
- structural and content comparators over final state
- selective commit or discard after review

Artifact readiness: the repository is public, populated, MIT-licensed, and has five tags through `v0.1.7`. It has no GitHub release object, and the default branch was last pushed on April 30, 2026. The paper reports about 250 lines for Plane's core copy-on-write integration plus about 540 lines for recording infrastructure.

Weakest point: this is a preliminary study on one PostgreSQL application and 20 workflows. Rewriting table topology through views and triggers is invasive. Start with a disposable mirror or staging database, not production.

Implementability score: 0.82

## Tactile turns GUI actions into semantic, verifiable objects

[Tactile](https://arxiv.org/abs/2607.14443v1) rejects screenshot-first control as the only desktop interface. It ranks evidence from operating-system accessibility semantics, OCR-grounded text, and visual fallback regions, then exposes compact target candidates with roles, text, state, geometry, supported actions, source labels, and verification cues.

The useful abstraction is an observe-ground-act-verify loop:

1. observe structured and visual evidence;
2. ground intent to a named target candidate;
3. prefer a native semantic action when one exists;
4. fall back to OCR-backed coordinates or vision only when needed;
5. re-observe and verify the expected state transition;
6. preserve the full observation and action provenance for replay.

On macOSWorld-style tasks, Tactile increased Codex Success@100 from 41.1 percent to 50.0 percent overall and from 45.2 percent to 55.3 percent on accessibility-adapted tasks. A 96-task subset showed gains across Codex, Claude Code, OpenCode, and Goose.

Practical tools and methods:

- [yliust/Tactile](https://github.com/yliust/Tactile)
- macOS Accessibility API and analogous Windows UI Automation or WAI-ARIA surfaces
- OCR text boxes as source-labeled fallback evidence
- semantic actions such as press, set value, focus, and select
- verification contracts over state, value, focus, dialog, and list changes
- trace records for source evidence, chosen target, action primitive, and outcome

Artifact readiness: the repository is public and populated with 145 tree entries. It has no tags or releases, is strongest on macOS, and uses the PolyForm Noncommercial 1.0.0 license. That makes it suitable for research and personal evaluation, not an automatic commercial dependency.

Weakest point: accessibility metadata can be missing, stale, or wrong, and visual fallback reintroduces coordinate ambiguity. The guardrail is to record why the semantic path was rejected and require explicit post-action evidence.

Implementability score: 0.74

## Stack implication

| Boundary | Runtime object | Required proof |
| --- | --- | --- |
| Application writes | isolated state branch | final state diff, operation lineage, commit or discard decision |
| Desktop action | semantic target plus executable affordance | source evidence, action primitive, post-action verification |

The implication is direct: evaluate and execute against runtime-owned state, not narrative claims about what the agent thinks it changed.
