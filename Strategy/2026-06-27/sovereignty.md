# Strategy daily scan, 2026-06-27

## Thesis

The strategic signal today is that agent scale has hard ceilings unless the control plane measures shared failure and governs tool catalogs before execution. More models, more agents, and more plugins are not automatically resilience. They can amplify correlated failure or hide authority inside unreviewed surfaces.

The useful strategy is evidence-first orchestration: measure where alternatives fail together, and gate what the agent is allowed to discover or install before the loop begins.

## Co-failure ceilings make model routing evidence-first

Core source: https://arxiv.org/abs/2606.27288v1

When Does Combining Language Models Help? introduces a simple but sharp constraint for model routers, voting systems, cascades, and mixture-of-agents systems: if every candidate model is wrong on the same query, no policy that outputs one member model's answer can beat that all-wrong rate. The paper calls this the co-failure ceiling.

The practical metric is beta: the rate where all models in the ensemble fail together. The paper argues that average pairwise error correlation is not enough because distributions with the same marginals and pairwise correlations can have different all-wrong tails. Across 67 frontier models from 21 providers, the observed all-wrong tail was materially underpriced by a Gaussian-copula estimate, including open-ended math beta of 0.052 versus 0.023 predicted, and execution-graded code beta of 0.079.

Why it matters: model-router strategy often assumes that enough providers plus voting will beat a strong single model. This paper says the first question should be whether the candidate set fails on different questions. If the all-wrong tail is large, orchestration cannot recover by voting harder.

How it fits into the strategic layer:

- Model-router governance: beta becomes a pre-deployment evidence field before training or buying a router.
- Evaluation: benchmark the all-wrong tail per task family, not only average model scores.
- Procurement: heterogeneous vendors help only if their failure sets differ on the actual work.
- Runtime policy: route when there is a strong query-level signal; otherwise the best single model may be cheaper and safer.

Practical tools, repos, and methodologies worth exploring now:

- Build a small task panel for each workflow class, then score every candidate model on the exact same items.
- Compute beta, best-model accuracy, oracle accuracy, pairwise overlap, and router headroom before adding a router.
- Log route reason and expected headroom per task class.
- Prefer heterogeneity that reduces shared failures, not cosmetic provider diversity.
- Use the co-failure ceiling as a kill criterion for expensive mixture-of-agents designs.

Implementability score: 0.77

The measurement is implementable now with ordinary eval harnesses. The strategic hard part is organizational: teams need to stop treating multi-model orchestration as a default upgrade and require evidence that the router has headroom.

## Tool catalogs need source allowlists and set-level poisoning tests

Core sources: https://arxiv.org/abs/2606.27027v1 and https://github.blog/changelog/2026-06-25-enterprise-managed-settings-now-support-strictknownmarketplaces-in-vs-code-and-the-cli

ShareLock showed the research-side risk on 2026-06-25: MCP poisoning can be distributed across multiple benign-looking tool descriptions and reconstructed only when enough tools are enabled together. GitHub's new enterprise-managed `strictKnownMarketplaces` setting is the product-side counter-signal: enterprises can now restrict Copilot CLI and VS Code plugin installation to explicitly allowed marketplaces.

The two sources point at the same governance boundary. Tool and plugin catalogs are not neutral menus. They are pre-execution authority surfaces. If an agent or developer can install plugins from untrusted marketplaces, or if an MCP client enables tool sets without set-level inspection, the agent can inherit malicious instructions before any runtime policy sees an action.

Why it matters: the old review model checks one tool, one plugin, or one server at a time. That is not enough for multi-tool poisoning and marketplace sprawl. The control plane needs both source-level admission and enabled-set analysis.

How it fits into the strategic layer:

- Agent gateway governance: inspect tool catalogs as sets, with update epochs and publisher trust.
- Runtime governance: bind installed plugins, enabled MCP servers, and marketplace sources into the run manifest.
- Enterprise policy: restrict installation surfaces before untrusted tools become prompt context.
- Audit: record catalog version, marketplace source, enabled set, and denied combinations in traces.

Practical tools, repos, and methodologies worth exploring now:

- Enable `strictKnownMarketplaces` for Copilot CLI and VS Code where GitHub Enterprise policy is available.
- Maintain an allowed-source list for MCP servers, plugins, and skills.
- Diff tool descriptions at every server update.
- Fuzz enabled-tool subsets for reconstructed malicious intent or unexpected instruction composition.
- Separate relevance ranking from trust ranking in tool discovery.

Implementability score: 0.82

Marketplace allowlisting is highly implementable where the enterprise control exists. Set-level poisoning analysis is harder, but a first pass can be built with catalog diffs, allowlists, update epochs, and adversarial fixtures.

## Working conclusion

The strategy lesson today is to reject scale as a substitute for evidence. Multi-model systems need measured non-overlap before routing. Tool-rich systems need catalog policy before execution. If those controls are absent, adding more models or tools mostly creates a larger place for correlated failure and hidden authority to live.