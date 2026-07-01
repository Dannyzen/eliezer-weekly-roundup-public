# Strategy Daily Sovereignty - 2026-07-01

Today's governance signal is blunt: interop protocols connect agents, but they do not govern agent communities. The missing layer is not another tool descriptor. It is membership, deliberation, dissent, escalation, and replayable decision evidence above MCP, A2A, ACP, ANP, and ERC-8004.

## Agent interoperability protocols still cannot govern communities

Core source: https://arxiv.org/abs/2606.31498v1

Governance Gaps in Agent Interoperability Protocols is the strongest strategy finding today because it separates connection from governance. The paper evaluates MCP, A2A, ACP, ANP, and ERC-8004 against six governance dimensions: membership, deliberation, voting, dissent preservation, human escalation, and audit/replay.

The useful conclusion is that current protocols support pieces of task coordination, identity, capability discovery, tool access, and message exchange, but they do not express governed community behavior. The paper reports universal gaps around voting and dissent preservation, with deliberation absent or partial. Its core claim is the right architectural frame: agent community governance is a missing layer above current interoperability standards, not a small feature inside each protocol.

Why it matters: serious multi-agent deployments will not only route tasks. They will make choices across agents with different roles, authorities, owners, and failure modes. If the system cannot preserve dissent, escalate conflict, replay a decision, or prove who had membership authority, then it is not a governed agent community. It is just a group chat with tools.

How it fits into the strategy layer:
- Agent community governance: define group membership, decision rights, dissent handling, escalation, and replay bundles.
- Agent authority manifests: bind each participant to role, scope, credential class, policy profile, and voting weight.
- Agent gateway governance: protocols should connect through gateways that can enforce community policy.
- Runtime governance: every group decision needs trace evidence, not only final output.

Practical tools, repos, and methodologies worth exploring now:
- agent assembly manifests that list members, principals, roles, scopes, allowed tools, and decision rights
- decision records with proposal, votes, dissent notes, escalation path, human approvals, and replay bundle
- workflow-level policy gates that distinguish advice, consensus, quorum, veto, and approval-required actions
- test fixtures where one agent dissents, abstains, times out, or requests escalation before a high-risk action

Implementability score: 0.48

The governance artifact layer is buildable now with manifests, traces, policy gates, and decision records. Protocol-native support is still mostly absent, so this needs an overlay architecture.

## Near misses and watchlist

The Microsoft MCP security post and related tool-poisoning coverage are directionally important, but they repeat the already-tracked lesson that tool descriptions are untrusted control data. The new strategic move today is broader: even clean interoperability protocols need a separate community-governance layer before agents can make collective decisions safely.
