# AgenticAI Daily Analysis - 2026-08-03

## Scope

Monday produced a real arXiv announcement batch. The strongest new implementation signal is that coding-agent reliability needs evidence-bearing control surfaces before edits, during repair, and at validation. All selected papers were first listed on Monday, 2026-08-03; their immutable v1 pages show submissions on 2026-07-30 or 2026-07-31.

The papers and public artifacts were inspected read-only. No external repository was cloned, installed, built, imported, or executed.

## Evidence-conditioned execution should gate code mutation

ECLoop interposes between a coding agent and the repository. It compiles observable evidence conditions from the issue and repository structure, tracks satisfaction from structured trajectory events, and postpones edits or patch submission while action-specific evidence gaps remain. On all 500 SWE-bench Verified instances across two models and two scaffolds, the paper reports Pass@1 gains of 4.8 to 11.8 percentage points and token reductions of up to 12.1 percent.

Why it matters: a plausible edit is not justified merely because the agent inspected the target function. Callers, tests, related implementations, and behavioral constraints may invalidate the proposal. The execution layer separates proposing a mutation from being allowed to commit it.

Stack fit: coding-agent control plane, repository exploration, deterministic action gates, and context policy.

Implementable now:
- compile issue-specific evidence requirements before the first write;
- represent repository observations as typed events;
- compute global and action-specific evidence gaps;
- postpone writes and submissions until deterministic conditions pass;
- log the condition set, observed evidence, postponed action, and eventual release decision.

Tools and methodologies worth exploring:
- ECLoop-style evidence specifications;
- AST and call-graph inspection;
- test discovery and reproduction checks;
- deterministic policy middleware around file writes and patch submission.

Implementability score: **0.78**

Caveat: the paper exposes no dedicated public implementation artifact on its primary pages, and condition compilation still uses a model. The execution check is deterministic only after the specification exists.

Core source:
- https://arxiv.org/abs/2607.28815v1

## Responsibility graphs make repair bounded and auditable

AuditCoder treats code and its construction trace as joint outputs. A contract-annotated task graph gives stable responsibility identities to commitments, owned code, provenance, validation evidence, and repair history. When validation fails, a conservative locator selects a node or dependency branch, or abstains, then regenerates only the supported region while freezing the complement.

On APPS, the paper reports 82.5 to 83.0 percent pass@1, still 7.5 to 8.5 points below AgentCoder. On ClassEval it reports 75.0 to 82.0 percent. A separate 200-record audit reaches 0.9725 decision-code trace coverage, but localizes only 26 of 60 failures; 17 of those bounded repairs pass.

Why it matters: repair authority should be narrower than repository authority. Stable responsibility IDs give the runtime a concrete unit for evidence, intervention, abstention, and replay.

Stack fit: coding-agent control plane, task decomposition, event-sourced repair, and auditability.

Implementable now:
- assign stable IDs before code generation;
- bind each ID to contract, owned files or symbols, dependencies, provenance, and checks;
- freeze unaffected code during repair;
- record cross-node exceptions explicitly;
- abstain when evidence does not justify a repair boundary.

Tools and methodologies worth exploring:
- AuditCoder's MIT-licensed public repository;
- contract-annotated task graphs;
- responsibility-to-code maps;
- containerized evaluation with network denial and read-only mounts.

Implementability score: **0.72**

Caveat: the public repository is populated with 282 files and documents a hardened evaluation container, but this cron did not execute it. The paper evaluates algorithmic and class-level tasks, not repository-scale audit chains, and usable localization is much weaker than trace retention.

Core sources:
- https://arxiv.org/abs/2607.29529v1
- https://github.com/puppet0x3f/AuditCoder

## Passing tests need bug-discrimination evidence

BSG-VA captures each validation command at its exact working-tree state, isolates the test-only patch, and replays it on the buggy base, the candidate state, and the developer gold fix. The replay assigns an evidence role to each event instead of treating every green test as proof of the repair.

Across 3,730 events from 643 rollouts on 110 tasks, 46.0 percent of positive comparable events carried no bug-discriminating information. In baseline runs, 23.8 percent closed with no positive evidence that distinguished the bug. Bug-contrast feedback reduced inadequate closure by 7.8 percentage points versus an attention-matched reminder and raised bug-discriminating evidence by 7.4 points, with no detectable repair-success cost. Both effects were below the prespecified 10-point practical threshold.

Why it matters: a passing regression suite can certify that the candidate did not break something while saying nothing about the assigned defect. Evaluation needs to classify what each check proves.

Stack fit: trajectory-aware evaluation, coding-agent release gates, exact-state evidence, and oracle quality.

Implementable now:
- capture validation commands with code-state hashes;
- isolate agent-added tests from production edits;
- replay checks on buggy, candidate, and gold states;
- classify evidence as bug-discriminating, candidate-specific, regression-only, misleading, unstable, or unevaluable;
- block closure when the positive evidence base never distinguishes the bug.

Tools and methodologies worth exploring:
- BSG-VA replay methodology;
- the open Zenodo JSONL dataset;
- disposable worktrees or containers;
- exact-state test receipts and evidence-role dashboards.

Implementability score: **0.86**

Caveat: the feedback effect is statistically detectable but smaller than the authors' practical threshold, and the extra value of bug-replay content did not reproduce consistently across exploratory model and scaffold variants. The open dataset resolves, but this cron did not download or execute it.

Core sources:
- https://arxiv.org/abs/2607.28871v1
- https://doi.org/10.5281/zenodo.21642576

## Working conclusion

A coding-agent control plane should compile evidence requirements before mutation, preserve responsibility through construction and repair, and certify what each validation event actually proves. Green output without provenance, scope, and contrast is not release evidence.
