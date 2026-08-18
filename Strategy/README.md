# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-18

### Delegation must narrow authority and close over prior actions

Summary: Static tool permissions do not prevent prohibited action sequences or over-broad subagent delegation. The Agentic Principal Chain narrows scope and budgets at each hop and checks new actions against accumulated session state.

Analysis: [daily strategy](2026-08-18/sovereignty.md#delegation-must-narrow-authority-and-close-over-prior-actions)
Core source: [Bounded Agents](https://arxiv.org/abs/2608.15888v1)
Tools and methodologies worth exploring now: signed authorization envelopes, scope attenuation, composition closure, exact-action approval tokens, fail-closed evidence sinks, utility-aware rollout tests
Implementability score: 0.76

## Current implication

Authority is a session object. Governed delegation requires an explicit chain, monotonic narrowing, history-aware admission, exact approvals, and evidence that enforcement did not destroy useful work.
