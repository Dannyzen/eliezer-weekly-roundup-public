# Daily AgenticAI Analysis: 2026-11-26

## Thesis

Agent systems improve fastest when production failures become replayable training and harness changes, while context itself becomes an explicit runtime interface with measured costs.

## Sports Agent turns production failures into bounded model and harness evolution

Sports Agent separates evolution into two coupled loops. A feedback engine verifies answers and trajectories, diagnoses recurring failures, synthesizes new questions from an error graph, and uses the resulting data for model training. The harness loop converts repeated production failures into prompt and skill changes, then requires independent audits, execution replay, regression testing, and performance-tolerance checks before adoption.

Across 30 reported harness-evolution rounds, the aggregate performance score rose 10.8 points. In the live product comparison, factual correctness rose 10.5 points, response richness rose 158.1%, and average latency fell 41.3% relative to the non-evolved version. The paper also reports a specialized Qwen3.6-35B-A3B SQL model with roughly three times the inference efficiency of the compared larger model.

Why it matters: this is a production-shaped pattern for continuous improvement. The useful unit is a diagnosed failure plus a replayable regression case, not a free-form prompt edit.

Stack fit: harness architecture, trajectory evaluation, model-data flywheels, and release governance.

Practical tools and methods worth exploring now:
- store failed trajectories with failure labels and source evidence;
- compile recurring failures into deterministic replay fixtures;
- version prompt, skill, model, and data changes separately;
- require independent replay and regression gates before promotion;
- use error graphs to generate diverse tests without copying the original failure.

Evidence and caveat: the paper reports production results from one Alibaba sports analytics system. No project-specific implementation repository was identified. The arXiv HTML links benchmark repositories, which are supporting evaluation infrastructure rather than the Sports Agent implementation.

Implementability score: 0.72

Core source: [Sports Agent v1](https://arxiv.org/abs/2611.33700v1)

## Model-managed context is becoming a measurable runtime API

The context-management paper gives models explicit operations to inspect, compact, and edit their own working context inside the open-source Mainplane harness. Across OfficeQA Pro v2, MLE-bench Lite, and DeepSWE, model-driven management often improved accuracy or reduced input tokens at tight budgets. The headline OfficeQA result moved GPT-6.1 from 21% to 56% at 32K context, while Kimi used up to 41% fewer input tokens. KV-cache editing reduced prefill compute by 4% to 15% per request in the reported setup.

Why it matters: context compaction can be treated as a tool-mediated state transition with telemetry, rather than a hidden summarization event chosen entirely by the harness.

Stack fit: context economy, agent harnesses, inference serving, and observability.

Practical tools and repositories worth exploring now:
- [Mainplane](https://github.com/mainplane-ai/mainplane), public MIT repository, contents inspected read-only;
- expose context inspection and compaction as typed runtime operations;
- log edit timing, retained spans, token deltas, cache reuse, and task outcome;
- keep a harness fallback because models varied widely in whether and when they compacted;
- evaluate context policy across several budgets rather than one long-context setting.

Evidence and caveat: OfficeQA Pro v2 has 90 questions and MLE-bench Lite has 22 competitions. The paper simulates pressure by shrinking context budgets, so it does not prove every long-horizon workload will behave the same way.

Implementability score: 0.76

Core source: [Letting Models Manage Their Own Context v1](https://arxiv.org/abs/2611.34147v1)
