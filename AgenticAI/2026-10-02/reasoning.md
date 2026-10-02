# Daily Agent Research: 2026-10-02

## Compile recurring multi-agent work into code

GitHub Dynamic Workflows put deterministic orchestration inside a Copilot extension. A program defines commands, tool calls, service calls, sequential or parallel agent stages, structured handoffs, review checkpoints, and resume behavior. Agents remain responsible for analysis and judgment, while code owns the repeatable control flow.

### Why it matters

This is a practical boundary between ordinary automation and agentic work. The workflow can collect evidence, fan work out, join structured results, pause for review, and resume without asking one model to remember the process. GitHub exposes creation, monitoring, resumption, scheduling, and AI-credit limits in the product surface.

### Fit in the stack

Dynamic workflows belong in orchestration and harness architecture. They make the execution graph a program artifact rather than an implicit prompt convention. The preview is available across Copilot plans, though Copilot CLI requires experimental mode and the surface can still change.

### Practical tools and methodologies worth exploring

- GitHub Copilot CLI dynamic workflows in experimental mode
- Copilot extensions as versioned workflow packages
- typed stage outputs and deterministic joins
- explicit parallel branches, review checkpoints, and resume points
- per-run AI-credit limits and terminal receipts
- paired runs against the current prompt-only process

Artifact status: official public preview and documentation verified. The feature was not run in this cron.

Implementability score: 0.90

Core sources:
- [Dynamic workflows release](https://github.blog/changelog/2026-10-01-dynamic-workflows-in-copilot-cli-and-the-copilot-app/)
- [Using dynamic workflows](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-dynamic-workflows)

## Evaluate the model, harness, tools, prompt, and budget as one system

Agents Are Systems, Not Models varies task information, reasoning, self-verification instructions, time budget, and backbone model across four scientific coding tasks. About 54 percent of outcome variance came from repeated runs of the same configuration. Task information mattered more than model size or time budget, and a dedicated verification tool changed verification behavior more than an instruction to self-verify.

### Why it matters

A model leaderboard cannot answer whether a deployed agent is reliable. The unit under test is the complete configuration, including the evidence supplied, the tools available, the budget, and run-to-run variance. More time helps only when the model and information are sufficient to use it.

### Fit in the stack

This strengthens the model-harness pair thesis with a concrete factorial evaluation method. It belongs in harness design and trajectory-aware evaluation: treat configuration dimensions as experimental factors, repeat each cell, and inspect behavior traces rather than relying on final scores.

### Practical tools and methodologies worth exploring

- factorial model, harness, information, tool, and budget sweeps
- repeated runs per configuration cell
- variance decomposition before leaderboard claims
- dedicated verification tools instead of verification-only prompts
- public trajectory corpora for behavior-taxonomy development

Artifact status: the public repository contains only a README and says full code and benchmark are coming soon. The linked Hugging Face dataset is public and ungated, with more than 18,000 trajectories reported by the paper.

Evidence caveat: the benchmark has four astrophysics and genomics tasks and three Qwen3.5 model sizes. Its configuration effects should be tested on other domains and models before generalization.

Implementability score: 0.82

Core sources:
- [Agents Are Systems, Not Models](https://arxiv.org/abs/2610.01618v1)
- [research repository](https://github.com/lusxvr/rethinking-agent-evaluation)
- [agentic science trajectories](https://huggingface.co/datasets/lusxvr/agentic-science-trajectories)

## Intervene on retrieval before using memory utility

Causal Memory Policy identifies a blind spot in memory optimization. A memory that is never retrieved cannot reveal its effect through store-level comparisons. On LongMemEval and LoCoMo, this identification failure affected 54 percent and 67 percent of required memories. Reserving retrieval slots with known sampling propensities improved required-versus-non-required discrimination from 0.54 to 0.66 AUC.

### Why it matters

A memory policy can delete useful records because its own retriever never exposed them. Logging memory operations does not reveal this failure. Evaluation needs randomized retrieval exposure, known propensities, and a separate decision rule for irreversible retention changes.

### Fit in the stack

CMP belongs between memory retrieval and retention policy. Raw events stay canonical. A bounded exploration lane exposes candidate memories, a causal estimator scores observed query utility, and a separate policy decides whether evidence is strong enough for deletion or consolidation.

### Practical tools and methodologies worth exploring

- fixed exploration slots in retrieval payloads
- logged sampling propensities and inverse-propensity estimates
- no-delete controls and reversible demotion before deletion
- per-query utility reports separated from future-query retention value
- LongMemEval and LoCoMo tests with retrieval intervention enabled and disabled

Artifact status: the paper-linked 4open.science snapshot resolved and was inspected read-only. It exposes pinned requirements, scripts, configs, raw results, manifests, and offline analysis files. Regenerating raw draws needs API keys and the README estimates about $195 in API cost; the artifact was not cloned or executed.

Evidence caveat: identified utility reached 0.78 AUC for the query on which it was estimated, but no tested aggregation predicted value on unseen queries. CMP improves measurement; it does not solve long-term retention.

Implementability score: 0.68

Core sources:
- [Causal Memory Policy](https://arxiv.org/abs/2610.02070v1)
- [paper-linked implementation artifact](https://anonymous.4open.science/r/cmp-release-D0C3/)

## Working conclusion

Compile stable control flow into code, evaluate the complete deployed configuration, and instrument memory exploration before optimizing retention. The common rule is to expose hidden system choices as versioned, testable factors.
