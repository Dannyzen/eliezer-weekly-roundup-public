# Context Economy for Agents

Context economy is the design discipline that decides what earns space in an agent's active context, what stays retrievable, what gets compressed, and what must remain auditable outside the prompt.

## Core thesis

The wrong question is "how large is the context window?"

The better questions are:
- what does this turn actually need to see?
- which tool schemas are plausible enough to promote from summary to full JSON?
- what repository context should be retrieved semantically instead of pasted wholesale?
- what memory should preserve event structure rather than flattening into facts?
- how much KV cache, latency, and cost does each added artifact impose on every future step?
- what should be kept outside the model context for audit, replay, or privacy reasons?

Agent systems that skip those questions will waste tokens, degrade reasoning, and confuse context abundance with operational durability.

## Why this topic now

The 2026-04-24 scan produced three reinforcing signals:

1. **DeepSeek-V4** makes long-context agent work a KV-cache and serving-efficiency problem. A 1M-token window matters only if every continuation at that depth remains affordable.
2. **Tool Attention** names the MCP/tools tax and proposes dynamic tool gating plus lazy schema loading instead of eagerly injecting every tool schema.
3. **Claude Context** is the GitHub-trending practical version for code agents: index the repository and retrieve relevant code into the agent context instead of loading everything.
4. **StructMem** extends the same lesson to memory: not every remembered item should be a flat fact; some context needs event structure and cross-event links.

Core sources:
- DeepSeek-V4 on Hugging Face: https://huggingface.co/blog/deepseekv4
- Tool Attention: https://arxiv.org/abs/2604.21816
- Claude Context: https://github.com/zilliztech/claude-context
- StructMem: https://arxiv.org/abs/2604.21748
- LightMem: https://github.com/zjunlp/LightMem
- Less Context, Better Agents: https://arxiv.org/abs/2606.10209v1

## The context budget is multi-dimensional

Token count is only the visible cost. Real agent context has at least six budgets:

### 1. Token budget
Every tool schema, file snippet, memory, and prior turn competes for prompt space.

### 2. KV-cache budget
Long-running sessions pay for retained context again and again during decoding. KV-cache growth is an infrastructure cost, not just a model limit.

### 3. Latency budget
Agents amplify latency because a single task can contain many model calls, tool calls, retries, approvals, and handoffs.

### 4. Reasoning budget
Irrelevant context can degrade decisions even when the model technically fits the window.

### 5. Governance budget
The model should not see tools, data, or memories that violate access scope just because they were available in a server registry.

### 6. Audit budget
Some evidence should stay outside the active prompt but remain replayable and inspectable later.

## What to build now

### Gate tools before schema injection
Keep compact tool summaries in context. Promote full schemas only when intent, state, and permissions make the tool plausible.

Minimum pattern:
1. maintain a tool registry with short summaries, preconditions, and scopes
2. embed summaries for rough intent matching
3. filter candidates with current state and access policy
4. load full schemas only for top-k tools
5. log when a needed tool was gated out so the router can improve

### Retrieve code context semantically
Large repositories should be searchable context stores, not prompt dumps. Use repository indexing, symbol search, exact file reads, and citations back to source files.

Practical starting points:
- `zilliztech/claude-context`
- local embeddings plus pgvector, Milvus, Zilliz, LanceDB, or SQLite vector extensions
- language-server symbol search paired with semantic search

### Measure context cost per agent loop
For every serious run, record:
- prompt tokens by category: user, memory, tools, retrieved code, previous turns
- number and size of injected tool schemas
- context length at each model call
- KV-cache or serving-memory pressure where available
- latency by model call, tool call, and router decision

If those numbers are invisible, context bloat will look like model weakness.

### Keep memory structured when continuity depends on it
Memory that supports long-horizon behavior should preserve event identity, timestamps, provenance, relationships, and supersession. Flat summaries are fine for some personalization facts; they are not enough for temporal reasoning or audit.

## What to avoid

Avoid these traps:
- treating a million-token window as permission to stop selecting context
- injecting every MCP schema on every turn
- loading whole repositories into prompts instead of indexing them
- using vector search as the only memory architecture
- hiding context growth inside framework internals with no telemetry
- allowing tool visibility to bypass access policy
- optimizing benchmark prompts while production sessions drown in tool and memory payloads

## Practical tools and methods worth exploring now

- [DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) for long-context open-model experiments
- [Tool Attention](https://arxiv.org/abs/2604.21816) for dynamic tool gating patterns
- [Claude Context](https://github.com/zilliztech/claude-context) for code-search MCP integration
- [LightMem](https://github.com/zjunlp/LightMem) for memory-augmented generation patterns
- vLLM or SGLang serving metrics for long-context and multi-agent tests
- OpenTelemetry-style agent traces with prompt-category token breakdowns

## May 5 update: context should be a maintained, incremental artifact

AOCI and CocoIndex sharpen this topic from token budgeting into context operations. AOCI argues for a stable symbolic-semantic repository representation: encoding rules plus entries per code unit, with architectural coordinates, semantic summaries, dependencies, constraints, and incremental maintenance. CocoIndex is the practical open-source signal: an incremental engine for long-horizon agents that keeps codebases, documents, logs, PRs, Slack, and other sources fresh without full rebuilds.

The practical lesson:
- build a reproducible context index with source hashes and index versions
- keep symbolic coordinates and semantic summaries separate from raw source
- recompute only changed entries and dependent summaries
- attach index version and retrieval IDs to every agent trace
- add stale-context tests to catch cases where the agent acts on an obsolete view

This extends the earlier context-economy thesis. The point is not only to select fewer tokens. The point is to make the agent's context substrate reproducible, incrementally updated, and auditable.

Sources:
- [AOCI](https://arxiv.org/abs/2605.02421v1)
- [CocoIndex](https://github.com/cocoindex-io/cocoindex)
- [CocoIndex V1 is Live](https://cocoindex.io/blogs/cocoindex-v1/)

## Deep Dive Wednesday 2026-05-06: stable context is an incremental artifact

### Overview

AOCI and CocoIndex won Deep Dive Wednesday because they turn the repo's context-economy thesis into an implementable substrate. The week's other signals were strong: MEMTIER clarified long-running memory, MOSAIC-Bench made coding-agent security more urgent, and provenance graphs sharpened prompt-injection defense. But AOCI plus CocoIndex attacks the layer that every serious coding, research, and memory agent depends on: the maintained representation of the world before the model acts.

The winning claim is simple: an agent should not reconstruct its working model of a repository, corpus, or workspace from scratch on every turn. It should read from a versioned, incrementally maintained context artifact whose sources, hashes, summaries, dependencies, and retrieval IDs are visible in the run trace.

### Core innovation

AOCI's core innovation is a file-level intent layer for LLMs. The paper argues that existing code context methods choose between raw code, syntax skeletons, retrieval, summarization, or runtime agent exploration. Each can help, but none simultaneously gives global coverage, deterministic representation, and incremental maintenance.

AOCI proposes a symbolic-semantic index:

- a project header that defines the architecture vocabulary and tag taxonomy;
- one independently maintainable entry per file or database table;
- symbolic tags for architectural layer, business module, importance, technical features, and scale;
- semantic fields for function, relations, APIs, and high-entropy design decisions;
- incremental regeneration where changed files update their own entries instead of rebuilding the whole representation.

The important phrase is not "better retrieval." It is "stable, LLM-readable blueprint." The paper reports 97.67% file-localization accuracy, second only to an oracle upper bound, and claims zero final-state defects across 19 industrial development tasks while Claude Code, Cursor, and OpenCode introduced defects in 12 tasks and used 4-130x more tokens. Those numbers need independent replication, but the architectural direction is obvious even if the exact effect size shrinks.

CocoIndex is the practical adjacent signal. Its V1 release frames agent context as state-driven data engineering: declare the target state as a function of source data, then let an incremental engine recompute only the delta. That maps cleanly onto the agent problem. Codebases, Slack, docs, PRs, logs, memory objects, and traces should become live context products, not stale batch snapshots or prompt-time improvisations.

### Why it matters

Most agent failures that look like "the model was dumb" are actually context-substrate failures:

- the agent searched the wrong files because retrieval built a partial view;
- the agent used stale source because the index did not track source hashes;
- the agent missed a cross-module dependency because no durable relation layer existed;
- the agent repeated work because prior decisions were buried in transcript sludge;
- the operator could not reproduce the run because the exact context view was never materialized.

Long-context models do not remove this problem. They make it easier to hide. A million-token window can ingest more irrelevant, stale, contradictory, or untraceable material. The architectural fix is not maximal context. It is maintained context: structured enough for the model, stable enough for replay, fresh enough for long-horizon work, and auditable enough for governance.

### How it fits into the agentic stack

This belongs below the reasoning loop and above raw storage.

- **Context substrate:** source repositories, documents, logs, tickets, and memory traces become materialized context indexes with versions.
- **Retrieval layer:** query-time retrieval becomes selection over a maintained artifact, not ad-hoc construction of a new worldview.
- **Coding-agent harness:** each code-edit run records the index version, file entries, dependency cues, and retrieval IDs it used.
- **Memory layer:** episodic and semantic memories can use the same pattern: source event, typed summary, relation hints, trust tier, and promotion history.
- **Evaluation layer:** stale-context, missing-dependency, and cross-module update tests become regression fixtures.
- **Governance layer:** source hashes and lineage let an operator ask, "What did the agent believe, and why?"

The deeper stack move is to treat context as a first-class build artifact. A context index should be generated, tested, diffed, versioned, cited, and rolled back like code.

### Practical tools, repos, and methodologies worth trying now

- [CocoIndex](https://github.com/cocoindex-io/cocoindex) for incremental context pipelines over code, docs, PDFs, conversations, and graph targets.
- CocoIndex V1's state-driven pattern: define `target = F(source)`, then rely on delta-only recomputation and lineage.
- Tree-sitter, language-server indexes, call graphs, and dependency graphs for deterministic symbolic anchors.
- pgvector, LanceDB, SQLite vector extensions, Postgres, or graph stores for searchable context targets.
- Source hashes, index version IDs, and retrieval IDs attached to every agent trace.
- Stale-context regression tests: change a file, table, API contract, or dependency edge and verify the agent no longer acts on the obsolete representation.
- AOCI-style file entries for high-value repos: role, relations, API surface, schema constraints, owner, risk tier, and high-entropy design decisions.

### Implementation complexity

A useful first version is not hard: generate a repo index with file paths, symbols, summaries, dependency hints, source hashes, and update timestamps; store it in a local database; expose retrieval through MCP or a local service; log index version and retrieved entries in every run.

The hard parts appear when this becomes production infrastructure:

- keeping semantic summaries synchronized without hallucinated drift;
- deciding how fine-grained the index should be below the file level;
- preserving exact identifiers when summaries compress too aggressively;
- detecting when dependency entries need recomputation after a related file changes;
- making index generation deterministic enough to diff;
- separating trusted source facts from model-written summaries;
- measuring whether the index actually improves downstream edit quality.

AOCI's paper is also not the final word. Its evaluation concentrates on web stacks, includes author-operated industrial tasks, and uses an LLM adjudication pipeline. Treat it as a strong architectural signal, not settled benchmark truth.

### Implementability score

0.84

The pattern is implementable now with ordinary engineering effort. Full AOCI-style benchmarking and production-grade incremental maintenance require sophistication, but a local versioned context index can be built immediately with existing parsers, databases, embedding stores, and trace logging.

### Strategic implications for this stack

The product moat for agents is moving from "chat with tools" to "owned context substrate." Whoever controls the maintained representation of the workspace controls the agent's beliefs, costs, safety boundary, and ability to improve across runs.

For this stack, this points to a concrete product principle: Hermes-like agents should make context indexes inspectable local infrastructure. A run should be able to say: here is the repo index version I used, here are the source hashes, here are the memory objects promoted, here is the evidence path, and here is what went stale after the run. That is the difference between an impressive demo and a system a serious operator can trust.

The worldview update is blunt: context is not prompt decoration. Context is state. State needs ownership, lineage, tests, and rollback.

### Why this beat the other findings this week

MCP-time security gates had the highest immediate implementability, and MEMTIER had the cleanest memory architecture. But stable incremental context won because it is the shared dependency underneath both. Security gates need to know what code and dependency state the agent touched. Memory systems need a maintained representation of what was written, promoted, and retrieved. Search agents need evidence portfolios that can be replayed. Multi-agent orchestration needs traces that reference stable artifacts.

AOCI plus CocoIndex names the missing middle layer: not raw files, not prompt stuffing, not one-off retrieval, but maintained context artifacts that agents can act from and operators can audit.

### Core sources and especially useful supporting sources

- [AOCI: Symbolic-Semantic Indexing for Practical Repository-Scale Code Understanding with LLMs](https://arxiv.org/abs/2605.02421v1)
- [AOCI artifact package](https://doi.org/10.5281/zenodo.19677251)
- [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex)
- [CocoIndex V1 is Live](https://cocoindex.io/blogs/cocoindex-v1/)
- [CocoIndex core concepts](https://cocoindex.io/docs/programming_guide/core_concepts)
- [Use CocoIndex with AI coding agents](https://cocoindex.io/docs/getting_started/ai_coding_agents/)

## May 7 update: context management needs runtime operations, not only indexes

LongSeeker, SCOUT, and CAR sharpen the context-economy thesis from another angle. A maintained index is necessary, but it is not enough. Long-horizon agents also need runtime context operations that decide what stays active, what is compressed, what gets reopened, and what can be safely deleted from the working set.

LongSeeker's Context-ReAct vocabulary is especially useful: Skip, Compress, Rollback, Snippet, and Delete. SCOUT's provenance-grounded epistemic state and CAR's confidence-aware reranking point in the same direction: active context should be promoted by task usefulness and evidence sufficiency, not merely by similarity or transcript order.

Practical lesson:
- log context operations as first-class trace events with source IDs, reasons, and before/after token impact
- preserve raw evidence outside the prompt when compressing active context
- test rollback/reopen behavior so compression does not erase critical evidence
- promote retrieved material by confidence delta, aspect coverage, provenance completeness, and task relevance
- pair maintained context indexes with loop-level policies for what gets injected, compressed, and removed

This turns context economy from prompt hygiene into runtime systems design. The agent should be able to explain not only which source it used, but which context operation changed the active evidence set and why.

Sources:
- [LongSeeker](https://arxiv.org/abs/2605.05191)
- [SCOUT](https://arxiv.org/abs/2605.04496)
- [CAR](https://arxiv.org/abs/2605.04495)
- [PageIndex](https://github.com/VectifyAI/PageIndex)

## May 15 update: citations need retrieval-path provenance

Why Neighborhoods Matter updates the context-economy thesis for Agentic GraphRAG. Final citations are not enough when an agent traverses a graph before answering. The answer can depend on cited nodes, uncited visited entities, traversed edges, and surrounding graph structure. The final source list may be necessary and still fail to explain what actually shaped the answer.

The practical lesson is to treat retrieval as a trace, not a footnote:
- log traversal paths, visited nodes, traversed edges, discarded candidates, and graph neighborhoods
- separate final answer citations from retrieval-path provenance
- attach retrieval-path IDs to generated claims and final citations
- run ablations that isolate cited evidence, remove cited nodes, remove uncited neighbors, and mask edges
- keep large provenance outside the active prompt when necessary, but preserve it for audit and replay

This is the same context accounting problem in a graph setting. The agent should be able to answer not only "what source supports this sentence?" but also "which retrieval path made this answer likely?"

Source:
- [Why Neighborhoods Matter](https://arxiv.org/abs/2605.15109v1)

## June 5 update: context compression is becoming local middleware

Headroom is a practical context-economy signal. It packages compression as a library, proxy, MCP server, and agent wrapper for tool outputs, logs, files, RAG chunks, and conversation history. The implementation claims still need local smoke testing, but the architectural direction is right: context reduction should be a measured layer with retrieval and audit, not an instruction to the model to be concise.

Practical lesson:
- classify content before compression because logs, JSON, code, prose, and RAG chunks need different reducers;
- keep originals outside the active prompt and retrieve them on demand;
- record before/after token counts, compression method, source IDs, and retrieval IDs in traces;
- run answer-preservation and failure-detection tests before deploying compression middleware;
- make compression reversible enough that auditors can inspect the original evidence path.

Source:
- [chopratejas/headroom](https://github.com/chopratejas/headroom)

## June 10 update: tool-response history should be pruned and summarized, not retained wholesale

Less Context, Better Agents turns context economy into an operational benchmark. In a Microsoft Dynamics 365 MCP expense workflow, full conversation history improved over no user model, but pruning to recent tool calls plus compact summaries did better on both reliability and efficiency. The lesson is not that five calls is magic. It is that tool-response history needs retention policy, not prompt maximalism.

Practical lesson:
- preserve full tool transcripts outside the prompt for audit and replay;
- keep only recent high-value tool state active unless older state is requested;
- summarize older tool interactions with source IDs, freshness labels, and links back to raw records;
- measure completion, tokens, stale-state errors, retries, and wall-clock time by retention policy;
- run full-history, last-N, summary-only, and last-N-plus-summary ablations before changing production context handling.

Source:
- [Less Context, Better Agents](https://arxiv.org/abs/2606.10209v1)

## June 12 update: tool execution granularity is context policy

HyperTool updates context economy at the tool-execution boundary. If a deterministic workflow requires five tool calls, four intermediate values, and one final answer, the model should not necessarily see every internal transition. The active context should contain the task-level operation, compact result, source IDs, and enough evidence to audit the block.

GitHub's Copilot CLI language-server post is the practical mirror. Code agents should ask semantic infrastructure for definitions, references, and type resolution instead of spending context and tool calls on brittle text search.

Practical lesson:
- wrap deterministic multi-tool subroutines as auditable executable blocks;
- preserve original tool schemas and local operation logs inside the block;
- return compact outputs with source IDs and failure summaries;
- give coding agents LSP-backed symbol tools before they fall back to grep;
- compare atomic-call, post-hoc summary, and executable-block modes on token cost, latency, retries, and answer quality.

Sources:
- [HyperTool](https://arxiv.org/abs/2606.13663v1)
- [GitHub Copilot CLI language servers](https://github.blog/ai-and-ml/github-copilot/give-github-copilot-cli-real-code-intelligence-with-language-servers/)

## June 16 update: context policy has to preserve both intention and cache continuity

SING and TokenPilot add two constraints to the context-economy thesis. SING shows that tool discovery should follow evolving task intention instead of static schema stuffing. TokenPilot shows that context pruning can accidentally destroy prefix-cache continuity, turning apparent token savings into hidden serving cost. LightMem2 makes the TokenPilot direction concrete as a runtime component for long-horizon agents.

The practical lesson is that context policy is no longer just "select fewer tokens." It has to decide which tools deserve full schema exposure, which segments should stay in a stable prefix, which segments can be compacted at ingestion, and which segments can be evicted only after their lifecycle expires.

Practical lesson:
- maintain compact tool summaries with preconditions, scopes, and collaboration hints;
- promote full tool schemas only when intent, state, and policy justify them;
- preserve stable prompt prefixes for recurring run scaffolds;
- separate ingestion-aware compaction from lifecycle-aware eviction;
- log schema exposure, context operations, token deltas, and cache-stability assumptions in the trace.

Sources:
- [SING](https://arxiv.org/abs/2606.16591v1)
- [TokenPilot](https://arxiv.org/abs/2606.17016v1)
- [LightMem2](https://github.com/zjunlp/LightMem2)

## June 25 update: design context should be a validated file, not prompt lore

DESIGN.md is a useful context-economy pattern because it gives agents a compact, validated artifact instead of a long taste prompt. YAML front matter carries normative tokens. Markdown carries rationale. Linting and diffing make the context reviewable before the agent edits UI code.

Practical lesson:
- put high-value agent context in files with schemas, not only in hidden prompts;
- distinguish normative machine-readable fields from human rationale;
- lint context files before agent runs and diff them during review;
- require agents to cite the context artifact they used when making UI or product changes;
- reuse the shape for other operational contexts such as security boundaries, data policies, runbooks, and repository conventions.

Sources:
- [google-labs-code/design.md](https://github.com/google-labs-code/design.md)
- [@google/design.md npm metadata](https://registry.npmjs.org/%40google%2Fdesign.md)

## Working conclusion

The future agent stack is not context maximalism. It is context accounting. Systems that know what to admit, retrieve, compress, cache, update incrementally, preserve prefix continuity, and audit will beat systems that merely buy larger windows and hope the model sorts it out.
