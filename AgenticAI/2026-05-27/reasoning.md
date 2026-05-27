# AgenticAI Daily Scan: 2026-05-27

Today’s AgenticAI signal is about routing before execution. Retrieval agents should route configuration per query instead of paying a fixed RAG tax, and skill systems should manage procedural knowledge as a lifecycle with creation, memory, selection, evaluation, and refinement. The common theme is that the harness has to decide what machinery deserves to influence this run before the model spends tokens or executes tools.

## Per-query retrieval configuration beats fixed RAG pipelines

BRANE reframes retrieval-agent routing from “which model should answer?” to “which full retrieval configuration should this query use?” The configuration includes the LLM, retriever, document count, hop count, and synthesis strategy. The paper’s reported result is strong: across MuSiQue, BrowseComp-Plus, and FinanceBench, per-query configuration can match the best fixed configuration’s accuracy at up to 89% lower cost.

Why it matters: most production RAG systems still pick one workload-level configuration and apply it to every query. That overpays for easy questions, under-builds for hard questions, and hides the fact that retrieval cost is a runtime policy problem. BRANE’s practical pattern is a pipeline catalog plus a lightweight correctness predictor. The router chooses the cheapest configuration that is likely to answer correctly, or the highest-quality configuration under a budget.

How it fits the stack: this belongs in the agentic search and model-routing layer. It is not only retriever selection. It is harness policy over the whole search/synthesis path.

Implementable now:
- define a small catalog of retrieval configurations: lexical only, vector, hybrid, multi-hop, reranker, long-context synthesis, cheap model, strong model;
- log query features, selected configuration, cost, latency, answer quality, and failure class;
- start with deterministic rules and a simple classifier before training a learned router;
- add an escalation cascade when cheap retrieval returns no evidence or low confidence;
- report success-versus-cost Pareto curves instead of one top-line answer score.

Tools, repos, and methodologies worth exploring:
- BM25/ripgrep plus vector hybrid retrieval, LangGraph/LlamaIndex query pipelines, LiteLLM cost telemetry, OpenTelemetry traces, Pydantic schemas for route decisions, FinanceBench/BrowseComp-style held-out tasks, post-retrieval cascades from production RAG practice.

Implementability score: 0.84

Core source: [Natural Language Query to Configuration for Retrieval Agents](https://arxiv.org/abs/2605.27361)

## Skill systems need lifecycle management, not just skill files

MUSE-Autoskill packages the next stage of the skills trend: skills should be created on demand, stored, selected, tested, refined, and transferred across agents. The useful part is not “let the agent write more markdown.” The useful part is treating each skill as a long-lived asset with its own memory, runtime feedback, unit tests, reuse history, and refinement loop.

Why it matters: yesterday’s CODESKILL and Skill Shadowing result made the bottleneck clear. Skills can help, but larger libraries also create wrong-skill selection failures. MUSE-Autoskill adds the lifecycle vocabulary needed to keep that from becoming uncontrolled self-editing: creation, memory, management, evaluation, and refinement.

How it fits the stack: this belongs in the procedural-memory and skills-as-control layer. Skills become a governed library, not a passive prompt pile.

Implementable now:
- require every high-value skill to declare intent, prerequisites, allowed tools, side effects, validators, and failure modes;
- keep per-skill memory: successful uses, rejected uses, failure cases, patches, and regression tasks;
- run no-skill, thin-skill, selected-skill, and full-library baselines;
- promote skill edits only after held-out task improvement;
- retire or quarantine skills whose selection hurts outcomes.

Tools, repos, and methodologies worth exploring:
- Git-backed skill folders, `SKILL.md` metadata, contract-style validators, task fixtures, unit tests for procedural constraints, semantic fuzzing, held-out evals, loaded-skill hash tracing, rejected-candidate buffers.

Implementability score: 0.70

Core source: [MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation](https://arxiv.org/abs/2605.27366)
