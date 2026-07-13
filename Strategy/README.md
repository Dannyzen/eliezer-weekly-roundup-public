# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-13

### GRACE makes persistent instruction updates locally verifiable

Summary: GRACE stores evolving system-level guidance as a typed semantic graph, validates proposed changes around affected neighborhoods, consolidates overlapping guidance, and reconstructs the accepted graph as a deployable text checkpoint. The strategic shift is from self-editing prompt prose to a versioned promotion pipeline for authority-bearing instructions.

Analysis: [daily sovereignty analysis](2026-07-13/sovereignty.md#grace-makes-persistent-instruction-updates-locally-verifiable)
Durable topic: [Persistent-State Agent Control](persistent-state-agent-control/persistent-state-agent-control.md)
Core source: [Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift](https://arxiv.org/abs/2607.09175v1)
Implementable now:
- split mutable guidance into typed, source-linked clauses
- encode conflict, supersession, dependency, and scope relations explicitly
- validate local changes, reconstruct text deterministically, and replay before promotion
Tools, repositories, and methodologies worth exploring:
- typed semantic graphs, graph diffs, structural validators, deterministic text reconstruction, distribution-shift replay, Git checkpoints
Artifact caveat:
- the paper's advertised `RedMind-Research/GRACE` repository returned 404 during this scan
Implementability score: 0.48

## Supporting recent Strategy context

The July 13 scan sharpens the evidence-is-not-authority thesis. Operational experience, raw trajectories, remembered configuration, and generated tests can all propose future behavior. None should govern side effects until a typed, replayable promotion gate accepts it.
