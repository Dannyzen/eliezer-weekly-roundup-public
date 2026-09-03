# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-03

### Halt evaluation once the trajectory already predicts the outcome

Summary: EarlyEval trains cheap success and failure predictors over trajectory prefixes and stops a run when either crosses a calibrated threshold. Across SWE-bench Verified, TerminalBench, and Toolathlon it reports 13% to 26% fewer steps and up to 44.1% fewer input tokens, with about 1 to 2 point resolve-rate movement.

Analysis: [daily analysis](2026-09-03/reasoning.md#halt-evaluation-once-the-trajectory-already-predicts-the-outcome)
Core source: [paper](https://arxiv.org/abs/2609.02783v1)
Tools and methodologies worth exploring now: prefix-feature logs, leave-one-agent-out LightGBM predictors, thresholded early stop for eval only, delta Pass@1 reporting, [inphotoo/earlyeval](https://github.com/inphotoo/earlyeval)
Implementability score: 0.70

### Evolve the harness from trajectories, then train the policy to use it

Summary: SafeEvolve turns on-policy traces into bounded prompt and SkillBank edits, then uses harness-use SFT plus GRPO. On Qwen3.5-4B, AgentDojo ASR falls from 2.37% to 0.79% while clean utility rises from 59.79% to 61.86%. Take the reversible admission loop, not unsupervised live-attack evolution.

Analysis: [daily analysis](2026-09-03/reasoning.md#evolve-the-harness-from-trajectories-then-train-the-policy-to-use-it)
Core source: [paper](https://arxiv.org/abs/2609.02786v1)
Tools and methodologies worth exploring now: named harness components, paired safety and utility gates, JSONL evolution logs, [MaoPopovich/SafeEvolve](https://github.com/MaoPopovich/SafeEvolve)
Implementability score: 0.50

### Audit skills as frozen behavioral policies, not just packages

Summary: SkillShift keeps the declared task and a valid output interface while steering shopping and dependency choices. PSR rises to 81.33% and 63.33% at 100% valid-output rate. Scanners that catch direct injection miss the stealth pair.

Analysis: [daily analysis](2026-09-03/reasoning.md#audit-skills-as-frozen-behavioral-policies-not-just-packages)
Strategy analysis: [daily strategy](../Strategy/2026-09-03/sovereignty.md#treat-reusable-skills-as-covert-policy-objects)
Core source: [paper](https://arxiv.org/abs/2609.02564v1)
Tools and methodologies worth exploring now: paired clean/attack fixtures, PSR and valid-output metrics, direct-injection positive controls, scanner-plus-behavior release gates
Implementability score: 0.72

## Previous structured update: 2026-09-02

### Implement the guard as a first-class skill, then keep the broker

Summary: Skill-augmented agents need a dedicated runtime guard skill with an explicit consult-before-action instruction. Flattening the same policy into a system prompt is weaker. The first Hermes slice is a small action schema plus delayed-harm fixtures, not paper-faithful MCTS.

Analysis: [daily analysis](2026-09-02/reasoning.md#implement-the-guard-as-a-first-class-skill-then-keep-the-broker)
Deep dive: [Defense as Skill](../Strategy/defense-as-skill/defense-as-skill.md)
Core source: [paper](https://arxiv.org/abs/2609.01487v1)
Tools and methodologies worth exploring now: dedicated guard skill, consult-before-action instruction, allow/replan/confirm records, delayed-harm fixtures, permission and sandbox brokers
Implementability score: 0.58

## Current implication

A skill is a policy object, a harness is an auditable artifact, and an eval run is a budgeted trajectory. Scanner verdicts, full-task spend, and ungoverned harness rewrites are not proof.
