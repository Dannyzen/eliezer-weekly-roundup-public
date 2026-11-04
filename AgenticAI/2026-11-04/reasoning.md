# AgenticAI Daily Analysis: 2026-11-04

## Scope

The Wednesday, November 4 arXiv listing is live. The selected papers were submitted November 2 or 3 and first listed November 4. Public project and repository pages were inspected read-only. No external source code was cloned, installed, built, imported, or executed. Blogwatcher was unavailable, so direct arXiv category pages and the Hugging Face feed supplied the primary discovery surfaces.

## 1. Audit the evaluation instrument beside every agent score

Silent Instrument Errors Reorder Agent Leaderboards re-derived two public evaluation pipelines from released artifacts. The audit found four plausible-looking failures: HAL counted nested model-call spans twice in 70 of 134 runs, graded only about half of one scaffold's episodes, mixed grader replay actions into 68% of 2,334 airline records, and produced version-sensitive re-grades that moved some scores by as much as 82 points.

Why it matters: a reproducible pipeline can reproduce a bad measurement. Agent results need provenance for the evaluator, task data, grading trigger, cost aggregation, and action authorship. A final score cannot expose a missing grade, duplicated trace span, contaminated trajectory, or replay against the wrong environment.

The practical pattern is small and immediate:
- report graded, ungraded, failed, and dropped episode counts separately;
- aggregate usage from root spans or deduplicate by response identity;
- tag every action with agent, user, simulator, grader, or recovery provenance;
- pin evaluator code and task-data versions in every result;
- publish per-task re-grade diffs and fail on excessive replay mismatches;
- ship machine-readable errata with frozen trace archives.

The paper's public repository contains disclosures and reproduction bundles and was inspected read-only. The evidence covers two leaderboards, so the general prevalence claim remains unmeasured.

Implementability score: 0.91

Sources:
- [Silent Instrument Errors Reorder Agent Leaderboards](https://arxiv.org/abs/2611.04399v1)
- [read-only reproduction repository](https://github.com/YangzeLiu/eval-instrument-disclosure)

## 2. Reuse evolution guidance, then discard task-local harness edits

Meta2 learns a textual Meta-Skill from contrasted training runs, then freezes that guidance for deployment. During a held-out run, a separate evolver decides whether to keep the harness or apply a bounded task-local edit to prompts, instructions, hooks, tools, memory, or checks. Every edit expires with the run, while the reusable guidance survives.

Why it matters: persistent self-modification can spread one task's workaround into unrelated work. Meta2 separates two kinds of state: cross-task guidance about when to intervene, and task-local changes motivated by one active trajectory. Its ablation supports the boundary. Carrying edits across tasks reduced Terminal-Bench performance from 81.00% to 78.33% and DeepSWE from 44.44% to 39.11%.

The practical pattern is:
- learn or hand-author act, avoid, and hold rules from contrasted trajectories;
- expose bounded checkpoints with explicit keep or evolve decisions;
- constrain edits to typed channels such as notice, instruction, read-only hook, or tool;
- preserve the active environment and partial trajectory across an edit;
- reset the harness at the next task while retaining only reviewed guidance;
- compare against a fixed seed harness and charge checkpoint cost explicitly.

Meta2 reports 81.00% on Terminal-Bench 2.1 and 44.44% on DeepSWE 1.1 with GPT-5.6-Terra, gains of 14.67 and 9.77 points over the shared seed. The study uses separate learned Meta-Skills per backbone, and the project page marks code as coming soon. This is an architecture pattern with paper evidence, not a ready implementation.

Implementability score: 0.67

Sources:
- [Meta2 paper](https://arxiv.org/abs/2611.05139v1)
- [project page](https://meta-square.github.io/)

## Working conclusion

Evaluation instruments and adaptive harnesses both need state boundaries. Scores require versioned measurement provenance, while harness evolution should retain reviewed cross-task guidance and discard run-specific edits.
