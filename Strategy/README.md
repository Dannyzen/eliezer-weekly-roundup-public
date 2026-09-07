# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-07

### Individually valid controls can compose into the wrong effect

Summary: CONTINUITY binds principal, task, provenance, delegation, policy, canonical action, and finality into one authenticated witness. Its deterministic suite committed no harmful effect in 2,560 modeled attacks, while the strongest incomplete gateway-plus-finality configuration still failed in 65.6% of attack instances.

Analysis: [daily strategy](2026-09-07/sovereignty.md#security-controls-need-end-to-end-continuity-contracts)
Core sources: [paper](https://arxiv.org/abs/2609.05269v1), [continuity](https://github.com/zast-ai/continuity)
Tools and methodologies worth exploring now: assume-guarantee contracts, typed releases, canonical action digests, transformation witnesses, finality revalidation, alternate-path fault injection
Implementability score: 0.83

## Current implication

A chain of green controls is not end-to-end authorization. The security context must survive every adapter and remain bound to a current, exact effect at finality.
