# AgenticAI Daily Analysis: 2026-11-17

The strongest implementation signal is to narrow the model's job. Let models judge choices and propose bounded changes, while deterministic code assembles calls, validates effects, and decides what survives.

## 1. Compile tool calls from request-bound choices

System 1 Agents replaces free-form tool-call generation with a deterministic compiler. The compiler turns a tool schema and user request into typed questions, offers only values found in the request, schema, environment, or fixed derivation rules, and lets a local decision model score those options. Code controls sequencing and assembles the final call. Missing required values trigger a fixed clarification path instead of model invention.

Why it matters: schema validity alone does not stop a model from inventing plausible argument values. A finite choice surface makes ungrounded values impossible by construction and leaves probability-bearing decisions that can be replayed and audited.

Implementable now:
- compile JSON Schema fields into finite choices and explicit missing-value states;
- extract free-value candidates from the request with deterministic rules;
- keep tool names, field names, defaults, and final call assembly in code;
- use confidence thresholds for decline and clarification;
- retain every question, option set, score, selected value, and final call for replay;
- use a compiler oracle and regression corpus before admitting new extraction rules.

Evidence and caveat: on 1,952 complete or out-of-scope requests spanning 157 biomedical tools, the best System 1 agent reached 97.0 percent tool-selection accuracy and 93.9 percent fully correct requests. None of 10,888 System 1 calls contained ungrounded content under the study's test, while 5.5 to 19.7 percent of LLM-agent calls did. The evaluation is domain-specific, mostly single-request tool selection, and did not execute tools during the comparison. Production workflows still need effect verification and recovery.

Artifact status: the Apache-2.0 repository contains the compiler, agent, tests, locked dependencies, evaluation data, stored outputs, and replay scripts. It was inspected read-only. No source was cloned or executed.

Implementability score: 0.84

Core source: [System 1 Agents v1](https://arxiv.org/abs/2611.21053v1)

Public artifact: [eltzanis/SystemOneAgents](https://github.com/eltzanis/SystemOneAgents)

## 2. Let agents propose, then let the harness accept

Agent-Guided Configuration Tuning separates creative search from acceptance. Codex and Claude agents inspect cvc5 documentation, source, and persistent experiment history, then propose bounded configuration edits. A deterministic harness runs the complete training group, validates returned models, applies per-division eligibility rules, and records the proposal, raw outputs, thresholds, and accepted incumbent.

Why it matters: long-running agent improvement becomes safer when agents cannot promote their own hypotheses. Persistent experiment records preserve useful search context, while a fixed harness keeps evaluation and promotion stable across thousands of proposals.

Implementable now:
- constrain proposals to a typed configuration surface;
- give fresh sessions the incumbent, prior hypotheses, measurements, and failure records;
- evaluate each proposal over the complete target group rather than cherry-picked examples;
- validate semantic outputs, not only speed or answer count;
- accept improvements per workload family and retain explicit margins;
- publish immutable experiment receipts and recover from the last accepted incumbent.

Evidence and caveat: the nine-week campaign recorded 4,545 proposals across 13 SMT-COMP divisions and 36 logics. On held-out problem identities, tuned configurations validated more problems than official cvc5 in 10 of 13 divisions for 2026 and eight for 2025, with geometric-mean gains of 7.8 and 6.8 percent. The authors did not establish content-level separation between training and test problems, compared local 24-second runs with official records rather than rerunning every competitor on one host, and provide a workflow paper rather than a packaged public implementation.

Artifact status: immutable paper and cited benchmark sources inspected. No public workflow repository was identified, and nothing was executed.

Implementability score: 0.68

Core source: [Agent-Guided Configuration Tuning for SMT Solvers v1](https://arxiv.org/abs/2611.20484v1)

## 3. Retrieve memory by downstream utility, with a scale gate

Jetriever scores each query-memory pair for whether the memory would help answer the query. This reverses the normal flow: instead of guessing a keyword or semantic association before retrieval, the system judges the utility of every candidate memory it can inspect.

Why it matters: similarity retrieval misses implicit associations. A nut allergy can matter to a macaron request even when the texts share no useful lexical cue. Utility scoring makes the hidden world-knowledge link part of ranking.

Implementable now:
- preserve raw memory chunks and stable IDs;
- define a task-specific binary utility question;
- calibrate scores for ranking rather than generating prose;
- compare top-k utility ranking against BM25 and embeddings on indirect queries;
- use a cheap similarity or metadata stage before utility reranking when the pool is large;
- log the candidate set, utility scores, latency, cost, and final answer effect.

Evidence and caveat: on 125 InMind indirect-query tasks, Jetriever ranked the gold exchange first in 84.8 percent of cases, versus 1.6 percent for BM25 and 0 percent for MiniLM when indexing user turns. The broader MemoryAgentBench check sampled only 60 of 3,671 questions. Full-pool scoring covered 241 exchanges per InMind query and averaged 1,258.2 conversations per sampled MemoryAgentBench query, so cost and latency become first-order limits.

Artifact status: the MIT repository contains a service implementation, Docker packaging, tests, audit hooks, and deployment documentation. It calls OpenRouter's Decisions API. The repository was inspected read-only; no source was cloned or executed.

Implementability score: 0.60

Core source: [Jetriever v1](https://arxiv.org/abs/2611.21478v1)

Public artifact: [imlrz/Jetriever](https://github.com/imlrz/Jetriever)

## Working conclusion

Use models as bounded judges and proposal engines. Keep action assembly, semantic validation, promotion, and replay in deterministic infrastructure. For memory, apply the same rule to retrieval: score usefulness explicitly, then gate the expensive judgment behind a scalable candidate stage.
