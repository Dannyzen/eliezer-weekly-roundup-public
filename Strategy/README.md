# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-19

### Authorize memory before it enters context

Summary: Relevance is not permission. A single anti-monotone audience-membership rule at the memory-to-context boundary keeps facts inside the audience that produced them and fails closed on ambiguous channels.

Analysis: [daily strategy](2026-08-19/sovereignty.md#authorize-memory-before-it-enters-context)
Core source: [Authorization Before Context](https://arxiv.org/abs/2608.17148v1)
Tools and methodologies worth exploring now: recorded-audience stamps, channel-metadata viewer sets, public fail-closed fallback, exact-context admission receipts
Implementability score: 0.78

### Self-improvement needs order and variance controls

Summary: Memory-based self-improving agents increased run-to-run variance in 71% of cases. The default easy-to-hard order produced a 1.5% gain; shuffled orders produced a 4.5% loss.

Analysis: [daily strategy](2026-08-19/sovereignty.md#self-improvement-needs-order-and-variance-controls)
Core sources: [On the Fragility of Self-Improving Agents](https://arxiv.org/abs/2608.18066v1), [replication repository](https://github.com/SalesforceAIResearch/self-improve-fragility)
Tools and methodologies worth exploring now: multi-run promotion gates, shuffled-order eval, environment-aware memory construction, human correction of wrong lessons
Implementability score: 0.84

## Current implication

Context assembly and self-improvement are authority operations. Admit memory by audience, not relevance. Promote learned artifacts only after multi-run and shuffled-order evidence.
