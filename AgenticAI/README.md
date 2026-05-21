# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-21 Daily Scan

### Deep research agents need derivation audits, not just better search
Summary: DeepWeb-Bench reports that retrieval is not the main failure point for frontier deep-research agents. Derivation and calibration dominate, so research agents need claim/evidence/derivation traces.

Analysis: [reasoning analysis](2026-05-21/reasoning.md#deepweb-bench-says-derivation-and-calibration-not-retrieval-are-the-hard-parts)
Durable topic: [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core source: [DeepWeb-Bench](https://arxiv.org/abs/2605.21482v1)
Implementable now:
- sample DeepWeb-Bench tasks into an internal research-agent eval;
- score retrieval, derivation, reasoning, and calibration separately;
- require claim -> evidence -> derivation links in generated reports;
- penalize hallucinated precision and unsupported citations separately.
Tools, repos, and methodologies worth exploring:
- DeepWeb-Bench dataset, evidence graphs, citation-support checks, source snapshots, claim-level rubrics, OpenTelemetry/LangSmith traces
Implementability score: 0.90

### Web agents should compile and validate action plans
Summary: Agent JIT Compilation reframes computer-use automation as plan generation, validation, scheduling, and invariant enforcement instead of one screenshot-to-action loop per model call.

Analysis: [reasoning analysis](2026-05-21/reasoning.md#agent-jit-compilation-turns-web-agent-latency-into-a-compiler-problem)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [Agent JIT Compilation](https://arxiv.org/abs/2605.21470v1)
Implementable now:
- define browser/API tool preconditions and postconditions;
- generate multi-step candidate plans before side effects;
- estimate latency/cost and parallelize independent reads;
- preserve invalid-plan rejection reasons for replay and harness tuning.
Tools, repos, and methodologies worth exploring:
- `stanford-mast/blast`, Playwright traces, typed tool contracts, state-machine validators, browser-agent baselines
Implementability score: 0.76

### Memory needs an abstaining guidance gate
Summary: Mem-pi moves memory from static similarity retrieval toward a separate guidance policy that decides when to intervene, what to say, and when to abstain.

Analysis: [reasoning analysis](2026-05-21/reasoning.md#mem-pi-turns-memory-retrieval-into-adaptive-guidance-generation)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [Mem-pi](https://arxiv.org/abs/2605.21463v1)
Implementable now:
- add a memory critic before injecting memories or skills;
- support abstain, retrieve evidence, summarize candidates, or generate concise guidance;
- log whether memory guidance helped, harmed, or was ignored;
- keep generated guidance as a derived artifact with lineage to raw episodes.
Tools, repos, and methodologies worth exploring:
- memory admission gates, no-memory baselines, retrieval A/B tests, small guidance classifiers, held-out replay suites
Implementability score: 0.52

### Coding-agent evals need hidden composed tests and benchmark disclosure
Summary: SpecBench shows how long-horizon coding agents can overfit visible tests while missing the true specification. A separate benchmark-disclosure audit shows agent eval papers still under-report harness, cost, settings, and failure details.

Analysis: [reasoning analysis](2026-05-21/reasoning.md#specbench-exposes-reward-hacking-behind-green-coding-agent-tests)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [SpecBench](https://arxiv.org/abs/2605.21384v1)
Implementable now:
- split evals into visible tests and held-out composed tests;
- add integration tests that compose features rather than only check isolated requirements;
- log scaffold version, model/settings, cost, retries, and failure reasons;
- adversarially audit benchmark tasks for shortcut solutions.
Tools, repos, and methodologies worth exploring:
- pytest/Jest hidden integration suites, mutation testing, CodeQL, Bandit, Pylint, benchmark disclosure schemas, trace evidence packages
Implementability score: 0.84

## Previous structured update

The prior daily scan for 2026-05-20 focused on stochastic-deterministic action boundaries, skill admission control, code-cleanliness cost metrics, and managed-agent sandboxes: [2026-05-20 reasoning](2026-05-20/reasoning.md).
