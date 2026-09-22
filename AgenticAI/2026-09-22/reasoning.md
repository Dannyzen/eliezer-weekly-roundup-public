# AgenticAI Daily Analysis - 2026-09-22

## Select regression tasks from prior trajectories, not convenient examples

A full agent benchmark is too expensive to run after every model, prompt, configuration, or harness change. The trajectory-aware subset study treats prior execution traces as a test-selection signal. It groups benchmark instances by historical outcome, sanitizes explicit result leakage from trajectories, embeds the remaining behavior, then deterministically selects instances nearest each outcome-group centroid.

The study evaluates 76 selection configurations over 31,779 trajectories from 58 runs and five agent frameworks. A 10 percent subset reduced measured token consumption from 3.44 billion to 345 million while keeping median resolve-rate estimation error below 5 percent and worst-case error below 10 percent. Against typical baseline draws, the method reduced worst-case error by 4 to 11 percentage points.

Why it matters: cheap evaluation sets should preserve observed agent behavior, not only task labels or random samples. The result turns historical traces into a reusable regression-testing asset while retaining periodic full-suite runs as the calibration source.

Practical tools and methods worth exploring now:
- collect normalized trajectories and final outcomes from full benchmark runs;
- remove explicit pass, fail, repository, and instance identity leakage before embedding;
- stratify by historical outcome, then select deterministic behavioral centroids;
- freeze task IDs, selector inputs, source-run identity, and expected error bounds in the regression receipt;
- compare the small set against later full runs and recalibrate when error or model behavior drifts;
- keep a full-suite release gate because a subset estimates aggregate resolve rate rather than proving every capability.

Artifact status: the public SAILResearch repository has a populated main branch with the parsing pipeline, selectors, results, reproduction entrypoint, requirements, and supporting data. It was inspected read-only and was not cloned or executed.

Evidence caveat: the datasets are code-repair benchmarks built from GitHub issues. Historical full runs are required before selection, and sanitized traces still retain pass or fail predictive signal through task-related words.

Implementability score: 0.88

Core sources:
- [Trajectory-aware subset paper](https://arxiv.org/abs/2609.24928v1)
- [Public repository](https://github.com/SAILResearch/swe-agent-subset-selection)

## Evaluate memory by future effects, cost, and latency

DolphinBench replaces recall questions with 600 action tasks across three simulated knowledge-work personas. Each persona has roughly 500,000 user-message tokens and 200 tests. A test is admitted only after an agent passes twice with the relevant history and fails twice without it. Evaluation then grades tool choice, target, arguments, and content, while also reporting total ingestion and test cost plus task latency.

The released leaderboard covers 13 system configurations. Hermes with GPT 5.6 Luna and Mem0 completed 70.7 percent of tasks at USD 96.21 total cost, compared with 65.7 percent at USD 61.48 for built-in memory. The ranking changes across models and harnesses, and some external memory systems reduce accuracy for specific personas. Memory quality is therefore a system property, not a provider leaderboard.

Why it matters: a memory layer is useful when it changes later actions correctly at an acceptable operational cost. Retrieval precision alone cannot prove that the model notices the memory, applies it to the right effect, or avoids stale and irrelevant influence.

Practical tools and methods worth exploring now:
- construct future tasks whose correct side effect depends on one buried historical rule;
- certify each task with paired oracle-history and no-history runs;
- grade exact tool effects, not recall prose;
- report accuracy, ingestion cost, test cost, median latency, and tail latency together;
- compare built-in, file-backed, and provider memory under the same model and harness;
- pin histories, simulated app state, graders, pricing inputs, and run traces by release hash.

Artifact status: the Apache-2.0 mem0ai/dolphinbench repository has a populated main branch with histories, tests, simulated MCP applications, graders, results, methodology, and a pinned release hash. The project site exposes the dataset and official results. Both were inspected read-only.

Evidence caveat: Mem0 created the benchmark and is one evaluated memory vendor. The histories are synthetic, all 600 tests cover three personas, and official configurations combine memory, model, provider, and harness differences.

Implementability score: 0.82

Core sources:
- [DolphinBench paper](https://arxiv.org/abs/2609.24971v1)
- [DolphinBench repository](https://github.com/mem0ai/dolphinbench)
- [DolphinBench project and results](https://dolphinbench.ai/)

## Distill harness behavior into the model before deployment

Harness-Zero uses an optimized harness as a temporary teacher. A separate harnessing agent reviews and corrects student responses in the target harness action space, producing supervised fine-tuning trajectories. The deployed model then runs under one fixed minimal harness without the specialized teacher or evolved harness.

Across spreadsheet work, multi-application tool use, and retrosynthesis, the reported Qwen3.5-9B macro-average task success rose from 23.3 percent to 44.3 percent after distillation. The same base model reached 41.7 percent with the specialized harness still attached. The distilled model recovered 82.3 percent of 28 harness-induced behavior patterns that were absent from the base model.

Why it matters: harness optimization can become a training-data compiler instead of permanent runtime baggage. This creates a path for transferring useful skills, validation habits, and tool-use procedures into a smaller fixed deployment surface.

Practical tools and methods worth exploring now:
- freeze a minimal target harness before data collection;
- treat an optimized harness as private teacher context rather than deployable authority;
- translate teacher guidance into corrections expressed in the student action space;
- filter reviewed rollouts, then train and evaluate with the teacher removed;
- retain per-pattern recovery tests and task-level held-out results;
- compare distilled behavior against the base model, attached-harness model, and stronger-model trajectory controls.

Artifact status: the Apache-2.0 public repository has a populated main branch with source, data, environments, tests, harness bank, pyproject, and uv lockfile. It was inspected read-only and was not cloned, installed, or executed.

Evidence caveat: the method depends on a strong harnessing model, uses LoRA fine-tuning, and adds one review model call per proposal during collection. The paper reports 2.4 times mean latency in one collection setting, and some harness mechanisms such as context management do not translate cleanly into student responses.

Implementability score: 0.52

Core sources:
- [Harness-Zero paper](https://arxiv.org/abs/2609.24974v1)
- [Harness-Zero repository](https://github.com/metaevo-ai/harness-zero)
