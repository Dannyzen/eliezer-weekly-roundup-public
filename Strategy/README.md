# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Week ending 2026-06-26

### Authority manifests and revocable capabilities define agent scope

Summary: Agent authority is becoming manifest-shaped. AgentRiskBOM, PORTICO, LedgerAgent, and GitHub issue-field MCP support make autonomy, tool access, credential scope, memory scope, approval gates, revocation, and external effects machine-readable and diffable.

Analysis: [weekly sovereignty analysis](2026-06-26/sovereignty.md#authority-manifests-and-revocable-capabilities-define-agent-scope)
Durable topics: [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [AgentRiskBOM](https://arxiv.org/abs/2606.21877v1), [PORTICO / Lingering Authority](https://arxiv.org/abs/2606.22504v1), [LedgerAgent](https://arxiv.org/abs/2606.20529), [GitHub issue fields MCP support](https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues)
Implementable now:
- define a JSON Schema authority manifest for every agent workflow
- fail CI when tools, credentials, memory scopes, delegation rights, or external effects expand without review
- issue scoped capability handles and close them when subtasks end
- log grant, invoke, close, deny, policy epoch, and affected resource in the same trace
Tools, repos, and methodologies worth exploring:
- JSON Schema or Cue manifests, scoped capability handles, OPA or Cedar over manifest fields, GitHub issue fields as guarded work-state, deployment mutation diff detectors
Implementability score: 0.81

### Memory becomes a policy-bearing authority object

Summary: Persistent memory can carry authority after a session ends. Origin-bound memory authority and governed shared memory make memory records policy-bearing objects with origin, scope, derivation, expiration, elevation rules, and direct-read controls.

Analysis: [weekly sovereignty analysis](2026-06-26/sovereignty.md#memory-becomes-a-policy-bearing-authority-object)
Durable topics: [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Shared-State Agents](shared-state-agents/shared-state-agents.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core sources: [Securing LLM-Agent Long-Term Memory Against Poisoning](https://arxiv.org/abs/2606.24322v1), [MEM-INV-Bench / TMA-NM](https://github.com/yedidel/mem-inv-bench), [Governed Shared Memory](https://arxiv.org/abs/2606.24535), [ESAA-Conversational](https://arxiv.org/abs/2606.23752)
Implementable now:
- add origin principal, source event, authority tier, scope, derivation, expiration, and elevation policy to memory records
- route semantic memory search and direct memory reads through the same policy gate
- require elevation before a memory can authorize tool use or external effects
- test laundering, stale propagation, contradiction persistence, direct-ID scope bypass, and derivation reconstruction
Tools, repos, and methodologies worth exploring:
- MEM-INV-Bench fixtures, memory authority metadata, vector-search policy gates, append-only memory event logs, supersession records, contradiction tests
Implementability score: 0.68

### Instructions and tool catalogs need external policy gates

Summary: Natural-language instructions and MCP tool descriptions are policy inputs, not enforcement. Autoformalized Cedar policies, ShareLock, ToolPrivBench, and Agentic Resource Discovery show that serious agent gateways need deterministic policy engines, set-level tool analysis, least-privilege tests, and governed discovery.

Analysis: [weekly sovereignty analysis](2026-06-26/sovereignty.md#instructions-and-tool-catalogs-need-external-policy-gates)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md)
Core sources: [Autoformalization of Agent Instructions into Policy-as-Code](https://arxiv.org/abs/2606.26649v1), [Sondera Harness](https://github.com/sondera-ai/sondera-harness-python), [ShareLock](https://arxiv.org/abs/2606.27027v1), [ToolPrivBench](https://arxiv.org/abs/2606.20023v1), [Agentic Resource Discovery](https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/)
Implementable now:
- put Cedar or OPA in front of one privileged agent tool
- compile natural-language rules into explicit action, resource, principal, context, and data-class fields
- inspect enabled-tool sets and update epochs, not only individual MCP tool records
- separate capability relevance score from trust score during discovery
Tools, repos, and methodologies worth exploring:
- Cedar, Sondera Harness, MCP catalog diffing, enabled-tool graph analysis, least-privilege paired-tool tests, ARD-style registries, canary MCP clients
Implementability score: 0.70

### Mutation and safety move below the prompt

Summary: Phoenix and the Unfireable Safety Kernel point at the same deployment rule: agents can propose actions, but external state machines, reference monitors, fail-closed kernels, signed evidence, and scoped credentials should decide whether side effects occur.

Analysis: [weekly sovereignty analysis](2026-06-26/sovereignty.md#mutation-and-safety-move-below-the-prompt)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core sources: [Phoenix](https://arxiv.org/abs/2606.20243v1), [The Unfireable Safety Kernel](https://arxiv.org/abs/2606.26057v1), [Can Trustless Agents Be Trusted?](https://arxiv.org/abs/2606.26028v1), [PORTICO / Lingering Authority](https://arxiv.org/abs/2606.22504v1)
Implementable now:
- route issue-to-PR work through labels, issue fields, baseline tests, post-patch comparison, branch protection, and role separation
- wrap one high-risk tool with an external reference monitor
- remove standing write credentials where possible and mint scoped credentials only after policy approval
- reject direct mutation identities when a broker path is required
Tools, repos, and methodologies worth exploring:
- GitHub label state machines, branch protection, baseline/post-patch CI comparison, external reference monitors, signed action certificates, workload identity, short-lived credentials, fail-closed timeout policy
Implementability score: 0.61

## Supporting recent Strategy context

The 2026-06-24 Deep Dive Wednesday update remains the strongest durable Strategy addition this week: [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md). The 2026-06-26 weekly synthesis folds that memory-authority model into the broader authority-manifest and policy-gate stack.
