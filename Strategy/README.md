# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-21

### Bind approval to one canonical action at use time

Summary: Human approval creates authority only for the exact action rendered and reviewed. Canonicalize the action, bind approval to its digest, and reject any material mutation before release.

Analysis: [daily strategy analysis](2026-09-21/sovereignty.md#bind-approval-to-one-canonical-action-at-use-time)
Durable deep dive: [Context-to-Execution Integrity](context-to-execution-integrity/context-to-execution-integrity.md)
Core sources: [Loopjacking paper](https://arxiv.org/abs/2609.21081v1), [evidence archive](https://github.com/adithyan-ak/loopjacking)
Tools and methodologies worth exploring now: canonical action manifests, complete approval rendering, signed digests, use-time equality checks, pending-state immutability, approval-to-result receipts
Implementability score: 0.96

### Put deterministic payment policy after planning and before transfer

Summary: APort Vault recorded zero forbidden-recipient transfers behind a typed pre-action policy layer across 69,297 evaluations, while the layer still executed 25,370 payments. The model may propose a payment; deterministic policy must authorize the final transfer.

Analysis: [daily strategy analysis](2026-09-21/sovereignty.md#put-deterministic-payment-policy-after-planning-and-before-transfer)
Durable deep dive: [Stateful Effect Governance](stateful-effect-governance/stateful-effect-governance.md)
Core sources: [APort Vault paper](https://arxiv.org/abs/2609.22076v1), [dataset](https://huggingface.co/datasets/aporthq/vault-benchmark-v1)
Tools and methodologies worth exploring now: typed payment passports, recipient allowlists, amount and time limits, commit-boundary checks, matched replay tests, authoritative transfer lookup
Implementability score: 0.93

## Current implication

Approval and policy must travel with one canonical effect. Render it completely, bind authority to it, and verify it again at the last reversible point before execution.
