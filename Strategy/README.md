# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-20

### Enforce policy over observed side effects

Summary: Tether executes proposed actions in an ephemeral sandbox, derives conservative system-level effects, and applies stateful information-flow policy before host mutation.

Analysis: [Daily strategy analysis](2026-11-20/sovereignty.md#1-enforce-policy-over-observed-side-effects-not-command-text)

Core source: [Tether v1](https://arxiv.org/abs/2611.25599v1)

Implementable now:
- disposable pre-execution sandboxes
- system-call to action normalization
- persistent security labels outside model context
- deny-overrides policy composition
- boundary blocking for untraced state

Implementability score: 0.62

### Check the closure of delegated authority

Summary: A signed object is authorized only when every reachable effect it enables stays inside the human mandate. Field matching and one successful simulation do not prove that property.

Analysis: [Daily strategy analysis](2026-11-20/sovereignty.md#2-check-the-closure-of-delegated-authority-before-signing)

Core source: [Signed, Valid, and Unauthorized v1](https://arxiv.org/abs/2611.24989v1)

Implementable now:
- explicit effect-set mandates
- retry, period, and sequence constraints
- contract-aware capability analysis
- bounded adversary programs before signing
- last-boundary authorization

Implementability score: 0.68

## Current strategic model

1. Treat visible intent and signatures as provenance.
2. Derive the effects a capability can actually produce.
3. Observe proposed system effects in isolation.
4. Carry stateful policy labels across steps.
5. Commit only effects inside the current mandate.
6. Preserve refusal and effect receipts.

## Browse

- [Daily roundup](../roundups/2026-11-20.md)
- [Daily strategy analysis](2026-11-20/sovereignty.md)
- [Runtime policy verification](runtime-policy-verification/runtime-policy-verification.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Agent authority manifests](agent-authority-manifests/agent-authority-manifests.md)
