# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-14 Daily Scan

The current implementation signal is explicit routing and derivation. Large catalogs need a selection stage outside task execution, and tool-call judges need a candidate-blind reference before scoring arguments.

### Preselect skills before task execution

Summary: With 1,000 irrelevant skills, loaded-skill recall falls from 73.6% to 27.4% and the zero-load rate rises from 9.3% to 51.6%. Explicit preselection from the same library retains 73.9% recall.

Analysis: [daily analysis](2026-10-14/reasoning.md#lost-in-implicit-routing-preselect-skills-before-task-execution)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.18522v1), [official repository](https://github.com/jinlinll/lost-in-implicit-routing)
Tools and methodologies worth exploring now: explicit top-k preselection, loaded-skill recall, zero-load rate, description ablations, catalog snapshot receipts, no-skill and golden-skill controls
Implementability score: 0.88

### Derive the expected argument before judging the candidate

Summary: Seven judges show a derivation gap when the source of a correct tool argument is missing. DeRef uses a separate candidate-blind derivation stage and raises controlled-test AUROC from chance or below to 98.40 through 99.59.

Analysis: [daily analysis](2026-10-14/reasoning.md#deref-derive-the-expected-argument-before-seeing-the-candidate)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.18497v1), [Apache-2.0 implementation](https://github.com/SarielMa/DeRef_release)
Tools and methodologies worth exploring now: candidate-blind derivation, source-span receipts, separate derivation and match scores, deterministic schema checks, high-impact human review
Implementability score: 0.81

## Current implication

Move selection and derivation out of the executor's hidden reasoning. Preserve each routing decision and reference as reviewable evidence.

Latest roundup: [2026-10-14 daily scan](../roundups/2026-10-14.md).
