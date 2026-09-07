# AgenticAI Daily Analysis - 2026-09-07

## Freshness and selection

arXiv exposed a real Monday, 7 Sep 2026 listing batch. The four selected v1 papers were submitted on 3 or 4 Sep UTC and first listed after the weekend. Hugging Face Daily Papers and GitHub search were used as discovery signals; claims below come from immutable arXiv records, PDFs, and read-only artifact inspection. No external repository was cloned, installed, built, imported, or executed.

## Memory migrations are model migrations

"Does Your Agent's Memory Survive a Model Upgrade?" tests one history represented four ways: verbatim long context, RAG chunks, model-compressed notes, and a fixed-schema knowledge graph. Across 48 synthetic histories and two open-weight models below 10B parameters, the fixed schema changed by only +0.0004 +/- 0.0020 after a writer swap. Natural-language notes moved asymmetrically by +9.91 or -13.28 percentage points depending on migration direction. A 50/50 mixed embedding index recovered only 4.96 points of the 11.90-point gain from full re-embedding.

Why it matters: keeping the database is not preserving memory behavior. Writer identity, reader identity, embedding space, schema, and raw evidence are part of the memory version. A provider upgrade without a migration test can silently change recall even when every row remains present.

Fit in the stack: memory systems and release engineering. The memory store needs an explicit compatibility matrix, not only backup and restore.

Practical tools and methodologies worth exploring now:
- retain raw source histories beside derived notes and graphs;
- bind every memory object to writer model, reader model, embedding model, vector size, schema version, and source IDs;
- forbid mixed embedding spaces unless a measured migration window explicitly allows them;
- run direction-specific old-writer/new-reader and new-writer/old-reader tests;
- compare store-only repair against repair from retained evidence.

Evidence caveat: the study is synthetic, uses 48 histories and two sub-10B models, and exposes no public implementation repository in the primary paper surfaces. It establishes a migration failure mode, not a production prevalence estimate.

Implementability score: 0.77

Core source: [Memory Portability, arXiv:2609.05339v1](https://arxiv.org/abs/2609.05339v1)

## Skill evolution needs frozen snapshots and provenance

"From Interaction Traces to Persistent Skills" converts GUI trajectories and evaluator feedback into a versioned skill library. Each iteration executes against a frozen snapshot; accepted creates, edits, deletes, or preserves appear only in the next iteration. Against a configuration-matched empty-library control, the full system reports higher post-warm-up evaluator scores in all four observed OSWorld domain runs, with mean differences from 5.7 to 18.6 percentage points.

Why it matters: online skill learning is safer when execution and mutation are separated. A live rollout should not rewrite the procedure currently controlling that rollout. Provenance and next-iteration exposure create a reviewable boundary.

Fit in the stack: skills as control plus procedural memory. The reusable object is not a prompt fragment. It is a versioned procedure with source traces, accepted-change evidence, and rollback identity.

Practical tools and methodologies worth exploring now:
- freeze the skill snapshot for each run and record its digest;
- extract structured facts from traces before proposing a skill mutation;
- require provenance, scope, and validation evidence on create, edit, delete, and preserve operations;
- compare every evolving-library run with an empty-library or frozen-library control;
- treat repeated revision without task recovery as a stop signal, not progress.

Artifact status: the public repository contains prompts, JSON schemas, and example skills in a populated branch. It has no GitHub license metadata, and full OSWorld experiments still require the environment and model services. The repository was inspected read-only.

Implementability score: 0.72

Core sources:
- [Persistent Skills, arXiv:2609.04869v1](https://arxiv.org/abs/2609.04869v1)
- [LongtaoHu/Skill-Evo4GUI](https://github.com/LongtaoHu/Skill-Evo4GUI)

## Harness choice dominates multi-harness RL claims

"What Does Multi-Harness RL Learn?" replays the same frozen task-harness records from Aider, OpenHands, Qwen Code, and SWE-agent from one Qwen3-8B warm start. Across 24,000 sealed evaluations, changing the evaluation harness moved mean solve rate from 2.14% to 9.27%, a 4.3x difference. Changing the cross-harness versus within-harness GRPO grouping moved it by only 1.16x. On a held-out minimal harness, Cross minus Within was +0.25 percentage points with a 95% confidence interval from -0.48 to +1.02.

Why it matters: multi-harness training can learn configuration adaptation that looks like general capability when evaluated through familiar wrappers. A held-out harness is an acceptance test for portability, not an optional ablation.

Fit in the stack: agent harness architecture, training governance, and trajectory evaluation. Harness identity belongs in the dataset and model card.

Practical tools and methodologies worth exploring now:
- record harness name, version, prompt, tool schema, parser, timeout, and retry policy on every trajectory;
- replay the same checkpoint across source and held-out harnesses;
- report the reward-group boundary explicitly;
- separate harness attribution from task capability with an out-of-fold classifier;
- use task-clustered inference and repeated attempts when runtime nondeterminism is material.

Evidence caveat: the study centers on one Qwen3-8B warm start and SWE-bench Verified. No study-specific public artifact resolved from the primary paper surfaces. Reproducing the full 24,000-evaluation design is operationally expensive.

Implementability score: 0.58

Core source: [Multi-Harness RL, arXiv:2609.04518v1](https://arxiv.org/abs/2609.04518v1)

## Working conclusion

Memory, skills, and RL policy do not transfer independently of their readers and harnesses. Freeze the representation and execution contract, test the migration direction, and require a held-out runtime before calling a capability portable.
