# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-08

### Experience-to-skill promotion is an authority boundary

Summary: PoisonedEvolution embeds target behavior in 546 of 600 SkillClaw trials and 369 of 600 Trace2Skill trials with only 10 percent attacker support.

Analysis: [daily analysis](2026-08-08/sovereignty.md#experience-promotion-is-an-authority-boundary)
Core source: [paper](https://arxiv.org/abs/2608.05563v1)
Tools and methodologies worth exploring now: evidence lineage, source-diversity gates, proposer-evaluator-promoter separation, adversarial canaries, replay receipts
Implementability score: 0.58

### Signing needs hardware confinement and exact-payload release

Summary: A PKCS#11 signing broker combines non-exportable keys, session policy, SHA-256 payload commitments, and receipts. Protected attack success was 0 of 192 combined trials, with a 95 percent upper bound of 2.0 percent.

Analysis: [daily analysis](2026-08-08/sovereignty.md#agent-signing-needs-hardware-confined-keys-plus-exact-payload-release)
Core sources: [paper](https://arxiv.org/abs/2608.06130v1), [read-only artifact](https://anonymous.4open.science/r/Hardware-Keystores-for-AI-Agent-Signing-Workflows-Artifact-357C)
Tools and methodologies worth exploring now: TPM 2.0, HSM, smart cards, PKCS#11, exact-payload commitments, policy receipts
Implementability score: 0.72

## Current implication

Authority should be earned at write time and re-checked at use time. Gateways need temporal and rate policy. Effects need commit-time validity. Skills need admission before they load. Session history needs authority labels before it can decide the next effect. The model may propose. The boundary still grants.
