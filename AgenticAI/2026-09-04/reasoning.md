# AgenticAI Weekly Analysis - 2026-09-04

## Thesis

The implementation unit is a measurement-and-acceptance pair: raw evidence the serving stack cannot delete, plus a second oracle that functional success cannot satisfy by itself.

## Acceptance needs dual oracles, not a single resolve rate

### Finding

SWE-Gate splits repository-level repair into two executable oracles: a functional test for the reported issue, and a constraint test derived from real pull-request review comments. Each of 303 instances, spanning 75 Python repositories, also ships a non-compliant patch that passes F and fails C, plus a gold patch that passes both. Under Mini-SWE-Agent, four backends produced 644 functionally successful repairs. 221 of those, 34.3%, failed the constraint suite. GPT-5.5 reached 74.9% functional success and only 52.8% joint success. Providing the constraint text raised joint success (GPT-5.5 +11.5 points) and constraint-following among functional repairs, while functional success itself did not improve.

LoopArena makes the same split at the loop layer. It fixes the coding Worker and evaluates a separate runtime Controller through typed Loop Contracts. Its 90-question cheap setting, 27 condensed tasks, and 27 full tasks expose a major gap: the best full-task Strict Success Rate is 24.69%, while condensed evaluation reduces estimated inference cost by 64.4% and preserves controller ordering.

EarlyEval then treats the rest of an already-decided eval run as optional spend. Cheap success and failure predictors over trajectory prefixes stop a run when either crosses a calibrated threshold. Across SWE-bench Verified, TerminalBench, and Toolathlon it reports 13% to 26% fewer steps and up to 44.1% fewer input tokens, with about 1 to 2 point resolve-rate movement.

### Why it matters

SWE-bench-style gates still answer "did the issue test go green." Production merge answers "would a reviewer accept this." Hidden failures are the gap between those questions. A controller score is likewise not a worker score, and a finished trajectory is not always worth finishing.

### Stack fit

This belongs in trajectory-aware evaluation and the coding-agent control plane. Pair EarlyEval with SWE-Gate: early stop can save eval budget; the dual oracle decides whether a green functional trajectory was even the right acceptance object.

### Practical path now

- Keep separate F and C oracles, plus a non-compliant reference that proves they are not the same test.
- Report FSR, CFR, JSR, and hidden-failure rate instead of a single resolve rate.
- Feed review constraints as first-class task input, then still hide the constraint tests.
- Evaluate runtime controllers separately from fixed workers on cheap fixtures and full-task anchors.
- Halt eval once a calibrated prefix predictor already knows the ending.
- Start with the released 303-instance SWE-Gate package rather than synthesizing a private dual-oracle set.

Implementability score: 0.74

The public SWE-Gate repository is populated: 303 instances, 99 Docker contexts, encoded model predictions, and a documented 48-instance gap in optional `validation_matrix.json` files. Running it needs Docker, Git, Node, and model credentials. This synthesis inspected metadata only. LoopArena is Apache-2.0 with a populated default branch. EarlyEval is MIT.

Core sources:
- [SWE-Gate](https://arxiv.org/abs/2609.04167v1)
- [SWE-Gate repository](https://github.com/DeepSoftwareAnalytics/SWE-Gate)
- [LoopArena](https://arxiv.org/abs/2608.27487v1)
- [LoopArena repository](https://github.com/AMAP-ML/LoopArena)
- [EarlyEval](https://arxiv.org/abs/2609.02783v1)
- [EarlyEval repository](https://github.com/inphotoo/earlyeval)

## The serving interface is part of the measurement instrument

### Finding

Interface-Induced Trajectory Censoring shows that a tool-call rate read off the serving stack can be zero while the model is emitting well-formed calls. On BFCL v4, holding weights, cases, executor, scorer, decoding, and seeds fixed, changing only the serving adapter moves the same model from 0.00 to 0.96 / 0.19 on simple_python / multi_turn_base. A 2x2 over chat template and parser puts both main effects at zero. The whole effect sits in their interaction. Qwen2.5-Coder 32B emits 80/100 well-formed calls while the server parses 0/100.

The RL contamination is the strategic half. In the author's GRPO/RLOO runs, pass@1 rose 2.6 to 2.8 points, but 91 to 94% of newly passing items passed on turn 1, and items rescued on turn 2 or later stayed flat at 6 to 9 of 540. A later 10-step GRPO run under function calling executed zero tool calls while `critic/rewards/mean` climbed from 0.233 to 0.281.

BTS-AgentBench supplies the complementary compiler: checksummed source records, a read-only tool store, typed multi-turn tasks, tool-derived gold evidence, an exclusion controller, and two-build replay proof. The 532-row release reproduced its 356/87/89 split exactly across independent builds. Hermes v0.21 made continuity and orchestration inspectable runtime surfaces rather than ambient chat state.

### Why it matters

Eval dashboards and RL critics will both look healthy while the branch being measured does not exist. EarlyEval assumes the trajectory is the agent's. This paper says the interface may have deleted the tool-using part first.

### Stack fit

Agent serving runtime first, RL training governance second, trajectory-aware evaluation third. Treat template, parser, tool schema, and token constraints as part of the measurement instrument, not as invisible plumbing.

### Practical path now

- Log raw model bytes, parser output, and executor admissions as three separate counters.
- Run a 2x2 over template and parser before publishing a tool-call score.
- Fail closed when HTTP 200 returns empty `tool_calls` but the completion contains a well-formed call.
- Compile operational records into deterministic, replayable evaluation episodes before model judging.
- Keep ERRATA.md in the loop; the IITC repo documents seven arms with wrong provenance and five inadmissible for pass-rate comparison.
- Treat continuity contracts as explicit, inspectable state with provenance and expiry.

Implementability score: 0.80

The IITC repository is populated with probes, analysis scripts, RESULTS.md, and pre-registrations. BTS-AgentBench is populated. Hermes v2026.8.31 is a tagged official release. This synthesis inspected metadata only.

Core sources:
- [Interface-Induced Trajectory Censoring](https://arxiv.org/abs/2609.03966v1)
- [IITC repository](https://github.com/nebula-1999/Interface-Induced-Trajectory-Censoring)
- [BTS-AgentBench](https://arxiv.org/abs/2608.27334v1)
- [BTS-AgentBench repository](https://github.com/kjy7567/BTS-AgentBench)
- [Hermes Agent v2026.8.31](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31)

## Audit skills as frozen policies, then keep the broker

### Finding

SkillShift formalizes Skill Policy Integrity: the policy induced by a skill must stay aligned with its declared functionality and the user-authorized objective. The attack is not prompt injection and not task hijacking. It is a semantically plausible skill that preserves the interface while steering the decision. Measured on two fixed-candidate domains, with 50 queries each and three runs per query, shopping PSR rose from 37.33% to 81.33% at 100% valid-output rate, and Python dependency PSR rose to 63.33% at 100% valid-output rate. Direct-Skill Injection reaches near-100% PSR but is the noisy control. SkillShift is the stealth path. Static scanners that catch direct injection do not distinguish Attack skills from paired Clean skills.

Defense-as-Skill is the complementary control. SkillSonar is an installable Markdown guard that sits beside untrusted task skills, checks proposed actions against the current user task, and returns allow, replan, or confirmation. On Claude Code with GLM-5, N = 10, it cuts in-distribution attack success from 0.482 to 0.104 and out-of-distribution attack success from 0.606 to 0.115, while keeping more utility than Claude Code's AcceptEdits permission preset. Adding an allowlist to AcceptEdits collapses protection. The guard is still instruction-following.

SafeEvolve turns on-policy traces into bounded prompt and SkillBank edits, then uses harness-use SFT plus GRPO. On Qwen3.5-4B, AgentDojo ASR falls from 2.37% to 0.79% while clean utility rises from 59.79% to 61.86%. Take the reversible admission loop, not unsupervised live-attack evolution.

### Why it matters

A skill can keep the original task, keep a valid answer, and still change what the agent prefers. Install-time vetting remains necessary. It is no longer sufficient. After a skill is in runtime context, a later user task can make leaking, approval bypass, or data staging look useful.

### Stack fit

This belongs in skills-as-control and the coding-agent control plane, with Strategy owning the delayed-authority and hook-admission layers. The implementable object is a paired selection fixture plus a consult-before-action guard, not a scanner score.

### Practical path now

- Audit skills with paired clean/attack selection fixtures, PSR, and valid-output metrics.
- Keep direct-injection positive controls so scanners are not credited for catching only the noisy attack.
- Treat loaded skills as delayed-authority objects with a task-conditioned consult-before-action guard.
- Keep hard brokers for host effects; Markdown guards cannot intercept a session-start shell.
- If evolving the harness from trajectories, require named components, paired safety and utility gates, and JSONL evolution logs.

Implementability score: 0.72

SkillShift has no public implementation repository in the daily notes. Defense-as-Skill is a design-plus-eval reference; the reusable object is the guard contract, not a drop-in product. SafeEvolve is populated on GitHub as a research loop, not a production admission system.

Core sources:
- [SkillShift](https://arxiv.org/abs/2609.02564v1)
- [Defense-as-Skill](https://arxiv.org/abs/2609.01487v1)
- [SafeEvolve](https://arxiv.org/abs/2609.02786v1)
- [SafeEvolve repository](https://github.com/MaoPopovich/SafeEvolve)

## Working conclusion

The agentic stack should treat functional tests, parsed tool-call rates, declared skill interfaces, and serving adapters as observations. Acceptance, measurement, and skill admission need independent oracles, raw evidence, and frozen-policy fixtures. Each transformation needs an explicit input identity, output identity, evaluator, uncertainty record, and rollback path.
