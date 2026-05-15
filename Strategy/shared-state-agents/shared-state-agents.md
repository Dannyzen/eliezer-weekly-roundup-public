# Shared-State Agents

The durable lesson from recent personal-agent work is simple: chat is not enough. If an agent ecosystem has no shared state substrate, every generated tool becomes another isolated island.

## Core thesis

Shared state is the missing systems layer between one-off agent interactions and coherent personal software.

A useful personal agent stack should let multiple tools, interfaces, and workflows operate on the same durable artifacts with explicit read and write paths. That means:
- persistent artifacts instead of prompt-only context
- typed schemas instead of vague conversational memory
- explicit write-back affordances instead of hidden side effects
- ownership and scope metadata instead of a single undifferentiated memory blob

## Why this matters

Most current personal agents are impressive demos wrapped around fragile state management.

Common failure modes:
- a tool created in one conversation is invisible to the next one
- GUI artifacts and chat actions drift apart
- memory becomes a transcript archive instead of an operational substrate
- later-generated tools cannot plug into earlier ones without manual rewiring

A shared-state layer fixes the right problem. It gives the agent environment somewhere stable to attach capability, memory, and interface behavior.

## Representative source

- PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in Personal AI Agents: https://arxiv.org/abs/2604.08529v1

## Practical design pattern

### 1. Make artifacts first-class
Treat notes, tasks, documents, settings, views, and generated mini-tools as durable objects with IDs and schemas.

### 2. Publish state changes onto a bus
Use a local event log or pub/sub layer so multiple tools can react to the same state change without chat acting as the relay.

### 3. Govern writes explicitly
Write-back should be a named capability with audit trails, ownership metadata, and scope rules.

### 4. Let chat be one interface, not the storage layer
The assistant should read from and write to shared state, but not be the canonical store for that state.

## Practical stack to try now

### Storage
- SQLite for local durable state
- append-only event logs for replay and audit
- file-backed artifact stores for larger structured objects

### Coordination
- pub/sub or event-bus patterns for cross-tool synchronization
- typed artifact registries
- schema validation on read and write paths

### Governance
- ownership metadata per artifact
- scoped capabilities for write operations
- trace-linked audit logs for edits and automations
- conflict resolution rules for concurrent updates

## What to avoid

Avoid these traps:
- storing everything as conversation text
- letting tools mutate shared state without explicit contracts
- conflating identity, memory, and capability into one opaque agent state blob
- assuming local execution alone creates sovereignty

## Working conclusion

Local-first agents become strategically interesting only when the user owns the state layer. Shared-state agents are not mainly a UX idea. They are the architecture that makes personal sovereignty, continuity, and composability possible.