# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-07-01

### Agent interoperability protocols still cannot govern communities

Summary: Governance Gaps in Agent Interoperability Protocols argues that MCP, A2A, ACP, ANP, and ERC-8004 support connection and task coordination, but do not express governed agent communities. Membership, deliberation, voting, dissent preservation, human escalation, and audit/replay need an overlay layer.

Analysis: [daily sovereignty analysis](2026-07-01/sovereignty.md#agent-interoperability-protocols-still-cannot-govern-communities)
Durable topics: [Agent Community Governance](agent-community-governance/agent-community-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md)
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

The 2026-06-26 weekly synthesis remains the broad current governance map: [weekly sovereignty analysis](2026-06-26/sovereignty.md). The 2026-06-30 scan said memory attacks and routing trust need observed behavior. The 2026-07-01 scan adds the community layer: agent protocols may connect participants, but governed decisions need explicit membership, dissent, escalation, and replay evidence.
