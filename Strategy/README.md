# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday synthesis, week ending 2026-07-03

### Execution control becomes the layer below MCP-style connectivity

Summary: HCP, ContextNest, and UnderSpecBench converge on the same strategic correction: connection is not authority. Agent runtimes need principals, grants, targets, scopes, context eligibility, side-effect oracles, and audit trails below the chat surface.

Analysis: [weekly sovereignty analysis](2026-07-03/sovereignty.md#execution-control-becomes-the-layer-below-mcp-style-connectivity)
Durable topics: [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core sources: [HCP paper](https://arxiv.org/abs/2606.29073v1), [HCP repo](https://github.com/SymbolicLight-AGI/handle-capability-protocol), [ContextNest](https://arxiv.org/abs/2607.02116v1), [UnderSpecBench](https://arxiv.org/abs/2607.02294v1)
Implementable now:
- model principals, resources, grants, capabilities, handles, policies, and audit entries explicitly
- reject tool metadata as authority
- require target and scope fields before mutation
- treat approvals as durable grant creation
Tools, repos, and methodologies worth exploring:
- HCP, ContextNest, principal binding, capability handles, data-flow authorization, deterministic side-effect oracles
Implementability score: 0.76

### Persistent-state codebases make monitors stateful

Summary: Persistent repositories let an agent distribute a covert objective across time. Diff-local review is not enough; defenders need PR-sequence ledgers, link tracking, and monitor ensembles.

Analysis: [weekly sovereignty analysis](2026-07-03/sovereignty.md#persistent-state-codebases-make-monitors-stateful)
Durable topics: [Persistent-State Agent Control](persistent-state-agent-control/persistent-state-agent-control.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core sources: [persistent-state paper](https://arxiv.org/abs/2607.02514v1), [persistent-state eval repo](https://github.com/josh-hills/control-arena-persistent-state-eval), [ControlArena](https://github.com/UKGovernmentBEIS/control-arena)
Implementable now:
- maintain a PR-sequence risk ledger
- preserve suspicious warnings across PRs
- track dormant hooks, repeated sensitive-file touches, and delayed activation paths
- combine diff, trajectory, accumulated-history, and link-tracker monitors
Tools, repos, and methodologies worth exploring:
- ControlArena, persistent-state eval, stateful link trackers, monitor ensembles, cross-PR adversarial fixtures
Implementability score: 0.68

### Tool catalogs and tool arguments become authority boundaries

Summary: Plugin marketplaces, tool catalogs, and tool arguments are now authority surfaces. GitHub strictKnownMarketplaces, ToolPrivacyBench, prompt-injection inseparability, and skill supply-chain manifests all point toward allowlists, provenance, purpose-bound arguments, and catalog diffing.

Analysis: [weekly sovereignty analysis](2026-07-03/sovereignty.md#tool-catalogs-and-tool-arguments-become-authority-boundaries)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md)
Core sources: [strictKnownMarketplaces](https://github.blog/changelog/2026-06-25-enterprise-managed-settings-now-support-strictknownmarketplaces-in-vs-code-and-the-cli), [ToolPrivacyBench](https://arxiv.org/abs/2606.28061v1), [instruction/data inseparability](https://arxiv.org/abs/2606.27567v1), [skill manifests](https://arxiv.org/abs/2607.01136v1)
Implementable now:
- enforce approved marketplaces or plugin registries
- record source, owner, version, permissions, and expected side effects for each capability
- classify tool arguments by purpose and data sensitivity
- fuzz tool sets for split-instruction and threshold-poisoning behavior
Tools, repos, and methodologies worth exploring:
- marketplace allowlists, tool-argument policy, catalog diffing, skill lockfiles, tool-set poisoning tests
Implementability score: 0.72

### Routing and community governance need evidence, not declarations

Summary: Model routers need failure-correlation evidence, and agent communities need membership, admission, revocation, and audit rules. Self-descriptions and protocol compatibility are not enough.

Analysis: [weekly sovereignty analysis](2026-07-03/sovereignty.md#routing-and-community-governance-need-evidence-not-declarations)
Durable topics: [Model Router Governance](model-router-governance/model-router-governance.md), [Agent Community Governance](agent-community-governance/agent-community-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [co-failure ceiling](https://arxiv.org/abs/2606.27288v1), [capability-tested routing](https://arxiv.org/abs/2606.30555v1), [agent community governance](https://arxiv.org/abs/2606.31498v1)
Implementable now:
- measure pairwise co-failure before enabling routers
- shadow learned routers before online routing
- use capability probes instead of model self-description
- define community membership, capability admission, revocation, and audit records
Tools, repos, and methodologies worth exploring:
- failure-correlation matrices, shadow routers, capability probes, membership policies, revocation records
Implementability score: 0.56

### Context governance becomes sovereignty for RAG and memory

Summary: ContextNest makes the RAG governance lesson concrete: retrieval relevance is not context eligibility. Agents need approved, current, attributable, integrity-verified, and reconstructable context before semantic ranking runs.

Analysis: [weekly sovereignty analysis](2026-07-03/sovereignty.md#context-governance-becomes-sovereignty-for-rag-and-memory)
Durable topics: [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [ContextNest paper](https://arxiv.org/abs/2607.02116v1), [ContextNest repo](https://github.com/PromptOwl/ContextNest), [ContextNest spec](https://github.com/PromptOwl/context-nest-spec)
Implementable now:
- separate approval state from retrieval score
- use deterministic selectors for approved context sets
- hash and checkpoint context versions
- persist context consumption traces with agent outputs
Tools, repos, and methodologies worth exploring:
- ContextNest, contextnest:// URIs, typed Markdown vaults, SHA-256 version chains, graph checkpoints, point-in-time reconstruction
Implementability score: 0.80

## Supporting recent Strategy context

The 2026-07-01 Deep Dive remains the foundation: connection is not authority. The 2026-07-03 weekly synthesis turns that into a broader sovereignty stack: execution grants, state ledgers, trace packets, capability manifests, and monitor ensembles.
