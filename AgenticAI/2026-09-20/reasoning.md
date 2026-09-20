# AgenticAI Daily Analysis - 2026-09-20

## Use correlated task sets for cheap coding-agent A/B tests

DeltaSelect starts from an uncomfortable result: only 22 of 113 DeepSWE tasks had a fifth-percentile Pearson correlation of at least 0.50 with full-benchmark performance. Picking a few convenient tasks is therefore not a cheap benchmark. It is usually an uncalibrated one.

The method selects a fixed task set whose one-run outcomes historically track the full benchmark, maps fractional verifier results into a common score, and respects a declared dollar budget. In a 13-evaluation case study, the recorded cost was $27.86. The adopted configuration cost 58.1% less than the initial configuration while its calibrated score rose from 36.46% to 42.36%.

Why it matters: daily agent engineering needs repeated baseline-versus-candidate decisions, not leaderboard claims. A small, pinned, uncertainty-aware task set can make instruction, skill, model, and harness changes cheap enough to evaluate before promotion.

Practical tools and methods worth exploring now:
- use Agent Layer's DeltaSelect tool to declare a budget and freeze a task set;
- retain task IDs, weights, model settings, verifier outputs, costs, and execution provenance;
- compare a baseline and one candidate under the same declared task set;
- report the selected-set result as local decision evidence, not broad capability;
- periodically rerun a larger suite to detect selector drift.

Evidence caveat: the selector is calibrated from published DeepSWE trials and does not prove transfer across harnesses or future changes. The adopted version's published-analog variance improvement was not statistically decisive (p=0.326). The public MIT repository was inspected read-only and not executed.

Implementability score: 0.88

Core sources:
- [DeltaSelect paper](https://arxiv.org/abs/2609.19607v1)
- [DeltaSelect tool](https://agent-layer.dev/deltaselect)
- [Agent Layer repository](https://github.com/conn-castle/agent-layer)

## Treat token efficiency as a measured harness outcome

SoL-Pi uses recursive auto-research across executable environments to select four harness mechanisms spanning action execution, context compaction, observation handling, and delegated reading. On 51 EdgeBench tasks, it reports performance comparable to Pi across GPT-5.6 Sol and Opus 5 while reducing recorded token traffic by 44.7% to 49.0% and API cost by about one third.

The important pattern is not unattended self-improvement by itself. It is treating harness changes as named components whose utility, token traffic, cost, and task success are measured together. That turns context economy from a prompt preference into an engineering outcome.

Why it matters: long trajectories compound redundant observations and repeated context. A harness efficiency gate can reject changes that save tokens by silently reducing useful work.

Practical tools and methods worth exploring now:
- benchmark action execution, compaction, observation filtering, and delegated reading separately;
- preserve a native-harness control and a minimal-harness control;
- report task success, token traffic, API cost, and latency per component;
- require held-out environments before promoting recursively discovered changes;
- treat SoL-Pi as a Pi extension to inspect, not as a drop-in result for other harnesses.

Evidence caveat: the authors evaluate their own open-source extension on one 51-task benchmark and two frontier-model configurations. Comparable performance in that setting does not establish general transfer, and the recursive efficient-improvement thesis remains a research vision. The MIT repository was inspected read-only and not executed.

Implementability score: 0.80

Core sources:
- [SoL-Pi paper](https://arxiv.org/abs/2609.20519v1)
- [SoL-Pi repository](https://github.com/NVlabs/SoL-Pi)
- [SoL-Pi project page](https://nvlabs.github.io/SoL-Pi/)

## Audit compressed memory against future updates

"Correct Now, Insufficient Later" tests a memory failure that ordinary recall benchmarks miss. Two histories produce the same current answer, then receive the same future update, but require different later answers. If compression erased the distinction, current accuracy hides a future failure.

The pilot evaluates 24 history pairs across six synthetic mechanisms, 12 memory conditions, two repeats, and two model backends. A deterministic frontier selector reached 96/96 strict reveal accuracy on DeepSeek and 82/96 on GLM, but identifier renaming reduced one late-reference result from 8/8 to 94/320 transformed instances. Removing tombstones caused 16/16 exact replay failures in the targeted mechanism.

Why it matters: memory should be evaluated as updateable state, not only as a retrieval cache. A representation can answer today's question and still be unsafe to evolve.

Practical methods worth exploring now:
- create paired histories with equal current answers but divergent future obligations;
- replay the same update against raw history and compressed state;
- test identifier renaming, tombstone deletion, contradiction, and late reference;
- separate retained-state adequacy, response delivery, and answer-schema compliance;
- keep raw episodes until compressed state passes update-sufficiency gates.

Evidence caveat: this is a small synthetic pilot with four pairs per mechanism, two updates, and no natural-task validation. Code and reproducibility materials were announced for later release, so the method is implementable now but the reported results are not independently reproducible from a public artifact yet.

Implementability score: 0.66

Core source: [Correct Now, Insufficient Later](https://arxiv.org/abs/2609.20045v1)
