# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Daily update: 2026-11-22

### Enforce source permissions before retrieval reaches the model

Summary: Organizational search should bind caller identity to source scope, filter retrieval before context assembly, and return cited source identities with the answer.

Analysis: [Daily strategy analysis](2026-11-22/sovereignty.md#1-enforce-source-permissions-before-retrieval-reaches-the-model)

Core sources: [Diderot repository](https://github.com/bluesky-social/diderot), [v1.0.0 release](https://github.com/bluesky-social/diderot/releases/tag/v1.0.0)

Implementable now:
- event-level source and principal scope
- request-bound caller identity
- pre-context retrieval filtering
- cited source and scope receipts
- Postgres event truth with a rebuildable vector projection

Implementability score: 0.78

## Weekly baseline: week ending 2026-11-20

### Put a deterministic effect boundary between intent and execution

Summary: The acting model should propose work while trusted runtime code compiles or observes typed effects, applies stateful policy, and owns commit authority.

Analysis: [Weekly strategy analysis](2026-11-20/sovereignty.md#1-put-a-deterministic-effect-boundary-between-intent-and-execution)

Core sources: [CapLite](https://arxiv.org/abs/2611.17115v1), [System 1 Agents](https://arxiv.org/abs/2611.21053v1), [Runtime Verification](https://arxiv.org/abs/2611.23074v1), [Tether](https://arxiv.org/abs/2611.25599v1)

Implementable now:
- separate planning and execution credentials
- typed action schemas
- disposable pre-execution sandboxes
- effect normalization and deny-overrides policy
- commit and refusal receipts

Implementability score: 0.76

### Check authority closure at the last trusted boundary

Summary: Provenance and valid signatures do not prove that every reachable effect stays inside the human mandate. The signing or execution boundary must check the full capability envelope.

Analysis: [Weekly strategy analysis](2026-11-20/sovereignty.md#2-check-authority-closure-at-the-last-trusted-boundary)

Core sources: [Intent Contracts](https://arxiv.org/abs/2611.24025v1), [Signed, Valid, and Unauthorized](https://arxiv.org/abs/2611.24989v1)

Implementable now:
- principal, resource, action, time, retry, and sequence constraints
- conservative reachable-effect analysis
- last-boundary mandate comparison
- independent capability expiry and revocation
- exact refusal receipts

Implementability score: 0.68

## Current strategic model

1. Resolve principal identity before retrieval or action.
2. Filter source evidence before model context assembly.
3. Treat model output as a proposal.
4. Compile proposals into typed action manifests.
5. Compare reachable effects with the current mandate.
6. Keep commit authority and persistent policy outside model context.

## Browse

- [Latest daily roundup](../roundups/2026-11-22.md)
- [Daily strategy analysis](2026-11-22/sovereignty.md)
- [Friday synthesis](../roundups/2026-11-20.md)
- [Weekly strategy analysis](2026-11-20/sovereignty.md)
- [Agent gateway governance](agent-gateway-governance/agent-gateway-governance.md)
- [Runtime policy verification](runtime-policy-verification/runtime-policy-verification.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Agent authority manifests](agent-authority-manifests/agent-authority-manifests.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
