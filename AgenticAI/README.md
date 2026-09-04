# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-04

### Passing functional tests is not enough for coding-agent acceptance

Summary: SWE-Gate adds an executable review-constraint oracle beside the functional suite. Across 303 instances from 75 Python repositories, 221 of 644 functionally successful repairs fail the constraint tests (34.3% hidden-failure rate). GPT-5.5 reaches 74.9% FSR and 52.8% JSR.

Analysis: [daily analysis](2026-09-04/reasoning.md#passing-functional-tests-is-not-enough-for-coding-agent-acceptance)
Core source: [paper](https://arxiv.org/abs/2609.04167v1)
Tools and methodologies worth exploring now: dual F/C oracles, non-compliant reference patches, FSR/CFR/JSR/HFR reporting, [DeepSoftwareAnalytics/SWE-Gate](https://github.com/DeepSoftwareAnalytics/SWE-Gate)
Implementability score: 0.74

### The serving interface can censor the trajectory before evaluation sees it

Summary: Changing only the serving adapter moves BFCL v4 from 0.00 to 0.96 / 0.19 for the same model. Qwen2.5-Coder 32B emits 80/100 well-formed calls while the server parses 0/100. GRPO can look healthy while multi-turn tool use never happens.

Analysis: [daily analysis](2026-09-04/reasoning.md#the-serving-interface-can-censor-the-trajectory-before-evaluation-sees-it)
Core source: [paper](https://arxiv.org/abs/2609.03966v1)
Tools and methodologies worth exploring now: raw-bytes vs parsed-call vs executor counters, template/parser 2x2, fail-closed empty `tool_calls`, [nebula-1999/Interface-Induced-Trajectory-Censoring](https://github.com/nebula-1999/Interface-Induced-Trajectory-Censoring)
Implementability score: 0.80

## Previous structured update: 2026-09-03

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

## Current implication

A green functional test and a parsed tool-call rate are both observations. Acceptance needs a second oracle. Measurement needs the raw completion, not only the adapter's empty array.
