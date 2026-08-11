# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-11

### Contract-equivalent histories should produce contract-equivalent code

Summary: SpecPath holds the repository, final contract, verifier, agent configuration, and budget fixed while varying only requirement history. Thirty-five of 100 complete passing blocks failed on at least one equivalent history.

Analysis: [daily analysis](2026-08-11/reasoning.md#contract-equivalent-specification-histories-expose-path-dependence-in-coding-agents)
Core source: [SpecPath](https://arxiv.org/abs/2608.09799v1)
Tools and methodologies worth exploring now: paired specification histories, executable outcome pairs, failing-history minimization, specification-path release gates
Implementability score: 0.91

### Context repair should start with source-level trajectory attribution

Summary: TRACE attributes dissatisfaction traces to prompts, knowledge, tools, or skills before choosing CREATE versus UPDATE. On 60 traces it reports 72.7 percent root-cause attribution, 82 percent fix effectiveness, and 96 percent operation accuracy.

Analysis: [daily analysis](2026-08-11/reasoning.md#context-maintenance-should-attribute-failures-before-rewriting-context)
Core source: [TRACE](https://arxiv.org/abs/2608.09153v1)
Tools and methodologies worth exploring now: source-identified traces, read-only source inspection, bounded patches, replay, rollback receipts
Implementability score: 0.74

### Deterministic stages should own code-review coverage and admission

Summary: OpenCodeReview uses deterministic dispatch, a curated tool loop, and independent falsification. On 200 pull requests and 1,505 expert-verified comments, it reports up to 2.17 times higher SEM-F1 with 5 to 15 times fewer tokens.

Analysis: [daily analysis](2026-08-11/reasoning.md#deterministic-code-review-stages-beat-general-agent-freedom-on-precision-and-cost)
Core sources: [paper](https://arxiv.org/abs/2608.09290v1), [GitHub repository](https://github.com/alibaba/open-code-review)
Tools and repositories worth exploring now: `alibaba/open-code-review`, deterministic file and rule dispatch, isolated review bundles, asymmetric reflection
Implementability score: 0.96

## Current implication

Equivalent contracts should yield equivalent code, context edits should follow attribution, and deterministic stages should own review coverage and comment admission.
