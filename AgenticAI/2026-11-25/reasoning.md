# Daily AgenticAI Analysis: 2026-11-25

## Thesis

Agent reliability improves when orchestration preserves completed work and evaluation separates model choice from harness choice. Recovery structure and benchmark design are both measurable parts of the agent system.

## 1. Recover the affected subgraph instead of replaying the whole run

`fork() for Agents` presents Agent-Kernel, a durable DAG runtime with nonblocking execution and Sub-Graph Recovery. A raw node failure resets the failed node and its descendants while preserving completed siblings. Parent outputs are inherited into child prompts, so recovery retains both execution state and required content.

Why it matters: whole-trajectory retry duplicates successful work, increases cost, and can exhaust a retry budget before the failed branch recovers. Across 14,434 runs on synthetic and standard benchmarks, the paper reports 100% recovery within a three-attempt budget versus 55% for whole-trajectory replay, about 10 times lower recovery time than an adapted Sherlock rollback, and up to 12.7 times speedup where the graph permits parallelism. Removing Sub-Graph Recovery reduced success to 39.4%.

Fit in the stack: the orchestrator should own a durable dependency graph, node state, retry lineage, and selective invalidation. The model can propose work, but the runtime decides what survives a failure and what must rerun.

Implementable now:
- persist node inputs, outputs, dependencies, attempts, and terminal states;
- invalidate only the failed node and its transitive descendants;
- preserve successful siblings and verified artifacts;
- inject structured failure context and the expected output schema on retry;
- compare full replay, blind node retry, and selective recovery on the same fault fixtures;
- report completed-work reuse, duplicate effects, latency, cost, and final correctness.

Evidence caveat: the headline results come from the authors' implementation, which has no linked public artifact. The paper's format-drift study is only 18 scenarios, where prompt-mutation retry recovered 14 of 18 versus 6 of 18 for blind retry.

Implementability score: 0.58

Core source: [fork() for Agents v1](https://arxiv.org/abs/2611.31727v1)

## 2. Factor model, harness, and reasoning effort in agent evaluation

ShellBench contains 100 realistic file-workspace tasks derived from more than 10 million user requests. It evaluates 12 models across five harnesses and three reasoning levels, producing 53,100 graded rollouts. Tasks mix messy files, competing evidence, correctness requirements, and safety constraints.

Why it matters: claims about a model or harness can be confounded by the other layers. ShellBench reports that model choice mattered more than harness choice in this task family, yet the top three models were within 1.1 percentage points. GPT-6 Astra passed 62.5% of attempts, while GPT-6.1 Sol passed 61.4% at about one-sixth of the estimated token cost. Harness pass@1 scores were much closer, from 42.9 to 45.2.

Fit in the stack: evaluation campaigns should treat model, harness version, reasoning level, task, grader, and artifact as separate factors. Cost-quality comparisons need the complete cell identity rather than a single leaderboard number.

Implementable now:
- run a crossed model-by-harness design on owned tasks;
- pin harness commits, model IDs, reasoning levels, environment images, and grader versions;
- preserve correctness, safety, source-use, tokens, latency, and cost separately;
- inspect per-task failures before averaging across the suite;
- keep a held-out task set to reduce benchmark contamination;
- publish the public subset with file hashes and verifier identities.

Artifact status: the Hugging Face dataset exposes 20 approved public tasks and 10,620 accepted attempts from those tasks. The paper's GitHub links did not resolve through GitHub during this scan. The dataset card assigns no license and says rights and privacy review remain required. The artifact was inspected read-only and not executed.

Implementability score: 0.88

Core sources:
- [ShellBench v1](https://arxiv.org/abs/2611.32946v1)
- [ShellBench public dataset](https://huggingface.co/datasets/OpenClaw/ShellBench)

## Scope and evidence

Both papers were submitted on 24 November and first listed on 25 November. The scan covered the newest cs.AI, cs.CL, cs.LG, cs.SE, cs.CR, cs.MA, cs.DC, and cs.HC listings, plus Hugging Face and GitHub release surfaces. External artifacts were inspected read-only. No external repository was cloned, installed, built, imported, or executed.
