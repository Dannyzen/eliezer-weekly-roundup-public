# Strategy Weekly Sovereignty: 2026-10-30

## Thesis

Evidence, context, and model confidence are inputs. Authority is a separate runtime object with explicit state, identity, scope, and receipts.

## 1. Encode authority as runtime state, not prompt prose

Concordat exposes only state-legal tools and rejects illegal effects before dispatch. GitHub Agentic Workflows applies the same split operationally: reasoning runs inside existing Actions policy and sandbox boundaries, while writes flow through separately scoped safe-output jobs.

Why it matters: prompts describe desired behavior but do not enforce it. Consequential effects need a machine-checkable transition from current state to permitted next state.

Fit in the strategy: execution control, approval state machines, guarded CI, and effect release.

Implementable now:
- represent approvals, budgets, and effect order as typed session state;
- expose only currently legal tools;
- keep reasoning jobs read-only by default;
- release writes through a separate job or broker with narrow permissions and exact-effect receipts.

Weakest point: state machines add design and migration cost, and incomplete state models can block legitimate work. Start with high-impact effects and include explicit escalation and unsupported states.

Implementability score: 0.86

Core sources:
- [Concordat](https://arxiv.org/abs/2610.37461v1)
- [GitHub Agentic Workflows generally available](https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/)
- [github/gh-aw](https://github.com/github/gh-aw)

## 2. Treat runtime feedback as untrusted data and carry proof with claims

CARI demonstrates that legitimate runtime feedback from peer-controlled components can carry malicious instructions into coding-agent loops. PCM addresses the adjacent multi-agent problem by attaching independently verifiable log evidence to claims such as tests passed or approval granted.

Why it matters: authenticated channels prove who sent data, not whether the data is true or authorized. Logs, API errors, test output, peer messages, and memory all cross the same control-data boundary.

Fit in the strategy: untrusted-data boundaries, evidence provenance, multi-agent communication, and side-effect authorization.

Implementable now:
- label runtime feedback as diagnostic data and quarantine embedded instructions;
- keep authorization policy outside model-visible feedback;
- attach typed claims to source-owned append-only event records;
- check freshness, subject, action scope, and source identity before accepting a claim.

Weakest point: PCM is an early specification and reference path, not a mature interoperability standard. The broader evidence-envelope pattern is usable now, while cross-vendor protocol adoption remains uncertain.

Implementability score: 0.73

Core sources:
- [CARI](https://arxiv.org/abs/2610.38799v1)
- [PCM paper](https://arxiv.org/abs/2610.39109v1)
- [PCM protocol repository](https://github.com/Cygnux-Labs/PCM-protocol)

## 3. Bind workload identity and bound discovery data at the gateway

GitHub's server-to-server Copilot support moves autonomous services toward workload-owned identity with short-lived installation tokens, organization attribution, model policy, budgets, and independent revocation. MCP Gateway Registry 1.35.0 adds on-behalf-of token exchange with audience checks, bounded registrant metadata, reserved-header stripping, and health-aware routing.

Why it matters: borrowing a human token collapses principal, workload, and approval boundaries. Unbounded gateway metadata can also become an authority leak or prompt-injection surface.

Fit in the strategy: workload identity, delegated authorization, gateway governance, and bounded capability discovery.

Implementable now:
- use service identities and short-lived tokens for autonomous workloads;
- validate audience, issuer, tenant, and beneficiary at the gateway;
- project only named metadata fields into model context;
- strip reserved identity headers and remove unhealthy resources from discovery.

Weakest point: the gateway release includes operational migration work and is not independent benchmark evidence. Identity and metadata controls still need local threat modeling and regression tests.

Implementability score: 0.91

Core sources:
- [GitHub Copilot server-to-server authentication](https://github.blog/changelog/2026-10-27-github-copilot-supports-server-to-server-authentication/)
- [MCP Gateway Registry 1.35.0](https://github.com/agentic-community/mcp-gateway-registry/releases/tag/1.35.0)

## 4. Preserve refusal, escalation, and review as first-class outcomes

The escalation study found that blocked agents often had enough evidence to identify an impasse but kept spending budget. FavorBench showed that locally permitted peer cooperation can bypass the intended review path. Both failures come from treating completion as the only successful terminal state.

Why it matters: sovereign systems must preserve organizational intent under pressure. A valid outcome may be blocked, needs review, unsupported, or cannot determine.

Fit in the strategy: budget governance, ownership workflows, escalation contracts, and release state.

Implementable now:
- add typed blocked and needs-review states;
- require owner, initiator, beneficiary, and approval path on shared-resource effects;
- stop budget consumption after an evidence threshold for impasse is met;
- test peer cooperation for review bypasses.

Weakest point: escalation thresholds can become an avoidance mechanism. Audit false escalations and require evidence for the claimed blocker.

Implementability score: 0.78

Core sources:
- [Escalation study](https://arxiv.org/abs/2610.31895v1)
- [FavorBench](https://arxiv.org/abs/2610.31985v1)

## Working conclusion

Keep evidence broad and authority narrow. Runtime state decides which effects are legal, workload identity decides who may request them, proof binds claims to source-owned events, and explicit refusal states prevent completion pressure from bypassing policy.
