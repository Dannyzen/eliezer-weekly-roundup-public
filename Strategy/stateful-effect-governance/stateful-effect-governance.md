# Stateful Effect Governance

## Overview

The most important agent-governance finding of the week is not a new policy language. It is a correctness boundary: request-time authorization is insufficient when the state that justified the decision can change before the effect commits.

[Stateful Governance for Concurrent Agentic Systems](https://arxiv.org/abs/2608.02764v1) names the failure **stale authorization** and defines **policy-state serializability** (PSS). PSS requires every committed effect to be explainable as authorized against the policy state immediately before that effect occurs.

That moves governance out of the prompt, out of a detached policy check, and into the commit path that owns the relevant state. The model proposes. The policy explains. The stateful effect boundary grants authority.

Primary category: Strategy

Stack layer: execution control between agent or workflow orchestration and the provider that commits a durable effect.

Implementability score: **0.67**

## Why this won the week

Other strong findings improved durable workflows, shared-workspace evaluation, local model deployment, and sandbox selection. Stateful governance mattered more because it closes a correctness gap that survives all of them.

A perfectly checkpointed workflow can resume into a stale approval. A strong model can still spend a budget that another agent already consumed. A tool allowlist can permit a refund whose cumulative limit changed one millisecond earlier. A human approval can become invalid while it waits in a queue.

This paper supplies three things the alternatives did not supply together:

1. a named failure mode, stale authorization;
2. a testable correctness condition, policy-state serializability;
3. a runtime pattern that preserves policy modularity without globally serializing all work.

That combination makes it architectural, measurable, and partially implementable now.

## Core innovation

### Policy-state serializability

The central rule is simple:

> A governed effect may commit only if its authorization is valid against the policy state immediately before commit.

The word "policy-state" matters. Ordinary database serializability protects data transactions. PSS additionally asks whether the policy meaning of each allowed effect is valid in a serial explanation of the committed history.

The paper's minimal example uses two transfers from different accounts under one shared team budget. Their account writes do not conflict, but their policy meaning does. Both can pass a request-time budget check and still violate the shared limit when both commit.

### Provider contracts

Provenact, the paper's research runtime, makes the underlying provider declare:

- certified policy-state views that policy programs may read;
- logical scopes that identify conflicts, such as team, account, order, inventory item, or quota bucket;
- governed effects that mutate durable state;
- transaction, hold, or reservation mechanisms that preserve the decision through commit.

This is the load-bearing shift. The runtime cannot infer a sound effect boundary from tool descriptions. The provider must declare the state dependencies and effect footprint that make enforcement possible.

### Three enforcement modes

The paper separates three useful mechanisms:

- **Scoped transaction:** re-evaluate and commit under one protected database transaction for synchronous effects.
- **Scoped hold:** preserve the relevant scope while human approval is pending, allowing unrelated scopes to proceed.
- **Reservation:** reserve consumable capacity, such as budget or inventory, while approval is pending and reject conflicting work immediately.

Revalidation alone prevents a stale commit but can invalidate a human approval after the person has acted. Holds and reservations preserve the approval's state basis. That distinction is strategically important: safe rejection is not the same as durable human authority.

## Evidence

The evidence is controlled rather than production-scale, but the failure and the control are both concrete.

### Concurrent budget conflict

In a 256-operation full-conflict workload, request-local Naive and Cedar baselines produced 30 to 31 stale allows and committed 79.4 to 80.8 transfers even though the shared budget allowed only 50. Global serialization, manual transactions, Provenact-Tx, and Provenact-Res committed exactly 50, denied the rest, and produced zero stale allows across five seeds.

### Scoped enforcement cost

In a 512-operation workload with 32 clients and 16 logical scopes, Provenact-Tx reached 86.4 operations per second at 10 ms service time. That was 0.93 times the hand-written transaction baseline and 1.64 times the global-lock baseline. At 0 ms service time, it reached 88.9 operations per second, matching the manual transaction path but only 0.87 times the global path.

The honest conclusion is not that governance is free. Scoped enforcement avoids the larger concurrency cost of one global lock when work has separable scopes.

### Delayed approval

In the single-approval experiment, a global hold preserved approval but blocked all unrelated transfers. Provenact holds and reservations preserved approval while all 16 unrelated transfers committed. In the 64-team scaling test, reservations preserved every pending approval and achieved 12.4 percent fixed-window unrelated progress, versus 7.5 percent for scoped holds. Revalidation modes preserved serializability but invalidated every pending approval basis in that workload.

### Scripted procurement workflow

The paper also ran 256 scripted, LLM-free procurement workflows over shared budget, inventory, approval, and per-agent cost state. AGT averaged 71.6 committed workflows but only 59.0 valid commits, with 12.6 stale authorizations. Omnigent averaged 107.6 commits but only 66.2 valid commits, with 41.4 stale authorizations. Both Provenact modes averaged 70.6 commits, all valid, with zero stale decisions or final policy-state violations.

This does not prove live production behavior. It does show why a policy vocabulary without decision-effect binding is insufficient.

## How it fits into the agentic stack

Stateful effect governance sits below orchestration and above durable providers.

1. **Model and planner:** propose an action and arguments.
2. **Agent runtime:** manage trajectory, checkpoint, tools, retries, and human interaction.
3. **Gateway and identity plane:** authenticate the principal, select allowed tools, and attach policy context.
4. **Stateful effect boundary:** evaluate certified policy state, protect logical scopes, preserve approvals, and bind authorization to one effect identity.
5. **Provider:** commit the database or external state transition.
6. **Evidence plane:** emit the policy version, state reads, scope set, decision, effect identity, commit result, and reconciliation outcome.

This deepens three existing repo concepts:

- [Context-to-Execution Integrity](../context-to-execution-integrity/context-to-execution-integrity.md): typed releases are necessary, but the release must still be valid against live policy state at commit.
- [Agent Execution Control Plane](../agent-execution-control-plane/agent-execution-control-plane.md): a capability can authorize an attempted action, while PSS governs whether the shared-state effect may commit now.
- [Runtime Governance](../runtime-governance/runtime-governance.md): governance becomes a consistency property over state and effects, not only a monitor or policy response.

## Practical implementation now

### Phase 1: database-contained effects

Start where the state and effect can share one transactional boundary.

1. **Inventory** each consequential tool's effect and every mutable fact its policy reads.
2. **Name** logical conflict scopes, for example `team:123:daily-budget`, `order:456:refund`, or `tenant:789:quota`.
3. **Define** a typed effect intent with principal, action, resource, arguments, policy version, idempotency key, and expected scopes.
4. **Evaluate** policy from provider-certified views inside the transaction.
5. **Commit** the effect and governance receipt atomically.
6. **Test** racing operations with deterministic barriers so both see the pre-conflict state before one is allowed to commit.

Useful components:

- PostgreSQL transactions and transaction-scoped advisory locks;
- Cedar or Open Policy Agent for reviewable policy programs;
- Pydantic or JSON Schema for effect-intent and provider-contract types;
- Hypothesis state machines, deterministic concurrency fixtures, and Jepsen-style histories for invariant tests;
- OpenTelemetry spans for decision, wait, reservation, commit, retry, and reconciliation events.

### Phase 2: human approval

Add explicit pending-state semantics:

- choose revalidation when losing the approval basis is acceptable;
- use scoped holds when conflicts should wait;
- use reservations for consumable capacity such as money, inventory, quota, or slots;
- define expiry, cancellation, release, and conflict behavior before exposing the workflow to users.

The receipt should distinguish `approved`, `approval_basis_preserved`, `revalidated`, `invalidated`, `committed`, and `released`. A timeless boolean approval is not enough.

### Phase 3: external effects

Many APIs cannot join a database transaction. The paper leaves this as future work. A practical protected-execution protocol should:

1. reserve or protect policy state;
2. persist a durable effect intent with one external operation identity;
3. invoke the external API with an idempotency key;
4. reconcile the provider result;
5. consume, release, or quarantine the reservation;
6. require operator review for ambiguous outcomes.

Use a transactional outbox, idempotent provider APIs, durable retries, and reconciliation workers. Do not claim PSS when the external provider cannot bind or recover the effect.

## Implementation complexity

The database-contained path is medium complexity. PostgreSQL already supplies the core concurrency primitives, and policy-as-code systems already supply reviewable decisions. The hard work is defining complete provider contracts and testing the dependency scopes.

Long-running approvals are higher complexity because holds and reservations need durable lifecycle semantics, expiry, cancellation, and fairness.

External effects are the weakest point. Without provider idempotency, durable intent identity, and reconciliation, the system cannot guarantee that a protected local decision matches the remote side effect.

> Choose scoped commit-boundary enforcement for consequential shared-state tools. You get a testable safety property and concurrency across independent scopes, but give up the simplicity of one request-time allow decision.

## What remains conceptual or blocked

The paper has several important limits:

- The benchmarks are controlled and the agentic workflow is scripted without an LLM.
- The prototype covers one concrete policy-state provider.
- No public Provenact repository was exposed in the primary paper or found in the verification search. The paper describes an artifact, but it is not a verified drop-in implementation.
- Production deployment tooling, signed policy bundles, and concrete MAF or LangGraph integrations are absent.
- External-effect recovery is explicitly future work.
- Provider contracts and provider implementations remain trusted code. Incorrect dependency declarations can destroy the guarantee.

The last point is the best objection. PSS is only as sound as the provider's declared views, scopes, and effects. The guardrail is fail-closed contract validation plus adversarial race tests. If the provider cannot enforce the required state boundary, the runtime must weaken the guarantee explicitly or refuse deployment.

## Strategic implications for Danny's product thinking

The durable product rule is: **authority expires when its state basis can change**.

That sharpens the bounded-agent model. Per-person identity, isolated credentials, tool allowlists, and human approval are necessary, but they do not protect shared budgets, inventory, quotas, schedules, or operational records from concurrent stale decisions.

For agent products that touch finance, provisioning, customer operations, scheduling, or fleet workflows:

- treat each consequential tool as a state transition, not a function call;
- make the shared-state owner, not the model, the final authority;
- preserve human approval with reservations when the user expects approval to mean the action will remain valid;
- sell auditable effect control and recovery, not merely better policy prompts;
- expose the distinction between proposed, allowed, reserved, committed, and reconciled states in the operator UI.

This also suggests a practical wedge for Hermes and FriendVM systems: a small stateful effect broker can sit beside the existing runtime and protect only the highest-consequence tools first. It does not require replacing orchestration, memory, or model routing.

## Core sources

- [Stateful Governance for Concurrent Agentic Systems, immutable v1 abstract](https://arxiv.org/abs/2608.02764v1)
- [Stateful Governance for Concurrent Agentic Systems, immutable v1 PDF](https://arxiv.org/pdf/2608.02764v1)

## Supporting sources and tools

- [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)
- [Cedar policy language](https://github.com/cedar-policy/cedar)
- [Open Policy Agent](https://www.openpolicyagent.org/)
- [PostgreSQL explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
- [Resume Means Resume, adjacent persistence-contract research](https://arxiv.org/abs/2608.03836v1)

## August 17 update: rollback and atomicity are one effect contract

AgentRewind and LegacyWorld connect two halves of stateful effect governance. Recovery needs an aligned context-environment checkpoint, while acceptance needs a four-way distinction between useful completion, safe failure, and persistent damage.

Practical lesson:
- bind checkpoint identity to the state basis used by the agent decision;
- declare every effect reversible, compensatable, or irreversible;
- protect validated prefix work during recovery;
- require independent post-run state validators;
- release only when both valid-success and atomicity thresholds pass;
- reconcile remote effects that cannot be restored locally.

Evidence caveat: AgentRewind controls managed state, while LegacyWorld observes declared state in isolated VMs. Neither removes the need for provider idempotency and reconciliation around external effects.

Sources:
- [AgentRewind](https://arxiv.org/abs/2608.14380v1)
- [LegacyWorld](https://arxiv.org/abs/2608.14131v1)
