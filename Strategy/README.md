# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-19

### Use intent contracts for attribution, then authorize the effect

Summary: Intent contracts make planner influence visible and replayable, but their own evaluation shows that visible intent does not prevent wrong-target actions when the executor lacks live environment evidence.

Analysis: [Daily strategy analysis](2026-11-19/sovereignty.md#1-treat-intent-contracts-as-provenance-not-authorization)

Core sources: [Intent Contracts v1](https://arxiv.org/abs/2611.24025v1), [implementation and run records](https://github.com/zwang-devv/intent-contracts)

Implementable now:
- planner and executor separation
- checked quotations and typed scope fields
- ordered contract and call logs
- live target resolution and final effect authorization

Implementability score: 0.76

### Compile skill obligations into runtime transitions

Summary: SkillCFI blocks permitted operations when they violate required sequence or evidence obligations, showing why allowlists cannot enforce procedures.

Analysis: [Daily strategy analysis](2026-11-19/sovereignty.md#2-compile-skill-prose-into-enforceable-control-flow)

Core source: [SkillCFI v1](https://arxiv.org/abs/2611.24185v1)

Implementable now:
- source-linked obligation graphs
- trusted boundary evidence
- deterministic host-side state
- legal next-step refusals
- mediated execution channels

Implementability score: 0.52

## Current strategic model

1. Separate planning from execution authority.
2. Keep intent visible through source-linked contracts.
3. Resolve targets against live environment state.
4. Compile procedural obligations into deterministic transitions.
5. Authorize each effect at the last trusted boundary.
6. Preserve contract, refusal, and effect receipts.

## Browse

- [Daily roundup](../roundups/2026-11-19.md)
- [Daily strategy analysis](2026-11-19/sovereignty.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Runtime policy verification](runtime-policy-verification/runtime-policy-verification.md)
