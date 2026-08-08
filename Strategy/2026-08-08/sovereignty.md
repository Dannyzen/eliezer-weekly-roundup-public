# Strategy Daily Sovereignty, 2026-08-08

No new arXiv listing appears on Saturday. These findings are from the Friday, 2026-08-07 listing batch, with v1 submissions dated 2026-08-06.

## Experience promotion is an authority boundary

When Experience Becomes Instruction shows why trajectory-to-skill promotion cannot be treated as ordinary summarization. PoisonedEvolution contributes only three attacker records in a 30-record batch, yet embeds target behavior in 546 of 600 SkillClaw trials and 369 of 600 Trace2Skill trials across six LLM evolvers. The attacker cannot edit the skill bank directly. It wins by making malicious evidence look causally useful, recurrent, and generalizable.

Why it matters: the dangerous transition is promotion from untrusted experience into durable instruction. Post-generation text scanning is too late because the promotion process has already granted authority.

Strategic fit: self-improvement governance, evidence provenance, skill admission control, and untrusted-data boundaries.

Implement now:
- label trajectory evidence by origin, principal, task, and outcome;
- require source diversity rather than repeated support from one principal;
- separate proposer, evaluator, and promoter roles;
- replay proposed skills against clean historical cases and adversarial canaries;
- retain the exact evidence set and promotion receipt;
- quarantine generated skills until deterministic and human gates pass.

Artifact status: no public implementation artifact was verified. The attack uses inert canaries.

Implementability score: 0.58

Core source: https://arxiv.org/abs/2608.05563v1

## Agent signing needs hardware-confined keys plus exact-payload release

Hardware Keystores for AI Agent Signing Workflows moves private keys behind PKCS#11 handles in an HSM, TPM, or smart card, then adds session identity, policy checks, SHA-256 payload commitments, and audit receipts around MCP-mediated signing. Across 192 combined trials, baseline attack success was 19.3 percent and protected attack success was 0 percent, with a 95 percent confidence upper bound of 2.0 percent. The study reports zero false positives across four benign scenarios and validates the adapter on SoftHSMv2 and an Infineon TPM 2.0.

Why it matters: secret isolation prevents extraction but not misuse. The signing boundary must bind principal, session, policy, exact payload, and receipt before the hardware operation occurs.

Strategic fit: execution control, credential sovereignty, context-to-execution integrity, and MCP gateway governance.

Implement now:
- generate non-exportable keys inside a TPM, HSM, or smart card;
- expose opaque signing handles through a narrow broker;
- commit the exact payload hash before release;
- require policy and session identity outside the model process;
- log a receipt containing payload digest, principal, policy decision, and key handle;
- test prompt-injection attempts against inert payloads before rollout.

Artifact status: the anonymous artifact resolves read-only with 83 files, including source, tests, benchmark material, and an MIT-licensed README. It was not cloned or executed.

Implementability score: 0.72

Core sources:
- https://arxiv.org/abs/2608.06130v1
- https://anonymous.4open.science/r/Hardware-Keystores-for-AI-Agent-Signing-Workflows-Artifact-357C

## Working conclusion

Durable instruction and cryptographic action are authority transitions. Experience needs provenance-gated promotion, and signing needs hardware confinement plus exact-payload release. The model may propose either transition, but it must not own the gate.
