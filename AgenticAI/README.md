# AgenticAI

Implementation analysis for agent evaluation, memory, context policy, tools, model routing, and orchestration.

## Latest Structured Update: 2026-10-24

### Verify remembered premises against the pending effect

Summary: Memory verification should scale with the action a remembered claim would authorize. AMV-Guard reports 33.9% lower ToolSandbox verification cost while retaining 100% safe-proceed recall and 0% gate-level harmful execution.

Analysis: [action-conditioned memory verification](2026-10-24/reasoning.md#1-verify-remembered-claims-in-proportion-to-the-action-they-authorize)

Core source: [When Is a Memory Safe Enough to Act On?](https://arxiv.org/abs/2610.31446v1)

Implementable now:
- classify effects by impact and reversibility;
- extract the remembered premises required by each effect;
- verify only premises that can change the admission decision;
- abstain when evidence is insufficient.

Implementability score: 0.78

### Grade the assurance suite with seeded faults

Summary: REGATTA evaluates whether tests expose specified faults, separating predicted coverage from observed detection. Its uncovered requirement tail makes a green aggregate score insufficient.

Analysis: [fault-injected assurance coverage](2026-10-24/reasoning.md#2-grade-the-assurance-suite-by-seeded-faults-not-only-agent-success)

Core source: [REGATTA](https://arxiv.org/abs/2610.30924v1)

Implementable now:
- define the fault catalog first;
- inject controlled deviations;
- report uncovered requirements and judge disagreement;
- audit source rules before treating them as ground truth.

Implementability score: 0.66

## Previous Structured Update: Week Ending 2026-10-23

### Preserve typed evidence through context transformations

Summary: Compaction, retrieval, and summarization need direct provenance and evidence-preservation tests. Correct computation is insufficient when the harness answers from the wrong output or turns untrusted text into apparent user authority.

Analysis: [preserve typed provenance through retrieval and compaction](2026-10-23/reasoning.md#1-preserve-typed-provenance-through-retrieval-and-compaction)

Core sources: [Compaction Laundering](https://arxiv.org/abs/2610.29869v1), [KEEP-Bench](https://arxiv.org/abs/2610.26827v1), [Same Simulation, Different Evidence](https://arxiv.org/abs/2610.26836v1)

Implementable now:
- preserve typed roles and source IDs;
- mark authoritative outputs;
- run proposition-level preservation fixtures;
- fail closed on missing required lineage.

Implementability score: 0.91

### Measure model and harness failures separately

Summary: Frozen budgets, first-failure records, user interaction, and terminal outcome grading reveal when an apparent model failure is a harness limit or a delivery failure.

Analysis: [treat benchmark scores as model plus harness scores](2026-10-23/reasoning.md#2-treat-benchmark-scores-as-model-plus-harness-scores)

Core sources: [ToolBottleneckBench](https://arxiv.org/abs/2610.21098v1), [FDE-Gym](https://arxiv.org/abs/2610.22350v1)

Implementable now:
- freeze tool menus and completion caps;
- record first unmet obligations;
- grade integration and customer outcome separately;
- pair static tasks with multi-turn user simulations.

Implementability score: 0.86

### Route execution abstractions from observed state

Summary: Choose micro tools, macro skills, model escalation, and planning gates during execution, after state and failure evidence exist.

Analysis: [route execution abstractions from observed state](2026-10-23/reasoning.md#3-route-execution-abstractions-from-observed-state)

Core sources: [Adaptive Skill Granularity](https://arxiv.org/abs/2610.31461v1), [LEASH](https://arxiv.org/abs/2610.22280v1), [PAUSE](https://arxiv.org/abs/2610.29870v1)

Implementable now:
- add macro preconditions and postconditions;
- record route transitions and costs;
- add one planner gate before the first source edit;
- shadow learned routers against deterministic rules.

Implementability score: 0.78

### Gate proactive memory on evidence and timing

Summary: Relevant memory does not prove that interruption or action is useful now. Retrieval, timing, silence, expiry, and reauthorization need separate tests.

Analysis: [gate proactive memory on evidence and timing](2026-10-23/reasoning.md#4-gate-proactive-memory-on-evidence-and-timing)

Core sources: [ProPerAgent](https://arxiv.org/abs/2610.22671v1), [CarryoverBench](https://arxiv.org/abs/2610.28425v1)

Implementable now:
- add trigger windows and cooldowns;
- store lineage and expiry with memory;
- separate facts from procedures and grants;
- test planting and triggering across sessions.

Implementability score: 0.45

## Current implication

Preserve evidence first, instrument the harness second, then optimize routing and models. Proactive memory remains the least mature layer because usefulness and authority both change over time.
