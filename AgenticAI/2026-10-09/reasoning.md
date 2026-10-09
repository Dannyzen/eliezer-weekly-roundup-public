# Daily AgenticAI Analysis: 2026-10-09

## Thesis

The useful shift is from post-hoc agent review to pre-action and in-flight control: monitor trajectory structure, check required obligations, govern skill selection, and compile policy into deterministic tool gates.

All four papers were submitted on 2026-10-08 and first listed in the relevant arXiv categories on 2026-10-09.

## Intervene on trajectory structure before failure completes

OnTrack compares a live agent trajectory with recorded successful runs through streaming structure-aware optimal transport. It supports three evidence regimes: historical runs plus tool schemas, tool schemas only, and logs only. The available intervention degrades from plan-violation detection to generic loop, stall, and repeated-call detection as reference evidence disappears.

On SWE-bench trajectories, the first eight steps improved failing-versus-success ranking by 0.057 AUROC over content-similarity baselines. Its abort policy saved about 18% of compute on failing runs, and five of six interrupted runs were headed toward failure. The paper reports about one millisecond of monitoring overhead per step.

Why it matters: observability becomes operational only when it can interrupt a run before the expensive or irreversible effect. The strongest implementation pattern is a streaming trajectory monitor with explicit abstain, warn, and abort thresholds.

Stack fit: trajectory-aware evaluation, sessionful loops, runtime telemetry, and intervention policy.

Implementable now:
- normalize tool calls and dependency edges into a streaming event schema;
- compare partial runs with successful and failed reference traces;
- separate warn, pause, and abort policies;
- record every intervention with evidence and false-positive review;
- evaluate compute saved alongside task success and interruption precision.

Implementability score: 0.62

Core source: [OnTrack paper v1](https://arxiv.org/abs/2610.12375v1)

Artifact status: paper and full method were inspected. No public implementation artifact was linked from the paper. The abort result contains only six interventions, so the 83% precision estimate is preliminary.

## Detect required actions that never happened

ObligationGuard expands agent safety from forbidden actions to required safety-critical actions that remain unperformed. In its preliminary study, 56.92% of GLM-5.3 trajectories contained unfulfilled obligations, compared with 30.00% containing forbidden actions. ObligationBench contains 240 expert-validated trajectories across issue resolution, feature development, and terminal operations.

Across 14 representative models, the best obligation recall was 48.97% and exact match was 10.00%. A model trained on 40,000 synthetic examples reached 57.52% recall and 21.67% exact match. The public repository includes the benchmark, training and validation splits, prompts, checksums, evaluation code, and local tests.

Why it matters: a safe-looking sequence of actions can still end in an unsafe state because cleanup, verification, disclosure, rollback, or handoff never occurred. Completion contracts need positive obligations, not only denial rules.

Stack fit: harness acceptance criteria, terminal-state evaluation, recovery checks, and safety policy.

Implementable now:
- add explicit obligations to task contracts before execution;
- evaluate terminal state against required cleanup, verification, and handoff actions;
- preserve evidence for each obligation and unresolved item;
- score obligation recall and exact completion separately from task success;
- use post-run obligation checks before granting completion authority.

Implementability score: 0.78

Core sources: [ObligationGuard paper v1](https://arxiv.org/abs/2610.11773v1), [public repository](https://github.com/THU-Agent/ObligationGuard)

Artifact status: repository contents were inspected read-only. It has a populated main branch with benchmark data, training data, prompts, tests, and documentation. GitHub did not detect a repository license, so reuse terms need clarification.

## Guard the first skill read

One Skill Too Many studies conflicts between co-installed coding-agent skills. From 20,947 repository snapshots, the authors mined 822,109 candidate similar-skill pairs, judged 3,754, and executed 312 confirmed pairs across three models. The study covers 6,368 runs, 169,294 tool calls, and 542 agent-hours.

A similar skill displaced the installed skill in one in five runs without lowering task completion. When the similar skill was opened first, more than one third of the installed skill's exclusive core functions were lost. The final response named the selected skill in only 0.9% of substituted runs. A pre-tool hook at the first skill read restored fidelity to the level seen when the intended skill was opened first.

Why it matters: skill selection is an early control-plane decision. Task-passing benchmarks can hide loss of normative requirements such as a prohibition on touching Git. Skill catalogs need conflict detection, selection receipts, and first-read enforcement.

Stack fit: skills as control, capability discovery, coding-agent configuration, and harness evaluation.

Implementable now:
- detect semantically overlapping skills before installation;
- define exclusive core functions for normative skills;
- intercept the first skill read and route to the intended skill;
- log which skill was selected and why;
- test paired skill configurations, including installation-location changes.

Implementability score: 0.90

Core sources: [One Skill Too Many paper v1](https://arxiv.org/abs/2610.11647v1), [replication package](https://github.com/ltroin/conflict)

Artifact status: the public repository has a populated main branch, run-level data, analysis scripts, prompts, and a first-read guard example. GitHub did not detect a repository license, so copy or redistribution rights are unclear.

## Compile policy into schema-checked tool gates

NOMOS uses a four-pass compiler to turn written policy into deterministic tool-call rules. Static checks operate against tool schemas without an online LLM, prover, or solver. Those checks repaired or rejected 37% of airline candidates and 13% of retail candidates that would otherwise have produced unusable rules.

On tau2-bench, violations of reference-encoded clauses among state-changing calls fell from 66.3% to 2.6% in airline and from 30.8% to 6.9% in retail. AgentDojo attack success reached zero on banking and at most 3.6% on the other evaluated suites. Decisions run in microseconds, with domain-dependent benign-utility cost.

Why it matters: written policy should compile into an auditable action gate with schema checks, preflight replay, and explicit rejection. Per-action LLM judgment is slower, less deterministic, and harder to audit.

Stack fit: tool gateways, policy compilation, static verification, and runtime enforcement.

Implementable now:
- compile policy clauses into typed forbidden-action and precondition rules;
- verify every rule against tool names and available arguments;
- replay rules over known-good transcripts before activation;
- block state-changing calls deterministically and emit rule receipts;
- measure policy violations and benign utility together.

Implementability score: 0.58

Core sources: [NOMOS paper v1](https://arxiv.org/abs/2610.11030v1), [public artifact repository](https://github.com/iamupd/NOMOS), [Zenodo v1.0 record](https://zenodo.org/records/22123420)

Artifact status: rules, policies, reports, logs, result summaries, and analysis scripts are public under CC BY-NC 4.0. The compiler, behavioral preflight, runtime gate, predicate tables, and raw simulation transcripts are withheld, so the headline system cannot be reproduced from the public package alone.

## Practical priority

1. Add obligation checks and first-skill-read receipts immediately.
2. Prototype streaming warn and pause decisions against existing traces before enabling aborts.
3. Compile one narrow policy domain into typed tool rules and run replay preflight.
4. Keep all four mechanisms subordinate to human-reviewed thresholds and reversible rollout.
