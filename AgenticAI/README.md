# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-24

### ESAA-Conversational turns agent handoff memory into an event log

Summary: ESAA-Conversational treats coding-agent continuity as an append-only event log plus deterministic projections. Instead of trusting private vendor transcripts, agents can consume `handoff.md`, `state.md`, `decisions.md`, and `tasks.json` views generated from `activity.jsonl`.

Analysis: [daily reasoning analysis](2026-06-24/reasoning.md#esaa-conversational-turns-agent-handoff-memory-into-an-event-log)
Durable topics: [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Memory Systems](memory-systems/memory-systems.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core source: [ESAA-Conversational](https://arxiv.org/abs/2606.23752)
Implementable now:
- capture visible conversation turns into a local JSONL or SQLite event store
- project handoff and state files deterministically from the event log
- require agents to read projected state before acting after a handoff
Tools, repos, and methodologies worth exploring:
- JSONL event logs, SQLite append-only tables, deterministic projectors, `handoff.md`, `state.md`, OpenTelemetry trace IDs, projection regression tests
Implementability score: 0.88

### GUI vs CLI shows that skill coverage controls computer-use reliability

Summary: A matched 440-task desktop benchmark shows screen-only GUI agents at 59.1%, original-skill CLI agents at 48.2%, and verifier-guided skill-augmented CLI agents at 69.3%. The practical bottleneck is often skill coverage, not whether the agent clicks or calls commands.

Analysis: [daily reasoning analysis](2026-06-24/reasoning.md#gui-vs-cli-shows-that-skill-coverage-controls-computer-use-reliability)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [GUI-Tool Path Orchestration](gui-tool-path-orchestration/gui-tool-path-orchestration.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [GUI vs. CLI](https://arxiv.org/abs/2606.24551)
Implementable now:
- run GUI-only, original-skill CLI, augmented-skill CLI, and hybrid baselines on the same tasks
- use final-state verifiers to identify missing skills
- log path labels for GUI steps, skill calls, verification, recovery, and abstention
Tools, repos, and methodologies worth exploring:
- desktop sandboxes, final-state verifiers, skill coverage maps, held-out skill augmentation tests, OSWorld-style tasks, JSONL action-path traces
Implementability score: 0.78
