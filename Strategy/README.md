# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-01

### Treat the user invocation as part of the repository-poisoning threat model

Summary: CIPR evaluates 1,920 poisoned-repository instances across 20 repositories. Task type creates up to a 4.5-fold attack-success difference, and test execution is a silent high-risk surface because agents treat injected infrastructure as something to run rather than audit.

Analysis: [daily strategy](2026-09-01/sovereignty.md#treat-the-user-invocation-as-part-of-the-repository-poisoning-threat-model)
Core sources: [paper](https://arxiv.org/abs/2608.30686v1), [repository](https://github.com/StarConnor/CIPR)
Tools and methodologies worth exploring now: task-risk classification, test and build preflight, effect prevention separate from alerting, invocation provenance, repository provenance, skill and permission traces
Implementability score: 0.84

### Make continuity durable without making it ambient authority

Summary: Hermes Agent v0.21.0 makes recurring memory, notepads, bot handoffs, delegation control, and instruction protection durable. The governance requirement is to label carried state by provenance, age, scope, and binding force before it can affect a later run.

Analysis: [daily strategy](2026-09-01/sovereignty.md#make-continuity-durable-without-making-it-ambient-authority)
Core source: [release](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31)
Tools and methodologies worth exploring now: explicit continuity contracts, bounded recurring state, protected instruction writes, state provenance and expiry, inspectable steer and stop events
Implementability score: 0.95

## Current implication

Continuity and user invocation are authority surfaces. Persistent state and trusted intent may inform an agent, but exact execution rights still belong to external policy, preflight, and effect gates.
