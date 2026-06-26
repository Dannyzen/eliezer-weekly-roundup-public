# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-26

### Agent instructions are becoming policy-as-code

Summary: Autoformalization of Agent Instructions into Policy-as-Code turns prompts, MCP tool definitions, and written policy documents into Cedar policies through a generator-critic loop, then enforces them with an external deterministic policy engine before tool execution.

Analysis: [daily sovereignty analysis](2026-06-26/sovereignty.md#agent-instructions-are-becoming-policy-as-code)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/abs/2606.26649v1)
Implementation artifact: [sondera-ai/sondera-harness-python](https://github.com/sondera-ai/sondera-harness-python)
Implementable now:
- put Cedar or OPA in front of one privileged tool
- compile natural-language rules into explicit action, resource, and context fields
- return deterministic denial reasons to the agent
- log policy ID, input fields, verdict, and final effect with the trace
Tools, repos, and methodologies worth exploring:
- Cedar, Sondera Harness, generator-critic policy compilation, schema hard critics, semantic coverage review, policy-denial recovery loops
Implementability score: 0.76

### ShareLock shows MCP poisoning is a multi-tool problem

Summary: ShareLock splits hidden malicious instructions across multiple benign-looking MCP tool descriptions using threshold sharing. The operational lesson is that MCP security has to inspect enabled-tool sets and update epochs, not only individual tools.

Analysis: [daily sovereignty analysis](2026-06-26/sovereignty.md#sharelock-shows-mcp-poisoning-is-a-multi-tool-problem)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md)
Core source: [ShareLock](https://arxiv.org/abs/2606.27027v1)
Implementable now:
- diff MCP tool descriptions on every server update
- analyze enabled-tool combinations, not just single tool records
- fuzz tool subsets for reconstructed intent and hidden coordination
- record tool catalog version, update epoch, selected tools, and denied combinations in gateway traces
Tools, repos, and methodologies worth exploring:
- MCP catalog scanners, cross-tool prompt-injection classifiers, canary tool bundles, update gates, enabled-tool graph analysis
Implementability score: 0.46

## Supporting recent Strategy context

The 2026-06-24 Deep Dive Wednesday update remains the strongest durable Strategy addition this week: [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md).
