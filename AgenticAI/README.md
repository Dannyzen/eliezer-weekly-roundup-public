# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-10

### Detect specification gaps before a coding agent invents the method

Summary: IdeaAMBIG's 660 evidence-grounded cases separate readiness assessment, defect localization, and clarification. Across 13 models, the best real-world defect recovery rate was 9.6%, while clarification success reached 80.6% once the defect was identified.

Analysis: [daily analysis](2026-09-10/reasoning.md#detect-specification-gaps-before-a-coding-agent-invents-the-method)
Core sources: [paper](https://arxiv.org/abs/2609.10539v1), [Yiling-Ma/IdeaAMBIG](https://github.com/Yiling-Ma/IdeaAMBIG)
Tools and methodologies worth exploring now: codification-readiness gates, typed blocker taxonomies, evidence-seeking clarification actions, unsupported-assumption rejection, separate localization and clarification metrics
Implementability score: 0.84

### Preserve memory, but make influence query-conditioned

Summary: RD-Forget keeps a retained source archive while building a query-specific answer view. On fact consolidation, it beat the stronger baseline by 11 to 26 points across four model backbones; removing forgetting or query conditioning caused the largest matched deficits.

Analysis: [daily analysis](2026-09-10/reasoning.md#preserve-memory-but-make-influence-query-conditioned)
Core source: [What Should an Agent Forget?](https://arxiv.org/abs/2609.10263v1)
Tools and methodologies worth exploring now: immutable source archives, semantic relation slots, supersession links, historical-intent rescue, budgeted answer-time evidence views, selected-memory receipts
Implementability score: 0.68

### Remediation agents should start from owned findings and land through review

Summary: GitHub Code Quality can assign up to 25 findings to Copilot, which repairs them on a branch, validates the changes, and opens a pull request. Existing enterprise Code Quality policy governs access; AI credits and independent acceptance remain real costs.

Analysis: [daily analysis](2026-09-10/reasoning.md#remediation-agents-should-start-from-owned-findings-and-land-through-review)
Core source: [GitHub changelog](https://github.blog/changelog/2026-09-09-remediate-code-quality-findings-with-agentic-autofix/)
Tools and methodologies worth exploring now: bounded finding batches, branch isolation, independent test ownership, review-constraint gates, acceptance and credit-cost telemetry
Implementability score: 0.92

## Current implication

The next useful control surface is preflight-to-acceptance continuity. Localize missing decisions before coding, limit memory influence at answer time without destroying history, and let remediation agents land only through isolated branches and independently owned acceptance.
