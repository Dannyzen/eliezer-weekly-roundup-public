# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-27

### Co-failure ceilings make model routing evidence-first

Summary: Multi-model orchestration only helps when candidate models fail on different questions. The co-failure ceiling makes the all-wrong rate, beta, a pre-deployment evidence field for routers, voting systems, cascades, and mixture-of-agents designs.

Analysis: [daily sovereignty analysis](2026-06-27/sovereignty.md#co-failure-ceilings-make-model-routing-evidence-first)
Durable topics: [Model Router Governance](model-router-governance/model-router-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core source: [When Does Combining Language Models Help?](https://arxiv.org/abs/2606.27288v1)
Implementable now:
- score every candidate model on the same internal task panel
- compute all-wrong beta, best-model accuracy, oracle accuracy, and route headroom
- require a query-level routing signal before adding expensive model-router complexity
- log route reason, expected headroom, and fallback outcome by task class
Tools, repos, and methodologies worth exploring:
- paired eval panels, beta/all-wrong analysis, oracle upper-bound analysis, router headroom reports, task-family routing traces
Implementability score: 0.77

### Tool catalogs need source allowlists and set-level poisoning tests

Summary: Tool and plugin catalogs are pre-execution authority surfaces. ShareLock shows MCP poisoning can be distributed across multiple benign-looking tool descriptions, while GitHub's `strictKnownMarketplaces` gives enterprises a practical source-allowlist control for Copilot CLI and VS Code plugins.

Analysis: [daily sovereignty analysis](2026-06-27/sovereignty.md#tool-catalogs-need-source-allowlists-and-set-level-poisoning-tests)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md)
Core sources: [ShareLock](https://arxiv.org/abs/2606.27027v1), [GitHub strictKnownMarketplaces](https://github.blog/changelog/2026-06-25-enterprise-managed-settings-now-support-strictknownmarketplaces-in-vs-code-and-the-cli)
Implementable now:
- enable `strictKnownMarketplaces` where GitHub Enterprise policy is available
- maintain allowed-source lists for MCP servers, plugins, and skills
- diff tool descriptions at every MCP server update
- fuzz enabled-tool subsets for reconstructed malicious intent
Tools, repos, and methodologies worth exploring:
- enterprise-managed Copilot settings, marketplace allowlists, MCP catalog diffing, enabled-tool graph analysis, set-level poisoning fixtures, update-epoch traces
Implementability score: 0.82

## Supporting recent Strategy context

The 2026-06-26 weekly synthesis remains the broad current governance map: [weekly sovereignty analysis](2026-06-26/sovereignty.md). The new 2026-06-27 daily scan tightens two decision gates: prove model-router headroom before orchestration, and govern catalog sources before tools enter context.
