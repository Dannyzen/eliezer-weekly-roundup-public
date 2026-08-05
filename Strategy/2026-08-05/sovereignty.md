# Strategy Daily Sovereignty - 2026-08-05

## Verdict

The strategic boundary is commit-time authority. Request-time approval is stale the moment shared policy state can change concurrently. Consequential agent actions need authorization, policy state, and the governed effect protected as one transaction.

## Stateful Governance moves policy enforcement to the commit boundary

Stateful Governance identifies stale authorization as the core failure mode in concurrent agent systems. Its policy-state serializability condition requires committed effects to be explainable as authorized against the policy state immediately before they occur. The Provenact prototype keeps reviewable policy programs while coordinating the policy state and effects needed to preserve each decision.

The paper's PostgreSQL benchmark makes the failure concrete. In a full-conflict budget workload, request-local Naive and Cedar baselines produce 30 to 31 stale allows and commit 79.4 to 80.8 transfers even though the budget permits only 50. Global serialization, manual transactions, and both Provenact modes commit exactly 50 with zero stale allows. In a separate 512-operation workload over 16 scopes, Provenact-Tx reaches 86.4 operations per second at 10 ms service time versus 52.7 for a global lock, averaged over five seeds.

Why it matters: identity, tool allowlists, and policy checks do not remain valid indefinitely. Budgets, inventory, approvals, and risk state can change between decision and effect. Governance that ends at an allow decision leaves the race inside the trusted path.

Implementable now:
- declare the policy-state scopes read and written by each governed effect;
- bind authorization and effect execution in one database transaction where possible;
- reserve policy state for delayed human approvals;
- revalidate stale decisions before commit;
- record policy version, state snapshot, principal, effect ID, and commit receipt;
- test conflicting operations with deterministic concurrency fixtures.

Tools and methodologies worth exploring:
- PostgreSQL serializable transactions, advisory locks, scoped reservations, Cedar or OPA policy programs, TLA+, Jepsen-style race tests

Evidence and caveat: the paper evaluates a Python prototype and scripted LLM-free workflows. No public implementation repository was exposed in the primary paper or verified by search, so Provenact is an architecture reference rather than a drop-in package.

Implementability score: 0.67

Core source: https://arxiv.org/abs/2608.02764v1

## Current implication

Move authority as close to the effect as possible. The model can propose and a policy engine can explain, but only a commit-time control that owns the relevant state can safely grant the side effect.
