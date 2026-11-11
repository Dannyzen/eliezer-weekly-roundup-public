# AgenticAI Daily Analysis: 2026-11-11

The strongest implementation signal is that durable agent state should stay inspectable: lessons need links to source trajectories, context replacement needs an ordinary persistent workspace, and evaluation must inspect the finished work product.

## 1. Link every reusable lesson to its source trajectory

WikiTrace addresses memory-induced degradation, where an agent fails a task it solves without memory because a stored lesson is wrong, incomplete, or misapplied. It stores a short insight, a compilation explaining the source run, and the raw trajectory as linked layers. During execution, the agent can descend into those layers when an insight conflicts, lacks details, or came from a failed run.

Across five benchmarks and eight suites, WikiTrace averaged 90.2 versus 87.0 for the same insights without source access and 79.5 with no memory. It reduced Regression, the share of tasks harmed relative to no memory, from 6.5 percent for insights alone to 4.5 percent. The experiment used three trials per suite. This is strong evidence for inspectable provenance, though it still uses one main agent setup and model family.

Why it matters:
- summaries are claims, not evidence;
- memory quality needs separate Gain and Regression measures;
- source descent can correct a lesson without rebuilding the memory store;
- read-only trajectory mounting keeps evidence available without allowing history rewriting.

Implementable now:
- store each memory item with source trajectory ID, outcome, compiler version, and content hash;
- expose source evidence read-only through ordinary file search;
- trigger source descent on conflict, missing detail, failed-source provenance, or action failure;
- measure memory Gain and Regression against the same no-memory task set;
- inspect the Apache-2.0 WikiTrace repository read-only before any isolated evaluation.

Implementability score: 0.88

Artifact status: contents inspected read-only. The public Apache-2.0 repository includes benchmark configs, resumable trials, stale-memory fingerprint checks, and analysis commands. No external code was executed.

First listed: 2026-11-11. Submitted: 2026-11-10 16:46:59 UTC.

Core sources: [paper v1](https://arxiv.org/abs/2611.14320v1), [repository](https://github.com/yukyeongleee/wikitrace)

## 2. Treat a persistent workspace as the model's memory interface

CAMG-II gives every long-horizon environment ordinary Bash access plus an episode-private workspace that survives context replacement. CAMP-II then uses on-policy distillation to teach 4B and 9B policies when to write, revise, search, and reuse files. The key design claim is practical: teachers and students already understand file operations, so the memory interface starts with a useful shared prior.

The trained 9B policy scored 38.0 on Terminal-Bench 2.1 and 30.1 on SWE-Bench Pro V2, compared with 33.8 and 27.4 for Qwen3.5-35B-A3B. The 4B policy improved by 6.9 points on both external suites over its starting model. On the five internal CAMG-II environments, CAMP-II achieved 2.97 times the gain of the strongest on-policy distillation baseline.

Why it matters:
- context replacement becomes a state-management problem rather than a prompt-length problem;
- plain files support inspectability, search, revision, and model transfer;
- hidden verifier materials remain outside the writable workspace;
- learned write and read policy can improve smaller models without inventing a new memory tool language.

Implementable now:
- give each run a private, persistent workspace across context compaction;
- standardize notes, evidence, plans, and receipts as files with stable paths;
- keep hidden tests and authority-bearing state outside that workspace;
- evaluate file-memory behavior with content interventions, not only final success.

The full training method is expensive and architecture-heavy. The paper covers students only up to 9B and one frozen teacher, and no public implementation artifact resolved from the paper.

Implementability score: 0.46

Artifact status: paper verified; public implementation unresolved. No external code was executed.

First listed: 2026-11-11. Submitted: 2026-11-10 12:49:24 UTC.

Core source: [paper v1](https://arxiv.org/abs/2611.14009v1)

## 3. Grade the rendered deliverable, not the chat transcript

Google DeepMind and Artificial Analysis released the Multimodal Knowledge Agent benchmark for professional work over schematics, scans, tables, images, and mixed project files. The full benchmark has 200 private tasks across 10 verticals and 83 occupations. Each task represents three to eight hours of expert work and uses a rubric averaging about 70 checks, weighted 75 percent toward factual accuracy and 25 percent toward visual design.

Every model runs in the same open-source Stirrup harness with the same tools, sandbox, and turn budget. An agentic grader opens the submitted files, renders pages, inspects spreadsheet formulas, and applies the rubric. Ten public tasks are available for format inspection and local adaptation, while the private set limits search and training leakage.

Why it matters:
- professional agent quality lives in the PDF, deck, spreadsheet, image, or report produced;
- common harnesses reduce confounding between model and tool environment;
- private evaluation plus public examples balances leakage resistance with implementability;
- factual and visual quality need separate rubric dimensions.

Implementable now:
- adapt the ten public examples into delivery-surface regression fixtures;
- render every artifact and inspect formulas, links, typography, and source use;
- pin one harness, tool set, sandbox policy, turn budget, and grader version;
- retain rubric-level evidence instead of one aggregate score.

Implementability score: 0.82

Artifact status: public dataset URL resolved; MIT Stirrup repository contents inspected read-only. The full 200-task benchmark remains private. No external code was executed.

Released: 2026-11-10.

Core sources: [Google announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/), [benchmark methodology](https://artificialanalysis.ai/articles/google-deepmind-multimodal-knowledge-agent), [public task sample](https://huggingface.co/datasets/google/multimodal-knowledge-agent), [Stirrup](https://github.com/ArtificialAnalysis/Stirrup)

## Working conclusion

Use inspectable state at every layer. Link lessons to raw evidence, preserve run state in ordinary private workspaces, and grade the delivered artifact under a pinned harness. Training a model to use files is promising, but the first practical gains come from making those files and their evaluations explicit now.
