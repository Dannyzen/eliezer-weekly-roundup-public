# Strategy Daily Sovereignty: 2026-10-15

## Scope

This scan combines a fresh arXiv security study first listed on October 15 with an official Google release published October 14. Public repositories and documentation were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Thesis

Agent authority needs controls at two boundaries: installation and invocation. Skill review should measure the capabilities a bundle can reach, while the tool gateway should keep authorization, traffic, and traces beside the systems of record.

## Capability profiling: measure what a skill can reach

Beyond Maliciousness evaluates 6,309 skill listings from two marketplaces using whole-bundle static analysis, dependency provenance checks, instrumented sandbox execution, and separate trace assessment. The study reports evidence of shell execution in half the corpus, filesystem reads in 35%, filesystem writes and network egress in 31% each, and credential access in 13%. Seven in ten listings carried at least one elevated capability.

The sharpest result is the declaration gap. Only 770 of 6,061 listings with parseable frontmatter declared anything, the vocabulary could not express credential or environment access, and 59% of declaring listings understated what their bundle could do. The paper distinguishes capability from malicious intent: 4,431 listings carried elevated capability, while 338 carried a non-benign verdict.

### Why it matters

Marketplace approval cannot rely on author declarations or a malware verdict. A benign skill can still direct an already-privileged agent toward shell, filesystem, network, or credential surfaces.

### Strategy fit

Capability profiling belongs before skill admission. Runtime policy and sandboxing remain necessary because static or detonation evidence describes reachable surface, not safe use.

### Practical tools and methods worth exploring

- Inspect the complete bundle, scripts, opaque assets, dependencies, and referenced accounts.
- Generate a reviewable capability manifest for shell, filesystem, network, environment, and credential reach.
- Compare declared capability to observed or inferred capability and fail closed on understatement.
- Pin the accepted capability surface in version control and block unreviewed drift in CI.
- Detonate representative skills in instrumented sandboxes without preselecting only suspicious artifacts.

### Evidence and caveat

The corpus is a point-in-time sample, marketplace popularity metrics differ, publisher concentration is uneven, and the human-review cohort does not establish a precision estimate. Runtime observations can establish co-occurrence without proving which component originated every behavior.

Implementability score: 0.70

Core sources:
- [paper v1](https://arxiv.org/abs/2610.19264v1)
- [SkilLock capability-surface lockfile project](https://github.com/skills-lock/skil-lock)

## Apigee hybrid: keep MCP traffic inside the governed cluster

Google now supports MCP in Apigee hybrid 1.17.0. An OpenAPI 3.0.x specification becomes an MCP Discovery Proxy: agents use JSON-RPC `tools/list` and `tools/call`, while Apigee handles discovery, protocol translation, authentication, authorization, quotas, and backend access.

The hybrid data plane runs inside the customer's Kubernetes cluster. MCP request traffic stays in the cluster, configuration is pulled from the control plane, and W3C trace context can flow through OpenTelemetry across the client, Apigee proxy, and backend.

### Why it matters

Sovereignty depends on where tool invocation is authorized and observed. Keeping the MCP data plane next to systems of record reduces unnecessary data movement and lets existing API governance become the agent tool boundary.

### Strategy fit

This is a concrete gateway pattern for regulated, on-premises, and multi-cloud estates. It does not remove the need for per-tool least privilege, response filtering, or effect receipts.

### Practical tools and methods worth exploring

- Compile approved OpenAPI operations into a reviewed MCP catalog instead of standing up parallel tool servers.
- Keep MCP ingress reachable only from authorized runtime pods.
- Reuse existing OAuth, mTLS, quota, threat-protection, and audit controls.
- Propagate one trace ID through the AI client, gateway, and backend effect.
- Treat enablement, chart order, canary rollout, and rollback as an approved maintenance change.

### Availability and caveat

The feature is available for Apigee hybrid 1.17.0 and later. It is conditional on an existing Apigee hybrid and Kubernetes estate. Enabling or disabling it triggers a staged canary rollout, and Google documents a required operator-chart-before-org-chart upgrade order.

Implementability score: 0.68

Core sources:
- [Google Developers announcement](https://developers.googleblog.com/en/announcing-mcp-support-in-apigee-hybrid-agentic-tools-that-run-in-your-own-cluster/)
- [Apigee MCP architecture documentation](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview)

## Strategic decision

Require an authority manifest before installation and a governed effect gateway at invocation. The first bounds what a capability may reach. The second proves what it actually did.
