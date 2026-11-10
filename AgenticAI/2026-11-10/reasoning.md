# AgenticAI Daily Analysis: 2026-11-10

Today's strongest implementation signal is that agent evaluation must grade whether the visible evidence supports the answer and whether orchestration improves the work under a shared budget. Cost optimization belongs below that evidence gate.

## 1. Grade evidence sufficiency before answer accuracy

Correct Answers from Insufficient Histories constructs pairs of complete histories that are compatible with the same visible prefix but produce different answers. That witness certifies that the prefix is insufficient even when a model happens to match a hidden reference.

On 203 certified-insufficient raw-prefix instances, Qwen3-32B and DeepSeek-V4-Flash produced concrete answers on 196 and 182 instances. They matched 87 and 85 hidden references, respectively. Those matches are unsafe evaluation positives: a correct-looking answer does not prove that the visible trajectory supports it.

Why it matters:
- final-answer accuracy can reward unsupported guessing;
- retrieval relevance is weaker than evidence sufficiency;
- judge scores can remain high while support errors persist;
- memory and trajectory benchmarks need an explicit abstention path.

Use now:
- generate two valid complete histories with the same visible prefix and different answers;
- label the prefix insufficient when both histories satisfy the environment rules;
- grade support, correctness, and abstention separately;
- keep deterministic witness checks ahead of LLM judges;
- retain the witness pair as part of the evaluation receipt.

Artifact caveat: the study says the retained artifact is not released as an anonymous public artifact. The method is implementable from the paper, but the exact study package is unavailable for independent replay.

Implementability score: 0.86

Core source: [Correct Answers from Insufficient Histories](https://arxiv.org/abs/2611.11840v1)

## 2. Measure orchestration as its own capability

WorkflowArena evaluates 145 long-horizon tasks across 8 domains and 17 task forms. Agents author executable worker workflows under the same wall-clock budget used for execution, while the benchmark records every delegation and verifies the integrated deliverable.

Across 25 configurations of nine models, the strongest system resolved 36.95 percent of tasks on average. The fixed-executor transfer experiment is the more durable contribution: it separates the quality of the authored workflow from the strength of the workers that execute it.

Why it matters:
- end-to-end success hides whether delegation helped;
- orchestration time and coordination cost must count against the same budget;
- fixed workers make workflow quality comparable across source models;
- delegation traces expose organization patterns that final scores miss.

Use now:
- define integrated tasks with interdependent artifacts;
- charge planning, delegation, and execution to one budget;
- record worker prompts, dependencies, revisions, and integration steps;
- compare authored workflows with fixed executors;
- require hidden final-state or artifact verifiers where possible.

Evidence caveat: each configuration ran once per task, so close rankings have no variance estimate. Claude and GPT systems used different harnesses, and some content and 3D tasks used LLM judges without measured human agreement. The public repository is populated, but GitHub reports no top-level SPDX license.

Implementability score: 0.74

Sources: [WorkflowArena paper](https://arxiv.org/abs/2611.12856v1), [public benchmark repository](https://github.com/Einsia/WorkflowArena), [project page](https://lab.einsia.ai/workflowarena)

## 3. Put cost optimization in a harness interposition layer

System Optimizations for Cost-Efficient Agent Harnesses profiles cost accumulation across agent traces, then proposes Agency as an interposition layer over context, tools, and environments. The paper reports proof-of-concept reductions of up to 35 percent with marginal accuracy loss.

The practical abstraction matters more than the headline maximum. Harness-side optimization can observe and transform repeated context, tool outputs, and calls without changing the model. That makes cost policy testable across models and harnesses.

Why it matters:
- input context dominates many long runs even with caching;
- tool-call economics are not captured by token count alone;
- deterministic transformations are easier to audit than model-prompted cleanup;
- one interposition API can support comparable experiments across harnesses.

Use now:
- trace cache reads, cache writes, uncached input, output, and tool charges separately;
- identify repeated context and redundant calls before adding a learned router;
- apply one optimization at a time behind a feature flag;
- compare cost, success, latency, and failure shape on repeated tasks;
- fail open to the unoptimized harness when a transform is uncertain.

Artifact caveat: no public Agency repository resolved from the paper or GitHub search. The 35 percent result is an upper bound across proof-of-concept techniques, not a guaranteed fleet-wide saving.

Implementability score: 0.62

Core source: [System Optimizations for Cost-Efficient Agent Harnesses](https://arxiv.org/abs/2611.12122v1)

## Working conclusion

Evaluation should first prove that the visible evidence supports the answer, then measure whether the workflow improves outcomes under a shared budget. Cost optimization comes last, through a reversible harness layer with accuracy and failure-shape gates.
