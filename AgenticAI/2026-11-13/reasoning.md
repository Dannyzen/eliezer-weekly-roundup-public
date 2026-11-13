# AgenticAI Daily Analysis: 2026-11-13

## 1. Delegate only when the orchestrator can preserve the evidence contract

Lost in Delegation compares single-agent search with forced delegation across purpose-built pre-cutoff and post-cutoff factual datasets. Delegation did not produce a consistent accuracy gain and more often reduced accuracy, with larger drops when the requested facts were outside the orchestrator's parametric knowledge. The recurring failures were concrete: orchestrators distorted delegated queries, executors used tools inefficiently, and retrieval failures or evidence were lost at the handoff boundary.

Why it matters: parallel workers reduce context pressure only when task decomposition preserves the actual question, evidence status, and uncertainty. A subagent answer without its query, source trail, retrieval failures, and confidence state invites the parent to overwrite fresh evidence with stale prior beliefs.

Stack fit: multi-agent orchestration and generative search.

Implementable now:
- gate delegation on subtask independence and evidence availability
- pass the source question and constraints without interpretive rewriting
- require returned sources, failed retrievals, and unresolved ambiguity
- compare delegated and direct-tool paths under equal budgets
- let the parent integrate evidence without silently replacing it with prior knowledge

Evidence caveat: the study focuses on composite factual search tasks. It does not establish that delegation is harmful for code, simulation, or artifact-producing work with independently verifiable outputs.

Artifact status: no dedicated implementation repository was identified from the primary paper. The paper and experimental details are public.

Implementability score: 0.83

Core source: [Lost in Delegation paper v1](https://arxiv.org/abs/2611.16526v1)

## 2. Train and test tool decisions against explicit task state

StateAlign constructs paired task states that differ in information availability, tool capability, or task progress, then combines outcome rewards with token-level state-contrastive reinforcement learning. Across five base models, the authors report gains on BFCL v4 multi-turn, ToolSandbox, and When2Call. On Qwen3-8B, BFCL v4 multi-turn accuracy rose from 45.5 percent to 55.2 percent, while no-tool hallucination on SimpleToolHalluBench fell from 62.2 percent under outcome-only training to 56.1 percent.

Why it matters: successful tool calling and justified tool calling are separate objectives. An agent can recognize that information is missing in its reasoning and still fabricate an argument or call an irrelevant tool. State-paired tests expose that gap directly.

Stack fit: tool-use training, harness evaluation, and action gating.

Implementable now:
- create paired fixtures for call, ask, retrieve, decline, continue, and stop states
- vary one state condition at a time
- grade action appropriateness separately from final task success
- preserve recovery cases after tool errors
- apply deterministic runtime guards even when model training is unavailable

Artifact status: the Apache-2.0 repository is public and populated with training configurations, sample data, evaluation scripts, and source modules. It was inspected read-only and was not executed.

Evidence caveat: reproducing the reported gains requires reinforcement-learning infrastructure. The state-paired evaluation pattern is much cheaper to adopt than the full training method.

Implementability score: 0.63

Core sources: [StateAlign paper v1](https://arxiv.org/abs/2611.16304v1), [repository](https://github.com/ZhexiLu/StateAlign), [model](https://huggingface.co/ZhexiLu/StateAlign-8B)

## 3. Turn memory requirements into deterministic scenario tests

AstroMemBench maps six operational challenge categories into 16 memory subchallenges across nine spacecraft tasks. Its 140 templates produce 2,240 instances, each with 30 historical interaction turns and deterministic scoring for completion, state changes, safety, and resource use. The six main configurations run on matched instances, and the paper reports that ordinary RAG was competitive with specialized memory systems in same-session tests, while Mem0 led RAG by 12.25 points after a session restart.

Why it matters: a memory benchmark becomes operationally useful when it tests history-dependent decisions rather than generic recall. The Scenario-Challenge-Capability method can be reused for client workflows: identify a real operating hazard, define the historical evidence required, and score the downstream action and side effects deterministically.

Stack fit: memory-system evaluation and embodied-agent testing.

Implementable now:
- derive memory cases from operational hazards and required capabilities
- generate matched clean, noisy, compacted, and restarted histories
- score completion, state, safety, and resource effects separately
- compare native context, RAG, and persistent memory on the same instances
- preserve deterministic scenario receipts for regression testing

Artifact status: the MIT repository is public and populated with benchmark data, evaluation code, documentation, and CI. It was inspected read-only and was not executed.

Evidence caveat: the benchmark is spacecraft-specific and uses long synthetic histories. Its reusable contribution is the test-design method, not direct transfer of the reported system ranking to enterprise agents.

Implementability score: 0.82

Core sources: [AstroMemBench paper v1](https://arxiv.org/abs/2611.16590v1), [repository](https://github.com/flyingView/AstroMemBench-v1)

## 4. Evolve memory programs under an accuracy-cost objective

MAPE treats memory construction, retrieval, and composition as a standardized programmable lifecycle. An iterative diagnosis and proposal loop evolves complete memory programs rather than tuning one component. On LoCoMo and LongMemEval, the authors report up to a 12 point absolute accuracy gain over manually designed baselines at 35 percent of the serving cost. Across runs, two patterns recurred: retain raw conversations as retrievable evidence, then process retrieved evidence through query-specific composition before answering.

Why it matters: memory architecture should be selected as a measured program, not as a fixed vendor feature. The strongest practical lesson is the objective function. Accuracy-only search added operations for marginal gains, while joint accuracy-cost search preserved cheaper candidate lineages and shifted computation toward selective query-time processing.

Stack fit: memory-system design, automated harness optimization, and cost-aware evaluation.

Implementable now:
- expose memory build, retrieve, compose, and answer stages behind stable interfaces
- retain raw evidence beside derived memories
- evaluate every candidate on fixed tasks, models, prompts, and judges
- optimize accuracy and lifecycle serving cost together
- keep candidate lineage, diagnostics, and failure attribution
- transplant successful components into existing systems before replacing the whole stack

Artifact status: the Apache-2.0 repository is public and populated with the evolution framework, baselines, evaluation harnesses, and locked environments. It was inspected read-only and was not executed.

Evidence caveat: the reported search uses LLM judges and meaningful evaluation compute. The transferable design patterns need independent workload-specific validation.

Implementability score: 0.58

Core sources: [MAPE paper v1](https://arxiv.org/abs/2611.17068v1), [repository](https://github.com/ash-ding/MAPE)

## Working conclusion

The shared pattern is state fidelity. Delegation needs lossless evidence handoffs, tool use needs explicit task-state contrasts, memory needs deterministic history-dependent tests, and architecture search needs fixed interfaces plus cost-aware receipts. More agents or more memory operations are weak substitutes for preserving the state that justifies the next action.
