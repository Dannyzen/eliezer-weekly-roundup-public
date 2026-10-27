# AgenticAI

Implementation analysis for agent evaluation, memory, context policy, tools, model routing, and orchestration.

## Latest Structured Update: 2026-10-27

### Evaluate model and harness as one deployed pair

Summary: Across 52,168 trajectories in 111 settings, harness rankings changed by model and task. Task success, valid completion, and token load exposed different execution profiles.

Analysis: [model-harness pair evaluation](2026-10-27/reasoning.md#1-evaluate-the-model-and-harness-as-one-deployed-pair)

Core source: [When Agents Fail](https://arxiv.org/abs/2610.32483v1)

Implementable now:
- cross models and harnesses on identical tasks;
- version the whole deployed pair;
- report valid completion and cost beside success.

Implementability score: 0.90

### Test delayed results as typed state transitions

Summary: On 200 executable tasks, asynchronous delivery reduced average success from 29.7% to 26.0%. Full replanning added calls for only small delayed-result gains.

Analysis: [asynchronous event contracts](2026-10-27/reasoning.md#2-test-delayed-subagent-results-as-state-changing-events)

Core source: [Async-RBench](https://arxiv.org/abs/2610.32429v1)

Artifact: [pope8zdt/Async-RBench](https://github.com/pope8zdt/Async-RBench)

Implementable now:
- type result relations;
- compute minimal invalidation;
- score event handling separately from final success.

Implementability score: 0.82

### Retire skills from unaided capability evidence

Summary: Gain-only retirement removed more than half of uncovered skills under each tested model. Per-model unaided verdicts were more reproducible and can remain reversible.

Analysis: [skill retirement certificates](2026-10-27/reasoning.md#3-retire-a-skill-only-when-unaided-capability-is-proven)

Core source: [Beyond Gain](https://arxiv.org/abs/2610.32322v1)

Artifacts: [SkillCorpus lifecycle](https://github.com/EverMind-AI/SkillCorpus/tree/main/skillcorpus/lifecycle), [dataset](https://huggingface.co/datasets/EverMind-AI/skillcorpus-lifecycle)

Implementable now:
- test unaided capability;
- require valid skill-sensitive probes;
- soft-retire per model with restoration evidence.

Implementability score: 0.78

## Previous Daily Update: 2026-10-26

### Validate tool prerequisites before execution

Summary: StateMirror converts proposed actions into live workspace predicates. It reached 0.940 precision and 0.817 F1 on 2,508 actions at 1.50 ms median latency, then corrected more than 95% of detected calls during intervention.

Analysis: [pre-execution state validation](2026-10-26/reasoning.md#1-validate-tool-prerequisites-before-execution)

Core source: [StateMirror](https://arxiv.org/abs/2610.32648v1)

Implementable now:
- validate paths, symbols, packages, and command assumptions before execution;
- return exact mismatch evidence;
- keep dynamic runtime failures on a separate fallback path.

Implementability score: 0.89

### Fault-inject the MCP path before release

Summary: In 1,350 experiment cells, realistic MCP faults cut completion quality by 60%. Model scale did not improve retained performance, while harness behavior differed materially.

Analysis: [MCP fault injection](2026-10-26/reasoning.md#2-fault-inject-the-mcp-path-before-release)

Core source: [MCP-Injector paper](https://arxiv.org/abs/2610.32555v1)

Artifact: [MCP-Injector](https://gitlab.com/uniluxembourg/snt/sedan/papers/mcp-injector)

Implementable now:
- inject seeded timeouts, errors, drops, and payload faults in staging;
- score completion, retry, and recovery separately;
- retain synthetic-fault receipts.

Implementability score: 0.91

### Convert impasse evidence into a complete handoff

Summary: Across 19,371 trajectories, agents usually observed enough evidence to know outside help was required but often kept trying. An explicit escalation tool cut budget exhaustion from 34.0% to 6.7%.

Analysis: [evidence-based stopping](2026-10-26/reasoning.md#3-turn-sufficient-evidence-of-an-impasse-into-a-structured-handoff)

Core source: [Knowing When to Stop](https://arxiv.org/abs/2610.31895v1)

Implementable now:
- define evidence thresholds for environment blockers;
- expose a blocked terminal action;
- require blocker, progress, verification, and next authority in every handoff.

Implementability score: 0.84

## Previous Daily Update: 2026-10-25

### Give live code precedence over stale descriptive instructions

Summary: Coding agents followed stale instruction files in 90.1% of choices across 320 runs. A one-sentence precedence rule raised code-conforming choices from 4.2% to 91.4%, stopped rewrites of working code, and restored a 100% test pass rate.

Analysis: [stale instruction precedence](2026-10-25/reasoning.md#1-give-live-code-precedence-when-repository-instructions-are-stale)

Core source: [Stale Instruction Files Override the Code in Coding Agents](https://arxiv.org/abs/2610.30571v1)

Artifact: [WenJing95/stale-docs-data](https://github.com/WenJing95/stale-docs-data)

Implementable now:
- add a live-code precedence rule for descriptive conventions;
- report every detected instruction-code conflict;
- seed stale instruction fixtures in coding-agent regression tests;
- preserve safety, approval, and scope instructions as higher-authority constraints.

Implementability score: 0.97

## Previous Daily Update: 2026-10-24

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
