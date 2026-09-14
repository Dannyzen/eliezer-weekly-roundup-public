# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the daily analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-14

### Build recovery tests around corrupted intermediate state

Summary: ParaRecover supplies 10,626 parallel tool-use fault cases across 14 error types and separates structural integrity, diagnosis, and repair strategy from terminal success. Models exceeded 89 percent Pass@1 while still scoring below 70 on the process rubric.

Analysis: [daily analysis](2026-09-14/reasoning.md#build-recovery-tests-around-corrupted-intermediate-state)
Core sources: [ParaRecover paper](https://arxiv.org/abs/2609.12345v1), [repository](https://github.com/gbw206/ParaRecover)
Tools and methodologies worth exploring now: controlled DAG fault injection, dependency-cone scoring, deterministic structural checks, repair-delta evidence, invalid-DAG rate, loop caps, replayable pre-fault and post-repair state
Implementability score: 0.82

### Optimize repository skills at one frozen base, then distrust small gains

Summary: Skill Issue mines tasks by reverse-applying merged pull requests at one frozen repository commit and compares candidate SKILLs against a no-skill seed. GEPA gained 4.9 points on average, but the authors could not separate that lift from run variance on 20 to 26-task holdouts.

Analysis: [daily analysis](2026-09-14/reasoning.md#optimize-repository-skills-at-one-frozen-base-then-distrust-small-gains)
Core source: [Skill Issue paper](https://arxiv.org/abs/2609.12742v1)
Tools and methodologies worth exploring now: frozen target SHAs, reverse-applied pull-request tasks, isolated test specifications, paired rollouts, GEPA, SkillOpt, variance reporting, maintainer review
Implementability score: 0.66

## Current implication

Put process evidence ahead of terminal success. Recovery benchmarks should expose where a parallel plan broke and how it changed; skill optimization should prove that the guidance belongs to one repository snapshot and clears a paired baseline.
