# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-22

### Let models propose policy, then certify and freeze it before effects

Summary: ActGov uses an LLM to propose policy, Z3 to check the complete bundle against declared invariants, and a deterministic runtime monitor to authorize each external action. The split preserves adaptive planning while keeping effect authority outside the model.

Analysis: [daily strategy analysis](2026-09-22/sovereignty.md#let-models-propose-policy-then-certify-and-freeze-it-before-effects)
Durable deep dive: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [ActGov](https://arxiv.org/abs/2609.24446v1)
Tools and methodologies worth exploring now: finite policy records, offline counterexample checking, frozen policy digests, deterministic pre-action enforcement, matched security and utility metrics, decision receipts
Implementability score: 0.48

## Current implication

Use models to draft policy and discover gaps. Use formal checks to certify a bounded policy model, then use deterministic runtime code to decide whether one exact external effect may proceed. Policy portability remains a separate test.
