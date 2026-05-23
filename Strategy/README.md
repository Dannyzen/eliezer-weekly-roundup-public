# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-23 Daily Scan

### KV-cache sharing is an opaque data boundary
Summary: LCGuard shows that multi-agent systems sharing KV caches can leak sensitive inputs through latent state even when no explicit text disclosure occurs. Text-only DLP is not enough once agents share model internals, embeddings, summaries, or compressed state.

Analysis: [daily sovereignty analysis](2026-05-23/sovereignty.md#kv-cache-sharing-creates-an-opaque-data-boundary)
Durable topic: [Agent Network Containment](agent-network-containment/agent-network-containment.md)
Core source: [LCGuard](https://arxiv.org/abs/2605.22786v1)
Implementable now:
- classify KV caches, embeddings, summaries, and compressed memories as governed data artifacts;
- forbid cross-principal latent-state sharing unless provenance, sensitivity, retention, and destination are explicit;
- test reconstruction leakage before enabling latent communication;
- keep latent-channel audit trails linked to text/tool traces.
Tools, repos, and methodologies worth exploring:
- latent-state provenance, adversarial reconstruction tests, data-class labels, cross-principal sharing policy, cache retention controls
Implementability score: 0.42

### Agent security needs whole-run evasion tests plus MCP client telemetry
Summary: A3S-Bench tests temporal, spatial, and semantic evasions that only become dangerous across turns, artifacts, and context. The live MCP clients dataset shows client capabilities vary enough that gateway policy should inventory them instead of treating all MCP clients as equivalent.

Analysis: [daily sovereignty analysis](2026-05-23/sovereignty.md#agent-security-needs-stateful-evasion-tests-plus-live-mcp-client-inventory)
Durable topics: [Agent Network Containment](agent-network-containment/agent-network-containment.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [A3S-Bench](https://arxiv.org/abs/2605.22321v1), [Agent3Sigma-Stage](https://github.com/antgroup/Agent3Sigma-Stage), [MCP clients dataset](https://huggingface.co/datasets/evalstate/mcp-clients)
Implementable now:
- run multi-turn evasion fixtures against staging agents;
- label trace influence paths across turns, files, web pages, memory, and tool outputs;
- scan external artifacts as spatial-evasion carriers;
- inventory MCP client name, version, and advertised capabilities;
- gate UI rendering, elicitation, roots, sampling, tasks, and experimental auth by policy.
Tools, repos, and methodologies worth exploring:
- Agent3Sigma-Stage/A3S-Bench, MCP clients dataset, MCP Inspector, OPA/Cedar policy, canary traces, artifact sandboxes, client-capability allowlists
Implementability score: 0.74

## Previous structured update

The prior Friday synthesis for 2026-05-22 focused on semantic API/MCP admission, memory as authority, managed agent infrastructure, and security coverage maps: [2026-05-22 sovereignty](2026-05-22/sovereignty.md).
