# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-19

### Gate agent updates against the incumbent

Summary: Safe Personal RSI evaluates candidate reusable instructions against the current version, repeats failures, uses rollback for repair evidence, and keeps the incumbent when no candidate passes both safety and utility gates.

Analysis: [Daily analysis](2026-11-19/reasoning.md#1-gate-personal-agent-updates-against-the-incumbent)

Core source: [Safe Personal RSI v1](https://arxiv.org/abs/2611.23651v1)

Implementable now:
- versioned instruction candidates and incumbents
- matched safety and utility fixtures
- repeated failure traces and rollback tests
- fail-closed promotion

Implementability score: 0.72

### Make memory visible, scoped, and reversible

Summary: MemoSync exposes memory proposal, scope, selection, citation, history, audit, and reversal through a local-first operator workbench.

Analysis: [Daily analysis](2026-11-19/reasoning.md#2-make-agent-memory-visible-scoped-and-reversible)

Core sources: [MemoSync paper v1](https://arxiv.org/abs/2611.24165v1), [MemoSync repository](https://github.com/SLEEPYBQ/MemoSync)

Implementable now:
- personal, project, and session scopes
- pre-turn memory selection receipts
- per-item version history
- post-turn memory-use audits
- local SQLite and Markdown projections

Implementability score: 0.86

## Current working model

1. Preserve canonical events and the incumbent configuration.
2. Propose memory and instruction changes as versioned candidates.
3. Expose scope, selection, citation, and history to the operator.
4. Test safety, utility, and actual memory use before promotion.
5. Keep every promoted state reversible and source-linked.

## Browse

- [Daily roundup](../roundups/2026-11-19.md)
- [Daily analysis](2026-11-19/reasoning.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Skills as control](skills-as-control/skills-as-control.md)
