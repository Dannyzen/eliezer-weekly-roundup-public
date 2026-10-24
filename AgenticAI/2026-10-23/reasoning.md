# AgenticAI Weekly Analysis - 2026-10-23

## Weekly thesis: preserve evidence before optimizing agents

The week's implementation signal is that context, tools, skills, and benchmarks are all harness objects. Model quality cannot compensate for provenance destroyed during compaction, authoritative evidence hidden during retrieval, work truncated by a completion cap, or a macro skill whose failed postcondition is never checked.

The practical stack is therefore ordered: preserve typed evidence, expose deterministic execution state, measure the harness limits, then optimize routing or models.

## 1. Preserve typed provenance through retrieval and compaction

Compaction Laundering shows a concrete trust-boundary failure. Five harnesses that flatten typed messages into labeled text preserved forged approvals 87% to 100% of the time, while four role-typed harnesses measured 0%. KEEP-Bench found that strong compressors preserved every required proposition in only 61.6% to 66.8% of 4,102 cases. Same Simulation, Different Evidence then isolated a separate retrieval failure: agents computed the right result and answered from the wrong output.

Why it matters: token savings are unsafe when a compressor changes who said something, drops a minority qualifier, or allows a derived file to displace the authoritative result.

Fit in the stack: provenance-preserving serialization and authoritative-output identity belong below retrieval, summarization, and prompt assembly. Evidence-recall tests belong beside latency and token metrics.

Implementable now:
- preserve typed roles and source IDs instead of flattening messages;
- escape in-band role labels before any text serializer;
- mark one output as authoritative and record which evidence closed the task;
- run proposition-level preservation fixtures for qualifiers, alternatives, and minority evidence;
- fail closed when a compactor cannot preserve required provenance fields.

Evidence caveat: the compaction study is a single-author preprint, and KEEP-Bench tests short inputs relative to advertised model windows. Together they still establish that compression correctness requires direct tests.

Implementability score: 0.91

Core sources:
- [Compaction Laundering v1](https://arxiv.org/abs/2610.29869v1)
- [KEEP-Bench v1](https://arxiv.org/abs/2610.26827v1)
- [KEEP-Bench repository](https://github.com/PlusLabNLP/KEEP-Bench)
- [Same Simulation, Different Evidence v1](https://arxiv.org/abs/2610.26836v1)

## 2. Treat benchmark scores as model plus harness scores

ToolBottleneckBench held tasks fixed while varying tool menus, registered catalogs, workflows, returned-state encoding, and harness budgets. Raising one completion cap sixteenfold removed most of the large-menu penalty in truncation-heavy configurations. FDE-Gym reached the opposite edge of the stack: the best configuration resolved only 14 of 95 realistic delivery tasks, even though agents sometimes found every key fact.

Why it matters: a final score can hide whether the model failed, the harness cut it off, the workflow omitted clarification, or the resulting system failed the customer's own objective.

Fit in the stack: deterministic first-failure records, frozen budgets, user interaction, and terminal outcome grading belong in the evaluation harness before model comparisons are trusted.

Implementable now:
- freeze tool menus, budgets, and completion caps in comparison runs;
- record the first unmet obligation and the harness limit that ended each episode;
- grade component completion, integration, incidents, and customer outcome separately;
- pair static tasks with clarification and changed-requirement user simulations;
- report cost and review effort alongside task success.

Implementability score: 0.86

Core sources:
- [ToolBottleneckBench v1](https://arxiv.org/abs/2610.21098v1)
- [ToolBottleneckBench repository](https://github.com/zichuanxu/tool-bottleneck-bench)
- [FDE-Gym v1](https://arxiv.org/abs/2610.22350v1)
- [FDE-Gym repository](https://github.com/deeplethe/fde-gym)

## 3. Route execution abstractions from observed state

Adaptive Skill Granularity treats micro tools, macro skills, and macro-to-micro recovery as runtime modes. LEASH applies the same principle to model routing by escalating during a computer-use trajectory rather than making one irreversible model choice at the start. PAUSE places one independent planning checkpoint immediately before the first durable source edit.

Why it matters: routing before execution lacks the most useful evidence. The runtime learns whether assumptions hold only after tools return state and macro postconditions are checked.

Fit in the stack: a small deterministic controller should sit between capability retrieval and tool execution. It should own mode choice, recovery, escalation, and the first irreversible edit gate.

Implementable now:
- give macro skills explicit preconditions, postconditions, and primitive fallbacks;
- record mode, transition reason, verifier outcome, and normalized cost;
- add one planner gate before the first durable source edit;
- start with auditable rules and shadow learned routers against them;
- retain an always-strong baseline for trajectory escalation experiments.

Evidence caveat: the adaptive-skill comparison uses 12 tasks, so its routing pattern is more mature than its generalization claim.

Implementability score: 0.78

Core sources:
- [Adaptive Skill Granularity v1](https://arxiv.org/abs/2610.31461v1)
- [Adaptive Skill Agent repository](https://github.com/Jayceon-3/Adaptive-Skill-Agent)
- [LEASH v1](https://arxiv.org/abs/2610.22280v1)
- [PAUSE v1](https://arxiv.org/abs/2610.29870v1)

## 4. Gate proactive memory on evidence and timing

ProPerMem separates evidence retrieval from intervention timing over histories averaging 618K tokens. Oracle evidence inside the correct window reached 96%, chosen timing fell to 38%, and retrieval instead of oracle evidence fell to 15%. CarryoverBench adds the security mirror: persistent instructions can re-fire across later sessions without measurable decay.

Why it matters: retrieving a relevant memory does not prove that an interruption is useful, current, or authorized. Persistence increases both utility and delayed-action risk.

Fit in the stack: memory retrieval should propose evidence. A separate policy should decide whether to surface it, interrupt, schedule work, or remain silent.

Implementable now:
- add trigger windows, cooldowns, silence grading, and expiry;
- store source, purpose, principal, trust, and revocation with persistent entries;
- separate facts and preferences from procedures and authority grants;
- test planting and triggering in different sessions;
- require current authorization before memory-derived effects.

Evidence caveat: the benchmark pattern is usable now, while reliable long-horizon retrieval and timing remain materially unsolved.

Implementability score: 0.45

Core sources:
- [ProPerAgent v1](https://arxiv.org/abs/2610.22671v1)
- [CarryoverBench v1](https://arxiv.org/abs/2610.28425v1)
- [CarryoverBench repository](https://github.com/igloomatics/CarryoverBench)

## Implementation order

1. Preserve typed roles, source lineage, and authoritative-output identity.
2. Add deterministic end-state checks and first-failure records.
3. Freeze harness budgets before comparing models or routers.
4. Add macro recovery and first-edit planning gates.
5. Pilot proactive memory only after timing, silence, expiry, and reauthorization tests exist.
