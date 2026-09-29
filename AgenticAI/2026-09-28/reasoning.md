# AgenticAI Daily Analysis - 2026-09-28

Monday's arXiv listing exposes the Friday, 25 September submission batch. The strongest implementation signals are provenance-aware memory admission, counterfactual workflow pruning, and trained search over large tool catalogs.

## Admit shared memory only after lineage-aware evidence

The Correlated Promotion Benchmark separates claim repetition from independent corroboration. CPB-Static freezes source-labelled admission decisions. CPB-Live records writes, retrievals, source lineage, and downstream answers from a shared store. Across four agent families, uncontested false claims were repeated in 0.97 to 0.99 of probes. A declared-source-type gate reduced false adoption to 0.06 to 0.09, compared with 0.22 to 0.47 for the other answering policies.

### Why it matters

Repeated agreement inside one retrieval lineage is one piece of evidence, not a vote. Shared memory needs a write gate that counts independent sources and preserves who copied whom.

### How it fits

This strengthens memory systems and memory authority. It supplies an evaluation fixture for the admission boundary that earlier memory work treated mainly as policy.

### Practical tools and methodologies

- Store claim, source class, parent claim IDs, writer, retrieval IDs, and admission decision together.
- Collapse paraphrases and copies onto one provenance root before counting support.
- Test uncontested false beliefs, competing truths, and repeated correlated agreement separately.
- Keep contest, demote, and supersede operations even though this paper did not evaluate correction.
- Use the public MIT repository as a fixture source, while treating withheld transcripts and run summaries as an evidence gap.

Evidence caveat: CPB-Live uses authored fictional scenarios, reports descriptive results without hypothesis testing, and human-checks each LLM grader on 120 items. Correction operations were not evaluated.

Artifact status: `lxy1134/iclr_2027` has a populated `main` branch, MIT license, source, tests, data, freeze hashes, and reproduction scripts. Transcripts and run summaries are withheld until acceptance.

Implementability score: 0.88

Core source: [A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory](https://arxiv.org/abs/2609.30813v1)

Supporting source: [lxy1134/iclr_2027](https://github.com/lxy1134/iclr_2027)

## Skip workflow components only with counterfactual evidence

Learning What to Skip treats planner, executor, verifier, and summarizer omission as a causal decision. Controlled skip interventions label whether each component was useful in the state where it would have run. Action-specific skip-safety models then combine held-out calibration, domain guards, and fall-through to later decisions.

Across Qwen2.5-7B and Mistral-7B on MATH, GSM8K, MMLU, and MBPP, the paper reports 8.6 to 31.2 percent token savings while preserving or improving aggregate full-workflow accuracy. Agreement is not a safe shortcut: one MMLU example had two executors agree on the wrong answer before the verifier corrected them.

### Why it matters

Always running every role wastes tokens. Heuristic skipping risks removing the one step that repairs a shared error. Counterfactual interventions provide the missing evidence.

### How it fits

This belongs in multi-agent orchestration and model-router governance. A component skip is a route decision inside a workflow, so it needs calibration and fallback just like model selection.

### Practical tools and methodologies

- Collect full-workflow traces plus controlled single-component omissions.
- Train skip policies per action instead of one global confidence threshold.
- Calibrate on held-out tasks and keep domain invariants as hard guards.
- Fall through to the next component when a skip decision is uncertain.
- Record tokens saved, task outcome, and component-specific regressions together.

Evidence caveat: the study uses a fixed five-role topology, two 7B model families, and saved single-component interventions. One MMLU item degraded despite unchanged aggregate accuracy.

Artifact status: the paper mentions supplementary code and trace scripts, but no independently resolvable public repository was found.

Implementability score: 0.83

Core source: [Learning What to Skip](https://arxiv.org/abs/2609.30734v1)

## Train tool search against confusing neighbors and full trajectories

ToolSearcher targets catalogs where sending every schema to the model is impossible. Its reinforcement-learning objective combines category-constrained discrimination among similar tools, event-level rewards when the target tool is discovered during multi-turn search, and trajectory-level credit across search and final selection.

StableToolBench contains 16,464 APIs. On Qwen2.5-7B, ToolSearcher reports overall F1 of 0.513 versus 0.496 for the strongest comparator. On out-of-distribution AppWorld, average task-goal completion is 0.334 versus 0.277.

### Why it matters

Large catalogs fail through near-neighbor confusion and search policy, not only weak embeddings. Training needs to reward the search path that exposes the right tool and the final choice that uses it.

### How it fits

This extends agent discovery into tool-catalog routing. Retrieval, disambiguation, and downstream execution belong in one evaluation record.

### Practical tools and methodologies

- Index tool descriptions by category and retrieve hard negatives from the same category.
- Reward target-tool discovery at the event level, then grade final task completion separately.
- Evaluate out of distribution with a stateful environment such as AppWorld.
- Keep catalog revision, retrieved candidates, selected tool, arguments, cost, and outcome in the trace.
- Treat the public repository as research code until its missing detected license is resolved.

Evidence caveat: training combinations are mainly synthetic and parallel, not stateful sequences. Training is capped at eight search turns, while AppWorld scenarios average more than eight APIs. Results cover Qwen 4B and 7B backbones.

Artifact status: `zhenlongDai/ToolSearcher` has a populated `main` branch with training, retrieval, inference, and evaluation scripts. No release tags or detected repository license were found.

Implementability score: 0.72

Core source: [ToolSearcher](https://arxiv.org/abs/2609.30906v1)

Supporting source: [zhenlongDai/ToolSearcher](https://github.com/zhenlongDai/ToolSearcher)
