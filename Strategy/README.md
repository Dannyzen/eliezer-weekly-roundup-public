# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-12

### Shared memory is an authority graph, not a semantic cache

Summary: MAP-Graph filters memory by inherited permissions before semantic ranking, propagates trust and revocation through ancestry, then applies an action-risk gate. It blocked every observed unauthorized read and all 450 revoked cases in its synthetic benchmark, but still allowed 41 unsafe action-risk decisions.

Analysis: [daily analysis](2026-08-12/sovereignty.md#shared-memory-needs-provenance-aware-admissibility-before-retrieval-and-action)
Core source: [MAP-Graph](https://arxiv.org/abs/2608.10509v1)
Tools and methodologies worth exploring now: typed provenance graphs, inherited scopes, hard eligibility filters, graded trust ranking, revocation propagation, action-specific gates
Implementability score: 0.74

## Current implication

Persistent memory must carry inherited authority and revocation before retrieval, while side effects still require a separate execution gate.
