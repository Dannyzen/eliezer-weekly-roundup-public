# Strategy Daily Sovereignty - 2026-07-01

Today's governance signal is that connection is not control. MCP-style systems can make tools reachable, and interop protocols can make agents discoverable, but serious agent products need runtime objects that bind authority, data flow, approvals, and audit before side effects happen.

## Deep Dive Wednesday: HCP makes execution control explicit

Deep dive: [Agent Execution Control Plane](../agent-execution-control-plane/agent-execution-control-plane.md)
Core source: https://arxiv.org/abs/2606.29073v1
Artifact repo: https://github.com/SymbolicLight-AGI/handle-capability-protocol

From Tool Connection to Execution Control is the strongest strategic finding from the last 7 days because it names the layer under the whole agentic stack. The paper argues that MCP-style ecosystems provide a useful connection layer for tools, resources, prompts, and transports, but execution security is still split across clients, servers, prompts, approval dialogs, OAuth deployments, and logs.

HCP, the Handle-Capability Protocol reference runtime, introduces explicit runtime objects: principals, resources, grants, capabilities, handles, policy decisions, data-pipe checks, tasks, approvals, and audit entries. Its eight execution-layer invariants are the useful part: metadata non-authority, grant-backed approval, canonical resources, principal binding, scoped capability invocation, source-and-target data-flow authorization, deny-path audit, and explicit protocol state.

Why it beat the week: ECHO improves source-indexed memory, CubeSandbox improves sandbox execution, agents-cli improves lifecycle delivery, and the governance-gaps paper improves the community layer. HCP sits underneath all of them. If tool outputs can become later writes, if approvals are not bound to grants, if resource hints can override canonical resources, or if denials disappear from traces, the stack is still prompt-managed authority with nicer connectors.

The paper reports a controlled 10-case benchmark where a naive MCP-like connection runtime permits all modeled attacks, a practice-informed mitigation baseline with metadata linting, session checks, and per-call approvals still permits 6 of 10, and HCP blocks all 10 while preserving audit evidence. The result is not production proof. It is a strong architectural warning: connection-layer mitigations do not substitute for execution-control objects.

How it fits into the Strategy layer:
- Agent execution control plane: own principal, grant, resource, capability, handle, policy, approval, data-flow, and audit objects.
- Agent gateway governance: admit MCP-style servers as providers behind the broker, not as the broker.
- Runtime governance: make every allow, deny, approval, handle projection, and data-pipe event replayable.
- Agent sandboxing: keep broker authority separate from OS, VM, browser, network, and credential isolation.

Practical tools, repos, and methodologies worth exploring now:
- HCP reference repo for object vocabulary, schemas, conformance fixtures, MCP compatibility shims, and paper artifacts.
- OPA, Cedar, or OpenFGA for deterministic checks over principal, resource, capability, data class, workflow, and approval state.
- OpenTelemetry or JSONL traces for allow, deny, approval, pipe, handle, task, and final-effect events.
- CubeSandbox or another sandbox worker layer beneath the broker, so execution control and blast-radius reduction are separate.
- Local fixtures for approval bypass, metadata authority, confused deputy resource resolution, wrong-principal handle access, target-side pipe bypass, and grant enumeration.

Implementability score: 0.71

A thin version is buildable now: put privileged tools behind a broker, canonicalize resources, add grants and approvals, store sensitive outputs behind handles, check source and target data flows, and emit deny audits. A production version needs durable policy stores, credential custody, provider attestation, signed approvals, multi-tenant isolation, and operator UX.

## Agent interoperability protocols still cannot govern communities

Core source: https://arxiv.org/abs/2606.31498v1
Durable topic: [Agent Community Governance](../agent-community-governance/agent-community-governance.md)

Governance Gaps in Agent Interoperability Protocols remains the strongest secondary strategy signal today because it separates connection from governance at the community layer. The paper evaluates MCP, A2A, ACP, ANP, and ERC-8004 against six governance dimensions: membership, deliberation, voting, dissent preservation, human escalation, and audit/replay.

The useful conclusion is that current protocols support pieces of task coordination, identity, capability discovery, tool access, and message exchange, but they do not express governed community behavior. The paper reports universal gaps around voting and dissent preservation, with deliberation absent or partial. Its core claim matches the HCP lesson one layer up: agent community governance is a missing layer above current interoperability standards, not a small feature inside each protocol.

Why it matters: serious multi-agent deployments will not only route tasks. They will make choices across agents with different roles, authorities, owners, and failure modes. If the system cannot preserve dissent, escalate conflict, replay a decision, or prove who had membership authority, then it is not a governed agent community. It is just a group chat with tools.

Practical tools, repos, and methodologies worth exploring now:
- agent assembly manifests that list members, principals, roles, scopes, allowed tools, and decision rights
- decision records with proposal, votes, dissent notes, escalation path, human approvals, and replay bundle
- workflow-level policy gates that distinguish advice, consensus, quorum, veto, and approval-required actions
- test fixtures where one agent dissents, abstains, times out, or requests escalation before a high-risk action

Implementability score: 0.48

The governance artifact layer is buildable now with manifests, traces, policy gates, and decision records. Protocol-native support is still mostly absent, so this needs an overlay architecture.

## Near misses and watchlist

ECHO is the stronger AgenticAI memory finding, but HCP won the deep dive because source-indexed memory still needs authority controls when remembered data is later routed into writes, sends, browser actions, or tool calls. CubeSandbox is more immediately deployable, but it controls the execution environment rather than the authority model. agents-cli is highly implementable, but lifecycle skills are one provider behind the broker. The Microsoft MCP security post and related tool-poisoning coverage reinforce the same direction: tool descriptions are untrusted control data, not policy authority.
