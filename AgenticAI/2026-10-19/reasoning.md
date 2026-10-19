# AgenticAI Daily Analysis: 2026-10-19

## Scope note

No new Monday arXiv listing or stronger agent release had appeared by the 12:00 UTC scan. These are unreported findings from the Friday carry-forward batch, submitted on October 15 and 16. Hugging Face's feed had no newer agent systems release, and GitHub Trending supplied watchlist signals rather than benchmark evidence.

## Recommend tools behind a scoped gateway

A deployed Arcade system replaces a static tool catalog with three fixed tools: `SelectTools`, `UseTool`, and `ListApps`. Recommendation runs only over tools already allowed by the gateway and executes each selected tool under the calling user's authorization.

The evaluation separates recommendation coverage from session economics. On ToolRet, with 7,961 queries over 44,453 tools, the system placed every required tool in the top ten for 45.2% of queries, versus 28.8% for BM25. Its first recommendation covered every required tool in 304 of 327 Codex sessions. Against a fixed list of 100 tools, paired runs reduced input tokens by 17% for Codex and 40% for Claude Code, with a 13.6% total bill reduction across the two clients and no task-completion change.

Why it matters: tool discovery belongs at the gateway. A dynamic catalog is useful only if recommendation cannot expand authority, credentials stay outside model context, and every invocation is rechecked against the principal and tool scope.

Stack fit: context economy, tool discovery, gateway authorization, and model-independent agent interfaces.

Implement now:
- expose a fixed discovery and execution interface instead of serializing every tool schema;
- retrieve within the principal's eligible tool scope, never across the global catalog;
- combine lexical and dense retrieval, then rerank ambiguous candidates;
- log candidate scope, selected tool version, consent state, latency, tokens, cost, and outcome;
- evaluate complete required-tool coverage, not only single-tool recall.

Evidence caveat: this is a vendor-authored evaluation of Arcade's deployed system. The paper reports 11 Codex and 3 Claude Code paired cost runs, and no public implementation artifact was identified.

Implementability score: 0.82

Core source: [Tool Recommendation for Multi-Step Agents v1](https://arxiv.org/abs/2610.23707v1)

## Hold harness budgets fixed before blaming the model

ToolBottleneckBench compiles matched task variants that change one pressure at a time: registered catalog, visible menu, certified workflow, or returned-record encoding. It grades the first unmet obligation and the harness limit that ended the episode without an LLM judge.

Across 21 configurations from seven organizations and 26,576 scored conditions, increasing the visible menu from 8 to 128 schemas reduced valid task success by 12.3 points under routed narrowing and 17.5 points when the full menu remained visible. A completion-cap sweep from 1,024 to 16,384 tokens reduced the pooled menu penalty for six truncation-heavy configurations from 43.7 points to 2.7 points. The reported repairs that beat every model configuration change altered which tools reached the model or delegated execution rather than improving the model itself.

Why it matters: a benchmark score mixes model behavior with menus, token caps, call limits, turn limits, result encodings, and routers. Those controls must become versioned parts of the evaluation contract.

Stack fit: deterministic evaluation, harness architecture, failure attribution, and regression testing.

Implement now:
- compile paired cases from one task while changing exactly one harness pressure;
- freeze completion, episode, call, and turn budgets per comparison;
- record the first unmet obligation and terminal limit for every failure;
- run cap sweeps before calling a large-menu loss a model-selection failure;
- compare routing or controller repairs against model switches on success and cost.

Artifact status: the public MIT repository contains the compiler, sandbox, exact grader, scored rows, protocols, analyses, tests, and a pinned ToolSandbox subset. It was inspected read-only and not executed.

Implementability score: 0.86

Core sources:
- [ToolBottleneckBench paper v1](https://arxiv.org/abs/2610.21098v1)
- [zichuanxu/tool-bottleneck-bench](https://github.com/zichuanxu/tool-bottleneck-bench)

## Store situational insights instead of next-tool prescriptions

A study across nine open-weight models, ToolSandbox, and the BFCL-v4 multi-turn subset found that tool graph memory rarely improved reliably over a memory-free agent. ToolNet underperformed the base agent for all nine models on BFCL-v4. H-EPM averaged 2.72 times as many LLM calls and 2.21 times as many tokens as the base agent on ToolSandbox.

The decisive ablation is stronger than the headline. Random tool suggestions or no suggestions retained most of H-EPM's gain. A simple instruction to try available tools before giving up matched or beat the graph at much lower inference cost. Distilling the same episodic summaries into natural-language insights about what to do and avoid produced a better performance-cost tradeoff.

Why it matters: a transition graph over tool names discards call necessity, prerequisites, arguments, and situation. Memory should bias judgment with source-linked guidance instead of prescribing the next action.

Stack fit: agent memory, tool-use planning, trajectory consolidation, and cost-aware evaluation.

Implement now:
- keep raw episodes as canonical evidence;
- distill source-linked situation, action, success, and failure insights;
- retrieve insights as soft priors, not executable instructions;
- test against no-memory, random-guidance, and extra-compute controls;
- measure model calls and tokens with task success.

Artifact status: no public implementation repository was identified from the primary source.

Implementability score: 0.74

Core source: [Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use v1](https://arxiv.org/abs/2610.21571v1)

## Gate proactive memory on interruption value and timing

ProPerMem pairs egocentric video with year-long personal histories averaging 618K tokens. The benchmark has 1,804 pairs, split into 904 training, 100 development, and 800 evaluation pairs, with human-verified trigger windows and a silence requirement outside those windows. Target evidence averages only 0.19% of memory.

The controlled result isolates the hard part. GPT-5.3-Chat reached 96% with oracle evidence delivered inside the correct trigger window. Letting the model choose timing reduced performance to 38%; replacing oracle evidence with retrieval reduced it to 15%. A graph-organized retrieval harness plus an interruption-worthiness gate reached 37.5% on Qwen3.8-27B and 38% on GPT-5.3-Chat without training; lightweight post-training reached 42.4%.

Why it matters: relevance does not authorize interruption. A proactive assistant needs separate evidence for what it knows, whether the evidence is current, and whether the present moment warrants action.

Stack fit: long-term memory, streaming agents, notification policy, and human-attention governance.

Implement now:
- annotate trigger windows and required silence in evaluation fixtures;
- separate retrieval quality, timing, content, early firing, and repeated firing;
- put an interruption-value gate between retrieval and generation;
- bind each alert to memory evidence IDs and the observed trigger;
- keep proactive actions read-only until a separate effect approval exists.

Artifact caveat: the authors say the evaluation set and code will be released upon publication. No public artifact is available yet.

Implementability score: 0.45

Core source: [ProPerAgent v1](https://arxiv.org/abs/2610.22671v1)

## Working conclusion

The common pattern is selection under explicit contracts. Tool catalogs need scoped recommendation, benchmarks need frozen harness budgets, memory needs soft evidence-bearing priors, and proactive assistants need a separate timing gate before they consume human attention.
