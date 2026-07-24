# Strategy

This index tracks the most recent structured update. Each finding includes a summary, a link into the detailed analysis, core sources, practical implementation paths, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday, 2026-07-24

### Stateless MCP makes application state explicit and conformance testable

Summary: The MCP 2026-07-28 release candidate removes protocol sessions and initialization, adds routable operation headers, cache scope, fixed trace propagation, formal extensions, and full JSON Schema 2020-12. State moves into explicit application handles, where scope and revocation become application responsibilities.

Analysis: [daily sovereignty analysis](2026-07-24/sovereignty.md#stateless-mcp-makes-application-state-explicit-and-conformance-testable)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md#july-24-update-stateless-mcp-moves-state-governance-into-explicit-handles)
Core sources: [release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/), [draft specification](https://modelcontextprotocol.io/specification/draft), [conformance suite](https://github.com/modelcontextprotocol/conformance)
Implementable now:
- run the official draft conformance suite in staging;
- inventory session and sticky-routing dependencies;
- bind explicit handles to tenant, resource, scope, expiry, and revocation;
- validate operation headers against request bodies.
Tools, repositories, and methodologies:
- MCP conformance suite, official SDKs, GitHub MCP Server, JSON Schema 2020-12, W3C Trace Context, contract tests
Implementability score: 0.90

### Per-agent telemetry should share one access and encryption boundary

Summary: AgentCore now sends traces, prompts, structured logs, and stdout to one per-agent CloudWatch log group. Correlation and policy become simpler, but concentrated run data requires tighter IAM, encryption, retention, redaction, and export controls.

Analysis: [daily sovereignty analysis](2026-07-24/sovereignty.md#per-agent-telemetry-should-share-one-access-and-encryption-boundary)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md#july-24-update-telemetry-needs-a-per-agent-policy-boundary)
Core sources: [AWS launch](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/), [developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html)
Implementable now:
- define IAM, CMK, retention, redaction, and export policy;
- upgrade ADOT and migrate one staging runtime;
- correlate prompt, tool, memory, identity, and stdout events;
- prove cross-agent log isolation.
Tools, repositories, and methodologies:
- CloudWatch, ADOT 0.17.1+, W3C Trace Context, IAM Access Analyzer, CMK policy tests, OpenTelemetry export
Implementability score: 0.92

## Current implication

Protocol state and telemetry should be explicit policy objects. Bind state handles, request operations, conformance results, and run evidence to one agent identity rather than relying on hidden sessions or shared log stores.
