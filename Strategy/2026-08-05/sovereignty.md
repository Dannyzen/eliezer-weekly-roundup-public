# Strategy Deep Dive - 2026-08-05

## Verdict

The strategic boundary is commit-time authority. Request-time approval is stale the moment shared policy state can change concurrently. Consequential agent actions need authorization, policy state, and the governed effect protected as one transaction.

## Deep Dive Wednesday: Stateful effect governance

[Stateful Governance for Concurrent Agentic Systems](https://arxiv.org/abs/2608.02764v1) is the week's strongest finding because it identifies the exact point where ordinary agent policy fails: shared state can change after an allow decision and before the effect commits.

The paper names this failure **stale authorization** and defines **policy-state serializability**. Every committed effect must be explainable as authorized against the policy state immediately before it occurs. Provenact implements that boundary with provider-certified state views, declared logical scopes, and scoped transactions, holds, or reservations.

The evidence is stronger than a conceptual architecture:

- In a 256-operation full-conflict budget workload, request-local Naive and Cedar baselines produced 30 to 31 stale allows and committed 79.4 to 80.8 transfers against a limit of 50. Provenact and other transactionally safe modes committed exactly 50 with zero stale allows across five seeds.
- In a 512-operation workload over 16 scopes, Provenact-Tx reached 86.4 operations per second at 10 ms service time, 1.64 times global locking and 0.93 times a hand-written transaction path.
- In delayed approval tests, scoped reservations preserved approval bases while unrelated scopes progressed. Revalidation prevented stale commits but could invalidate approval after the human had acted.
- In 256 scripted procurement workflows, Provenact committed 70.6 valid workflows on average with zero stale decisions. AGT and Omnigent produced 12.6 and 41.4 stale authorizations respectively under the paper's tested integrations.

The practical rule is direct: authorization, the mutable state that justifies it, and the governed effect need one protected commit path. For database-contained effects, build this now with PostgreSQL transactions, advisory locks, scoped reservations, typed effect intents, policy-as-code, and deterministic race fixtures. For external APIs, use durable intent identity, idempotency, outbox delivery, reconciliation, and quarantine, but do not claim the same guarantee until the provider path is recoverable.

The strongest objection is provider trust. Provenact cannot protect dependencies that a provider contract omits, and no public Provenact repository was exposed or verified. Production deployment, signed bundles, concrete framework adapters, and external-effect recovery remain unfinished.

Durable deep dive: [Stateful Effect Governance](../stateful-effect-governance/stateful-effect-governance.md)

Tools and methodologies worth exploring:
- PostgreSQL transaction-scoped advisory locks and serializable transactions;
- Cedar or Open Policy Agent for reviewable policy programs;
- Pydantic or JSON Schema for provider and effect contracts;
- Hypothesis state machines, deterministic barriers, and Jepsen-style histories;
- transactional outbox, idempotency keys, and reconciliation workers for external effects.

Implementability score: 0.67

Core source: https://arxiv.org/abs/2608.02764v1

## Current implication

Move authority as close to the effect as possible. The model can propose and a policy engine can explain, but only a commit-time control that owns the relevant state can safely grant the side effect.
