# AgenticAI Daily Analysis: 2026-09-23

## Runtime reliability now lives in controlled state transitions

Today's strongest implementation signal is that agent quality depends on what the harness preserves, removes, and corrects between model calls. Faithful compaction lowers long-run cost without recursive summary drift. Failure-informed policies convert reachable solutions into repeatable delivery without changing model weights.

## Compact by deletion, never recursive rewriting

CliffCompaction reduces long-horizon context by truncating or dropping original content. It does not paraphrase retained content, and each pass starts from original material instead of compacting a previous compaction. The paper reports up to 50 percent lower cost under a bounded context, more than 10 percentage points of Terminal-Bench improvement for less than two full-context runs, and continued KernelBench optimization beyond one million tokens.

Why it matters: compaction becomes a testable state transformation rather than an opaque summary call. The key property is lineage preservation. Every retained unit still maps to original evidence, and repeated compaction cannot amplify a rewritten mistake.

Fit in the stack: context economy and long-horizon harness state.

Tools and methodologies worth exploring now:
- preserve original events outside the active prompt;
- compact only original content and discard prior compacted views;
- allow deletion and truncation while forbidding semantic rewrite in the faithful path;
- bind compaction policy, retained spans, dropped spans, token count, cost, and task result in one receipt;
- compare against full context, fixed-window retention, and ordinary summarization on the same tasks;
- stop promotion if savings reduce accepted task outcomes.

Artifact status: `nguyenvuthientrang/cliffcompaction` is a public MIT repository with a populated default branch, a Python package, OpenAI and Anthropic dialects, a proxy, and tests. It was inspected read-only and was not installed or executed in this run.

Evidence caveat: the reported gains come from Terminal-Bench and KernelBench under the authors' model and harness configurations. The API proxy needs provider credentials and operational review before production use.

Implementability score: 0.86

Core sources:
- [CliffCompaction paper](https://arxiv.org/abs/2609.26779v1)
- [CliffCompaction repository](https://github.com/nguyenvuthientrang/cliffcompaction)

## Convert observed failures into narrow runtime policies

FIRE records states that preceded observed failures, then applies targeted natural-language instructions or action denials when similar states recur. Across the complete 87-task Terminal-Bench 2.1 suite, repeated success increased in all three tested GPT-5.6 tiers. Sol rose from 64.4 percent to 73.6 percent pass-squared while best-of-two changed by 1.2 points, which supports the claim that the policy mostly improves delivery consistency rather than latent capability.

Why it matters: the harness can learn a bounded operational correction from incident evidence without modifying model weights or inflating every prompt with generic advice.

Fit in the stack: harness reliability, incident replay, and runtime policy.

Tools and methodologies worth exploring now:
- cluster failed trajectories by the exact state and procedural mistake;
- express each correction as a narrow instruction or deterministic action denial;
- match policies only at explicit runtime states;
- run a sham-policy control and generic verification control;
- measure repeated success separately from best-of-k capability;
- version policy eligibility, trigger evidence, action, and outcome;
- retire policies that stop helping on held-out incidents.

Artifact status: the public Hugging Face dataset `failproofai/fire-runtime-policy-reliability` is available under CC BY 4.0. No standalone runtime implementation artifact was identified in the paper surface.

Evidence caveat: each task has only two attempts. The study uses one English benchmark, the Codex CLI, one model family, and one reasoning effort. Model routes are provider identifiers rather than immutable checkpoint hashes.

Implementability score: 0.74

Core sources:
- [FIRE paper](https://arxiv.org/abs/2609.26048v1)
- [FIRE dataset](https://huggingface.co/datasets/failproofai/fire-runtime-policy-reliability)

## Implementation implication

Preserve raw state, derive narrow transformations from measured failure, and verify both cost and accepted outcomes. Context reduction and reliability policy belong in the harness because they need deterministic lineage, replay, rollback, and cross-model comparison.
