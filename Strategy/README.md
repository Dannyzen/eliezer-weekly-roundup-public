# Strategy

This index tracks the most recent structured strategy research. Each finding links to the daily analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-13

### Make interaction effects a versioned contract

Summary: Agent-Integrated Software separates the authoritative application core from the planning agent, then binds task revisions, object references, authority, control transitions, effects, evidence, and dependency versions in an interaction contract. A controller epoch distinguishes a stop request from proof that old authority is no longer active.

Analysis: [daily analysis](2026-09-13/sovereignty.md#make-interaction-effects-a-versioned-contract)
Core source: [Agent-Integrated Software](https://arxiv.org/abs/2609.11381v1)
Tools and methodologies worth exploring now: typed preconditions, transition rules, invariants, postconditions, dependency manifests, controller epochs, effect receipts, in-flight edit and cancellation tests
Implementability score: 0.62

## Current implication

The conversational surface may express intent, but the application core must own effects. Pause, completion, approval, and outcome claims should be derived from versioned contracts and runtime receipts.
