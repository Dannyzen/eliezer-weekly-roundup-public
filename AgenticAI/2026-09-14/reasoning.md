# AgenticAI Daily Analysis: 2026-09-14

## Freshness and selection

A real Monday arXiv listing batch appeared on September 14. The four selected v1 papers were submitted on September 10 or 11 and first listed on Monday, so they are fresh listing-window findings after the weekend, not strict trailing-48-hour submissions at scan time. The arXiv API returned HTTP 429; category pages, immutable v1 pages, arXiv HTML, and downloaded PDF text supplied the primary evidence.

Hugging Face, GitHub Trending, official release feeds, and web news were scanned as supporting surfaces. Hugging Face had no newer relevant primary post, and GitHub Trending was used only as a demand signal. Public repositories were inspected through GitHub metadata, trees, README files, and licenses. Nothing from an external repository was cloned, installed, built, imported, or executed.

Duplicate checks against the existing Markdown corpus found no prior coverage of the four selected IDs or exact titles.

## Build recovery tests around corrupted intermediate state

### Finding

ParaRecover evaluates whether a parallel tool-use agent can localize an intermediate failure, understand its downstream impact, and produce a minimal corrective plan. Its 10,626 instances cover 14 error types across two levels: recent-step failures and multi-turn propagated failures. The SDE rubric separates structural integrity, diagnostic reasoning, and evolutionary strategy instead of collapsing the run into final success.

More than ten models were evaluated. The paper reports average SDE scores below 70; Claude Opus 4.6 scored 69.23 on Level 1 and 66.85 on Level 2. The sharper result is the disagreement between completion and recovery quality: Pass@1 exceeded 89 percent across models even while evolutionary-strategy scores remained the weakest dimension. A Qwen3-8B model trained with SDE-derived preferences improved average scores by 5.24 points on Level 1 and 4.71 on Level 2. Judge-free measures also moved: Level 2 invalid-DAG rate fell from 13.22 to 9.08 and Pass@1 rose from 91.37 to 93.97.

### Why it matters

Final success can hide redundant calls, lucky recovery, state drift, or a plan that would fail under the next fault. Parallel execution makes this worse because a local error can corrupt several dependent branches before the terminal verifier sees anything.

### Stack fit

This belongs in trajectory-aware evaluation and multi-agent orchestration. A parallel workflow trace should expose the corrupted node, dependency cone, diagnosis, repair delta, rounds consumed, and terminal result as separate evidence.

### Practical path now

- Add controlled tool errors to DAG and fanout test fixtures.
- Score localization, dependency impact, minimal repair, goal preservation, invalid-DAG rate, rounds, and terminal success separately.
- Keep deterministic structural checks outside the model judge.
- Compare single-step and propagated faults.
- Preserve the pre-fault plan, tool receipts, repair plan, and resulting state in one replayable record.
- Cap loops explicitly and classify cap exhaustion rather than silently timing out.

Implementability score: 0.82

Artifact status: `gbw206/ParaRecover` is a populated public repository with an MIT license, four JSONL datasets, the agent environment, concurrent DAG executor, evaluation scripts, and analysis utilities. It has no release and no pull-request history. Reproduction needs model API credentials. The benchmark uses simulated tools, an LLM judge for abstract rubric dimensions, and DAG workflows that omit richer loops, conditionals, and asynchronous interactions. The artifact was inspected read-only and not executed.

Core sources:
- [ParaRecover paper](https://arxiv.org/abs/2609.12345v1)
- [ParaRecover repository](https://github.com/gbw206/ParaRecover)

## Optimize repository skills at one frozen base, then distrust small gains

### Finding

Skill Issue builds repository-specific coding tasks from merged pull requests. Each change is reverse-applied at one frozen base commit, then admitted only when the reverted repository produces a test failure that isolates the original change. The same coding agent is compared with and without each candidate SKILL.

Across Kotest, Ktor, and Koog, GEPA-generated documents raised the paired score by 4.9 percentage points on average; SkillOpt produced only a 0.1-point gain. The authors explicitly do not treat that as statistical proof. After mining and validation, held-out splits contained only 20 to 26 tasks, no optimizer cleared a 0.05 sign-test threshold, and one rollout cost $0.84 on average. A single Koog maintainer preferred the GEPA document as a mergeable draft, and two open-issue exercises finished faster and more cheaply with either generated SKILL, but that review is too small to establish general transfer.

The strongest finding is methodological: using historical parent commits caused generated documentation to mix incompatible repository eras. Replaying all tasks at one frozen base made the resulting SKILL version-specific and reviewable.

### Why it matters

A synthesized skill can sound authoritative while describing paths, APIs, or build commands that never coexisted. Repository guidance needs the same source binding as code: one target snapshot, tests that define the task, a no-skill control, and human review before merge.

### Stack fit

This belongs in skills-as-control and the coding-agent control plane. Skill optimization is a repository evaluation problem, not a prose-generation problem.

### Practical path now

- Mine merged pull requests only when the change can be reverse-applied at one frozen target commit.
- Admit a task only when tests isolate the reverted behavior.
- Compare candidate SKILLs against the same seed on paired rollouts.
- Record target SHA, task split, model, harness, tools, budget, result, and run variance.
- Treat small pass-rate gains as inconclusive when they fit inside baseline variance.
- Require maintainer review before merging generated guidance.

Implementability score: 0.66

Artifact status: the paper provides the mining procedure, generated SKILLs, prompts, cost data, and case material in its appendices, but no paper-specific public replication repository was linked from the immutable v1 surfaces. The method also requires enough stable pull-request history to leave at least 100 graded tasks before a three-way split; two candidate repositories failed that gate.

Core source:
- [Skill Issue paper](https://arxiv.org/abs/2609.12742v1)

## Working conclusion

Evaluate what happens between plan and completion. Parallel agents need fault-localization and repair evidence, while repository skills need snapshot-bound tasks, paired controls, and statistical humility. Both patterns are implementable now, but neither lets the agent grade itself into trust.
