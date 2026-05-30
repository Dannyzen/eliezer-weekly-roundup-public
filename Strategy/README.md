# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-30 Daily Scan

### NSA’s MCP guidance makes gateway mediation non-optional
Summary: NSA’s MCP security guidance frames MCP as production automation infrastructure with systemic risks around dynamic tool invocation, implicit trust, context sharing, serialization, approval, tokens, audit logs, output poisoning, and execution.

Analysis: [daily sovereignty analysis](2026-05-30/sovereignty.md#nsas-mcp-guidance-makes-gateway-mediation-non-optional)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [NSA MCP security release](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/)
Implementable now:
- put MCP behind identity, scope, approval, validation, logging, and sandbox policy;
- constrain tool execution and chained output pipelines;
- scan for exposed or vulnerable MCP servers;
- track MCP vulnerabilities as runtime infrastructure risk.
Tools, repos, and methodologies worth exploring:
- MCP gateways, MCP Inspector, OPA/Cedar, OAuth/OIDC scope review, OpenTelemetry, audit logs, local MCP scanners, parameter allowlists, sandboxed execution
Implementability score: 0.78

### Batch-invariant inference is a runtime governance issue
Summary: MarginGate shows that temperature-zero BF16 inference can change under batching. Agent audits and evals need serving metadata and determinism policy, not only prompt/model logs.

Analysis: [daily sovereignty analysis](2026-05-30/sovereignty.md#batch-invariant-inference-is-a-runtime-governance-issue)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [MarginGate](https://arxiv.org/abs/2605.30218v1)
Implementable now:
- record precision, batch mode, model build, decoding settings, and verifier policy;
- run solo-vs-batch determinism tests;
- reserve deterministic serving for eval baselines, approvals, and audits.
Tools, repos, and methodologies worth exploring:
- vLLM/TGI/llama.cpp serving telemetry, deterministic replay suites, batch/solo A-B tests, logit-margin monitors, eval-run pinning, OpenTelemetry trace fields
Implementability score: 0.55

### Structured MCP knowledge tools raise the bar for data sovereignty
Summary: `mcp-proto-okn` is useful because it exposes structured knowledge through discovery, schema inspection, constrained query execution, ontology expansion, identifier bridging, and transcripts. That is the right data-tool shape if the gateway owns policy.

Analysis: [daily sovereignty analysis](2026-05-30/sovereignty.md#structured-mcp-knowledge-tools-raise-the-bar-for-data-sovereignty)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [mcp-proto-okn paper](https://arxiv.org/abs/2605.30283v1), [sbl-sdsc/mcp-proto-okn](https://github.com/sbl-sdsc/mcp-proto-okn)
Implementable now:
- keep structured MCP data tools read-only by default;
- log graph IDs, schema snapshots, generated queries, result counts, and transcript hashes;
- enforce graph-level and field-level scopes before query execution.
Tools, repos, and methodologies worth exploring:
- FastMCP, SPARQL gateways, data catalogs, schema registries, graph-level RBAC, query allowlists, transcript hashing, provenance tables
Implementability score: 0.70

## Previous structured update

The prior Friday synthesis for 2026-05-29 focused on agent gateways as control plane, latent/shared state as sovereignty boundary, deployment-shaped safety governance, and sandbox/data-flow budgets: [2026-05-29 synthesis](../roundups/2026-05-29.md).
