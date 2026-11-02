# Strategy

Governance research for runtime authority, evidence provenance, identity, gateways, and sovereign control surfaces.


## Daily addendum: 2026-11-02

### Authorize effects across every interface

Summary: normalize GUI, CLI, API, script, and MCP routes into one effect model, then bind authorization to the concrete route and revalidate state at commit.

Analysis: [Daily strategy](2026-11-02/sovereignty.md#1-authorize-effects-across-every-interface-then-bind-the-decision-to-commit-state)

Core source: [Cross-Interface Authorization](https://arxiv.org/abs/2610.41397v1)

Implementable now:
- effect-route inventory
- typed effect manifests
- route-bound expiring grants
- commit-time precondition checks
- sink receipts and bypass mutants

Implementability score: 0.64

### Treat tool-call traces as sensitive behavioral data

Summary: tool names, arguments, returned results, and cross-session linkage can reveal user attributes without conversation access.

Analysis: [Daily strategy](2026-11-02/sovereignty.md#2-treat-tool-call-traces-as-sensitive-behavioral-data)

Core sources: [PrivacyTrace paper](https://arxiv.org/abs/2610.41885v1), [read-only artifact](https://github.com/AI45Lab/PrivacyTrace)

Implementable now:
- payload minimization and redaction
- receipt and payload separation
- tenant-isolated short-lived trace stores
- purpose-bound cross-session joins
- profile-inference audits

Implementability score: 0.78

## Daily addendum: 2026-11-01

### Treat repository instruction files as untrusted policy-bearing input

Summary: coding-agent memory files are executable context, and model awareness of a malicious file does not reliably protect the generated code.

Analysis: [Daily strategy](2026-11-01/sovereignty.md#1-treat-repository-instruction-files-as-untrusted-policy-bearing-input)

Core source: [Security Impact of Coding Agent's Memory Files](https://arxiv.org/abs/2610.38521v1)

Implementable now:
- CODEOWNERS and branch rules for instruction files
- separate instruction-diff review
- provenance in run manifests
- no authority amplification from repository context
- security regression fixtures on instruction changes

Implementability score: 0.90

### Keep behavioral probes advisory and enforce secrets at the release boundary

Summary: activation probes can warn shortly before disclosure, but they confuse permitted and prohibited releases and broad halting disrupts benign work.

Analysis: [Daily strategy](2026-11-01/sovereignty.md#2-keep-behavioral-probes-advisory-and-enforce-secrets-at-the-release-boundary)

Core sources: [Pre-Crime for Agents](https://arxiv.org/abs/2610.40588v1), [read-only artifact](https://github.com/leonidas1712/precrime-agents)

Implementable now:
- exact secret-release grants
- trained text baseline in shadow mode
- matched permitted and prohibited disclosure tests
- external policy after learned warnings
- disclosure and disposition receipts

Implementability score: 0.38

## Daily addendum: 2026-10-31

### Authorize information for its full propagation scope

Summary: judge sensitive information against recipient history and the complete planned agent route, then bind every release to an allowed propagation subgraph.

Analysis: [Daily strategy](2026-10-31/sovereignty.md#1-authorize-information-for-its-full-propagation-scope)

Core source: [Judging Before Propagation](https://arxiv.org/abs/2610.39532v1)

Implementable now:
- per-recipient disclosure history
- purpose and information-type labels
- graph-versioned propagation scopes
- frontier redaction or removal
- transfer receipts

Implementability score: 0.68

## Latest structured week: 2026-10-30

### Encode authority as runtime state, not prompt prose

Summary: consequential effects need machine-checkable session state and a separate write-release path. Prompts can describe policy; the runtime must enforce it.

Analysis: [Weekly strategy](2026-10-30/sovereignty.md#1-encode-authority-as-runtime-state-not-prompt-prose)

Core sources: [Concordat](https://arxiv.org/abs/2610.37461v1), [GitHub Agentic Workflows](https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/)

Implementable now:
- typed session state
- legal-tool projection
- read-only reasoning jobs
- separately scoped write-release jobs

Implementability score: 0.86

### Treat runtime feedback as untrusted data and carry proof with claims

Summary: authenticated messages and legitimate tool output can still contain false claims or malicious instructions. Keep feedback diagnostic and bind authoritative claims to independently verifiable events.

Analysis: [Weekly strategy](2026-10-30/sovereignty.md#2-treat-runtime-feedback-as-untrusted-data-and-carry-proof-with-claims)

Core sources: [CARI](https://arxiv.org/abs/2610.38799v1), [PCM](https://arxiv.org/abs/2610.39109v1)

Implementable now:
- control-data separation
- instruction quarantine for tool output
- typed evidence envelopes
- append-only source event logs

Implementability score: 0.73

### Bind workload identity and bound discovery data at the gateway

Summary: autonomous services need their own short-lived identity, while gateways must validate delegated audiences and limit which metadata reaches models or backends.

Analysis: [Weekly strategy](2026-10-30/sovereignty.md#3-bind-workload-identity-and-bound-discovery-data-at-the-gateway)

Core sources: [GitHub server-to-server authentication](https://github.blog/changelog/2026-10-27-github-copilot-supports-server-to-server-authentication/), [MCP Gateway Registry 1.35.0](https://github.com/agentic-community/mcp-gateway-registry/releases/tag/1.35.0)

Implementable now:
- workload-owned service identities
- short-lived delegated tokens
- audience and tenant validation
- bounded metadata projection and reserved-header stripping

Implementability score: 0.91

### Preserve refusal, escalation, and review as first-class outcomes

Summary: completion pressure causes agents to burn budget after an impasse and lets peer cooperation bypass intended review paths. Blocked and needs-review are valid terminal states.

Analysis: [Weekly strategy](2026-10-30/sovereignty.md#4-preserve-refusal-escalation-and-review-as-first-class-outcomes)

Core sources: [Escalation study](https://arxiv.org/abs/2610.31895v1), [FavorBench](https://arxiv.org/abs/2610.31985v1)

Implementable now:
- typed blocked and needs-review states
- evidence thresholds for impasse
- owner and beneficiary binding
- cooperation-bypass tests

Implementability score: 0.78

## Current strategic model

1. Evidence informs decisions but does not grant authority.
2. Runtime state defines legal effects.
3. Workload identity and gateway policy bind each request to a principal and scope.
4. Sensitive information carries an explicit propagation scope.
5. Source-owned proofs support claims across agent boundaries.
6. Refusal and escalation preserve policy when completion is unsafe or unsupported.

## Browse

- [Daily roundup](../roundups/2026-11-02.md)
- [Latest dated strategy](2026-11-02/sovereignty.md)
- [Weekly synthesis](../roundups/2026-10-30.md)
- [Evidence provenance control plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Untrusted data boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
