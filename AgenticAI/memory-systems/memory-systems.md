# Memory Systems

Last updated: 2026-07-27

Memory is becoming the real architecture question for long-lived agents.

The durable pattern across recent work is simple: agents become more useful when memory preserves ground truth, retrieves broader context than a single chunk, and distinguishes between what should stay local, what should become durable profile data, and what should remain ephemeral. The new wrinkle is that the best systems are no longer treating memory as transcript storage. They are turning experience into portable guidance and giving operators much better control over what gets written and recalled.

## Why this topic now

The April 2026 wave of memory work is pushing seven ideas into focus:
- **MemMachine** argues that episodic memory should preserve full conversational evidence rather than summarize too aggressively.
- **FileGram** argues that personalization should be grounded in behavioral traces from local file activity, not just dialogue.
- **Springdrift** argues that persistent memory must be embedded in an auditable runtime with explicit recovery and policy controls.
- **ALTK-Evolve** argues that the real goal is not replaying transcripts but extracting reusable guidelines, policies, and SOPs from trajectories.
- **Drawing on Memory** argues that durable facts should be paired with contextual scene traces so temporal reasoning and update tracking survive across sessions.
- **claude-mem** shows that installable memory infrastructure with search, citations, and progressive disclosure is a more practical product shape than hidden context injection.
- **Memory Transfer Learning** shows that memory becomes much more valuable when distilled lessons transfer across domains instead of staying trapped inside one benchmark.
- **StructMem** argues that long-horizon memory needs event-level bindings, temporal anchors, and cross-event links rather than isolated vectorized facts.

Core sources:
- MemMachine: https://arxiv.org/abs/2604.04853
- FileGram: https://arxiv.org/abs/2604.04901
- Springdrift: https://arxiv.org/abs/2604.04660
- ALTK-Evolve article: https://huggingface.co/blog/ibm-research/altk-evolve
- ALTK-Evolve paper: https://arxiv.org/abs/2603.10600
- Drawing on Memory: https://arxiv.org/abs/2604.12948
- claude-mem: https://github.com/thedotmack/claude-mem
- Memory Transfer Learning: https://arxiv.org/abs/2604.14004
- Experience Compression Spectrum: https://arxiv.org/abs/2604.15877
- StructMem: https://arxiv.org/abs/2604.21748
- LightMem: https://github.com/zjunlp/LightMem
- DMF: https://arxiv.org/abs/2606.03463v1
- Infini Memory: https://arxiv.org/abs/2606.10677v1

## Core thesis

The wrong question is "how do we give the agent more memory?"

The right questions are:
- what evidence should be preserved verbatim?
- what can be compressed safely?
- what should become a reusable guideline?
- what should remain local?
- what contextual trace should travel with a stored fact?
- how should retrieval adapt to the query?
- what policy should govern writes, reads, and profile formation?
- what abstraction level makes a memory transferable to new tasks?

If those questions are ignored, memory turns into a lossy, leaky mess that is simultaneously unhelpful and unsafe.

## The three memory layers that matter

### 1. Episodic memory
This is the raw record of what happened: conversations, tool calls, outcomes, and surrounding context.

Current lesson:
- preserve more of the original episode than most systems do today
- index it intelligently, but do not treat aggressive extraction as truth preservation
- keep enough context to reconstruct why a fact was learned, not just the fact itself

### 2. Profile memory
This is the durable model of the user, workflow, project, and preferences.

Current lesson:
- build profile memory from repeated evidence, not one-off statements
- distinguish stable traits from transient task state
- keep especially sensitive profile signals local by default

### 3. Procedural memory
This is how the system remembers how to act: routines, playbooks, policies, and recovery paths.

Current lesson:
- some of the most important memory is operational, not conversational
- if the runtime cannot recover, replay, and justify decisions, the memory system is incomplete
- the most useful promoted memories often look like guidelines, not transcripts

## What to build now

### Preserve raw episodes
Store the full interaction episode plus metadata, then layer indexing and summarization on top. Do not throw away ground truth during ingestion.

### Retrieve neighborhoods, not just chunks
When one relevant turn is found, expand around it. Adjacent actions and context often matter more than the isolated snippet that matched the query.

### Separate trust tiers
Not every memory object deserves the same scope.

Use at least three tiers:
- ephemeral working memory
- durable but local profile memory
- externally shareable or system-wide memory

### Put policy on memory writes
Treat memory writes as consequential actions. Some memories change future behavior and should pass policy checks or confidence thresholds before becoming durable.

### Distill guidelines, not just summaries
Run offline passes that convert repeated trajectory patterns into concise guidelines, policies, and SOPs. Retrieval should surface those distilled lessons when they matter instead of dragging whole transcripts back into the prompt.

### Store contextual traces with durable facts
A durable memory entry should not be only a proposition. Pair it with a lightweight scene trace: where it came from, when it was learned, and what local situation made it relevant.

### Promote memories at the abstraction level that transfers
Raw traces are useful for audit and close-match replay, but cross-domain reuse depends on extracting higher-level workflows, validation routines, and generalizable insights.

### Measure memory by continuity, transfer, and reversibility
Useful metrics include:
- factual continuity across sessions
- profile accuracy over time
- retrieval precision under noisy histories
- token efficiency for grounded recall
- reversibility and auditability of memory changes
- transfer gain from retrieved guidelines on unseen tasks
- temporal reasoning and update-tracking accuracy

## What to avoid

Avoid these traps:
- turning every conversation into a flattened summary
- treating vector search alone as a memory architecture
- mixing user profile, task scratchpad, and governance history into one blob
- letting behavioral traces flow into permanent memory without clear consent or scope
- assuming bigger context windows remove the need for memory design
- confusing transcript replay with actual learning
- writing decontextualized facts and hoping retrieval can recover the missing situation later
- promoting overly specific low-level traces as if they will transfer cleanly to new task domains

## New April 2026 additions

### Typed semantic memory is the practical middle path after vector-only and graph-heavy memory
Memanto sharpens the memory architecture tradeoff. The paper argues that high-fidelity agent memory does not always require LLM-mediated entity extraction, explicit graph schema maintenance, and multi-query retrieval. Its proposed pattern is typed semantic memory, automated conflict resolution, temporal versioning, and a single-query retrieval path.

The immediate design lesson is not to depend blindly on one proprietary retrieval backend. It is to make memory writes more disciplined:
- classify durable memories into typed categories;
- attach timestamp, source, supersession, and conflict metadata;
- reconcile contradictions at write time instead of asking the answerer to improvise later;
- keep the online retrieval path cheap enough to use continuously;
- evaluate long-horizon continuity with realistic temporal and multi-session tasks.

This connects directly to StructMem and WorldDB. Flat memory is too lossy, but full graph memory can be expensive and brittle. A typed, versioned event/state layer is the practical middle path for many agent products.

Source:
- [Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents](https://arxiv.org/abs/2604.22085)

### Memory, skills, and rules are one compression pipeline
Experience Compression Spectrum adds the abstraction this category was missing. Episodic memory, procedural skills, and declarative rules are not separate product features. They are compression levels for the same underlying experience. The practical move is to preserve evidence once, then promote it along a governed ladder from episode to reusable routine to compact rule when transfer value is high and specificity costs are acceptable. The paper's "missing diagonal" is the opportunity: most systems can store or summarize, but very few can adapt compression level to the query, the time horizon, or the privacy tier.

The concrete design hint is useful immediately. Treat memory promotion as a lifecycle problem with three explicit targets:
- episodic recall when auditability and context fidelity matter
- skill extraction when a reusable procedure keeps paying off
- rule distillation when the lesson is stable enough to survive aggressive compression

The compression ratios in the paper make the trade-off legible instead of mystical: roughly 5-20x for episodic memory, 50-500x for skills, and 1,000x or more for rules. That is the right language for designing memory budgets.

### Cross-domain transfer favors insight over trace replay
Memory Transfer Learning sharpens the promotion problem. The memory object that transfers best is usually not the full episode and not even the task-specific summary. It is the reusable insight: validation habits, safe-editing routines, workflow constraints, and debugging patterns that survive a change of benchmark.

### Searchable memory compression is becoming installable infrastructure
`claude-mem` is useful signal because it turns persistent memory into a product surface an operator can actually use: one-command install, searchable observations, progressive disclosure, explicit privacy exclusions, and inspectable citations. That pushes memory architecture in the right direction. Durable context should behave like governed infrastructure, not hidden prompt residue.

### Dual-trace encoding fixes the weakest part of flat memory
Drawing on Memory makes the strongest recent empirical case that a fact should travel with a scene trace. That extra encoding pressure improves the kinds of recall that agents actually fail at in the wild: temporal reasoning, update tracking, and multi-session aggregation.

### Guidelines beat transcripts when the goal is transfer
ALTK-Evolve sharpens the practical memory lesson of the month: the agent should not keep relearning from raw logs every time. Good memory systems preserve the episode, then promote the parts that proved reusable. That makes memory smaller, more auditable, and more transferable.

### Memory quality loops belong off the critical path
The most robust pattern is a two-loop design: the online loop acts, while a background consolidation loop scores, merges, and prunes learned guidance. That keeps the action path lean without giving up long-term improvement.

### Write-time reconciliation is the next memory moat
WorldDB adds an important correction to current memory fashion. The problem is not only retrieving the right fact. It is deciding what a new write should do to the memory state. Flat vector stores and many graph memories still treat updates as passive additions, then hope the answerer can reconcile contradictions later. WorldDB argues for the opposite design: nodes should be immutable and content-addressed, while edge types should execute write-time behavior such as supersession, contradiction handling, and merge proposals.

That matters because many of the failures operators actually care about are state failures, not retrieval failures:
- stale preferences that should have been replaced
- conflicting facts that should have remained visible as conflicts
- aliases that should have been merged earlier
- audit trails that vanish once summaries overwrite the past

The practical lesson is immediate even if the full architecture is heavy. High-value memory should stop behaving like an append-only note pad. It should have explicit mutation semantics, version lineage, and enough structure that update tracking does not depend on whatever the answering model improvises at query time.

### StructMem makes event structure the practical middle path between flat memory and brittle graphs
StructMem adds a useful correction to the memory stack. Flat memory is cheap, but it loses the relations that matter for long-horizon behavior. Full graph memory can model relationships, but construction and maintenance are expensive and fragile. StructMem sits in the middle: preserve event-level bindings, temporally anchor memories, induce cross-event links, and periodically consolidate related items in the background.

The implementation lesson is direct:
- store memory as events with provenance, timestamps, participants, and relation candidates
- retrieve event neighborhoods rather than isolated nearest-neighbor chunks
- run consolidation off the critical path so the online loop stays fast
- evaluate memory on temporal and multi-hop behavior, not just fact recall

Source:
- [StructMem: Structured Memory for Long-Horizon Behavior in LLMs](https://arxiv.org/abs/2604.21748)
- [zjunlp/LightMem](https://github.com/zjunlp/LightMem)

## April 30 update: optical memory preserves verbatim traces under token pressure

OCR-Memory adds a useful multimodal twist to this topic. The paper renders historical agent trajectories into images annotated with unique visual identifiers, uses visual anchors to locate relevant regions, then transcribes the corresponding verbatim text. The point is not that OCR is inherently better than text retrieval. The point is that a rendered trace can preserve spatial/local structure and act as a high-density index while still recovering exact evidence.

This complements the existing memory thesis: preserve raw episodes, retrieve neighborhoods, and do not trust summary-only memory for evidence-sensitive work. OCR-Memory’s locate-and-transcribe pattern is especially relevant for long agent traces where the system needs to find the right part of history without stuffing the whole trajectory into the prompt.

Practical lesson:
- render long traces into stable, addressable artifacts such as HTML, PDF, or images
- map visual regions back to exact raw text spans and tool-call records
- retrieve candidate regions first, then inject exact text only when needed
- use OCR/layout retrieval as an index layer, not as the only source of truth
- evaluate memory on faithful evidence recovery under strict context budgets

Source:
- [OCR-Memory](https://arxiv.org/abs/2604.26622v1)

## May 1 update: memory retrieval needs an abstain action

“Learning When to Remember” adds the safety mechanism this topic needed: memory retrieval should be a decision policy with an explicit no-injection action, not a reflexive top-k lookup. The paper’s RSCB-MC controller stores issue knowledge as pattern, variant, and episode; converts retrieval evidence into a 16-feature state covering relevance, uncertainty, structural compatibility, feedback history, false-positive risk, latency, and token cost; then chooses whether to inject one memory, summarize candidates, retrieve high precision/high recall, abstain, ask for feedback, or use no memory.

The product lesson is immediate: a coding agent should sometimes decide that the best available memory is not safe enough to influence the run. Superficially similar stack traces, terminal errors, and config symptoms can hide different causal structures. False-positive memory injection is a distinct failure mode and should be penalized more heavily than missed reuse.

Practical lesson:
- add an explicit abstain/no-memory branch to memory retrieval
- score structural compatibility, uncertainty, false-positive risk, token cost, and latency
- store issue memories with pattern/variant/episode structure instead of flat notes
- log when retrieved memories worsen a debugging run
- start with calibrated rules or a simple classifier before training a bandit controller

Source:
- [Learning When to Remember](https://arxiv.org/abs/2604.27283)

## May 2 update: memory is becoming a write-path and code-graph discipline

Schema-grounded memory adds the missing systems-of-record language to this topic. The paper argues that exact facts, current state, updates, deletions, aggregations, relations, negative queries, and explicit unknowns cannot be handled reliably by vector recall alone. The interpretation burden has to move to the write path: object detection, field detection, field-value extraction, validation gates, local retries, and constrained reads over verified records.

The same design pressure shows up in local code context. `code-review-graph` is useful demand signal because it turns codebase context into a local Tree-sitter graph exposed through MCP, instead of asking a coding agent to repeatedly reread the whole repository. That is context economy as infrastructure: query the graph, inject the scoped evidence, and leave the rest local.

Practical lesson:
- define schemas for high-value memories before they become durable
- validate writes and preserve evidence, timestamps, confidence, and supersession lineage
- use local code graphs, LSP metadata, and Tree-sitter indexes before whole-repo context stuffing
- expose memory/code context through governed local services or MCP with explicit read scopes
- keep vector search for thematic recall, not as the only source of truth

Sources:
- [From Unstructured Recall to Schema-Grounded Memory](https://arxiv.org/abs/2604.27906)
- [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)

## May 3 update: governed memory wants a database core, not a vector sidecar

Oracle AI Agent Memory is product signal for the architecture this topic has been converging on. It treats working, semantic, episodic, and procedural memory as access patterns over one governed state core backed by Oracle AI Database, with vector search, relational querying, graph-aware access, JSON, transactional consistency, tenant isolation, auditing, encryption, and high availability.

The practical lesson is not Oracle-specific:
- store high-value memories in a transactional governed backend
- keep vector search as one retrieval path, not the whole system
- put memory writes behind validation, evidence retention, tenant scope, and forgetting/deletion semantics
- expose the same memory core to LangGraph, OpenAI Agents, Claude Agent SDK, or custom harnesses through narrow adapters
- audit both memory writes and future runs that consume those memories

This is the move from memory-augmented agents to memory-aware agents. The agent does not merely search a store; it participates in a governed state system.

Source:
- [Oracle AI Agent Memory](https://blogs.oracle.com/developers/oracle-ai-agent-memory-a-governed-unified-memory-core-for-enterprise-ai-agents)

## May 4 update: memory admission belongs on the write path

MemRouter adds an online-control point to the memory stack. The paper replaces per-turn LLM decoding for memory management with an embedding-based write-side router trained with lightweight classification heads. Under a matched LoCoMo harness, it reports better F1 than an LLM-based memory manager and a large latency reduction for memory-management decisions.

The practical lesson is direct:
- put an explicit admission gate before durable memory writes
- keep memory admission separate from downstream answer generation
- start with rules and embeddings, then train a small classifier from accepted/rejected memory writes
- log every admit, reject, merge, and review decision with evidence
- evaluate memory on write quality, not only retrieval quality

This connects the recent memory findings into one lifecycle: preserve evidence, validate high-value writes, route what deserves durable storage, store it in governed state, and retrieve only when the policy says the memory is useful enough to influence the run.

Source:
- [MemRouter](https://arxiv.org/abs/2605.00356v1)

## May 6 update: tiered memory makes retrieval a governed subsystem

MEMTIER turns the memory lesson into a more concrete runtime pattern: keep episodic memory structured, retrieve through multiple weighted signals, consolidate asynchronously into semantic memory, and tune retrieval policy from evidence rather than intuition.

The important correction is that memory quality is not only a storage problem. It is a subsystem with four control points:
- what gets written into episodic memory;
- which signals retrieve or suppress a candidate memory;
- which facts graduate into semantic memory;
- how retrieval behavior is evaluated over multi-session tasks.

That maps cleanly onto the existing memory thesis. Start with inspectable rules, append-only evidence, and background consolidation. Only then consider PPO-style adaptation of retrieval weights. If the system cannot replay why a memory was retrieved or promoted, it is not ready for learned policy updates.

Practical lesson:
- store episodic memory with provenance, timestamps, tool/action metadata, outcomes, confidence, and trust tier
- consolidate in a background worker rather than inside the hot action path
- blend recency, semantic similarity, entity match, task continuity, and source trust during retrieval
- evaluate memory on temporal reasoning, multi-session synthesis, and false-positive retrieval harm
- keep retrieval-weight changes versioned so memory behavior can be rolled back

Source:
- [MEMTIER](https://arxiv.org/abs/2605.03675)

## May 7 update: storage is not memory

Storage Is Not Memory sharpens this topic with a useful design rule: preserve events first, retrieve late. Extraction at ingestion is dangerous because the future query is unknown. A profile fact, summary, or schema field may be useful later, but it should remain a derived artifact with lineage back to the raw event, not a destructive replacement for that event.

The reported True Memory system is also practical signal because it runs as a single SQLite file with a multi-stage retrieval pipeline rather than requiring a heavyweight vector database or graph store. The exact benchmark numbers need replication, but the architecture aligns with the repo's memory thesis: memory quality lives in event preservation, retrieval policy, evidence neighborhoods, and derived-summary lineage.

Practical lesson:
- keep verbatim event logs for conversations, tool calls, files, URLs, outcomes, and timestamps
- use SQLite/FTS5/BM25, entity/time indexes, and reranking before semantic synthesis
- retrieve neighborhoods around events rather than isolated nearest-neighbor chunks
- store derived memories as pointers to raw evidence
- evaluate memory by evidence recovery, update tracking, false-positive recall harm, and temporal reasoning

Source:
- [Storage Is Not Memory](https://arxiv.org/abs/2605.04897)

## May 8 update: memory invalidation is a first-class eval axis

STALE sharpens the memory stack around a failure mode that normal recall tests miss: an agent can retrieve updated evidence and still behave as if an old belief is valid. The paper's Implicit Conflict framing is useful because many real updates are not phrased as direct negations. A user moves, a project changes policy, a credential is rotated, a meeting is canceled, or a preference flips under new context. The old memory is now stale even if the latest turn never says "forget X."

The practical lesson:
- memory entries need validity state, timestamps, source evidence, superseded-by links, and conflict metadata
- memory retrieval should surface update neighborhoods around changed state, not isolated facts
- eval suites should include stale premises embedded in user questions and score whether the agent resists them
- downstream behavior should adapt to implicit changes, not merely mention that newer evidence exists
- write-path policies should create explicit supersession or conflict records when a new event invalidates old state

This turns memory from a retrieval problem into a state-maintenance problem. A long-lived agent that cannot invalidate stale memories is not personalized; it is confidently out of date.

Source:
- [STALE](https://arxiv.org/abs/2605.06527)

## May 10 update: memory is becoming structured agent state, not transcript recall

Memori, Statewave, MemReranker, and SkillRet sharpen the memory stack around an implementable product shape: raw agent events should compile into typed, attributed, provenance-bearing state, and retrieval should be evaluated separately from storage.

Memori is useful signal because it captures memory from what agents do, not just what they say: entity/process attribution, sessions, conversations, tool calls, decisions, and outcomes. Statewave is useful signal because it makes the same idea more infrastructure-shaped: events compile into typed memories with confidence, provenance, subject timelines, token-bounded context bundles, conflict handling, Postgres/pgvector storage, connectors, and OpenTelemetry tracing. MemReranker adds the retrieval correction: generic semantic rerankers miss temporal, causal, and dialogue-context constraints. SkillRet adds the catalog correction: reusable skills need retrieval quality tests once explicit name invocation stops scaling.

Practical lesson:
- store entity, process, session, source episode, tool call, decision, outcome, timestamp, and confidence with memory events
- preserve raw events and treat typed memories as derived artifacts with lineage
- benchmark transcript stuffing, simple RAG, typed memory, and reranked memory on the same repeated tasks
- add stale-memory, implicit-conflict, and skill-retrieval fixtures to the eval suite
- expose memory through governed local services or MCP/CLI adapters only after write and read policy are explicit

Sources:
- [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori)
- [Statewave](https://github.com/smaramwbc/statewave)
- [MemReranker](https://arxiv.org/abs/2605.06132)
- [SkillRet](https://arxiv.org/abs/2605.05726)

## May 11 update: memory needs usability budgets and writeback firewalls

The Memory Curse, scale-conditioned memory evaluation, and unintended long-term state poisoning make a blunt correction: memory is an active behavioral control surface, not a passive recall buffer.

The Memory Curse shows that longer accessible history can erode cooperation in multi-agent social dilemmas because the retrieved content changes the agent's reasoning pattern. Scale-conditioned evaluation shows that memory quality has to be reported as an agent-interface-scale-budget property, not a single recall score. Unintended long-term state poisoning shows that routine conversations can corrupt durable state by weakening confirmation boundaries, expanding tool defaults, or increasing unchecked autonomy.

Practical lesson:
- report budget-compliant reliability and tail memory-call burden, not only answer accuracy
- hold relevant evidence fixed while adding irrelevant sessions to find the usable-scale boundary
- treat retrieval-call budgets and stop conditions as part of memory quality
- audit durable state diffs before writeback, especially instruction-like memories that change future permissions or autonomy
- preserve source episode, validity state, supersession links, confidence, and rollback metadata with high-impact memories
- sanitize or summarize long histories when raw recall encourages retaliation, paranoia, or unhelpful over-deliberation

Sources:
- [The Memory Curse](https://arxiv.org/abs/2605.08060)
- [Scale-Conditioned Evaluation of Agent Memory](https://arxiv.org/abs/2605.07313)
- [Unintended Long-Term State Poisoning](https://arxiv.org/abs/2605.06731)

## May 13 update: memory must test dependencies deletion and absence

MEME turns the memory stack's hardest product question into a small, inspectable benchmark shape: can the system maintain evolving state across multiple entities? Static retrieval is not enough. The project reports that six memory systems collapse on dependency reasoning under default settings, averaging 3% on Cascade and 1% on Absence, even when static retrieval looks acceptable.

The practical correction is that memory eval needs to look more like state-machine testing. Deletion should leave tombstones or validity metadata. Supersession should connect old and new facts. Absence should be answerable as a grounded negative result, not a confused retrieval miss. Dependency reasoning should test whether a change to one entity propagates to the questions that depend on it.

Practical lesson:
- create controlled episodes with several entities, updates, deletions, and dependent facts
- score Cascade, Absence, and Deletion separately from exact recall and aggregation
- store supersession edges, deletion tombstones, validity state, and dependency metadata with high-impact memories
- evaluate memory systems under a fixed cost and retrieval-call budget so expensive internal models do not hide bad architecture
- treat a file-based memory agent's expensive partial success as a diagnostic, not as the default production answer

Sources:
- [MEME](https://arxiv.org/abs/2605.12477v1)
- [MEME project](https://seokwonjung-jay.github.io/meme-eval/)

## May 17 update: continuous consolidation should not overwrite evidence

Useful Memories Become Faulty When Continuously Updated by LLMs adds the strongest warning yet against destructive memory promotion. The paper’s setup is exactly the pattern many agent products are drifting toward: an LLM repeatedly rewrites raw trajectories into a durable textual memory bank. The reported result is that utility can rise and then fall, and can even drop below a no-memory baseline. The abstract reports GPT-5.4 failing on 54% of a set of ARC-AGI problems it had previously solved without memory after consolidation from ground-truth solutions.

The practical lesson is not to abandon memory. It is to stop treating the latest consolidated text as the source of truth. Raw episodes should be first-class evidence; consolidated memories should be derived artifacts with lineage, confidence, and rollback.

Practical lesson:
- preserve raw trajectories, tool calls, files, outcomes, and timestamps as append-only evidence
- store derived memories as pointers to raw episodes, not destructive replacements
- gate consolidation in background jobs with provenance, confidence, diff review, and rollback metadata
- replay important tasks with and without consolidated memory to catch regression from faulty abstraction
- separate harmless recall from sensitive-action justification when memory influences future authority

Source:
- [Useful Memories Become Faulty When Continuously Updated by LLMs](https://arxiv.org/abs/2605.12978)

## May 18 update: population-broadcast memory needs promotion gates

FORGE adds the positive counterpart to yesterday’s memory-warning pattern. Continuous consolidation can become faulty, but evaluated memory promotion can still improve agents when the loop is explicit. FORGE converts failed trajectories into rules, examples, or mixed memory artifacts, scores them in a bounded environment, broadcasts the best-performing artifact to the agent population, and freezes converged instances.

The design lesson is that memory promotion should look like a release pipeline, not a hidden summarizer:
- raw trajectories remain append-only evidence;
- candidate rules/examples are derived artifacts with lineage;
- promotion requires held-out evaluation, not vibe-based reflection;
- broadcast scope is controlled because a bad memory can degrade every worker;
- rollback is part of the memory object, not an afterthought.

This also clarifies the role of population learning. A team of agents should not each hallucinate its own private memory bank indefinitely. When a memory artifact proves useful, broadcast can amortize learning. But when the artifact is unverified or externally tainted, broadcast becomes a failure multiplier.

Source:
- [FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast](https://arxiv.org/abs/2605.16233)

## May 19 update: evaluation memory can improve rubrics without corrupting user memory

AMARIS adds a useful positive memory pattern after the recent warnings about faulty consolidation and sleeper poisoning. Its memory is not a free-form user profile and not a self-mutating instruction bank. It is persistent evaluation history: rollout diagnostics, step-level summaries, recent context, and dynamically retrieved similar failures used to update rubrics.

That distinction matters. Evaluation memory is still a derived artifact and still needs provenance, but it has a cleaner threat model than user-facing behavioral memory. It can be append-only, scoped to a training run, versioned with rubric changes, and replayed against held-out evals.

Practical lesson:
- store rubric-level failures, not only pass/fail outcomes
- retrieve recent failures and semantically similar historical failures before rubric updates
- keep rubric changes versioned with source diagnostics and rollback metadata
- run rubric refinement asynchronously, outside the hot action path
- evaluate whether updated rubrics improve held-out behavior before promotion

Source:
- [AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.18592v1)

## May 21 update: generated memory still needs an abstain gate

Mem-pi adds the next positive memory pattern after the recent warnings about faulty consolidation and memory broadcast risk. It does not retrieve static memories or skills by similarity alone. It uses a separate language or vision-language model to decide when to generate task-specific guidance and what guidance to generate, with an explicit ability to abstain.

The implementation lesson is broader than the paper's RL setup. Memory should be an intervention policy. A long-running agent should ask whether a memory object deserves to influence this run, whether raw evidence should be shown instead, whether a concise derived hint is enough, or whether the safest choice is no memory.

Practical lesson:
- add a memory critic before injecting memories, skills, or guidelines;
- support abstain, raw-evidence retrieval, candidate summarization, and generated guidance as separate actions;
- log whether each memory intervention helped, harmed, or was ignored;
- keep generated guidance as a derived artifact with lineage to raw episodes;
- replay important tasks with memory disabled, static retrieval, and adaptive guidance to measure marginal value.

Source:
- [Mem-pi: Adaptive Memory through Learning When and What to Generate](https://arxiv.org/abs/2605.21463v1)

## May 26 update: personalized memory starts at session admission

Personalize-then-Store adds a user-specific correction to the memory stack. Universal memory policies are too blunt: a session that is durable signal for one person can be disposable noise for another. PerMemBench turns that into a benchmark shape with multi-year, multi-domain histories across personas, and the proposed session-level storage gate is the practical primitive.

This extends the existing write-path thesis. Memory admission is not only “is this fact important?” It is “is this session worth memory operations for this user, this project, this privacy tier, and this future retrieval budget?”

Practical lesson:
- classify each session before durable writes: profile, project fact, reusable procedure, evidence event, ephemeral scratch, or reject;
- store admission reason, confidence, persona/project scope, retention tier, and source episode;
- keep raw evidence append-only while treating durable memories as derived artifacts;
- evaluate memory under personalized retention budgets, false-positive write rates, and downstream continuity tasks;
- make local-only and forgettable memory tiers explicit before adding cross-agent sharing.

Source:
- [Personalize-then-Store](https://arxiv.org/abs/2605.25535)

## May 28 update: memory failures need operation-level attribution

MemTrace makes the next memory-system requirement explicit: memory should be traceable as an evolving graph, not only queried as a blob. The paper models memory pipelines as executable memory evolution graphs so failures can be traced to operation-level causes such as information loss, retrieval misalignment, stale propagation, or corrupted synthesis.

The practical lesson is that memory observability has to sit inside the pipeline. Final-answer scoring cannot tell whether a bad response came from bad retrieval, unsafe consolidation, lossy summarization, or a stale fact that should have been superseded. Every write, merge, summary, retrieval, and final-use event needs provenance.

Implementation moves:
- attach stable provenance IDs to memory writes, source spans, summaries, merges, retrieval decisions, and final answer citations;
- store memory operations as append-only events before promoting compacted declarative memories;
- classify failure cases by operation type instead of treating all bad answers as model failures;
- use attributed failures to patch prompts, routing rules, or consolidation policy;
- keep raw transcripts and evidence available for high-stakes recall.

Sources:
- [MemTrace](https://arxiv.org/abs/2605.28732)
- [zjunlp/MemTrace](https://github.com/zjunlp/MemTrace)


## May 31 update: belief memory needs stay-update-isolate tests

Contextual Belief Management adds the state-transition lens this memory topic needed. The important failure is not only “retrieved the wrong memory.” It is “updated when it should have stayed,” “stayed when it should have updated,” or “let irrelevant noise influence state.” BeliefTrack’s closed-world tasks make those failures measurable with symbolic verifiers.

The practical lesson is that memory write policy should be tested like a state machine. Before a long-running agent changes durable state, it should record whether the incoming evidence triggers stay, update, or isolate; what source evidence justified that decision; and what old belief was superseded or preserved.

Practical lesson:
- model high-value memory as typed beliefs with source evidence, confidence, validity state, and supersession links;
- add explicit stay/update/isolate decisions before durable writes or profile changes;
- create small closed-world fixtures with distractors, contradictions, and delayed updates;
- score Failed Stay, Failed Update, and Failed Isolation separately;
- treat belief-state prompts as insufficient unless the trace shows the transition decision and evidence.

Source:
- [Contextual Belief Management / BeliefTrack](https://arxiv.org/abs/2605.30219v1)

## June 1 update: memory evals need heterogeneous evolving source streams

RHELM adds the realism constraint that memory benchmarks often avoid. Dialogue-only personas are too flat for long-running assistants. Real memory has to absorb conversations, documents, emails, and event trajectories that evolve over time. RHELM's LOOP construction, plan, rollout, evolve, prune, is useful because it makes temporal coherence and heterogeneous evidence part of the test, not background flavor.

The implementation lesson is immediate: memory systems should be evaluated against mixed-source fixtures with supersessions, stale facts, contradictions, and source-specific evidence. A system that recalls a fact but cannot identify whether the email, document, or later conversation superseded it is not ready for durable personalization.

Practical lesson:
- build memory evals from chats, files, emails, notes, and calendar-like events, not only synthetic dialogue;
- add explicit supersession, stale-evidence, contradiction, and distractor cases;
- score profile-state updates, forgetting, evidence citation, and retrieval separately;
- keep source evidence attached to memory-backed answers;
- treat memory continuity as a temporal state problem, not a top-k recall problem.

Source:
- [RHELM: Beyond Static Dialogues](https://arxiv.org/abs/2605.31086)

## June 3 update: deterministic retention beats hidden write-time summarization

DMF adds a concrete systems pattern to the memory topic: treat retention, decay, and pruning as deterministic calculations over evidence and provenance before asking an LLM to summarize anything. The exact Survival Score formula is less important than the architectural boundary. A memory system should be able to replay why a fact, episode, or interaction survived, decayed, or disappeared.

This complements recent warnings about faulty consolidation. LLM-written memory can still be useful, but it should be derived from raw evidence and guarded by reproducible scoring, not trusted as the only record. Deterministic scoring also makes local-first memory more practical because CPU-side feature extraction and simple vector geometry can run continuously without turning every write decision into another expensive model call.

Practical lesson:
- preserve raw episodes as append-only evidence;
- compute retention from deterministic content, provenance, salience, recency, role, entity, action, and outcome features;
- store score components, decay state, source span, and supersession links with each memory object;
- replay pruning and decay decisions during audits or regression tests;
- compare deterministic retention against LLM summaries and vector-only recall on the same long-horizon fixtures.

Source:
- [DMF](https://arxiv.org/abs/2606.03463v1)

## June 6 update: memory now needs write-path and read-path profiling

Agent Memory adds the missing systems lens to this topic. Long-horizon memory is not one feature. It is a workload with construction, retrieval, update, and generation phases. Different architectures move cost between write time, read time, prompt size, freshness, and fleet management. If those costs are not measured separately, a memory system can look helpful in a demo while becoming too slow or stale in production.

TokenMizer supplies the practical companion pattern. It treats session history as a typed graph and serializes compact resume blocks, preserving decisions, file histories, task transitions, and rationale instead of flattening everything into a summary.

Practical lesson:
- profile memory construction, retrieval, update, compression, and generation as separate phases;
- store session memory as typed events or graph nodes when decisions and rationale need to survive;
- test resume blocks on decision recall, file recall, and rationale preservation, not only token reduction;
- keep raw episodes and source spans behind compact active-context summaries;
- measure freshness-latency tradeoffs before making memory writes synchronous.

Sources:
- [Agent Memory](https://arxiv.org/abs/2606.06448v1)
- [TokenMizer](https://arxiv.org/abs/2606.06337v1)
- [Shweta-Mishra-ai/tokenmizer](https://github.com/Shweta-Mishra-ai/tokenmizer)

## June 7 update: memory search needs policy and contradiction semantics

Beyond Similarity and TOKI sharpen the policy side of this topic. Similarity retrieval can find a semantically close memory that is still wrong for the current situation: stale, sensitive, cross-domain, consent-scoped, contradictory, or unsafe when paired with a downstream tool action. TOKI adds the write-side correction: persistent memory is a versioned substrate where contradictory claims need declared isolation and resolution semantics.

The practical memory design is now two-stage. Before retrieval enters context, policy should check domain, sensitivity, consent, recency, confidence, and action class. Before a write mutates the durable store, the system should preserve evidence, valid time, transaction time, supersession, and the conflict operator used to resolve or defer contradiction.

Practical lesson:
- gate memory retrieval by domain, sensitivity, consent, recency, confidence, and downstream tool-action implications;
- store memory facts with valid_from, valid_until, transaction time, supersession, and evidence pointers;
- make conflict resolution explicit: last-writer-wins, evidence-weighted merge, await-confirmation, or policy-rule resolution;
- add tests for stale, sensitive, contradictory, cross-domain, and action-triggering memories;
- preserve raw evidence so policy and contradiction decisions can be audited later.

Sources:
- [Beyond Similarity](https://arxiv.org/abs/2606.06054v1)
- [TOKI](https://arxiv.org/abs/2606.06240v1)
- [ZenAlexa/toki-bitemporal-memory](https://github.com/ZenAlexa/toki-bitemporal-memory)

## June 10 update: topic documents need staged consolidation and iterative inspection

Infini Memory gives this topic a practical document-shape: maintain long-term memory as topic-structured documents with staged observations, metadata, fact revision, and iterative evidence inspection. That is the missing middle between raw episodes and one-shot retrieval. The agent should not blindly inject a nearest chunk; it should inspect a maintained topic surface, then drill into source evidence when needed.

Practical lesson:
- maintain one topic document per recurring entity, project, workflow, or decision area;
- stage new observations in a buffer before promotion to canonical memory;
- preserve source span, timestamp, author/tool, confidence, supersession, and conflict metadata;
- let retrieval return topic neighborhoods, then allow iterative inspection through memory tools;
- evaluate memory on update tracking, contradiction handling, and evidence citation, not only top-k recall.

Source:
- [Infini Memory](https://arxiv.org/abs/2606.10677v1)

## June 11 update: project memory should judge proposed actions

PROJECTMEM closes the loop between memory and action. It records development as append-only typed events: issues, attempts, fixes, decisions, and notes. It then projects those events into compact MCP summaries and adds a deterministic pre-action gate that warns before repeating a failed fix or touching a known-fragile file.

That is the memory-systems correction this topic has been building toward. Memory is not only recall. High-value memory should sometimes become an action predicate: do not retry this patch class, do not edit this file without review, do not trust this old decision without its source event.

Practical lesson:
- store project memory as local typed events, not only summary pages;
- keep failed attempts and fragile surfaces as first-class memory objects;
- project active summaries from the log, but preserve raw event evidence;
- let memory gates warn, block, or require approval before risky repeated actions;
- evaluate memory on avoided repeated failures, saved context tokens, and auditability, not just retrieval relevance.

Sources:
- [PROJECTMEM](https://arxiv.org/abs/2606.12329v1)
- [riponcm/projectmem](https://github.com/riponcm/projectmem)

## June 12 update: memory access is not compliance

Getting Better at Working With You and Selection Integrity for LLM Graph Memory both push memory toward enforcement. Trace shows that a remembered correction can still be violated unless it becomes an applicability check plus runtime verifier. Selection Integrity shows that graph-memory structure can steer which authenticated facts are selected, even when the final citations are clean.

The memory lesson is blunt: write-path and read-path controls matter as much as recall quality. Some memories should become executable checks. Some graph writes should be barred from steering high-authority selection. The system should preserve not only what was retrieved, but why that memory was allowed to influence the run.

Practical lesson:
- compile repeated user corrections into atomic rules, applicability checks, and final-state verifiers;
- store source correction, body hash, last-fired event, and false-positive notes with each rule;
- label graph edges, merges, and selection features by writer principal and trust tier;
- log memory-selection paths in addition to final retrieved facts;
- separate advisory memory from memory that can affect tool authorization, policy creation, external sends, or durable profile changes.

Sources:
- [Getting Better at Working With You](https://arxiv.org/abs/2606.13174v1)
- [Selection Integrity for LLM Graph Memory](https://arxiv.org/abs/2606.12290v1)

## June 13 update: memory evolution needs compression and poisoning gates

EvoArena, MemRefine, and SMSR turn the June memory thesis into a tighter runtime requirement. Memory is not only a derived summary, topic document, or retrieval policy. It is an evolving state system that has to survive environment change, storage budgets, and adversarial writes.

EvoArena makes the evaluation dynamic: terminal, software, and social-preference domains change over time, and agents have to preserve complete evolving environment states. MemRefine makes memory compression a policy decision, not a similarity cleanup job: delete, merge, and preserve decisions should be judged by factual value under a storage budget. SMSR adds the security floor: persistent memory writes need provenance, and retrieval needs influence controls because multi-session poisoning can steer future runs without touching model weights or code.

Practical lesson:
- store memory patches or update histories instead of overwriting canonical state silently;
- keep storage budgets explicit and log delete, merge, preserve, and abstain decisions;
- attach writer principal, source hash, trust tier, and validity metadata to every durable memory write;
- test memory poisoning separately for unsigned, authenticated, and agent-written poison;
- bound read-path influence with randomized ablation, voting, or equivalent canaries before memory affects high-authority actions.

Sources:
- [EvoArena](https://arxiv.org/abs/2606.13681v1)
- [MemRefine](https://arxiv.org/abs/2606.13177v1)
- [SMSR](https://arxiv.org/abs/2606.12703v1)

## June 15 update: reasoning memory needs version control and local retention

GitOfThoughts and TencentDB Agent Memory converge on a practical memory substrate: local, replayable, and history-aware. GitOfThoughts proposes representing reasoning as a git repository where scored thoughts are commits, scores are notes, outcomes are tags, and retrieval is history inspection. TencentDB Agent Memory is the tooling demand signal: local long-term memory for agents with no external API dependency.

The implementation lesson is that durable memory should not be a hidden prompt cache. High-value memories should behave like state transitions: append-only evidence, diffable changes, rollback path, writer identity, and local retention by default.

Practical lesson:
- store promoted memories as append-only events with stable IDs;
- add diff, blame, rollback, and merge semantics before allowing memory to steer privileged actions;
- keep sensitive project and user memory local unless explicitly exported;
- record source episode, writer, timestamp, trust tier, and observed outcome with every memory write;
- run memory replay tests after schema, compression, or retrieval-policy changes.

Sources:
- [GitOfThoughts](https://arxiv.org/abs/2606.14470v1)
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)

## June 18 update: shared memory needs utility, access, and forgetting together

GateMem turns memory safety into a measurable shared-state problem. Long-lived assistants in hospitals, offices, schools, and households are not single-user recall systems. Multiple principals write to one memory pool and query it under different roles, scopes, and relationships. A memory system that answers legitimate questions but leaks protected information or reconstructs deleted data is not deployment-ready.

The useful metric shape is multiplicative: utility times one minus access-control violation rate times one minus active-forgetting failure rate. That prevents a system from hiding leakage behind high recall or hiding uselessness behind strict denial.

Practical lesson:
- tag memory writes by principal, role, relationship, source event, trust tier, and deletion state;
- keep deletion tombstones and test whether the agent reconstructs or confirms deleted facts;
- run authorized recall, unauthorized access, and active-forgetting checkpoints in the same eval;
- compare long-context, naive RAG, policy-aware RAG, and external-memory systems under one governance score;
- log memory-selection paths and policy verdicts before retrieved memories influence high-authority actions.

Sources:
- [GateMem](https://arxiv.org/abs/2606.18829v1)
- [rzhub/GateMem](https://github.com/rzhub/GateMem)

## June 20 update: transactive memory makes trajectories reusable across agents

Multi-Agent Transactive Memory extends the memory thesis from individual recall to population-level experience sharing. The memory object is a completed trajectory, not just a summary or extracted fact. Producer agents contribute traces; consumer agents retrieve relevant traces to improve task execution in interactive environments such as ALFWorld and WebArena.

The practical correction is that shared memory needs both utility and authority controls. A trajectory can encode a useful procedure, but it can also encode stale state, private data, unsafe shortcuts, or tenant-specific assumptions. Treat retrieved trajectories as examples and warnings, not direct instructions.

Practical lesson:
- store completed trajectories with task, environment, tool sequence, state deltas, outcome, failure notes, and source-agent metadata;
- index trajectories by intent, environment state, tools touched, artifacts changed, and outcome quality;
- retrieve trajectories with policy checks over principal, tenant, data class, deletion state, and source trust;
- run ablations with and without retrieved trajectories before promoting a trajectory repository as default context;
- preserve memory influence in the trace so harmful cross-agent reuse can be debugged.

Source:
- [Multi-Agent Transactive Memory](https://arxiv.org/abs/2606.19911)

## June 28 update: stale facts need deterministic validity ledgers

Temporal Validity in Retrieval Memory makes the memory update problem concrete. If a function name, API endpoint, port, dependency version, or user fact changes, the old and new statements can remain embedding-near. The paper reports cosine AUROC 0.59 for separating contradictions from duplicates, near chance, and argues that staleness is a write-path state problem rather than a retrieval-threshold problem.

Practical lesson:
- store structured facts with valid-from, valid-until, superseded-by, source event, and writer principal;
- apply deterministic subject-relation-object supersession rules for high-value typed memories;
- preserve retired facts as lineage rather than deleting them;
- keep vector search for candidate recall, not for deciding current truth;
- evaluate memory on marker-free evolving facts, including code mutation, config migration, dependency bumps, and API evolution.

Source:
- [Temporal Validity in Retrieval Memory](https://arxiv.org/abs/2606.26511v1)

## July 1 update: selective turn memory needs source-indexed reconstruction

ECHO sharpens the memory-system thesis from another angle: pruning context should not erase the evidence path. It compresses completed environment turns into compact memory records, reconstructs bounded policy contexts by selecting records, and uses the selected source indices to route outcome credit back to supporting evidence.

The implementation lesson is direct. A memory object that can influence an action should carry a source pointer. If the system cannot reconstruct which original turn supported a final answer, it also cannot evaluate whether the memory policy helped or harmed the trajectory.

Practical lesson:
- store completed turns as compact records with stable source IDs, hashes, timestamps, tool outputs, and outcome labels;
- log selected memory IDs every time a bounded context is reconstructed;
- compare full history, rolling summaries, selected turn memory, and no-memory variants before changing compaction policy;
- keep memory-selection traces available for offline credit assignment, not only prompt reconstruction;
- treat lossy summaries as derived views, not as the only training or audit substrate.

Source:
- [ECHO](https://arxiv.org/abs/2606.31650v1)

## July 2 update: memory management is becoming an action policy

AutoMem strengthens the memory-systems thesis by making memory operations part of the agent's action space. The important move is not the file system itself. It is that read, write, search, append, and map-update decisions become traceable decisions that can be reviewed, optimized, and trained separately from task actions.

Practical lesson:
- expose memory operations through a narrow action API with typed events;
- log memory decisions with source episode, target file, operation, selected evidence, and downstream outcome;
- optimize memory scaffolds as versioned components, not hidden prompt edits;
- train or tune memory proficiency from successful memory decisions only after the trace can prove which decisions helped;
- keep task competence and memory competence separable in ablations.

Sources:
- [AutoMem](https://arxiv.org/abs/2607.01224v1)
- [AutoMem project](https://autolearnmem.github.io/)
- [autoLearnMem/AutoMem](https://github.com/autoLearnMem/AutoMem)

## July 3 update: bounded memory contracts beat transcript stuffing

AgenticSTS adds an experimental shape this topic needed: memory should be evaluated as a per-decision visibility contract. Instead of appending every prior observation, tool call, and reflection to each prompt, the harness assembles a fresh prompt through typed retrieval and preserves condition tags, frozen memory snapshots, skill snapshots, and prompt records.

Practical lesson:
- define which memory layers each decision is allowed to see;
- store retrieved item IDs, memory layer IDs, prompt records, and skill snapshot IDs with the trajectory;
- run no-store, full-history, typed-retrieval, and skill-triggered ablations on the same task;
- treat memory snapshots as versioned harness artifacts;
- score memory by downstream decision quality, not by retrieval plausibility alone.

Source:
- [AgenticSTS](https://arxiv.org/abs/2607.02255v1)

## July 5 update: memory must be tested by influence, not only recall

MemSyco-Bench and A-TMA sharpen the memory thesis from two sides. MemSyco-Bench shows that retrieved memories can induce sycophancy: the agent over-applies user preference, ignores objective evidence, or treats scoped personalization as fact. A-TMA shows the state version of the same failure: old, current, and transition facts can coexist in memory, mix during retrieval, and produce ghost-state answers.

Practical lesson:
- add memory tests where the correct behavior is to ignore, scope, or override a recalled memory;
- tag memory packets as current, superseded, historical, transition, conflicting, or personalization-only;
- evaluate bank maintenance, retrieval, and answer-time resolution separately;
- preserve source event and supersession lineage through summaries and derived memories;
- score memory by downstream decision quality, not only by storage and retrieval accuracy.

Sources:
- [MemSyco-Bench](https://arxiv.org/abs/2607.01071v2)
- [XMUDeepLIT/MemSyco-Bench](https://github.com/XMUDeepLIT/MemSyco-Bench)
- [A-TMA](https://arxiv.org/abs/2607.01935v1)


## July 30 update: memory security is a lifecycle test

MemSecBench turns memory poisoning into a linked Write-Execute-Forget protocol. The benchmark checks persistence, recall, adoption, external effect, targeted repair, and preservation of benign memory across seven checkpoints and 24 exact agent configurations.

Practical lesson:
- preserve one verified post-write snapshot and branch execute and repair tests from it;
- verify external effects programmatically rather than grading only model text;
- score malicious persistence, end-to-end attack success, selective repair, and benign preservation separately;
- bind harness, memory backend, model backend, prompts, snapshots, judges, and evidence packs to every case;
- treat missing evidence channels as evaluation errors, not as attack failures.

Artifact caveat: no paper-owned public implementation repository was found during the 2026-07-30 scan.

Source:
- [MemSecBench](https://arxiv.org/abs/2607.27080v1)

## Working conclusion

The next generation of agents will be differentiated less by how eloquently they speak and more by how faithfully and safely they remember. The winning systems will preserve evidence, route memory writes explicitly, retrieve context adaptively, abstain when memory is unsafe, validate high-value writes, make retention and pruning decisions replayable, query local graphs when code structure matters, promote only the right lessons into durable guidance, attach enough context for updates and temporal reasoning, choose abstraction levels that transfer across tasks, keep the most sensitive memory close to the user and under policy control, run durable memory through a governed database-backed state core, separate evaluation memory from user-facing memory, measure whether memories remain usable under scale, budgets, and writeback review, expose operation-level provenance, make reasoning history diffable, test belief-state stay/update/isolate decisions, gate retrieval by policy, resolve contradictions with bitemporal evidence, evaluate memory against heterogeneous evolving source streams, and defend memory write/read paths against poisoning so failures can be traced instead of guessed.


## July 8 update: multi-agent memory should preserve conflicts

StateFuse sharpens the memory-systems thesis for multi-agent runtimes. Branches, retries, and replicas should not silently overwrite each other. The memory contract should preserve immutable operations, evidence-linked claims, explicit conflicts, correction handles, and deterministic materialized views.

Practical lesson:
- treat disagreement as a first-class memory object;
- store claim provenance and evidence links with every durable assertion;
- use exact IDs and semantic handles for correction and retraction;
- materialize task-specific views from a canonical operation log instead of mutating shared truth in place;
- keep resolver output separate from the underlying conflict record.

Sources:
- [StateFuse paper](https://arxiv.org/abs/2607.05844v1)
- [nZiben/statefuse](https://github.com/nZiben/statefuse)

## July 10 update: memory should decide when to intervene

Remember When It Matters turns memory influence into an explicit policy. A sidecar memory agent maintains structured execution state and chooses whether a grounded reminder should enter the next action context or whether it should remain silent. That is more precise than passive retrieval or always-on injection because it makes memory influence observable, abstainable, and independently testable.

Practical lesson:
- maintain typed records for requirements, environment facts, failed attempts, diagnoses, and open subgoals;
- add explicit `inject` and `remain_silent` decisions before action-agent calls;
- log selected memory IDs, evidence, intervention reason, token cost, and downstream outcome;
- compare no-memory, passive, always-on, and selective variants on identical trajectories;
- keep proactive reminders grounded in stored evidence rather than turning the memory layer into a general advisor.

Artifact caveat: the advertised repository had no populated default branch during the 2026-07-10 scan, so this is an implementable architecture pattern but not yet a ready-to-run public package.

Sources:
- [Remember When It Matters](https://arxiv.org/abs/2607.08716v1)
- [Advertised proactive-memory-agent repository](https://github.com/yifannnwu/proactive-memory-agent)

## July 13 update: durable memory should preserve configuration, not replay traces

Shared Selective Persistent Memory adds a concrete promotion boundary. The reusable cross-session objects are task specifications, data schemas, tool configurations, and output constraints. Old reasoning traces, tool logs, intermediate states, and recovery paths remain episodic evidence and stay out of the next active context.

The architecture also connects memory to artifact operations: Git-versioned generated programs, draft isolation, role-based workspace sharing, and fresh runtime data binding without model reinvocation. The reported completion comparison, 96% selective memory versus 79% no memory and 71% full history, supports the direction but comes from a closed enterprise implementation.

Practical lesson:
- define explicit promotable memory types rather than summarizing whole sessions;
- keep raw episodes available for audit and close-match replay;
- version promoted memory with the generated artifact it governs;
- bind fresh data at runtime so repeated updates do not require another model call;
- test no-memory, full-history, summary, and selective-memory conditions on identical tasks.

Artifact caveat: no public implementation or dataset link is exposed. The four memory categories are implementable, but the reported end-to-end result is not independently reproducible from the paper alone.

Source:
- [Shared Selective Persistent Memory for Agentic LLM Systems](https://arxiv.org/abs/2607.09493v1)

## July 15 update: memory quality is an operation trace, not a final answer

MemOps gives memory systems a lifecycle-level test contract. Remembering, forgetting, updating, reflecting, and composed operations should each carry a trigger, target, scope, before state, after state, and supporting evidence. Final-answer accuracy is downstream evidence, not proof that the memory state is correct.

Practical lesson:
- store typed memory operations in a canonical event log;
- grade introduction capture, target binding, state transition, ordered trajectory, evidence use, and final answer separately;
- preserve explicit supersession and forgetting rather than relying on retrieval rank to hide stale values;
- compare turn-level retrieval, session-level retrieval, full context, and managed memory on identical lifecycle traces;
- test abstention when the ordered state trajectory cannot be reconstructed.

Artifact caveat: the public repository is MIT-licensed and populated, but the full pipeline needs external model APIs, an OpenAI-compatible gateway, UltraChat, and LLM judging.

Sources:
- [MemOps](https://arxiv.org/abs/2607.12893v1)
- [MemTensor/MemOps](https://github.com/MemTensor/MemOps)

## July 16 update: memory access is a control policy

MemCon makes retrieval, plan injection, re-retrieval, consolidation, forgetting, and silence explicit policy actions. That is the right boundary even if the first implementation uses rules rather than a learned bandit.

Practical lesson:
- expose memory actions behind one typed controller interface;
- log controller state, action, selected records, token cost, outcome, and policy update;
- include no-op and forget as normal actions, not error paths;
- keep evidence truth, provenance, retention authority, and destructive deletion outside the learned controller;
- evaluate static retrieval, always-on retrieval, selective intervention, and learned control on identical streams.

Artifact caveat: the repository is populated and its README declares MIT, but no license file or release was detected. Its large tree vendors multiple frameworks. Treat it as an architecture and experiment reference before attempting full reproduction.

Sources:
- [Memory as a Controlled Process](https://arxiv.org/abs/2607.13591v1)
- [ericjiang18/MemCon](https://github.com/ericjiang18/MemCon)

## July 24 update: working memory delivery should be a harness policy

Delivery, Not Storage shows that durable storage and reliable delivery are different systems. The model can ignore a pre-seeded store for 114 turns, while a harness can evaluate path, symbol, semantic, event, and temporal cues and inject a scoped fact at the relevant moment.

Practical lesson:
- keep memory evidence separate from trigger and delivery policy;
- evaluate cues on file, symbol, failure, phase, temporal, and compact-resume events;
- log candidates, injections, rejections, token cost, downstream use, and false deliveries;
- compare voluntary retrieval, always-on injection, and cue-triggered injection on identical tasks;
- preserve provenance and scope checks before injection reaches active context.

Evidence caveat: the reported probe covers one controlled coding task and no public implementation artifact. Treat the numbers as a motivating failure case, then measure false delivery and transfer locally.

Source:
- [Delivery, Not Storage](https://arxiv.org/abs/2607.20972v1)

## July 27 update: memory benchmarks need tenure checkpoints

Ground Truth First makes time a first-class memory evaluation variable. Facts are generated with validity intervals and source channels before conversations exist, then questions are created from that truth model. This avoids extracting an answer key from already-rendered dialogue.

Practical lesson:
- generate canonical facts before rendered conversations;
- test short, medium, and long tenure with identical answerer and judge versions;
- include as-of-date questions, supersession, staleness traps, source trust, and injection probes;
- report write quality, recall, read cost, and provenance failures separately;
- do not promote a short-horizon memory winner without a long-horizon checkpoint.

Artifact caveat: Veracium is a populated MIT-licensed repository and PyPI package, but this scan inspected it read-only. The nine-week ranking inversion covers six users and 108 long-horizon questions in a synthetic corpus.

Sources:
- [Ground Truth First](https://arxiv.org/abs/2607.21962v1)
- [Veracium](https://github.com/veracium-ai/Veracium)
- [Veracium on PyPI](https://pypi.org/project/veracium/)

## July 28 update: decision-time relevance can require world knowledge

Keep It InMind separates direct recall from indirect application. Query-conditioned retrieval can store a fact correctly and recall it on demand, yet fail to surface it when relevance depends on world knowledge not present in either text.

Practical lesson:
- pair direct recall with indirect application queries;
- instrument storage, target recall, bridge competence, and final application separately;
- keep high-impact stable constraints in typed visible state when feasible;
- compare query retrieval, proactive routing, and always-in-state profiles on identical tasks;
- treat memory routing as a policy problem, not only an embedding problem.

Artifact caveat: the public repository contains the 125-task dataset, schema, checksum, and documentation, but no release or GitHub license metadata. It was inspected read-only.

Sources:
- [Keep It InMind](https://arxiv.org/abs/2607.24368v1)
- [InMind repository](https://github.com/imlrz/InMind)
- [InMind project site](https://keep-it-inmind.github.io/)

## August 5 update: memory changes need transaction semantics

TARL strengthens the memory-control thesis by separating append, revise, reject, defer, and ignore. The important unit is not a retrieved paragraph or a Write/Hold label. It is a typed operation with a before state, after state, source, temporal scope, and execution result.

Practical lesson:
- retain accepted, pending, rejected, and superseded ledgers;
- keep the proposed operation separate from the deterministic executor;
- test next-state accuracy, pollution, conflict preservation, and calibration;
- preserve source-family holdouts and temporal shifts in regression suites;
- require explicit provenance for revisions and rejections.

Artifact caveat: the paper reports five-run cross-source results, but its code, TARL-Mem dataset, and reproduction materials are deferred until final publication.

Source:
- [TARL](https://arxiv.org/abs/2608.03699v1)
