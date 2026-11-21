# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Daily update: 2026-11-21

### Prove mandate and answerability before action release

Summary: Realistic trajectory audits should test whether an agent stays inside its mandate, while paired-state audits should prove that the decision received enough current state to be answerable.

Analysis: [Daily strategy analysis](2026-11-21/sovereignty.md)

Core sources: [Continuation Audits](https://arxiv.org/abs/2611.24491v1), [State-Dependent Command Safety](https://arxiv.org/abs/2611.24682v1)

Implementable now:
- redacted real-session prefixes in disposable audit fixtures
- separate deviation and consequence scoring
- paired cases with identical commands and opposite state-dependent outcomes
- exact state and policy snapshot capture
- fail-closed handling for missing or stale state

Implementability scores: 0.60 for continuation audits; 0.90 for answerability audits

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

1. Treat model output as a proposal.
2. Preserve provenance without treating it as authorization.
3. Compile proposals into typed action manifests.
4. Compute or observe the reachable effects.
5. Compare those effects with the current mandate.
6. Keep commit authority and persistent policy outside model context.

## Browse

- [Latest daily roundup](../roundups/2026-11-21.md)
- [Daily strategy analysis](2026-11-21/sovereignty.md)
- [Friday synthesis](../roundups/2026-11-20.md)
- [Weekly strategy analysis](2026-11-20/sovereignty.md)
- [Runtime policy verification](runtime-policy-verification/runtime-policy-verification.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Agent authority manifests](agent-authority-manifests/agent-authority-manifests.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
