# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Deep Dive Wednesday 2026-07-01

### HCP makes MCP-style execution control explicit

Summary: From Tool Connection to Execution Control argues that MCP-style systems provide connection, not execution authority. HCP adds runtime objects for principals, grants, canonical resources, capabilities, handles, policy decisions, data-pipe checks, approvals, tasks, and audit entries. The architectural move is to make execution-layer security invariants explicit and testable instead of scattering them across prompts, tool metadata, OAuth, UI approvals, and logs.

Analysis: [daily sovereignty analysis](2026-07-01/sovereignty.md#deep-dive-wednesday-hcp-makes-execution-control-explicit)
Durable topic: [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md)
Adjacent topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md), [Agent Community Governance](agent-community-governance/agent-community-governance.md)
Core sources: [HCP paper](https://arxiv.org/abs/2606.29073v1), [HCP reference repo](https://github.com/SymbolicLight-AGI/handle-capability-protocol), [HCP security invariants](https://github.com/SymbolicLight-AGI/handle-capability-protocol/blob/main/docs/security-invariants.md)
Implementable now:
- put privileged tools behind an execution-control broker
- bind every invocation to principal, grant, canonical resource, capability, and policy decision
- store sensitive tool outputs behind handles with principal-aware projections
- check both source handle and target capability before data moves into write, send, shell, browser, database, or memory actions
- log allow and deny paths with stable reason codes and replayable audit entries
Tools, repos, and methodologies worth exploring:
- HCP reference runtime and conformance fixtures, OPA, Cedar, OpenFGA, OpenTelemetry, JSONL traces, CubeSandbox, approval-bypass fixtures, confused-deputy fixtures, handle-exfiltration fixtures, data-pipe laundering fixtures
Implementability score: 0.71

### Agent interoperability protocols still cannot govern communities

Summary: Governance Gaps in Agent Interoperability Protocols argues that MCP, A2A, ACP, ANP, and ERC-8004 support connection and task coordination, but do not express governed agent communities. Membership, deliberation, voting, dissent preservation, human escalation, and audit/replay need an overlay layer.

Analysis: [daily sovereignty analysis](2026-07-01/sovereignty.md#agent-interoperability-protocols-still-cannot-govern-communities)
Durable topic: [Agent Community Governance](agent-community-governance/agent-community-governance.md)
Core source: [Governance Gaps in Agent Interoperability Protocols](https://arxiv.org/abs/2606.31498v1)
Implementable now:
- define an agent assembly manifest for multi-agent workflows
- record proposal, votes, dissent, escalation, policy verdicts, and replay bundle for group decisions
- distinguish advice, consensus, quorum, veto, approval-required, and single-owner decisions
- test dissent, abstention, timeout, and escalation paths before high-risk actions
Tools, repos, and methodologies worth exploring:
- agent assembly manifests, Open Policy Agent or Cedar, decision records, quorum and veto schemas, trace replay bundles, policy-gated multi-agent workflows
Implementability score: 0.48

## Supporting recent Strategy context

The 2026-06-26 weekly synthesis remains the broad current governance map: [weekly sovereignty analysis](2026-06-26/sovereignty.md). The 2026-06-30 scan said memory attacks and routing trust need observed behavior. The 2026-07-01 deep dive adds the execution-control layer: agent products should prove why a tool effect was allowed, not only that the agent could reach the tool.
