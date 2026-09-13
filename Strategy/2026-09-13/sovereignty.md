# Strategy Daily Sovereignty Analysis: 2026-09-13

## Freshness and selection

There is no new weekend arXiv batch. This paper was submitted on September 10 and first listed Friday, September 11, so it is a listing-window carry-forward. It survived duplicate checks because it adds an application-level control object that the repository's existing context-to-execution work did not yet name explicitly.

## Make interaction effects a versioned contract

### Finding

Agent-Integrated Software separates the conventional application core, which owns domain objects and durable state, from the agent that plans and invokes capabilities. It introduces an Intent-Level Interaction Abstraction for goals, contextual references, proposals, endorsements, interventions, and outcomes, then requires those task-level events to correspond to concrete application effects.

The useful control object is an interaction contract with five parts: preconditions including authority, allowed task and control transitions, invariants, postconditions that define a fulfilled effect or report, and dependencies that name the assumptions and versions supporting the claim. Continuous assurance maintains the standing of those claims as policies, tasks, components, and dependencies change.

The paper also separates a stop request from proof that stopping took effect. A controller epoch identifies the active generation of authority; an acknowledged stop invalidates that generation for later admissions while earlier effects can still be reconciled.

### Why it matters

A chat panel can display the right words while the application continues the wrong work. Product surfaces need a maintained correspondence between user intent, shared object state, authority, control transitions, and effect evidence. Otherwise pause, edit, approve, and completion become cosmetic states.

### Strategy fit

This belongs in context-to-execution integrity and stateful effect governance. The application core remains authoritative, while the agent operates through versioned task and effect contracts that can be invalidated and rechecked.

### Practical path now

- Define a typed contract with `pre`, `step`, `invariants`, `post`, and `dependencies` for each consequential operation.
- Bind every task to object IDs, role-specific authority, a controller epoch, and an evidence requirement.
- Distinguish requested, acknowledged, admitted, applied, reconciled, and reported states.
- Revalidate contract dependencies after user edits, policy changes, retries, and component upgrades.
- Make the UI derive pause, completion, and outcome claims from runtime receipts, not model prose.
- Add tests where users edit shared objects or cancel work while execution is in flight.

Implementability score: 0.62

Artifact status: this is a perspective and semantic-framework paper. No public implementation artifact was linked. The contract shape is implementable now, but complete continuous assurance needs application-specific abstractions, monitors, and evidence ownership.

Core source:
- [Agent-Integrated Software: Interaction Contracts and Continuous Assurance](https://arxiv.org/abs/2609.11381v1)

## Working conclusion

Agent integration is dependable only when user-visible intent and runtime effects share a versioned contract. The application core, not the conversational layer, must own state, authority, cancellation, and proof of completion.
