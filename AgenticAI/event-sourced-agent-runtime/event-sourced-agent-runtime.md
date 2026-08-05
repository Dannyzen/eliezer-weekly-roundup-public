# Event-Sourced Agent Runtime

Last updated: 2026-06-24

Event-sourced agent runtime is the design discipline of making the agent’s durable state an append-only event history, then deriving working state, memory views, audit trails, and replayable traces from that history.

## Core thesis

The log should not be a side effect of the agent. For serious long-running agents, the log is the state substrate.

A transcript, vector memory, and final artifact are not enough. They usually cannot answer:
- which model call created this claim;
- which evidence object informed it;
- which tool response changed the agent’s belief;
- whether a rerun from the same prefix would reconstruct the same state;
- how a different prompt, policy, or tool result would have changed the trajectory;
- why a downstream object became stale after an upstream source changed.

An event-sourced runtime can answer those questions because every mutation is an event and every current-state view is a projection.

## Why this topic now

*The Log is the Agent* and ActiveGraph make the pattern concrete. ActiveGraph uses an append-only event log as the source of truth, projects that log into a working graph, and lets behaviors react to graph changes. The useful contribution is not another agent framework. It is a runtime claim: replay, fork, diff, and lineage should be primitive operations.

Core sources:
- The Log is the Agent: https://arxiv.org/abs/2605.21997
- ActiveGraph site: https://activegraph.ai/
- ActiveGraph repository: https://github.com/yoheinakajima/activegraph

## Stack position

This layer sits below orchestration and above raw storage.

- **Workflow layer:** decides what work should happen next.
- **Event-sourced runtime:** records every model call, tool call, object mutation, relation, rejection, failure, and policy decision.
- **Working graph:** projects the current world state from the log.
- **Memory layer:** retrieves or summarizes views over event history; it is not the only source of truth.
- **Evaluation layer:** replays logs, forks runs, diffs outcomes, and checks lineage.
- **Governance layer:** ties approvals, denials, credentials, scopes, and side effects to traceable events.

## Minimum viable implementation

Start smaller than a full framework:

1. Define event types for model requests, tool requests, tool responses, object creation, relation creation, patches, policy decisions, approvals, failures, and final artifacts.
2. Store events append-only with run ID, parent event ID, actor, timestamp, payload hash, and source version.
3. Project the log into a simple graph or table model: tasks, claims, evidence, files, tools, decisions, and artifacts.
4. Attach relations such as `derived_from`, `depends_on`, `contradicts`, `verified_by`, and `supersedes`.
5. Cache model/tool responses for deterministic replay where possible.
6. Build fork-and-diff for one narrow workflow before generalizing.
7. Treat policy denials and failed tool calls as first-class events, not noise.

## What to avoid

Avoid these traps:
- flattening event history into periodic summaries and calling it memory;
- letting agents mutate state without preserving the proposed patch and the accepted/rejected verdict;
- replaying only natural-language turns while ignoring tool outputs and environment state;
- treating vector retrieval as provenance;
- allowing self-modifying behavior without fork/diff and rollback evidence;
- mixing audit events and derived summaries without source hashes.

## Practical tools and methods worth exploring now

- `yoheinakajima/activegraph` for a concrete event-sourced graph runtime.
- Temporal, Inngest, Prefect, or durable workflow engines for outer orchestration.
- SQLite/Postgres append-only event tables for a minimum viable substrate.
- OpenTelemetry trace IDs carried through model/tool events.
- Graph stores or relational projections for claim/evidence/task lineage.
- Git-style branch/diff mental models for agent run forks.
- Policy-as-code hooks on event acceptance, not only on final tool execution.

## Implementability score

0.84

The first useful version is implementable now: append events, project graph state, record lineage, and replay one workflow. Production-grade determinism, cached model replay, fork/diff UX, policy integration, and self-modification controls require real architecture work.

## June 11 update: project memory makes event sourcing an agent-facing primitive

PROJECTMEM applies the event-sourced runtime pattern at the coding-agent project level. The useful move is the projection boundary: raw events remain local and append-only, while the agent receives compact summaries and action warnings through MCP. That keeps provenance intact without stuffing the whole history into the prompt.

Practical lesson:
- define typed event classes for issues, attempts, fixes, decisions, notes, fragile files, and rejected proposals;
- project summaries, risk flags, and next-action constraints from the event log;
- expose those projections through MCP or local files, not by giving the agent uncontrolled write access to the source log;
- treat failed attempts and policy denials as events that future runs can query before acting.

Sources:
- [PROJECTMEM](https://arxiv.org/abs/2606.12329v1)
- [riponcm/projectmem](https://github.com/riponcm/projectmem)

## Strategic implication

This is a local-first and governance-friendly primitive. If the agent’s state is an inspectable event log, the operator can keep it on their own infrastructure, sync selected projections, audit risky actions, and replay failures without trusting a vendor dashboard as the only source of truth.

The durable bet: future serious agents will look less like chat transcripts and more like event-sourced operating systems with model calls inside them.


## June 19 update: session becomes the runtime value

OpenRath strengthens this topic by making Session the first-class object that flows through agents, workflows, sandboxes, tools, memory, and selectors. The key design correction is that the event log and the active runtime value should not be unrelated artifacts. Session should carry enough lineage, evidence, placement, and pending-work metadata that fork, merge, compression, replay, and branch comparison are normal runtime operations.

Practical lesson:
- pass a structured Session or run-state object through every agent transformation;
- store branch ID, parent session ID, sandbox placement, token usage, tool evidence, memory references, and pending work;
- keep raw events append-only, then project compact Session views into prompts;
- make fork, merge, replay, compression, and selector decisions explicit operations;
- link final artifacts to the session branch and tool evidence that produced them.

Sources:
- [OpenRath](https://arxiv.org/abs/2606.19409v1)
- [Rath-Team/OpenRath](https://github.com/Rath-Team/OpenRath)


## June 20 update: task ledgers are the compact state projection before side effects

LedgerAgent is an event-sourced runtime pattern in small. It does not require a full replay engine to be useful. It maintains observed task state as a separate ledger of facts, identifiers, constraints, and conditions, renders that ledger into the prompt, and checks state-dependent policy constraints before environment-changing tools execute.

The runtime lesson is that a ledger is a current-state projection with authority implications. Raw events still matter for replay and audit, but the agent needs a compact, typed state object at decision time. Policy needs the same object before mutation.

Practical lesson:
- store raw observations and tool returns as append-only events;
- project them into a compact task ledger with source event IDs and validity metadata;
- render the ledger into the prompt as state, not as unstructured transcript context;
- attach ledger snapshot hash, policy ID, and verdict to every side-effecting tool call;
- treat ledger schema changes as runtime migrations because they can change policy outcomes.

Source:
- [LedgerAgent](https://arxiv.org/abs/2606.20529)


## June 24 update: conversational handoff memory belongs in the event log

ESAA-Conversational applies the event-sourced runtime thesis directly to coding-agent handoffs. The useful correction is that `handoff.md`, `state.md`, `decisions.md`, and `tasks.json` should be projections, not hand-written summaries. The source of truth is an append-only conversation event log such as `activity.jsonl`.

Practical lesson:
- capture visible agent turns as typed events with source, actor, timestamp, and workspace scope;
- project compact handoff and state views deterministically from the log;
- keep durable decisions and task curation explicit instead of letting every summary become authority;
- test that a known event log regenerates the same projections;
- let heterogeneous coding agents collaborate through local projections rather than private vendor logs.

Source:
- [ESAA-Conversational](https://arxiv.org/abs/2606.23752)

## August 5 update: resume is an event-sourced conformance boundary

Resume Means Resume turns durable execution into six testable properties: prefix continuation, effect exactly-once, fork determinism, checkpoint validity, consume-once, and recovery determinism. The event log is useful only if replay and resume preserve those properties across crashes and framework upgrades.

Practical lesson:
- assign stable IDs to runs, checkpoints, interrupts, forks, and effects;
- persist intent and outcome around every non-idempotent effect;
- inject faults before dispatch, after dispatch, after commit, and before observation;
- test fork and consume-once semantics separately from ordinary replay;
- bind conformance results to exact runtime versions.

Artifact caveat: the paper reports five pinned frameworks, 7.4 million checked TLA+ states, and a 39-cell fault matrix, but its probes and Remit implementation remain private pending publication.

Source:
- [Resume Means Resume](https://arxiv.org/abs/2608.03836v1)
