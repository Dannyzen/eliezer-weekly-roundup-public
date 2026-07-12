# Strategy Daily Sovereignty - 2026-07-12

## Daily thesis

Agent sovereignty is moving into gateway and workflow contracts. The strategic boundary is no longer simply which model or cloud runs the task. It is whether identity delegation, tool discovery, sandbox selection, credential custody, failure propagation, and deployment location are explicit control-plane objects.

## LiteLLM v1.92.0 makes delegated MCP identity a gateway feature

LiteLLM v1.92.0 promotes MCP OAuth On-Behalf-Of token exchange onto its v2 resolver. The release adds RFC 9728 to RFC 8414 endpoint discovery instead of identity-provider guessing, persisted Dynamic Client Registration, per-server outbound concurrency limits, and an `mcp_tool_search` virtual tool for large catalogs. It also hardens administrative access, encrypts credentials at rest with AES-256-GCM, redacts secrets from startup and router errors, and adds Google Distributed Cloud Gemini for on-prem and sovereign deployments.

Why it matters:

- remote MCP access needs the user's delegated identity, not a shared gateway super-token;
- discovery, registration, refresh, concurrency, tool search, and audit belong in one gateway lifecycle;
- large tool catalogs need scoped search without dumping every schema into model context;
- on-prem model routing matters only if identity, policy, credentials, and traces can remain under the same operating boundary.

Fit into the strategic layer:

This belongs in agent gateway governance and local-first infrastructure. A serious gateway should bind principal, client, MCP server, resource, token audience, allowed tools, concurrency budget, policy version, and trace sink before a tool call leaves the agent runtime.

Implementable now:

- deploy v1.92.0 only in a lab or staged gateway first, using the signed release image or pinned package;
- configure one remote MCP server with delegated OAuth and verify discovery, Dynamic Client Registration persistence, refresh, revocation, and audit behavior;
- set per-server concurrency and expose only policy-approved tool search results;
- test credential-log redaction and denied administrative routes;
- compare a sovereign GDC route against the same gateway policy and telemetry contract used for hosted providers.

Tools, repositories, and methodologies worth exploring:

- `BerriAI/litellm` v1.92.0;
- OAuth 2.0 On-Behalf-Of token exchange;
- RFC 9728 Protected Resource Metadata and RFC 8414 Authorization Server Metadata;
- per-server MCP concurrency budgets;
- catalog search with authorization filtering before model exposure.

Implementability score: 0.82

Core sources:

- [LiteLLM v1.92.0 release notes](https://docs.litellm.ai/release_notes/v1.92.0/v1-92-0)
- [LiteLLM v1.92.0 GitHub release](https://github.com/BerriAI/litellm/releases/tag/v1.92.0)

Caveat: production-ready in a release note does not make delegated OAuth simple. Token audiences, client registration, refresh, revocation, tenant isolation, and upstream server behavior still need integration tests and operator runbooks.

## Compiled sandbox policy is becoming portable infrastructure

GitHub Agentic Workflows v0.82.8 makes gVisor selection and mount configuration workflow fields, while also surfacing token failures and safe-output completion. Strategically, this is a shift from "the runner is probably isolated" to "the workflow declares its execution substrate and terminal evidence."

Why it matters:

- containment choices can be reviewed, versioned, reused, and compared across workflows;
- authentication failure becomes part of the durable run record;
- AI-authorship disclosure becomes an output contract rather than optional prose;
- transitive workflow imports and lock files become governance artifacts.

Fit into the strategic layer:

This belongs in agent sandboxing and governed workflow substrates. The control plane should compile natural-language or declarative workflows into an exact execution manifest that includes imported dependencies, sandbox backend, mounts, network policy, token scope, output types, and conclusion semantics.

Implementable now:

- create approved sandbox partials for read-only source, writable scratch, and no-secret defaults;
- require compiled lock and import evidence during review;
- fail closed when token checks, threat-detection engines, or safe-output integration fail;
- attach sandbox runtime and mount hashes to the run receipt.

Implementability score: 0.72

Core source:

- [GitHub Agentic Workflows v0.82.8](https://github.com/github/gh-aw/releases/tag/v0.82.8)

Caveat: the release is a prerelease. Portability is still limited by self-hosted runner support and the difference between declaring gVisor and proving effective containment.

## Strategic conclusion

The immediate build target is a gateway-to-runner contract. Delegated identity should arrive at a scoped tool gateway, and the resulting workflow should execute inside a declared sandbox with reviewable mounts and durable failure evidence. Model choice remains replaceable. Identity, containment, and receipts are the strategic moat.
