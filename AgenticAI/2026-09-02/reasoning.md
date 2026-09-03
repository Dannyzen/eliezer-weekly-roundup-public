# AgenticAI Daily Reasoning - 2026-09-02

## Scope note

Deep Dive Wednesday. The winning finding is a Strategy control-plane change: loaded skills need a task-conditioned runtime guard. This file records the implementation slice only. Primary analysis lives in Strategy.

The selected paper was submitted 2026-09-01T16:19:31Z and first listed on 2026-09-02. Immutable v1 PDF text was inspected. No public SkillSonar repository resolved. No external source code was cloned or executed.

## Implement the guard as a first-class skill, then keep the broker

Skill-augmented agents load reusable packages into persistent runtime context. That is already how Hermes, Claude Code, and OpenClaw add procedure. The new failure is delayed: a skill looks fine at install, then a later user task makes an unsafe action look in-scope.

The implementable pattern is small.

1. Ship a dedicated guard skill, not a longer system prompt.
2. Give it an explicit consult-before-action instruction. Safety skills are not discovered the way capability skills are.
3. Classify proposed effects as allow, replan, or confirm against a typed user-task boundary.
4. Leave permission systems and sandboxes as hard denial.

On Claude Code / GLM-5, that pattern beat a safety system prompt (ID ASR 0.414 to 0.104) and preserved more utility than AcceptEdits (0.779 versus 0.650). Flattening the same policy into a prompt is a weaker control. Unsupervised MCTS over attack rollouts is research, not the first product loop.

Why it belongs here: AgenticAI already treats skills as versioned packages. The missing runtime object is the consult record: skill id, proposed effect, task id, decision, and broker override.

Implementability score: 0.58 for a Hermes guard skill plus fixtures. 0.35 if the goal is paper-faithful MCTS evolution.

Durable deep dive:
- [Defense as Skill](../../Strategy/defense-as-skill/defense-as-skill.md)

Core source:
- [Defense-as-Skill](https://arxiv.org/abs/2609.01487v1)
