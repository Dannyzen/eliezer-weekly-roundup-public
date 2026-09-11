# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-11

### Independent evidence beats a second model at commit time

Summary: In VP-CONTROL's 2,880 scenarios, cross-model voting over shared evidence approved 62.9% of unsafe proposals, versus 22.9% with an independent source. Evidence-source diversity moved results by 40.9 points, compared with 11.3 points for model diversity.

Analysis: [daily analysis](2026-09-11/sovereignty.md#independent-evidence-beats-a-second-model-at-commit-time)
Core sources: [paper](https://arxiv.org/abs/2609.10969v1), [MIT artifact](https://doi.org/10.6084/m9.figshare.33511441.v1)
Tools and methodologies worth exploring now: evidence-lineage IDs, deterministic fault injection, calibrated verification portfolios, transactional preconditions, explicit defer states, offline replay from frozen records
Implementability score: 0.74

### Protocol compliance is not delegation safety

Summary: A2ABreak reports 11 A2A vulnerabilities exploitable by a specification-compliant adversary, including cross-client context injection, multi-hop identity loss, and unattested capability claims. Its formal framework reached 73.3% precision and 84.6% F1 against expert review.

Analysis: [daily analysis](2026-09-11/sovereignty.md#protocol-compliance-is-not-delegation-safety)
Core sources: [paper](https://arxiv.org/abs/2609.10871v1), [A2ABreak](https://github.com/arlotfi79/A2ABreak), [A2A specification](https://a2a-protocol.org/latest/specification/)
Tools and methodologies worth exploring now: tenant-bound context IDs, end-principal identity, delegation-chain receipts, capability attestations, audience-bound credentials, formal lifecycle review
Implementability score: 0.73

## Current implication

Independent models are not independent verifiers when they share evidence. Preserve independent state lineage at commit time, and carry context ownership, principal identity, and capability authority across every A2A hop.
