# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-29 Friday Synthesis

### Agent gateways are becoming the real control plane
Summary: MCP servers and generated tools are moving into privileged administration. Governance now means schema pinning, identity, OAuth scope, data-flow controls, mutation approvals, traces, and rollback.

Analysis: [weekly sovereignty analysis](2026-05-29/sovereignty.md#agent-gateways-are-becoming-the-real-control-plane)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [MCP metadata security](https://arxiv.org/abs/2605.24069), [permission laundering](https://arxiv.org/abs/2605.26542), [Tool Forge](https://arxiv.org/abs/2605.28000), [Chrome Enterprise MCP post](https://blog.google/security/bringing-ai-agents-to-chrome-enterprise-security-management/), [Chrome Enterprise MCP repo](https://github.com/google/chrome-enterprise-premium-mcp)
Implementable now:
- pin MCP server/tool identity and schemas;
- validate generated tools before registration;
- split diagnosis from mutation and approval-gate high-blast-radius changes.
Tools, repos, and methodologies worth exploring:
- MCP gateways, MCP Inspector, Tool Forge, Chrome Enterprise Premium MCP, Pocket CEP, OPA/Cedar, OAuth scope review, OpenTelemetry, rollback tests
Implementability score: 0.70

### Latent state and shared state are sovereignty boundaries
Summary: KV caches, memories, summaries, embeddings, and shared clients can influence future actions without appearing as ordinary tool inputs. They need trust zones, provenance, expiry, and rollback semantics.

Analysis: [weekly sovereignty analysis](2026-05-29/sovereignty.md#latent-state-and-shared-state-are-sovereignty-boundaries)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Shared-State Agents](shared-state-agents/shared-state-agents.md)
Core sources: [LCGuard / KV-cache leakage](https://arxiv.org/abs/2605.22786v1), [personalized memory gates](https://arxiv.org/abs/2605.25535), [MemTrace](https://arxiv.org/abs/2605.28732), [zjunlp/MemTrace](https://github.com/zjunlp/MemTrace)
Implementable now:
- separate cache and memory trust zones;
- log which memories, summaries, embeddings, or cached states affected a run;
- require memory-write provenance, expiry, deletion, contradiction checks, and rollback.
Tools, repos, and methodologies worth exploring:
- MemTrace, append-only logs, pgvector provenance tables, taint labels, cache isolation, memory-write approval gates, contradiction checks
Implementability score: 0.50

### Deployment-shaped safety governance beats abstract safety scores
Summary: A3S-Bench, MCP-client telemetry, ITBench-AA, RAMPART, and Gram all evaluate agents inside tool-bearing scenarios. Governance should score traces, concealment, evasion, incident response, and sabotage incentives.

Analysis: [weekly sovereignty analysis](2026-05-29/sovereignty.md#deployment-shaped-safety-governance-beats-abstract-safety-scores)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Network Containment](agent-network-containment/agent-network-containment.md)
Core sources: [A3S-Bench](https://arxiv.org/abs/2605.22321v1), [Agent3Sigma Stage](https://github.com/antgroup/Agent3Sigma-Stage), [MCP client telemetry](https://huggingface.co/datasets/evalstate/mcp-clients), [ITBench-AA](https://huggingface.co/blog/ibm-research/itbench-aa), [RAMPART](https://github.com/microsoft/RAMPART), [Gram](https://arxiv.org/abs/2605.30322)
Implementable now:
- build sabotage, overeagerness, evasion, and incident-response scenarios per agent role;
- preserve full trajectories for review;
- run ablations on realism, objective wording, tool scope, and approval gates.
Tools, repos, and methodologies worth exploring:
- A3S-Bench, Agent3Sigma Stage, RAMPART, pytest, red-team scenario cards, LangSmith/Langfuse, OpenTelemetry, approval-gate ablations
Implementability score: 0.62

### Sandboxing and data-flow budgets are the practical policy layer
Summary: Permission laundering and lightweight process sandboxing show that policy has to track information movement and local effects, not just approve individual tool calls.

Analysis: [weekly sovereignty analysis](2026-05-29/sovereignty.md#sandboxing-and-data-flow-budgets-are-the-practical-policy-layer)
Durable topic: [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core sources: [permission laundering](https://arxiv.org/abs/2605.26542), [Sandlock paper](https://arxiv.org/abs/2605.26298), [multikernel/sandlock](https://github.com/multikernel/sandlock)
Implementable now:
- tag data with capabilities and allowed destinations;
- block tool chains that launder restricted data;
- wrap local process execution with file/network/syscall constraints.
Tools, repos, and methodologies worth exploring:
- OPA/Cedar, capability labels, eBPF/audit logs, Sandlock, containers, microVMs, seccomp, file/network allowlists, policy-as-code tests
Implementability score: 0.74

## Previous structured update

The prior Friday synthesis for 2026-05-22 focused on semantic API readiness, MCP authentication, managed-agent infrastructure, memory authorization, and security coverage maps: [2026-05-22 synthesis](../roundups/2026-05-22.md).
