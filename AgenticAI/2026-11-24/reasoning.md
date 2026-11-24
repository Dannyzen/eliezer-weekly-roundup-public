# Daily AgenticAI Analysis: 2026-11-24

## Thesis

Agent evaluation must include the runtime that serves the work and the software that grades it. A strong model or workflow can look weak under queue pressure, while a weak evaluation can award a shortcut.

## 1. Benchmark multi-agent systems under runtime pressure

MASSys holds tasks and multi-agent candidates fixed while replaying them across serving backends, hardware tiers, and request loads. The benchmark spans five workload families and records completion, usable artifact delivery, latency, cost, queueing, KV-cache pressure, and task quality.

Why it matters: evaluated-only quality can hide dropped jobs. In the paper's 2xH200 runs, SWE-bench effective quality fell from 49.33% to 11.72% when offered load rose from 0.05 to 0.10 jobs per second, while quality among evaluated jobs moved only from 64.91% to 60.71%. A workflow ranking is therefore conditional on the serving substrate and load regime.

Fit in the stack: this belongs between orchestration design and production observability. It turns the runtime, queue, model server, retry policy, tool latency, and deadline policy into part of the evaluated system.

Implementable now:
- replay identical candidate-task pairs across at least two load levels;
- report submitted, completed, execution-successful, and evaluated jobs separately;
- include P50 and P95 runtime, queue wait, timeout, token, and tool-latency metrics;
- compute effective quality over all submitted jobs, not only survivors;
- preserve traces that bind each score to the exact serving cell.

Artifact status: the Apache-2.0 repository, project page, and trace dataset resolved and were inspected read-only. The code was not cloned or executed.

Implementability score: 0.62

Core sources:
- [MASSys paper v1](https://arxiv.org/abs/2611.28671v1)
- [MASSys repository](https://github.com/MAS-Sys-Bench/MAS-Sys)
- [MASSys trace dataset](https://huggingface.co/datasets/MAS-Sys/MAS-Sys-Traces)

## 2. Treat the evaluation itself as a maintained system

Hugging Face's agentic-evaluation guide follows a task through claim definition, task selection, baseline execution, adaptation, grader testing, trace review, score reporting, and model comparison. Its worked example shows why each layer needs proof: a shortcut passed all eight tasks when the grader checked only the final ratio, then failed all eight after checks were added for the required intermediate fits.

Why it matters: agent scores combine the model, harness, environment, tools, verifier, repeated trials, and reporting choices. The guide also cites a Terminal-Bench audit where changing the harness moved accuracy by up to 29.9 percentage points with the model fixed.

Fit in the stack: this is the maintenance loop for trajectory-aware evaluation. Evaluation artifacts need versions, adversarial grader tests, repeated rollouts, trace inspection, and explicit uncertainty.

Implementable now:
- write the narrow capability claim before selecting tasks;
- run the reference solution, a no-op, and at least one shortcut against every grader;
- repeat each task and report pass@k or pass^k according to the decision;
- read successful traces as well as failures;
- publish task, environment, harness, verifier, trace, and result identities together;
- keep held-out answers private when needed while opening the surrounding methods and evidence.

Evidence caveat: the worked Raman example has eight synthetic development tasks. It demonstrates evaluation construction and failure discovery, not broad model capability.

Implementability score: 0.92

Core source: [How to build and maintain an agentic evaluation](https://huggingface.co/blog/agentic-evals)

## Scope and evidence

The arXiv scan covered the 24 November cs.MA and cs.SE listings plus recent cs.AI, cs.LG, cs.CL, and cs.CR pages. The Hugging Face source was published on 23 November. External repositories and datasets were inspected read-only. No external source code was cloned, installed, built, imported, or executed.
