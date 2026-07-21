# Strategy Weekly Sovereignty - 2026-07-17

## Weekly thesis

This week's strategy signal is that agent sovereignty depends on runtime ownership of boundaries. The model may propose an identity, plan, permission, or connection. The runtime must resolve it, authorize it, mediate it, and preserve a receipt.

The tempting default is to trust framework labels such as approved, cancelled, secure, or private. The real cost is that those labels can coexist with unverified packages, stale authority, sibling effects, orphaned work, and broad network reach.

> Choose runtime-owned boundary objects. You gain inspectable and replayable authority, but give up framework convenience and take on schemas, interceptors, state storage, and operational drills.

## Exact identity and deterministic admission belong before execution

Three independent signals point to the same preflight control.

[Skills That Don't Exist](https://arxiv.org/abs/2607.12340v1) measured 15,000 prompts across 12 configurations. Every configuration hallucinated skill names, with average rates of 36.0 percent for standalone models and 36.9 percent for agents, rising to 43.1 percent on developer questions. Retrieval grounding cut one rate from 40.8 to 3.2 percent, but the best defended system still recommended the correct skill only about one time in six.

[Setup Complete, Now You Are Compromised](https://arxiv.org/abs/2607.15143v1) shows that ordinary setup documentation can redirect coding agents to wrong names, vulnerable versions, or hostile registries. The 12-scenario, five-attack-class study found that safety depends on the harness-model pair and that source redirection is missed broadly. Its proposed deterministic pre-install check resolves names, sources, and versions before any package code runs.

GitHub's [CodeQL 2.26.0](https://github.blog/changelog/2026-07-10-codeql-2-26-0-adds-kotlin-2-4-0-support-and-ai-prompt-injection-detection) adds a JavaScript and TypeScript system-prompt-injection query. That is the product-side version of the same rule: turn ambiguous model risk into a normal engineering gate before merge or execution.

Implementable controls:

- resolve registry, publisher, repository URL, version, license, hash, and vulnerability state before install;
- deny unapproved registries and unpinned sources;
- fingerprint approved MCP server configuration and require review on drift;
- run CodeQL prompt-injection data-flow checks in CI;
- preserve the resolver decision as a signed or append-only admission receipt.

Tools, repositories, and methodologies worth exploring:

- registry metadata APIs, lockfiles, OSV, Sigstore, SLSA, CodeQL 2.26.0, Cedar or OPA, approved-catalog manifests

Evidence caveat: the setup-attack paper's advertised benchmark repository did not resolve. CodeQL's current query is a concrete JavaScript and TypeScript data-flow control, not a complete prompt-injection defense. Registry identity also does not prove publisher trust.

Implementability score: 0.90

## Permission must survive until the final effect

Approval at plan time is not authority at commit time.

[Temporary Authority, Permanent Effects](https://arxiv.org/abs/2607.10487v1) tested browser, API, and multi-agent workflows whose earlier authority was invalidated before durability. In the primary matrix, 262 of 270 runs reached the visible result, but only 55 were authorized completions. Among 216 invalidating rows, 207 still committed after the authorizing path had failed.

[Stop Means Stop](https://arxiv.org/abs/2607.14166v1) tests approval, cancellation, timeout, and replay semantics across six open-source frameworks. All six violated the implied barrier contract, and 215 of 1,200 live-model runs executed an effect during an approval pause. Its SOUNDGATE design puts hold, rejection, replay deduplication, cancellation fencing, and environment-external mediation below the agent framework.

[CAVA](https://arxiv.org/abs/2607.13716v1) adds a useful representation: canonicalize heterogeneous runtime records into one action identity so approval and evidence bind to the same effect across tools, browsers, gateways, and workflow engines.

A credible effect boundary needs:

- one canonical effect fingerprint;
- fresh, causally prior, effect-bound authority;
- hold-until-decided semantics;
- idempotency and replay deduplication;
- cancellation and timeout fencing;
- structural mediation of the protected effect path;
- a final-effect receipt.

Tools, repositories, and methodologies worth exploring:

- durable outbox patterns, append-only receipts, egress proxies, network namespaces, idempotency keys, TLA+, Verus, Loom, policy epochs

Evidence caveat: the two strongest enforcement papers are fresh and not independently replicated. SOUNDGATE's source repository did not resolve in this scan; only PyPI package metadata was verified. Complete mediation remains the hard systems requirement.

Implementability score: 0.68

## Gateways and durable workflows are becoming the governance plane

Connectivity and durability are no longer plumbing details. They determine where identity, policy, and evidence can be enforced.

[LiteLLM 1.92.0](https://docs.litellm.ai/release_notes/v1.92.0/v1-92-0) adds production MCP OAuth On-Behalf-Of discovery, persisted Dynamic Client Registration, per-server concurrency limits, catalog search, credential hardening, and a Google Distributed Cloud provider. This makes delegated MCP identity a gateway lifecycle rather than a secret pasted into an agent.

The [OpenBox and Temporal integration](https://www.prnewswire.com/news-releases/as-enterprises-move-ai-agents-into-production-openbox-ai-and-temporal-introduce-runtime-governance-for-long-running-agents-302820622.html) combines durable workflow execution with runtime authorization, approvals, attestations, and audit claims. The [SDK repository](https://github.com/OpenBox-AI/openbox-temporal-sdk-python) is populated, licensed, and released, although the July integration claims remain vendor-reported rather than independently benchmarked.

[Anthropic MCP Tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) adds outbound-only private MCP connectivity, inner TLS, upstream IP restrictions, workload identity, certificate lifecycle, and separate upstream OAuth. The security model is explicit, but so are the costs: research-preview access, no uptime or continuity commitment, Cloudflare transport dependence, token and private-key custody, certificate rotation, and network-policy ownership.

The adoption order should be:

1. centralize remote MCP identity and catalog policy;
2. move long-running work onto a durable workflow substrate;
3. attach authorization and receipts to workflow activities;
4. expose private servers only through outbound-only transport and narrow routes;
5. rehearse revocation, rotation, cancellation, recovery, and teardown.

Tools, repositories, and methodologies worth exploring:

- LiteLLM, Temporal, OpenBox, Anthropic MCP Tunnels, OAuth token exchange, workload identity federation, mTLS, Kubernetes NetworkPolicy, certificate rotation

Evidence caveat: LiteLLM is a large fast-moving gateway, OpenBox's integration claims are vendor-authored, and Anthropic MCP Tunnels are access-gated research preview with third-party transport dependency.

Implementability score: 0.74

## Strategic implication

The sovereign stack is not the stack with the most self-hosted components. It is the stack where every promotion boundary has an owner:

| Boundary | Runtime owner | Required proof |
| --- | --- | --- |
| Artifact admission | registry and policy gate | exact identity and admission receipt |
| Permission to effect | execution-control broker | fresh authority and final-effect receipt |
| Delegated connectivity | gateway and network plane | principal, route, credential, rotation evidence |
| Long-running work | durable workflow engine | state, retry, approval, cancellation, audit trail |

If an effect can bypass the object that records approval, the approval is interface theater, not control.
