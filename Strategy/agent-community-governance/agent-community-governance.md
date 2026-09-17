# Agent Community Governance

Last updated: 2026-09-16

Agent community governance is the layer that decides whether agents serving different principals may coordinate, which protocol states are valid, how local authority remains bounded, and what evidence survives for investigation.

## Overview

Transport carries messages. A social harness governs the relationship created by those messages.

MCP, A2A, ACP, ANP, and similar protocols can expose capabilities, tasks, messages, and artifacts. They do not by themselves establish who a sender represents, whether a message is valid in the current workflow, whether the recipient may act on it, or who can investigate harm later. Cross-principal coordination therefore needs a control plane above transport and below local execution.

## Core innovation

The paper separates the personal harness from the social harness. The personal harness protects one principal's private context and effect authority. The social harness governs the shared protocol across principals through identity, ordered messaging, local firewalls, task-specific norms, and post-hoc institutions.

The social harness must not become a shared brain. Each personal agent keeps its principal's private context, memory, credentials, tools, and approval policy. The shared layer owns only the inter-agent contract: identity, message order, protocol state, bounded claims, violations, and replay evidence.

## Why it matters and why this finding won the week

The week produced strong work on benchmark resolution, skill admission, action-time permission, transactional tool contracts, and MCP identity. The social-harness finding matters more architecturally because it names a missing stack boundary rather than improving one component.

`Agentic Societies Need a Social Harness` studies agents coordinating across trust boundaries for different principals. Its 600 released meeting-scheduling runs show that basic messaging and capable models do not reliably produce satisfactory collaboration. Honest agents can fail as participant count and concurrency rise. Faulty or malicious participants can stall work, steer outcomes, or exploit the fact that each agent sees only part of the interaction.

The paper's durable contribution is not the scheduling benchmark. It is the separation between a personal harness and a social harness. Personal harnesses protect one principal. Social harnesses govern the shared protocol without absorbing each principal's private authority.

## Evidence and limits

The paper evaluates six meeting-scheduling experiments, E1 through E6, with ten-run cells across model, topology, context, and participant configurations. The companion repository releases all 600 runs, configurations, principal inputs, calendars, transcripts, verdicts, aggregate results, and a static trace viewer.

The evidence supports three claims:

- delivery is not coordination, because honest agents can still livelock, split bookings, or create excessive message traffic;
- message ordering is not action ordering, because agents can create local side effects while concurrently generating replies;
- local helpfulness is not cross-principal safety, because deception, stalling, and privacy attacks may look acceptable from one participant's partial view.

The limits are material. The domain is meeting scheduling. Most quantitative cells contain ten runs. The released artifact is a trace corpus and viewer, not a production social-harness implementation. The five-layer architecture is a strong design reference, not an independently reproduced system.

## The five-layer social harness

### L1: unforgeable, verifiable identity

Bind each agent to its principal, deployment, credential class, and active task. Prevent agent spoofing, principal spoofing, and Sybil-style ambiguity before higher layers reason over messages.

### L2: reliable, ordered messaging

Give every message a stable ID, sender, task, sequence, timestamp, expiry, and delivery state. Ordering and duplicate suppression are necessary, but not sufficient, because model execution and local side effects can still race.

### L3: personal firewalls

Let each principal's agent reject, defer, redact, or escalate messages using local policy. The shared harness supplies verified evidence. The personal harness retains final authority over private state and local effects.

### L4: shared collaboration norms

Compile task-specific norms into deterministic state transitions. Define who may speak next, which message types are valid, what evidence is required, and which commitments are provisional or final. Free-form conversation can carry explanations, but it cannot define the workflow state.

### L5: social institutions

Preserve evidence for post-hoc investigation, adjudication, reputation, suspension, or other consequences. Some harms are visible only across multiple principals or over time. A local agent cannot reliably detect them from one conversation slice.

The layers divide control by failure time: L1 and L2 prevent classes of ambiguity, L3 and L4 reject invalid interactions during execution, and L5 investigates failures that only become clear afterward.

## Fit in the agentic stack

The clean architecture has four boundaries:

1. Personal harness: private memory, credentials, tools, local approval, and the principal's policy.
2. Social harness: identities, message envelopes, shared task state, protocol validation, violation evidence, and replay.
3. Transport: A2A, queues, webhooks, or another delivery mechanism.
4. Execution control: the local gate that decides whether an accepted message may cause an exact effect.

The social harness can authorize a message transition. It must not authorize the recipient's side effect. That final decision remains with the receiving principal's execution-control boundary.

## Practical prototype now

### 1. Keep principal authority local

Do not centralize calendars, credentials, private memory, or general tool access. Exchange bounded availability claims, commitments, and receipts.

### 2. Use a signed social envelope

Minimum fields:

- `message_id`
- `community_id`
- `task_id`
- `protocol_version`
- `protocol_state`
- `sender_agent_id`
- `sender_principal_id`
- `recipient_agent_ids`
- `message_type`
- `claim_or_commitment`
- `evidence_refs`
- `issued_at`
- `expires_at`
- `idempotency_key`
- `allowed_next_states`
- `signature`

CloudEvents is a useful envelope substrate for identity, source, type, time, and stable event IDs. It does not supply principal binding or workflow semantics, so extend it rather than treating it as the governance layer.

### 3. Compile the protocol

Represent the task as a JSON Schema plus a deterministic state machine. Evaluate each transition with OPA, Cedar, or equivalent policy code. Reject messages that are valid JSON but invalid in the active task state.

### 4. Separate message acceptance from effect release

An accepted scheduling proposal is not permission to edit a calendar. The receiving agent should produce a local effect request, then pass it through its own approval and execution-control gate.

### 5. Preserve a replay bundle

Store the signed envelopes, state transitions, local policy verdicts, exact effects, and final outcome. Use the released 600-run corpus as read-only fixtures for livelock, split-decision, stalling, deception, and privacy cases.

## Tools, repositories, and methods worth trying

- [Social harness trace corpus](https://github.com/social-harness/social-harness-paper): use the released traces and result files as regression fixtures. Do not mistake the viewer for an implementation.
- [A2A protocol](https://github.com/a2aproject/A2A): use tasks, messages, artifacts, and status as transport primitives, then add the social contract above them.
- [CloudEvents specification](https://github.com/cloudevents/spec): use stable event IDs, source, type, subject, and time as envelope foundations.
- [Open Policy Agent](https://github.com/open-policy-agent/opa): evaluate deterministic transition and recipient policy over structured envelopes.
- Append-only event sourcing: retain ordered envelopes and verdicts so concurrency, retries, and later adjudication are replayable.
- Adversarial protocol fixtures: test out-of-order delivery, duplicates, stale messages, hidden recipients, inconsistent commitments, stalling, false claims, and cross-principal privacy requests.

## Implementation complexity

The implementation burden is uneven:

- L1 identity and L2 message envelopes are normal engineering work if the deployment already controls agent identities and transport.
- L3 personal firewalls require each principal to define local policy and safe disclosure rules.
- L4 collaboration norms require a protocol per task family, plus compatibility and migration rules.
- L5 institutions require governance outside code: investigators, appeals, consequences, retention, and due process.

The first useful prototype is not a universal agent society. It is one narrow cross-principal workflow with an explicit state machine, signed envelopes, local effect gates, and replay.

## Implementability score

0.68

A narrow prototype is implementable now with existing identity, event, policy, and state-machine tools. A general-purpose social harness remains blocked on task-specific norms, privacy-preserving evidence exchange, institutional ownership, and evidence from domains beyond scheduling.

## Strategic implications for Danny

This fits the Friend Node model directly. Each person's node should remain sovereign and hold that person's private context. Cross-node work should pass through a shared social harness that moves bounded claims and commitments, not raw memory or shared credentials.

That changes the product boundary. The valuable shared service is not a central super-agent. It is a coordination control plane that can prove who said what, under which task contract, what each node accepted, which local effect was released, and where a violation occurred.

For client work, start with workflows where multiple principals already negotiate structured commitments: scheduling, document approvals, delegated tasks, service handoffs, and scoped data requests. These produce clearer value and safer evidence than open-ended agent chat.

## Strongest objection

The unflattering fact is that the paper does not ship the harness it proposes, and its evidence comes from one synthetic task family with small quantitative cells.

That is survivable because the proposed layers map to mature distributed-systems primitives: identity, ordered events, state machines, local policy, and audit logs. The guardrail is to build one bounded workflow and test it against the released traces. Do not claim general social safety, do not centralize principal authority, and do not let the shared harness release local side effects.

## Relation to existing topics

- [Agent Authority Manifests](../agent-authority-manifests/agent-authority-manifests.md): defines individual authority; the social harness binds messages to that authority without expanding it.
- [Agent Execution Control Plane](../agent-execution-control-plane/agent-execution-control-plane.md): releases exact local effects after a social message is accepted.
- [Agent Gateway Governance](../agent-gateway-governance/agent-gateway-governance.md): authenticates and scopes protocol access; community governance validates the shared workflow.
- [Stateful Effect Governance](../stateful-effect-governance/stateful-effect-governance.md): handles ambiguous, retryable, staged, or compensating effects created by collaboration.
- [Shared-State Agents](../shared-state-agents/shared-state-agents.md): governs shared memory and state; the social harness should minimize what becomes shared.

## Core and supporting sources

- Paper: https://arxiv.org/abs/2609.17527v1
- Immutable PDF: https://arxiv.org/pdf/2609.17527v1
- Authors' explanation: https://social-harness.org/blog/agentic-societies-need-a-social-harness/
- Released traces: https://github.com/social-harness/social-harness-paper
- A2A protocol: https://github.com/a2aproject/A2A
- CloudEvents specification: https://github.com/cloudevents/spec
- Open Policy Agent: https://github.com/open-policy-agent/opa
