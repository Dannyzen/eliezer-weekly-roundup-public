# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-21 Daily Scan

### Treat persistent state as delayed execution authority

Summary: Memory files and scheduled wake-ups can replay a one-time injection after the attacker and user are gone; govern every persistent write as a future authority request.

Analysis: [treat persistent state as delayed execution authority](2026-10-21/sovereignty.md#treat-persistent-state-as-delayed-execution-authority)

Core sources: [carryover attacks paper v1](https://arxiv.org/abs/2610.28425v1), [CarryoverBench repository](https://github.com/igloomatics/CarryoverBench)

Implementable now:
- quarantine untrusted instructions before persistence;
- label writes with origin, principal, scope, and authority;
- test planting and triggering separately across clean sessions;
- reauthorize scheduled wake-ups and memory resurfacing.

Implementability score: 0.78

### Monitor policy across executions, not only actions

Summary: Individually permitted calls can combine into a forbidden purpose, consent, provenance, or delegation outcome; some policies require cross-execution comparison.

Analysis: [monitor policy across executions, not only actions](2026-10-21/sovereignty.md#monitor-policy-across-executions-not-only-actions)

Core sources: [Local Allow, Global Deny paper v1](https://arxiv.org/abs/2610.27620v1), [empty advertised repository](https://github.com/anmolpandey299/al-synth)

Implementable now:
- bind workflows to declared purpose and principal;
- retain policy projections of prior executions;
- generate relational witnesses with formal or property-based methods;
- state the accepted false-alarm trade explicitly.

Artifact caveat: the named repository has no default branch or populated tree.

Implementability score: 0.56

## Current implication

Authority must remain coherent across time and across executions. Per-call approval cannot govern delayed triggers or relational policy by itself.
