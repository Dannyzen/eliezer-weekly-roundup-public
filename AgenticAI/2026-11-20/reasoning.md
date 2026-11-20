# AgenticAI Daily Analysis: 2026-11-20

## Scope

This scan covers sources first listed by arXiv on 20 November 2026. Held While Waiting was submitted on 19 November at 17:40 UTC. DriftGuard was submitted on 19 November at 06:26 UTC. Public artifacts were inspected through repository pages, metadata, trees, and README files only. No external source was cloned, installed, built, imported, or executed.

## 1. Stop reserving one environment per waiting session

Held While Waiting measures the resource shape of agent runtimes instead of treating an agent turn as ordinary request-response compute. Across 3,549 deployed LangGraph and Strands steps, model waits dominated wall time while estimated framework work was only 5 to 40 milliseconds per step. On AgentCore, the median model wait was 2.7 seconds.

The capacity failure comes from session ownership. A dedicated environment remains reserved while the model is thinking and, unless the client explicitly closes it, for a default 15-minute idle period after a customer-service conversation that averaged 33 seconds. The paper estimates that only 2 to 15 of every 1,000 held environments are computing at a given moment. Its direct capacity checks cover up to 400 concurrent sessions.

Why it matters: agent capacity is constrained by held environments before it is constrained by CPU. The first operational fix is client-owned and cheap: close sessions as soon as the conversation ends. The larger platform fix is multiplexing. In the paper's workload-driven simulation, 64 conversations sharing one environment required 59 times fewer environments, while 99% of replies gained no more than 40 milliseconds of delay.

Fits into the stack: agent serving, session lifecycle, capacity planning, isolation, and queueing.

Practical tools and methods worth exploring now:
- [MEKHALA/agent-runtime-capacity](https://github.com/MEKHALA/agent-runtime-capacity), inspected read-only;
- explicit session-close calls on every terminal path;
- held-environment seconds as a first-class metric;
- separate model-wait, framework-CPU, tool-wait, and idle-retention spans;
- capacity tests with real waits instead of tight back-to-back loops;
- workload-driven simulation before platform-level multiplexing.

Artifact status: contents inspected read-only. The Apache-2.0 repository has a populated `main` branch, shipped measurements, calibration notes, a nine-platform survey, analysis scripts, tests, and workload-driven simulation outputs. It has five commits and no release tags, so treat it as a research artifact rather than a maintained package.

Evidence limit: CPU time is bracketed rather than directly observed for deployed steps. The simulation's memory footprint is illustrative. The author works for AWS, says the work was independent, and studies AWS services among the surveyed platforms.

Implementability score: 0.82

Core sources: [Held While Waiting v1](https://arxiv.org/abs/2611.26480v1), [agent-runtime-capacity artifact](https://github.com/MEKHALA/agent-runtime-capacity)

## 2. Train memory guards from counterfactual trajectory evidence

DriftGuard treats a retrieved memory as risky only when neutralizing it changes downstream execution. Offline, it branches from the same pre-action state, neutralizes one memory at a time, repeats the paired replay three times, and labels four effects: action change, attack removal, policy-violation removal, and task recovery. A 7B online risk model then predicts those intervention-derived labels before the action without replaying the trajectory online.

This is stronger than scoring memory text for suspicious wording. Across MINJA, AgentPoison, and MPBench, DriftGuard beat zero-shot and few-shot frontier-model rankers on memory-level attribution. On the three online-defense benchmarks, it reduced Mem2ActBench attack success from 46.7% to 5.3% for direct override and from 77.4% to 3.3% for sleeper memory. Its reported added latency was 1.52 seconds per task on a held-out set of 100 tasks, versus 6.19 seconds for A-MemGuard, 8.53 seconds for an LLM memory auditor, and 17.24 seconds for SMSR.

Why it matters: provenance and content filters can show where a memory came from or whether it looks suspicious. They do not show whether that memory causes a harmful branch in the current task. Counterfactual replay supplies that causal supervision offline, then amortizes it into a serving-time guard.

Fits into the stack: persistent memory, trajectory replay, causal evaluation, online guardrails, and memory repair.

Practical tools and methods worth exploring now:
- [DriftGuard anonymous artifact](https://anonymous.4open.science/r/DriftGuard-7F0B), inspected read-only;
- source-linked memory records and pre-action checkpoints;
- repeated single-memory neutralization over recorded trajectories;
- separate labels for action, attack, violation, and task effects;
- validation-calibrated intervention thresholds;
- quarantine before rewrite, with the original memory retained for audit.

Artifact status: contents inspected read-only. The snapshot dated 8 November contains configs, implementation modules, examples, schemas, scripts, tests, a license, and a README. Full experiments depend on six external benchmark or agent-environment resources.

Evidence limit: training used eight RTX 4090 GPUs, single-memory interventions do not capture multi-memory interactions, thresholds are benchmark-specific, and rewrite-based neutralization has no guarantee under domain shift or unseen attacks.

Implementability score: 0.63

Core sources: [DriftGuard v1](https://arxiv.org/abs/2611.25583v1), [DriftGuard artifact](https://anonymous.4open.science/r/DriftGuard-7F0B)

## Working conclusion

Agent runtimes need two forms of accounting that chat abstractions hide: resources held while the model waits, and state that causally changes the next action. Measure both at the trajectory boundary.
