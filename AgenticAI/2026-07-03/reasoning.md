# Daily AgenticAI Research - 2026-07-03

Thesis: today's implementation signal is bounded state. Long-horizon agents do not mainly need bigger context. They need explicit contracts for what memory each decision can see, plus ablation-ready traces that show which memory layer helped or hurt.

## AgenticSTS turns memory into an ablatable contract

Category: AgenticAI

Core source:
- AgenticSTS paper: https://arxiv.org/abs/2607.02255v1

Implementability score: 0.72

AgenticSTS frames memory for a long-horizon LLM agent as a contract about what each future decision is allowed to see. Instead of appending raw observations, tool calls, and reflections to every prompt, the harness assembles each decision from a fresh user message plus typed retrieval. The prompt stays bounded across arbitrarily long runs, and memory layers can be ablated separately.

The testbed is Slay the Spire 2, which is useful precisely because it forces hundreds of tactical and strategic decisions rather than one-shot answer quality. The paper reports 298 completed trajectories with condition tags, frozen memory and skill snapshots, prompt records, and analysis scripts. In its fixed-A0 ablation, no-store wins 3 of 10 games, while adding triggered strategic skills wins 6 of 10. The authors correctly caveat the sample size: Fisher exact p is about 0.37, so the result is directional rather than decisive.

Why it matters: this is the right experimental shape for agent memory. A memory system should not only make the next answer look better. It should expose what memory was visible, which layer supplied it, whether the layer can be removed without breaking the run, and whether that visibility contract holds over long trajectories.

How it fits the stack:
- Memory Systems: memory becomes a typed retrieval contract, not transcript stuffing.
- Context Economy: bounded prompts are enforced by design rather than by after-the-fact summarization.
- Agent Harness Architecture: condition tags, frozen snapshots, prompt records, and analysis scripts make memory experiments replayable.
- Trajectory-Aware Evaluation: long-run decisions become the unit of measurement.

Practical tools, repos, and methodologies worth exploring now:
- typed retrieval layers for facts, strategic skills, tactical heuristics, and current state;
- no-store, full-history, typed-memory, and skill-triggered ablations on the same task family;
- frozen memory snapshots stored with each evaluation condition;
- prompt records that make the memory visibility contract auditable;
- condition-tagged trajectory archives that can be re-scored when the memory policy changes.

The actionable version is to stop treating memory as a single feature flag. Build memory harnesses where each decision records which memory layers were visible and where every layer can be removed cleanly for an ablation.

## What did not beat the top AgenticAI finding

ReContext is a strong long-context reasoning method because recursive evidence replay improves evidence utilization without training or context pruning. It is useful for context-economy experiments, but it is less agent-specific than AgenticSTS because it targets long-context answer generation more than long-horizon action memory. Source: https://arxiv.org/abs/2607.02509v1

EvoPolicyGym is a strong harness signal because it evaluates repeated edits to executable policies under fixed budgets and publishes a public repo, dataset, and project page. It is worth a follow-up when the repo wants a dedicated policy-evolution topic. Sources: https://arxiv.org/abs/2607.02440v1, https://github.com/Linzwcs/EvoPolicyGym, https://huggingface.co/datasets/linzw/EvoPolicyGym-Exp-data, https://linzwcs.github.io/EvoPolicyGym/

SkillCoach is useful for skill-process rubrics, but yesterday already carried the heavier skill-supply-chain finding. Source: https://arxiv.org/abs/2607.01874v1

## Implementation checklist

1. Define memory visibility as a per-decision contract, not as a global context mode.
2. Store prompt records, memory layer IDs, retrieved item IDs, and skill snapshot IDs with each run.
3. Run no-store, full-history, typed-retrieval, and skill-triggered ablations on recurring long-horizon tasks.
4. Score memory by downstream decision quality, not only retrieval relevance.
5. Treat memory snapshots as versioned harness artifacts with rollback and diff support.
