# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-15

### Derive write authority from schemas and the user request

Summary: CapLite replaces model-written security artifacts with fixed schema rules, precommitted writes, and deterministic checks that bind authority-bearing arguments to values stated by the user.

Analysis: [Daily analysis](2026-11-15/reasoning.md#1-derive-write-authority-from-schemas-and-user-stated-values)

Core source: [CapLite v1](https://arxiv.org/abs/2611.17115v1)

Implementable now:
- classify recipient, amount, object, and destination fields
- freeze intended writes before reading untrusted content
- require normalized equality with user-stated authority values
- test write injection separately from answer-only injection

Implementability score: 0.78

### Schedule native accelerator work at the command boundary

Summary: Metal Sandbox preserves private agent workspaces while serializing accelerator-sensitive commands and migrating eligible queue work across Macs.

Analysis: [Daily analysis](2026-11-15/reasoning.md#2-schedule-native-accelerator-work-at-the-command-boundary)

Core source: [Metal Sandbox v1](https://arxiv.org/abs/2611.17294v1)

Implementable now:
- parallel-safe versus serialized command classes
- per-instance workspace and HOME isolation
- command-to-trajectory identity through migration
- fixed-trace replay before live scheduling

Implementability score: 0.66

## Current working model

1. Models propose plans and candidate arguments.
2. Deterministic code owns authority-bearing writes.
3. Sandboxes preserve workspace and process boundaries.
4. Schedulers allocate scarce execution at command granularity.
5. Promotion follows matched attack, correctness, and throughput evidence.

## Browse

- [Daily roundup](../roundups/2026-11-15.md)
- [Daily analysis](2026-11-15/reasoning.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Sandbox-native agent workers](sandbox-native-agent-workers/sandbox-native-agent-workers.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
