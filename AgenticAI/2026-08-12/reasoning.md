# AgenticAI Daily Analysis, 2026-08-12

The Wednesday arXiv batch is live. The selected papers were first listed on 2026-08-12. One Recipe, Many Harnesses was submitted on 2026-08-10; REDAgentBench was submitted on 2026-08-11. The Quadrat-IPI article and dataset update were published on 2026-08-12. Exact-title and source-ID checks found no prior coverage in this repository.

## Self-evolving harnesses should produce typed, transferable contracts

One Recipe, Many Harnesses holds one evolution recipe fixed across eight programming languages and three base models. Each edit starts from a typed failure signal and becomes a falsifiable contract rather than an unstructured reflection. The complete study reports 15,054 rollouts and 737,188 agent steps.

The result is not a universal self-improvement recipe. Held-out solve rates improved over a minimal seed and mini-SWE-agent in most cells, but Python was flat under every model and GPT-5-mini was flat across every language. The shared playbook transferred, while 20 to 40 percent of each harness remained ecosystem-specific. Non-compiling changes accounted for 70 percent of C++ rollout defects but under 10 percent of Go defects.

Why it matters: harness evolution is most useful as measured compensation for known execution defects. A global skill or prompt should carry only the verified common core; ecosystem-specific controls need native evaluation.

Practical tools and methodologies worth exploring now:
- classify failure signals before proposing harness edits;
- record each edit as a falsifiable contract with a held-out gate;
- separate portable control logic from language and repository adapters;
- keep null regions as evidence that no edit is needed;
- measure transfer before promoting evolved rules into a global harness.

Implementability score: 0.78

Core source: [One Recipe, Many Harnesses](https://arxiv.org/abs/2608.10178v1)

Evidence boundary: the paper reports code availability but the inspected primary text did not expose a resolvable exact repository URL. The method is compute-heavy and still needs replication outside Multi-SWE-Bench.

## Agent red teaming should separate exposure, execution, observation, and adjudication

REDAgentBench contains 1,661 executable cases across 15 intervention strategies, 11 vulnerability types, 28 constraints, and five service surfaces. It evaluates six models under three agent harnesses. The central measurement is not one attack-success rate: the harness and evidence view can change the reported outcome even when the underlying model or rollout is fixed.

The paper verifies harmful effects from service receipts and final-state changes. Its macro-average attack-success rate is 65.69 percent. In a state-grounded cohort, almost one in five confirmed violations with resolved action anchors occurred after the agent had stated the relevant constraint. A training-free reminder at the action boundary reduced confirmed violations by more than 70 percentage points in matched replay.

Why it matters: a safe-sounding trajectory is not proof of a safe effect. Red-team systems need separate receipts for whether hostile content reached the agent, what action executed, what state changed, and how the result was judged.

Practical tools and methodologies worth exploring now:
- derive attacks from explicit constraints and mapped vulnerabilities;
- run side effects against isolated service doubles;
- grade service receipts and final-state diffs instead of agent prose;
- disclose harness identity and evidence view with every safety score;
- replay recognition-execution failures with a deterministic pre-action reminder.

Implementability score: 0.72

Core source: [REDAgentBench](https://arxiv.org/abs/2608.10669v1)

Evidence boundary: the paper is authored partly by the evaluated vendor team, and no exact public implementation artifact was verified in this scan. The reported reminder effect is a matched benchmark result, not a deployment guarantee.

## Prompt-injection detectors need attack-family maps at fixed false-positive budgets

Quadrat-IPI publishes 16,800 unique indirect injections and 63,000 clean documents across email, web, and document carriers. Its 92 populated attack cells cross ten delivery levers with ten attacker objectives. It measures nine detectors at fixed 0.1 percent and 1 percent false-positive operating points.

The actionable result is that a detector does not have one recall. Across measured systems, the gap between the weakest and strongest attack cells spans 4 to 76 percentage points. The public harness fixes threshold selection, detector input, and measurement protocol so adapters are compared on the same corpus and operating point.

Why it matters: a headline recall number hides the exact attacks and carriers a deployed agent will miss. Detector admission should be tied to the traffic mix, attack family, and acceptable false-alarm budget.

Practical tools and repositories worth exploring now:
- [Quadrat-IPI dataset](https://huggingface.co/datasets/mihailgribov/quadrat-ipi), 79,800 rows, version 1.0.1;
- [quadrat-ipi-eval](https://github.com/mihail-gribov/quadrat-ipi-eval), inspected read-only, Apache-2.0, populated main branch;
- per-carrier false-positive budgets;
- attack-cell coverage thresholds;
- pinned dataset revisions and saved detector score receipts.

Implementability score: 0.95

Core source: [How to compare indirect prompt injection detectors](https://huggingface.co/blog/mihailgribov/compare-prompt-injection-detectors)

Evidence boundary: this is a new community-authored dataset and harness with no independent replication. The corpus mixes public-record and ODC-BY sources under a dataset-level `other` license tag, so downstream use needs a source-license review. This cron inspected metadata, documentation, and repository contents only; it did not run the harness.

## Working conclusion

Evolve harnesses from typed failures, grade safety from realized state, and evaluate prompt-injection detectors by attack family at a fixed false-positive budget.
