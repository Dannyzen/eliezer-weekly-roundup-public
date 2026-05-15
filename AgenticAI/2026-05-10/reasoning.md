# AgenticAI Daily Analysis: 2026-05-10

Today's agentic-stack signal is practical and implementation-heavy. Memory systems are becoming structured runtime infrastructure. Tool access is splitting into discover/inspect/call/audit phases to control prompt bloat. Agent evaluation is absorbing chaos-engineering habits so teams can break systems before users do.

## Memory is becoming structured agent state, not transcript recall

Memori and Statewave are strong product signals because they both describe memory as agent-native infrastructure rather than a hidden prompt appendix. Memori's README says it builds "memory from what agents do, not just what they say," supports entity/process attribution, groups interactions into sessions, captures conversation and agent execution including tool calls, decisions, and outcomes, and exposes MCP and Hermes integration paths. Statewave makes the same architecture more database-like: raw events become typed memories with confidence scores, provenance, subject timelines, token-bounded context bundles, conflict handling, OpenTelemetry spans, connectors, and Postgres/pgvector deployment.

The research side is converging with the product side. MemReranker argues that generic semantic rerankers miss the key information needed for memory questions, especially temporal constraints, causal reasoning, coreference, and dialogue context. SkillRet extends the same retrieval problem to reusable agent skills: once the skill library is large, invoking skills by name stops scaling and retrieval quality becomes an agent capability.

Why it matters: long-lived agents do not fail because they have no storage. They fail because storage does not know what to admit, what changed, what evidence supports a memory, what entity/session it belongs to, and when retrieval should abstain or rerank. The implementable pattern is now clear enough to try.

How it fits into the stack: this belongs in the memory and context layer. It connects directly to previous work on write-path admission, stale-memory invalidation, tiered memory, and event preservation. The new emphasis is operational: memory systems should expose subject/session attribution, provenance, confidence, retrieval budgets, and connectors instead of hiding memory behind opaque context injection.

Implementable now:
- store agent events with entity, process, session, tool-call, decision, and outcome metadata;
- preserve raw events and compile typed memories as derived artifacts with provenance;
- compare transcript stuffing, simple RAG, Memori/Statewave-style memory, and reranked memory on repeated user/project tasks;
- add stale-memory and implicit-conflict fixtures before trusting personalized recall;
- add skill-retrieval tests once a skill catalog grows beyond explicit name invocation.

Tools, repos, and methodologies worth exploring:
- Memori: https://github.com/MemoriLabs/Memori
- Statewave: https://github.com/smaramwbc/statewave
- MemReranker methodology: https://arxiv.org/abs/2605.06132
- SkillRet retrieval benchmark shape: https://arxiv.org/abs/2605.05726
- pgvector/Postgres, SQLite/FTS, rerankers, LoCoMo-style memory tests, stale-memory evals

Implementability score: 0.80

Core source links:
- https://github.com/MemoriLabs/Memori
- https://github.com/smaramwbc/statewave
- https://arxiv.org/abs/2605.06132
- https://arxiv.org/abs/2605.05726

## Capability routing is escaping prompt-bloated MCP catalogs

QVeris is a useful current implementation signal for a pattern yesterday's TSCG and DADL sources made explicit: tool catalogs are too important to leave as passive schema blobs in every prompt. The QVeris README frames the system around `Discover / Inspect / Call / Audit`, exposes CLI, MCP, Python SDK, and REST surfaces, and explicitly argues that CLI execution can be more token-efficient than MCP because it runs as a subprocess rather than injecting every tool schema into the model context.

The important lesson is not that QVeris specifically is the default answer. The lesson is architectural: tool access is becoming a routed capability network. An agent should be able to discover candidate capabilities cheaply, inspect only the small subset it might use, execute through a deterministic interface, and then audit the usage and charge/effect evidence without dumping the whole catalog into the prompt.

Why it matters: large MCP catalogs create token cost, latency, and attention problems. They also make governance harder because the active tool surface can become too broad to reason about. A discover/inspect/call/audit protocol gives the harness a smaller decision surface and better evidence.

How it fits into the stack: this is an agent-harness and tool-governance pattern. It pairs naturally with tool-schema compilation, MCP gateways, OpenTelemetry, and policy layers. The harness should choose the minimum tool exposure mode needed for the task: prompt-level schema, MCP server, CLI call, gateway API, or manual approval.

Implementable now:
- define tool access as discover, inspect, call, and audit phases;
- keep large catalogs outside the model prompt until the agent has narrowed candidates;
- log discovery query, candidate IDs, inspected schemas, final call, result, cost, latency, and audit verdict;
- compare MCP schema injection against CLI/subprocess calls on correctness, token cost, latency, and debuggability;
- require trust review before allowing an external capability marketplace to execute side-effecting actions.

Tools, repos, and methodologies worth exploring:
- QVeris Agent Toolkit: https://github.com/QVerisAI/qveris-agent-toolkit
- MCP gateway middleware, CLI/subprocess tool adapters, tool registry scorecards, schema compilation, OpenTelemetry

Implementability score: 0.68

Core source link:
- https://github.com/QVerisAI/qveris-agent-toolkit

## Agent eval is becoming chaos engineering

EvalMonkey is useful because it packages a pragmatic local eval harness for agents rather than another static leaderboard. Its README describes an agent benchmarking and chaos-engineering framework that talks to agents over plain HTTP, supports multiple common frameworks, runs standard text benchmarks, injects latency/header/schema perturbations, and emits `traces.json`, `evals.json`, and `improvement_prompt.md` when scores are poor.

This fits the week's evaluation theme. TEBench showed that coding agents react to failing tests but miss stale or missing tests. PrefixGuard showed that traces can warn before final failure. EvalMonkey contributes the operator workflow: run a small local benchmark, perturb the environment, preserve traces, and hand the failure evidence back to a coding agent or human maintainer.

Why it matters: production agents fail in the seams: bad request formats, changed schemas, latency spikes, missing tools, ambiguous response paths, and middleware behavior. If eval only checks clean benchmark prompts, it misses the failures that break deployments.

How it fits into the stack: this belongs in trajectory-aware evaluation and harness operations. The eval harness should be close enough to the runtime to perturb transport, schema, latency, and tool assumptions, while still producing artifacts that can be replayed and repaired.

Implementable now:
- expose internal agents through stable local HTTP endpoints;
- start with tiny benchmark samples as smoke tests before spending on full evals;
- inject schema corruption, latency, malformed headers, and response-shape mismatches;
- preserve traces, eval cases, and improvement prompts as CI artifacts;
- connect chaos failures to concrete harness fixes, not just model swaps.

Tools, repos, and methodologies worth exploring:
- EvalMonkey: https://github.com/Corbell-AI/evalmonkey
- LangGraph, Pydantic AI, OpenAI Agents SDK, AutoGen, chaos engineering, trace artifacts, TEBench-style stale/missing-test fixtures

Implementability score: 0.82

Core source link:
- https://github.com/Corbell-AI/evalmonkey
