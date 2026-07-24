# Strategy Daily Sovereignty - 2026-07-24

## Verdict

Protocol and observability defaults are becoming governance surfaces. The MCP release candidate removes hidden transport sessions and adds conformance gates; AgentCore puts each agent's complete telemetry under one access and encryption boundary.

The useful rule is not to adopt vendor defaults blindly. Make application state explicit, then bind every request and every trace to the same agent identity and policy scope.

## Scan boundary

- The MCP 2026-07-28 release candidate is available before the July 28 final specification. GitHub announced production support on 2026-07-23.
- The draft specification, official conformance suite, official Go SDK, and GitHub MCP Server were inspected read-only. All have populated default branches; no source was cloned or executed.
- AWS announced AgentCore unified observability on 2026-07-23. The launch page and developer guide agree on the per-agent log-group path, migration flag, and ADOT requirement.
- NotebookLM remained disabled and untouched.

## Stateless MCP makes application state explicit and conformance testable

Core sources: [MCP release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/), [draft specification](https://modelcontextprotocol.io/specification/draft), [conformance suite](https://github.com/modelcontextprotocol/conformance), [GitHub implementation note](https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification)

Release state: candidate available now; final specification scheduled for 2026-07-28. GitHub support announced 2026-07-23.

### What changed

The new core removes `initialize`, `initialized`, and protocol-managed sessions. Version, client information, and capabilities move into each request. Stateful applications must return explicit handles such as browser or basket IDs and receive them back as normal tool arguments.

Required `Mcp-Method` and `Mcp-Name` headers let gateways route, rate-limit, log, and scan requests without parsing the body. Catalog reads gain `ttlMs` and `cacheScope`. W3C trace context receives fixed metadata names. Long-running tasks and MCP Apps move into opt-in extensions, and tool schemas expand to full JSON Schema 2020-12.

The governance change matters as much as the transport change. Standards-track features now require matching conformance scenarios. The public conformance repository has a populated 292-entry main tree and supports client, server, auth, metadata, extension, back-compatibility, and draft suites. GitHub's MCP Server has already removed Redis session traffic and adopted header-level inspection through the official Go SDK.

This is a breaking release candidate, not a stable final target. Explicit handles also expose state to the model, so authorization, tenant scope, expiry, and target binding must travel with the handle rather than disappear with protocol sessions.

### Why it matters

Hidden session affinity made scaling and policy attribution operationally expensive. Stateless requests improve routing and observability, but they also force applications to own state identity directly. That is healthier only if handles are scoped, revocable, and auditable.

### Fit in the stack

- **Gateway governance:** route and enforce policy from explicit operation headers and principal metadata.
- **Execution control:** bind every state handle to tenant, resource, action class, expiry, and policy version.
- **Observability:** propagate one trace through host, client, server, and downstream tools.
- **Release governance:** require conformance scenarios before protocol features become authoritative.

### Implementable now

1. Run the official draft conformance suite against a staging client and server.
2. Inventory every dependency on `initialize`, `Mcp-Session-Id`, sticky routing, and Redis session state.
3. Replace ambient session state with typed handles carrying tenant, scope, expiry, and revocation metadata.
4. Validate body and `Mcp-Method` or `Mcp-Name` agreement at the gateway.
5. Preserve compatibility until the final July 28 specification and Tier 1 SDK support are verified.

Tools and methodologies worth exploring:

- MCP conformance suite, official Go SDK, GitHub MCP Server, JSON Schema 2020-12, W3C Trace Context, contract tests, state-handle threat modeling

Implementability score: **0.90**

The tests and reference implementations are public and current. The score stays below 1.0 because this is a breaking release candidate and application-state migration is real work.

## Per-agent telemetry should share one access and encryption boundary

Core sources: [AWS launch](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/), [AgentCore observability guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html)

Release date: 2026-07-23.

### What changed

AgentCore now sends traces, prompts, structured logs, and standard output to one per-agent CloudWatch log group: `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>`. Previously, spans went to shared `aws/spans` while prompts and event logs went elsewhere.

The unified destination lets IAM policy, customer-managed encryption keys, export subscriptions, and retention apply at agent granularity. New agents created from 2026-07-20 use the destination by default in supported regions. Existing agents can opt in with `UNIFIED_TRACES_DESTINATION_ENABLED=true` and ADOT 0.17.1 or later.

The convenience has a direct privacy cost: prompts, inputs, outputs, traces, and stdout now sit together. A broader single reader or export can expose the full run. Per-agent grouping improves isolation only when IAM, CMK, retention, redaction, and export policy are actually narrower than the old shared arrangement.

### Why it matters

Trace correlation and data governance should use the same runtime identity. Splitting one run across shared and resource-specific stores makes incident response, deletion, encryption, and least privilege harder to prove.

### Fit in the stack

- **Runtime governance:** one agent identity owns traces, prompts, logs, and stdout.
- **Observability:** correlate spans and events without cross-log reconstruction.
- **Privacy:** scope access, encryption, retention, and export to one agent boundary.
- **Multi-agent systems:** keep worker histories separate while preserving shared trace context.

### Implementable now

1. Inventory existing AgentCore runtimes and current span destinations.
2. Define IAM, CMK, retention, redaction, and subscription policy before migration.
3. Upgrade ADOT and enable unified traces on one staging agent.
4. Verify prompt, tool, memory, gateway, identity, and stdout correlation under one trace ID.
5. Test that one agent's operator and exporter cannot read another agent's log group.

Tools and methodologies worth exploring:

- CloudWatch per-agent log groups, ADOT 0.17.1+, W3C Trace Context, IAM access analyzer, CMK policies, retention tests, OpenTelemetry export

Implementability score: **0.92**

The feature is available and the migration path is explicit. The remaining work is policy design and privacy verification, not missing infrastructure.

## Working conclusion

Remove hidden protocol state, but do not remove state governance. Bind explicit handles, request headers, conformance results, and telemetry to one agent identity with scoped access, expiry, and trace evidence.
