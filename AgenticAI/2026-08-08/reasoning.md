# AgenticAI Daily Analysis, 2026-08-08

No new arXiv listing appears on Saturday. These findings are from the Friday, 2026-08-07 listing batch, with v1 submissions dated 2026-08-06.

## Harness evolution needs held-out evaluation and causal failure localization

HarnessOpt-Bench turns harness optimization into a controlled capability test. An optimizer edits prompts, tools, control flow, memory, and orchestration code under a fixed evaluation budget. Final candidates are scored on an inaccessible held-out partition inside isolated sandboxes. The benchmark covers five frontier optimizer models, four downstream tasks, and 111 scored runs.

TRAJDEBUG complements that protocol by locating the earliest failure-responsible step rather than grading only the final answer. TRAJERRBENCH contains 486 manually annotated failed trajectories from tau2-Bench and SWE-Bench Pro. Its trigger, state, and causal-attribution stages distinguish repaired errors from harmless errors and terminally consequential errors.

Why it matters: self-improving agents need two separate proofs. A harness candidate must generalize on held-out work, and failed runs need evidence-grounded causal diagnosis so the next edit targets the real defect.

Fit in the stack: harness evaluation, trajectory observability, regression control, and self-improvement governance.

Practical tools and methods:
- immutable Git commits for every candidate;
- hidden test partitions and fixed token or evaluation budgets;
- isolated sandboxes with request, tool, state, and cost receipts;
- causal labels for trigger, resolution state, and terminal impact;
- replay fixtures that compare final outcome and earliest decisive error.

Artifact status: no exact public HarnessOpt-Bench repository was verified. The TrajDebug repository resolves, but its README says source code and data are pending internal approval, so it is a preview rather than a runnable release.

Implementability score: 0.62

Core sources:
- https://arxiv.org/abs/2608.06301v1
- https://arxiv.org/abs/2608.06346v1
- https://github.com/THU-KEG/TrajDebug

## Global skill evolution needs relation graphs and replay gates

Learning Globally Reusable Skills for Coding Agents treats a skill bank as an interconnected system rather than a pile of local patches. GSE records dependency, co-usage, and conflict relations, clusters related proposals into reusable abstractions, and replays historical cases before promotion. It evaluates 108 real bugs from nine open-source projects and 500 industrial reports from eight production repositories, using OpenHands and mini-SWE-agent. An internal deployment reports a 61.4 percent F1 improvement.

Why it matters: local skill edits can fix one trace while breaking another skill or overfitting to one repository. The actionable pattern is graph-aware admission plus held-out replay, not blind self-rewrite.

Fit in the stack: skill lifecycle, coding-agent control plane, memory-to-procedure promotion, and regression testing.

Practical tools and methods:
- explicit dependency, co-usage, and conflict edges;
- typed skill-change proposals with rationale and expected effect;
- project-held-out evaluation;
- historical replay before merge;
- append or patch with provenance instead of whole-bank rewrites.

Artifact status: no GSE implementation repository was verified from the primary paper.

Implementability score: 0.64

Core source: https://arxiv.org/abs/2608.06153v1

## Working conclusion

A self-improving agent should not edit its harness or skill bank directly from one successful trace. Candidate changes need immutable identity, held-out evaluation, causal failure evidence, relation-aware impact analysis, and replay before promotion.
