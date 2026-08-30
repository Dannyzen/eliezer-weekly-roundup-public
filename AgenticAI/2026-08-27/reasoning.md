# AgenticAI Daily Analysis - 2026-08-27

## Scope note

The August 27 arXiv listing was live at the 12:00 UTC scan. ProgRouter and CaSKG were first listed on Thursday, August 27 and their immutable v1 submissions were posted on August 26, inside the strict trailing 48-hour window. Exact IDs and titles were checked against the existing repository and were not previously covered.

Hugging Face Daily Papers and its blog feed, GitHub Trending, GitHub's August 26 changelog, and current web search were also scanned. `blogwatcher-cli` was unavailable, so direct feeds and primary pages were used. External repositories were inspected read-only through GitHub metadata, trees, and raw README files. No external source code was cloned, installed, built, imported, or executed. NotebookLM remained disabled and untouched.

## Route models from measured progress, not only the initial query

ProgRouter replaces one-shot model selection with step-level routing inside an evolving multi-agent workflow. A coordinator maintains a structured workflow-state ledger. A multi-view scorer tracks outcome regime, subtask completion, progress trend, and state quality. A dual-path predictor estimates the marginal progress gain of each candidate model, and a meta-gate balances that estimate against deadline, energy, and long-run cost constraints.

The evaluation covers HumanEval Plus, MBPP, MATH-500, and ASQA. On HumanEval Plus, ProgRouter reports a 93.0 percent pass rate inside a 4,800 J budget, 2.1 points above MasRouter and 8.2 points above CASCADIA. On MBPP it reports the best pass rate at 79.4 percent, the lowest energy at 3,376 J, and the shortest execution time at 10.3 seconds. The paper also shows why greedy progress-per-cost routing fails: cheap models can stall, forcing repeated recovery calls.

Why it matters: model routing becomes useful only when it observes the trajectory. The initial prompt cannot reveal whether a cheap model made progress, whether the task entered a harder phase, or whether the remaining budget justifies escalation.

Practical tools and methodologies worth exploring:
- maintain a typed workflow ledger with completed subtasks, unresolved blockers, state quality, elapsed time, and cumulative cost;
- log marginal progress after each agent step rather than only final success;
- start with deterministic escalation rules based on stalls, regressions, and remaining budget;
- shadow a learned progress predictor before allowing it to choose models online;
- evaluate quality, latency, energy, and recovery calls together.

Artifact status: no public implementation repository was linked from the immutable abstract, HTML, or exact-title search. The paper was accepted to EMNLP 2026 Findings, but the reported gains cover four benchmark families and do not yet establish generalization to browser, infrastructure, or external-tool workflows.

Implementability score: 0.61

Core source:
- [ProgRouter paper](https://arxiv.org/abs/2608.25992v1)

## Calibrate skill dependencies before graph retrieval

CaSKG treats a skill graph as an executable dependency surface rather than a collection of semantic associations. It first builds a high-recall directed candidate graph from lexical, semantic, input/output, and structural evidence. It then removes, substitutes, and reorders skill pairs in textual counterfactual probes, aggregates the results with Bayesian smoothing, and publishes confirmed, uncertain, rejected, and bounded unvalidated edges at different weights.

The graph is frozen before evaluation and the downstream agent policy is unchanged. Across six model backbones on ALFWorld ID-140 and ScienceWorld U211, CaSKG reports the highest task score in all 12 model-benchmark combinations. Relative to Graph-of-Skills, the six-model macro-average ScienceWorld score rises from 72.62 to 80.50 and ALFWorld success rises from 80.01 percent to 86.79 percent. Mean environment steps fall from 16.39 to 15.29 on ScienceWorld and from 15.96 to 14.05 on ALFWorld.

Why it matters: a retrieved skill can be textually relevant but operationally wrong. Skill routing should preserve prerequisites, state-changing actions, verification routines, and completion steps, which requires evidence about directed relations rather than embedding proximity alone.

Practical tools and methodologies worth exploring:
- represent skill prerequisites, produced state, consumed state, recovery paths, and completion checks as directed edges;
- generate candidate edges broadly, then admit them through counterfactual or trace-backed tests;
- preserve confirmed, uncertain, and rejected edge states rather than collapsing every relation to present or absent;
- freeze one graph version for each evaluation run and retain the evidence that promoted every edge;
- compare task success and environment steps against vector-only and uncalibrated graph baselines.

Artifact status: the paper links `ZhiyuanLi218/Caskg`. The public repository resolves, but its tree contains only `README.md`, whose complete content says the code will be released within a few days. Treat this as a paper-backed method with a placeholder artifact, not implementation-ready source.

Implementability score: 0.58

Core sources:
- [CaSKG paper](https://arxiv.org/abs/2608.25500v1)
- [CaSKG placeholder repository](https://github.com/ZhiyuanLi218/Caskg)
