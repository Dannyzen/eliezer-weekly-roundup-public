# Knowledge-State Orchestration

Knowledge-state orchestration is the discipline of making an agent’s evolving epistemic state explicit, recoverable, and auditable during long-horizon work.

The durable pattern is not “use more agents” or “use a longer context window.” The durable pattern is to treat claims, evidence, assumptions, open questions, contradictions, partial artifacts, and final conclusions as state transitions that can be inspected and resumed.

## Why this topic now

ADEMA sharpened the problem on 2026-04-28. Its core claim is that long-horizon LLM tasks often fail because knowledge state drifts, intermediate commitments remain implicit, and interruptions fracture the evidence chain.

Core source:
- ADEMA: https://arxiv.org/abs/2604.25849v1

## Core thesis

Long-horizon synthesis needs an epistemic state machine.

A serious research or planning agent should know:
- what it currently believes;
- which sources support each claim;
- which assumptions are still unverified;
- which contradictions remain unresolved;
- which artifacts have been produced;
- what changed since the previous checkpoint;
- whether the final answer actually follows from the evidence chain.

If that state only exists in a transcript, it will drift.

## Minimum state model

### 1. Claims

A claim is a durable statement the agent may reuse later. It should store source links, confidence, and status.

### 2. Evidence

Evidence should remain attached to its source artifact. Summaries are useful, but they should not replace the source-backed record.

### 3. Assumptions

Assumptions should be marked explicitly so they can be challenged before final synthesis.

### 4. Open questions

Open questions guide further search and prevent premature closure.

### 5. Contradictions

Contradictions should not be hidden in prose. They should become state objects with resolution status.

### 6. Artifacts

Intermediate outputs should be first-class: tables, outlines, code, decision logs, analysis notes, and review packets.

### 7. Checkpoints

A checkpoint should preserve enough state to resume after interruption without silently losing commitments or provenance.

## What to build now

Start small:
1. Store long-horizon research state in a typed SQLite/Postgres table or structured markdown file.
2. Checkpoint after each source-gathering, synthesis, and review phase.
3. Keep source notes separate from final prose.
4. Require every durable claim in the final report to link back to evidence.
5. Run a second evaluator over state transitions, not just the final answer.

## What to avoid

Avoid these traps:
- one giant transcript as the only memory;
- summaries that sever source provenance;
- evaluator agents that grade prose without inspecting state changes;
- artifacts that cannot be resumed or replayed;
- treating interruption recovery as an ops nicety instead of a correctness requirement.

## Implementability score

0.58

The basic pattern is implementable with today’s workflow engines, databases, repo artifacts, and review checklists. The hard part is designing state schemas and evaluator loops that improve truthfulness without adding bureaucracy or false confidence.
