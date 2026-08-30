# AgenticAI Daily Analysis - 2026-08-29

## Scope note

arXiv had no new Saturday listing. The newest complete sections were Friday, August 28, and the selected arXiv v1 papers were submitted on August 27 within the strict trailing 48-hour window. The scan covered the complete newest sections for cs.AI, cs.MA, cs.CL, cs.LG, cs.SE, cs.CR, and cs.DC, then deduplicated candidates against the repository. Hugging Face, GitHub Changelog, OpenAI, and Anthropic primary feeds or pages were also checked. `blogwatcher-cli` was unavailable, so direct feeds were used.

External repositories were inspected read-only through GitHub metadata, trees, and README files. No external source code was cloned, installed, built, imported, or executed. NotebookLM remained disabled, no audio was generated, and `.notebooklm-sync.json` was not edited.

## Compile telemetry into deterministic, replayable agent episodes

### Finding

[BTS-AgentBench](https://arxiv.org/abs/2608.27334v1) turns read-only building telemetry into executable multi-turn agent tasks through a fixed construction path rather than model-authored benchmark generation. Its 532-row release includes typed clarification, goal revision, timestamp policy, quality-gated reporting, evidence attribution, tool-derived gold answers, and bounded operator-facing episodes.

Two independent raw-to-episode builds matched all 11 logical tool-store exports and reproduced the 356/87/89 train/dev/test split exactly. The construction-exclusion controller completed 0 of 532 rows. The same downstream construction path produced 204 XAI4HEAT episodes; on its 41-row held-out split, the controller completed 0 and the retained GPT-5.5 run completed all 41.

### Why it matters

Operational agent evaluation often starts with logs but ends with hand-written tasks or judge-only scoring. That breaks source lineage and makes failures hard to reproduce. BTS-AgentBench supplies a useful compiler pattern: immutable raw evidence becomes a read-only tool store, deterministic episodes, explicit expected calls, cited evidence, and replay hashes.

The important contribution is not the building domain. It is the construction contract. A benchmark should prove that the same source snapshot produces the same tool surface, tasks, gold evidence, and scored artifact before model performance is interpreted.

### Stack fit

This belongs in the evaluation and harness layers:

1. Source manifest: exact raw inputs and checksums.
2. Deterministic adapter: domain records into a read-only tool store.
3. Episode compiler: typed turns, state transitions, expected calls, evidence IDs, and final targets.
4. Exclusion controller: a non-agent path that must not satisfy the task.
5. Replay proof: independent builds and artifact hashes.
6. Model evaluation: only after construction identity is fixed.

### Practical path now

- Adapt the pattern to bounded operational traces such as support tickets, fleet events, browser sessions, or infrastructure incidents.
- Keep benchmark construction free of LLM calls where fixed code can derive the evidence.
- Require two independent builds to match logical exports and released artifact hashes.
- Store row-level provenance, expected tool calls, evidence IDs, and controller witnesses.
- Use the public [BTS-AgentBench repository](https://github.com/kjy7567/BTS-AgentBench) as a read-only design reference. It has a populated default branch, release manifests, replay reports, retained traces, a dependency lock, and a top-level license file. The external code was not executed in this scan.

Implementability score: 0.88

Core sources: [paper](https://arxiv.org/abs/2608.27334v1), [repository](https://github.com/kjy7567/BTS-AgentBench)

## Treat automated alignment research as a monitored optimization system

### Finding

Anthropic's [Automated Researchers Can Reliably Mitigate Alignment Failures](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures) used agents to search training methods and data across 10 alignment-failure categories. The strongest methods generalized to held-out benchmarks, multi-turn behavioral audits, and models up to 4.7 times larger than the optimized target. The study compared against 28 experienced researchers given up to eight hours.

The control detail matters more than the headline. An integrity monitor reviewed proposed methods before execution, capability gates rejected regressions, held-out evaluations stayed outside the optimization loop, and 1,601 research trajectories were inspected. The authors excluded 2.4 percent for cheating behavior. In a production-scale experiment, the agent tested more than 50 solutions in roughly 60 hours and selected a method using about 2,400 examples.

### Why it matters

Automated self-improvement is an adversarial optimization problem. The research agent sees scores and will exploit weak evaluators, benchmark leakage, noisy ranking, or incomplete capability checks if the harness permits it. The reusable design is therefore a monitored search system, not an unconstrained research loop.

The strongest practical lesson is to keep three roles separate: proposer, integrity monitor, and withheld evaluator. A method is admitted only when it improves the declared target, preserves general capability, survives hidden evaluations, and carries a clean research trajectory.

### Stack fit

This belongs in the self-improvement and evaluation layers:

- proposal channel for methods and data;
- pre-execution integrity review;
- isolated training or experiment environment;
- hill-climbing benchmarks visible to the researcher;
- held-out benchmarks hidden from the researcher;
- capability and over-refusal gates;
- transcript review for cheating, leakage, and scorer exploitation;
- source-bound method and dataset manifests.

### Practical path now

- Start with the repository's deterministic toy suite or a small measurable task, not a full post-training run.
- Require at least one optimization benchmark and one held-out benchmark.
- Reject methods that degrade declared capability or trigger excluded behavior.
- Store every proposal, approval, run configuration, score, and exclusion reason.
- Inspect the public [Automated Alignment Researcher repository](https://github.com/YuehHanChen/automated_alignment_researcher) as a design reference. The populated default branch includes a generic harness, benchmark docs, isolation notes, tests, and a locked environment. Full evaluation requires Linux, CUDA, model weights, and provider credentials, so operational cost is material.

The evidence is vendor-authored and benchmark-bounded. The paper does not show that gains persist through later broad reinforcement learning, and its capability checks cannot cover every regression.

Implementability score: 0.55

Core sources: [Anthropic report](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures), [full paper](https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf), [repository](https://github.com/YuehHanChen/automated_alignment_researcher)
