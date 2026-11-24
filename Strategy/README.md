# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Daily update: 2026-11-24

### Mediate concrete effects before execution

Summary: Tool-call text is insufficient authority evidence. Runtime policy should inspect and deny the system calls that implement file, process, network, credential, and package effects.

Analysis: [Daily strategy analysis](2026-11-24/sovereignty.md#1-mediate-actual-effects-below-tool-calls)

Core source: [AgentBouncer](https://arxiv.org/abs/2611.30621v1)

Implementable now:
- pre-effect system-call mediation
- task-bound necessity and safety checks
- deterministic deny rules
- scope-aware decision caching
- allowed and denied effect receipts

Implementability score: 0.48

### Isolate recovery and administrator authority

Summary: Scoped database identities need independent deny rules, unreachable backups, credential separation, and exercised restore proof.

Analysis: [Daily strategy analysis](2026-11-24/sovereignty.md#2-pair-least-privilege-with-tested-recovery-and-credential-isolation)

Core sources: [database agent blast-radius study](https://arxiv.org/abs/2611.30483v1), [harness and records](https://github.com/libredb/agent-blast-radius)

Implementable now:
- task-specific database identities
- external backup and recovery authority
- destructive-action deny rules
- credential isolation
- change-log reconciliation

Implementability score: 0.86

## Daily update: 2026-11-23

### Reconcile effects before changing suppliers

Summary: Effectful tool failover needs persistent attempt state. An uncertain write must block cross-supplier retry until the original outcome is reconciled.

Analysis: [Daily strategy analysis](2026-11-23/sovereignty.md#1-keep-supplier-choice-and-uncertain-effects-outside-the-agent)

Core source: [Keep the Process, Change the Supplier](https://arxiv.org/abs/2611.26966v1)

Implementable now:
- typed capability calls
- persistent attempt identities
- explicit uncertain outcomes
- fail-closed reconciliation
- supplier idempotency contracts

Implementability score: 0.62

### Govern tool descriptions as executable inputs

Summary: MCP tool descriptions can steer consequential argument values while preserving normal-looking tool selection, so descriptors need provenance, admission, and regression gates.

Analysis: [Daily strategy analysis](2026-11-23/sovereignty.md#2-treat-tool-metadata-as-executable-supply-chain-input)

Core source: [Subverting Tool Arguments](https://arxiv.org/abs/2611.27041v1)

Implementable now:
- approved descriptor origins
- pinned descriptor and schema hashes
- exact-change approval views
- request-bound argument authority
- descriptor red-team fixtures

Implementability score: 0.76

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

1. Resolve principal and source identity before retrieval or action.
2. Treat tool descriptions and schemas as admitted supply-chain inputs.
3. Compile model proposals into typed capability calls.
4. Keep supplier routing and effect state outside model context.
5. Block uncertain writes until reconciliation.
6. Preserve policy, supplier, argument, effect, and refusal receipts.

## Browse

- [Latest daily roundup](../roundups/2026-11-24.md)
- [Daily strategy analysis](2026-11-24/sovereignty.md)
- [Friday synthesis](../roundups/2026-11-20.md)
- [Weekly strategy analysis](2026-11-20/sovereignty.md)
- [Agent gateway governance](agent-gateway-governance/agent-gateway-governance.md)
- [Runtime policy verification](runtime-policy-verification/runtime-policy-verification.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Agent authority manifests](agent-authority-manifests/agent-authority-manifests.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
