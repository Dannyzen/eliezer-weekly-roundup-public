# Daily AgenticAI Analysis: 2026-10-08

## Thesis

Long-running agents need explicit time control, concurrency needs selective admission, reusable skills need paired execution tests, and memory should attach to stable artifact identities.

All four papers were submitted on 2026-10-07 and first listed in the relevant arXiv categories on 2026-10-08.

## Measure time control in native harnesses

AgentTime tests whether agents can follow a requested duration, forecast runtime, and estimate elapsed time after execution. The suite contains 222 tasks from 18 benchmark families and preserves native harnesses and graders.

GPT-6 Astra ended 63% of runs within 5% of the requested duration, GPT-5.6 Sol reached 39%, and Fable 5.1 reached 4%. Among 158 classifiable reviewed runs, 14 explicitly slept after appearing to finish. Forecasts were high in 83% of Sol runs, 66% of Astra runs, and 63% of Fable runs.

Why it matters: a long-horizon agent needs runtime-owned deadlines, heartbeats, cancellation, progress evidence, and quality gates. Model self-estimates are telemetry, not authority.

Stack fit: sessionful loops, runtime governance, evaluation harnesses.

Implementable now:
- record requested, predicted, elapsed, active, idle, and blocked time separately;
- enforce deadlines and cancellation outside the model;
- test early return, overrun, sleeping, and score-versus-time behavior;
- retain native task graders alongside timing metrics.

Artifact status: the public GitHub repository was inspected read-only and reports an MIT license. The Hugging Face transcript dataset is access-gated, 419 MB, and carries benchmark-specific redistribution and training restrictions.

Caveat: each agent ran each duration condition once for most tasks, so run-to-run variance is not fully measured.

Implementability score: 0.90

Core sources:
- [AgentTime paper v1](https://arxiv.org/abs/2610.09944v1)
- [AgentTime repository](https://github.com/michaelofengenden/agenttimebench)
- [AgentTime transcript dataset](https://huggingface.co/datasets/mofengenden/agenttime-transcripts)

## Enable dynamic concurrency selectively

The dynamic-concurrency study compares native parallel sub-agent modes against sequential execution across Codex, Claude Code, and Kimi Code. Its artifact contains 2,124 trajectories. The authors reviewed 650 concurrent trajectories and recorded 804 instances across four main categories, 13 subcategories, and 28 failure patterns.

Mean runtime increased in 14 of 15 agent-benchmark combinations. On SWE-bench Verified, the Claude Code pass rate fell by 24.0 percentage points under concurrency, while its LoopsBench pass rate rose by 14.3 points. The effect depended on task horizon, decomposability, and integration quality.

Why it matters: delegation should be an earned execution mode. The main agent still owns task partitioning, file ownership, interface contracts, integration, and final verification.

Stack fit: multi-agent orchestration, governed workflow substrates, coding-agent harnesses.

Implementable now:
- enable concurrency only for independent components, diverse attempts, or evidence gathering;
- assign single-writer ownership for shared files and interfaces;
- require join deadlines, result receipts, and an integration gate;
- compare concurrent and sequential runs on task quality, elapsed time, tool calls, tokens, and merge failures.

Artifact status: the public trajectory repository was inspected read-only. It has a populated main branch and no reported license, so reuse terms remain unclear.

Caveat: long-horizon evaluation is expensive, limiting repeated stochastic runs. The paper compares specific July 2026 agent-model pairings.

Implementability score: 0.86

Core sources:
- [Dynamic concurrency paper v1](https://arxiv.org/abs/2610.10263v1)
- [Trajectory artifact](https://github.com/schwerli/Concurrency-Failures-Trajectory-Artifact)

## Admit skills through synthesized paired tests

SkillSandbox builds a novel executable scenario around each candidate skill, then compares the same scenario with and without the skill. The verifier scores executability, utility, and efficiency before issuing Keep or Reject.

Semantic retrieval exposed the relevant situation in at most 6.66 of ten selected tasks per skill. After 500 downstream tasks, 17% to 32% of skills remained unexercised, and 45% to 56% had fewer than five execution opportunities. Across ALFWorld and WebShop with three executor models, the synthesized-scenario library produced the strongest downstream performance and fewer steps.

Why it matters: a skill library is executable policy. Admission should depend on observed effect in novel scenarios, not prose quality or success on the source task.

Stack fit: skills as control, skill admission, self-improvement governance.

Implementable now:
- derive the claimed preconditions and effect from each skill;
- synthesize at least one novel positive case and one misuse or boundary case;
- run paired executions with and without the skill;
- retain effect evidence, reject reasons, and source lineage with the skill version.

Artifact status: the anonymous 4open.science snapshot was inspected read-only. It exposes code for ALFWorld, WebShop, and paired reusability verification. It is an anonymous snapshot rather than a stable named repository.

Caveat: the tested environments are bounded simulations, and scenario quality still depends on model-generated proposals and builders.

Implementability score: 0.74

Core sources:
- [SkillSandbox paper v1](https://arxiv.org/abs/2610.10088v1)
- [anonymous implementation snapshot](https://anonymous.4open.science/r/skillsandbox-647C/)

## Ground memory in stable artifact identities

ExperienceIndex stores what one artifact contributed to prior tasks and which artifact pairs were structurally related. It uses stable artifact IDs to retrieve prior analysis and adjust later search results or prompts.

Across seven datasets spanning conversation, code, scientific documents, technical documentation, multi-hop QA, tables, and text-to-SQL, the paper reports gains of up to 11.0 answer-quality points and online cost reductions of up to 50.5%. Averaged across evaluation models, it improved answer score by 3.9% over the strongest baseline and reduced online cost by 20.8% relative to baseline solutions.

Why it matters: corpus memory should preserve what was learned about a source, where it came from, and which neighboring sources matter. This is more auditable than free-floating semantic summaries.

Stack fit: memory systems, agentic search, evidence provenance.

Implementable now:
- key memory records by stable artifact ID and source version;
- separate single-artifact claims from artifact-pair relations;
- store task lineage and confidence with every learned relation;
- validate retrieved memories against current artifact versions before injection.

Artifact status: the paper provides algorithms, prompts, and implementation details, but no public implementation repository was linked from the primary paper page.

Caveat: most scoring uses LLM judges, and the default evaluation uses an 80% experience split with 20% held out. Production systems still need contradiction, staleness, and source-update tests.

Implementability score: 0.65

Core source:
- [ExperienceIndex paper v1](https://arxiv.org/abs/2610.10091v1)

## Implementation cut

1. Add runtime-owned timing telemetry and cancellation before asking models to self-budget.
2. Gate parallel sub-agents on decomposability and integration cost.
3. Test every reusable skill in a novel paired scenario before admission.
4. Anchor learned memory to versioned artifact identities and provenance.
