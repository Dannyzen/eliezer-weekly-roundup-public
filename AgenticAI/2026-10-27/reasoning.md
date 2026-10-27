# AgenticAI Daily Analysis, 2026-10-27

The strongest new evidence says agent quality belongs to the deployed loop, not to the model in isolation. Cross model and harness tests expose pairing failures, asynchronous tests expose stale handoffs, and skill retirement tests expose false evidence of redundancy.

## 1. Evaluate the model and harness as one deployed pair

When Agents Fail crosses four general-purpose harnesses with four core models across six benchmarks, then adds fixed native systems and stress conditions for 52,168 trajectories in 111 evaluation settings. Harness rankings changed across models and tasks. OpenCode led aggregate Cross-Model Fit on the tested balanced panel, while model-specific preferences and intermediate ranks still moved. Similar task scores also hid different valid-completion and resource-use profiles.

Why it matters: a model leaderboard cannot select a production agent stack. The same model can terminate, hand off, recover, and consume resources differently under another harness.

Fit in the stack: evaluation and release gating. Treat the model, harness, tool surface, limits, and task family as one versioned test subject.

Implementable now:
- cross candidate models and harnesses on the same task fixtures;
- record task outcome, valid completion, first failure, token load, latency, and terminal handoff separately;
- freeze model, harness, task, and policy revisions in every result;
- require pair-specific evidence before a model or harness promotion.

Caveat: OpenCode's aggregate lead is panel-dependent. The paper itself shows model-specific reversals, so this is a method for choosing a pair, not a universal winner claim.

Implementability score: 0.90

Core source: [When Agents Fail v1](https://arxiv.org/abs/2610.32483v1)

## 2. Test delayed subagent results as state-changing events

Async-RBench supplies 200 executable tasks with controlled result release and per-event response contracts. Across nine agents, delayed-result scores ranged from 19.2 to 45.1. Asynchronous delivery lowered average task success from 29.7% to 26.0%, and eight of nine agents consumed more tokens. Forced full-plan rebuilding improved delayed-result scores by only 2.6 to 3.5 points while increasing model calls by 7.5% to 10.2%.

Why it matters: a late result is not extra context. It can supersede work, invalidate checks, conflict with another result, or require no change. Replanning everything is costly and weak.

Fit in the stack: multi-agent orchestration and event-sourced runtime. Each result arrival needs a typed relation to current state and a bounded reconciliation contract.

Implementable now:
- tag handoffs as additive, superseding, conflicting, duplicate, failed, or advisory;
- bind each handoff to the source state and artifacts it assumed;
- compute the minimal invalidation set before changing work;
- rerun only checks affected by accepted changes;
- score update, preserve, no-side-effect, and re-verification behavior separately from final success.

Artifact status: the public Apache-2.0 repository contains 200 task bundles, schemas, adapters, documentation, tests, and experiment manifests. It was inspected read-only and not executed.

Implementability score: 0.82

Core source: [Async-RBench v1](https://arxiv.org/abs/2610.32429v1)

Artifact: [pope8zdt/Async-RBench](https://github.com/pope8zdt/Async-RBench)

## 3. Retire a skill only when unaided capability is proven

Beyond Gain shows why near-zero benefit is unsafe retirement evidence: both an internalized skill and a capability that fails with or without the skill can have zero gain. A published gain-band rule removed more than half of uncovered skills under each of four models. On SkillsBench, 28 of 31 retirements rested on probes no run passed fully. Unaided-level verdicts reproduced better across tasks than gain verdicts, with kappa 0.42 versus 0.23, but parallel-form reliability remained only 0.41.

Why it matters: skill libraries need reversible, per-model lifecycle state. A skill that appears useless may still encode a capability the model lacks and the current probe failed to expose.

Fit in the stack: skill registry governance. Retirement is a capability certificate, not a storage cleanup heuristic.

Implementable now:
- measure unaided capability on executable tasks before retirement;
- use another model's skill gain as evidence that the probe actually exercises the skill;
- issue retire, keep, repair, regenerate, or gather-more-evidence verdicts per model;
- soft-retire from retrieval while preserving the skill and its provenance;
- rerun certificates when models, tasks, or skill content change.

Artifact status: the MIT lifecycle code and public Hugging Face dataset resolve. The released corpus contains 1,251 skills, tasks, rubrics, and item-level scores across four models. Both were inspected read-only and not executed.

Implementability score: 0.78

Core source: [Beyond Gain v1](https://arxiv.org/abs/2610.32322v1)

Artifacts: [SkillCorpus lifecycle](https://github.com/EverMind-AI/SkillCorpus/tree/main/skillcorpus/lifecycle), [skillcorpus-lifecycle dataset](https://huggingface.co/datasets/EverMind-AI/skillcorpus-lifecycle)

## Working conclusion

Evaluate the exact deployed pair, treat delayed results as typed state transitions, and retire capabilities only from reproducible unaided evidence. Aggregate success and near-zero marginal gain both hide operational failure.
