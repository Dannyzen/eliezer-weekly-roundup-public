# Agent Community Governance

Last updated: 2026-07-01

Agent community governance is the layer that decides how groups of agents make decisions, preserve disagreement, escalate to humans, and produce replayable evidence.

## Core thesis

Interop protocols are connection layers. They should not be mistaken for governance layers.

MCP, A2A, ACP, ANP, and ERC-8004 can help agents discover capabilities, exchange messages, and call tools. That is necessary, but it is not enough for a governed community of agents. A serious community needs membership rules, deliberation structure, voting or approval semantics, dissent preservation, escalation paths, and audit/replay evidence.

## Why this topic now

Governance Gaps in Agent Interoperability Protocols evaluates mainstream agent protocols against six governance dimensions: membership, deliberation, voting, dissent preservation, human escalation, and audit/replay. Its strongest conclusion is architectural: current protocols do not express governed agent communities. Voting and dissent preservation are universally absent in the evaluated set, and deliberation is absent or partial.

That matters because multi-agent systems are moving from demos into enterprise workflows. Once agents coordinate across teams, tenants, vendors, or principals, the system needs to explain group decisions and failure paths. Otherwise orchestration becomes informal authority laundering.

Core source:
- https://arxiv.org/abs/2606.31498v1

## The missing primitives

### Membership

A community needs an explicit roster: agent identity, owner, role, tenant, credential class, allowed data classes, and admission evidence.

### Deliberation

A proposal should have a structured discussion path: who may argue, what evidence is cited, what policy applies, and when the discussion closes.

### Voting or approval

Not every decision should be majority vote. The useful primitive is a decision rule: quorum, veto, unanimity, role-weighted approval, human approval, or single accountable owner.

### Dissent preservation

Dissent is not noise. In high-risk workflows, preserved dissent becomes future evidence. It tells the reviewer which agent objected, why, and whether the objection was overruled.

### Human escalation

A governed community needs explicit escalation triggers: conflicting evidence, missing authority, policy uncertainty, high blast radius, low confidence, or repeated retries.

### Audit and replay

The system should preserve proposal, evidence, retrieved context, agent roles, votes, dissent, approvals, policy verdicts, tool calls, and final action in one replay bundle.

## What to build now

Start with an overlay, not a new protocol.

1. Define an agent assembly manifest for each multi-agent workflow.
2. Bind every participant to identity, owner, role, scope, model, tools, and policy profile.
3. Record every group decision as a structured decision record.
4. Preserve dissent and abstention as first-class fields.
5. Route high-risk decisions through human approval or explicit veto rules.
6. Attach replay bundles to final artifacts, tickets, memory writes, deployments, or external sends.

## Practical schema sketch

Minimum fields:
- `community_id`
- `workflow_id`
- `members[]`: identity, owner, role, model, tool scopes, data scopes, voting weight
- `proposal`: goal, risk class, required decision rule, deadline
- `evidence[]`: source URL, memory ID, trace ID, artifact ID, policy ID
- `votes[]`: member, vote, confidence, rationale, timestamp
- `dissent[]`: member, objection, cited evidence, escalation request
- `human_escalation`: required, requested_by, approver, verdict
- `policy_verdicts[]`: policy, decision, reason, timestamp
- `replay_bundle`: trace path, artifact hashes, final action, outcome

## Relation to existing topics

- [Agent Authority Manifests](../agent-authority-manifests/agent-authority-manifests.md): defines individual agent authority. Community governance defines group decision authority.
- [Agent Gateway Governance](../agent-gateway-governance/agent-gateway-governance.md): enforces scoped tool and protocol access. Community governance defines who may decide to use that access.
- [Runtime Governance](../runtime-governance/runtime-governance.md): captures execution-time evidence. Community governance decides which group-level evidence must exist before execution.
- [Shared-State Agents](../shared-state-agents/shared-state-agents.md): covers shared memory and state. Community governance covers shared decisions.

## Implementability score

0.48

The overlay is implementable now with manifests, policy checks, traces, and decision records. The low score reflects the missing protocol-native support. Builders will have to own the governance layer above current interop standards.

## Working conclusion

Do not wait for MCP, A2A, or ACP to become constitutions. Treat them as transport and capability layers, then build community governance as an explicit overlay with membership, dissent, escalation, and replay evidence.
