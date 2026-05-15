# Daily AgenticAI Scan: 2026-05-09

Today's strongest implementation signal is that tool access and evaluation are becoming compiler-and-monitor problems. The useful agent does not merely receive more tools or produce a nicer final answer. It gets a compressed, model-legible tool surface; it emits traces that can be scored before terminal failure; and it can be tested against project-level states where the test suite itself must evolve.

## Tool-schema compilation turns MCP catalogs into an optimization target

Core source: [TSCG: Deterministic Tool-Schema Compilation for Agentic LLM Deployments](https://arxiv.org/abs/2605.04107)

Supporting sources:
- [SKZL-AI/tscg](https://github.com/SKZL-AI/tscg)
- [DADL: A Declarative Description Language for Enterprise Tool Libraries in LLM Agent Systems](https://arxiv.org/abs/2605.05247)

TSCG is the most actionable tool-use finding in today's scan. The paper argues that production agent frameworks transmit tool schemas as JSON, but language models often interpret that representation poorly at production catalog sizes. TSCG converts JSON schemas into compact structured text through a deterministic compiler, not through another model call, fine-tuning step, or runtime search loop. The arXiv abstract reports a formal compression bound above 51%, roughly 19,000 benchmark calls, and large recovery effects for small models at 20 to 50 tools. The repository describes npm packages for `@tscg/core`, `@tscg/mcp-proxy`, and `@tscg/tool-optimizer`.

The durable point is bigger than one repository. Tool schemas are now part of the agent harness. If a harness exposes 30, 50, or 200 tools, the schema representation itself becomes a cost, accuracy, latency, and routing variable. DADL points in the same direction from the enterprise API side: instead of one wrapper server per REST API, describe endpoints, auth, pagination, response shaping, and access classification declaratively, then route through one controlled execution layer.

Why it matters: MCP adoption alone does not make a tool surface usable. The next layer is schema compilation, catalog summarization, tool grouping, and access classification that can be tested like ordinary infrastructure.

How it fits into the stack:
- Harness layer: tool descriptions become versioned, compiled artifacts rather than ad hoc prompt text.
- Model-routing layer: small or local models may become viable for larger tool catalogs when schemas are represented in a model-legible form.
- Gateway layer: catalog compression and declarative API descriptions can sit before policy, logging, and approval hooks.
- Evaluation layer: tool-call accuracy should be measured against schema representation variants, not only model families.

Implementable now:
- Audit the largest MCP/tool catalogs for repeated JSON-schema overhead, verbose descriptions, and ambiguous parameters.
- Try a deterministic schema-compression layer in front of low-risk tools before expanding to privileged tools.
- Record tool-schema version, compression profile, catalog size, and model in every tool-call trace.
- Evaluate native JSON schemas versus compiled/structured representations on the same tasks before adding more tools.
- Treat API-description files as reviewed infrastructure artifacts with owners, scopes, and changelogs.

Tools, repos, and methodologies worth exploring:
- `@tscg/mcp-proxy`, `@tscg/tool-optimizer`, LangChain/Vercel AI SDK tool wrappers, MCP gateway middleware
- JSON Schema audits, catalog-size sweeps, BFCL-style tool-call tests, OpenTelemetry traces with schema-version attributes
- DADL-style declarative API catalogs for internal tools

Implementability score: 0.86

## Agent evaluation is shifting to prefix warnings and test-suite co-evolution

Core sources:
- [PrefixGuard: From LLM-Agent Traces to Online Failure-Warning Monitors](https://arxiv.org/abs/2605.06455)
- [Breaking, Stale, or Missing? Benchmarking Coding Agents on Project-Level Test Evolution](https://arxiv.org/abs/2605.06125)
- [iSEngLab/TEBench](https://github.com/iSEngLab/TEBench)

Practical tooling source:
- [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

PrefixGuard and TEBench push evaluation earlier in the run. PrefixGuard trains lightweight prefix-risk monitors from typed trace views, so a long tool-using agent can emit a warning before a final outcome check arrives. The paper's important claim is not that monitors are perfect; it is that typed trace representations beat raw text controls and that online warning should be evaluated as its own protocol.

TEBench adds the coding-agent version of the same lesson. Real projects do not only need code changes. They need tests to co-evolve with production changes. The benchmark separates Test-Breaking, Test-Stale, and Test-Missing cases, forcing agents to identify which tests need updates and where new tests are required. That is a better coding-agent eval than asking whether a patch happens to pass today's suite.

Chrome DevTools MCP is the implementation-side demand signal. It gives coding agents access to live browser state, console messages, network requests, screenshots, and performance traces through MCP. This is useful only if the resulting evidence becomes part of the trace and evaluation loop rather than another ungoverned tool surface.

Why it matters: final-pass eval is too late for autonomous workflows. Agents need runtime warning, evidence capture, and regression tasks that measure whether the system maintained the surrounding verification harness.

How it fits into the stack:
- Trace layer: raw event logs need typed adapters that preserve tool calls, observations, state changes, and risk signals.
- Evaluation layer: project-level eval should include stale tests and missing tests, not only failing tests.
- Developer-tool layer: browser/network/runtime evidence should feed the trace store and CI gates.
- Improvement loop: failed prefixes and stale-test misses become new regression fixtures.

Implementable now:
- Add prefix-level warning labels to existing agent traces: risky command, repeated failed retrieval, missing source evidence, stale test, missing browser assertion.
- Build a small internal TEBench-style fixture set from real commits where tests broke, went stale, or were missing.
- Feed Chrome DevTools MCP or equivalent browser evidence into CI artifacts and agent traces when debugging web apps.
- Compare final success, prefix warning quality, test-update quality, and human-intervention rate as separate metrics.

Tools, repos, and methodologies worth exploring:
- OpenTelemetry spans, LangSmith/Langfuse traces, typed-step adapters, simple supervised risk classifiers
- TEBench methodology, affected-test analysis, coverage overlap, stale-test fixtures
- Chrome DevTools MCP, Playwright traces, browser console/network evidence as graded artifacts

Implementability score: 0.78

## Watchlist signals

- [LatentRAG](https://arxiv.org/abs/2605.06285) and [MemReranker](https://arxiv.org/abs/2605.06132) both argue that agent retrieval and memory need more than semantic similarity. The practical move is still to log retrieval intent, time, dialogue context, and negative evidence before adopting new latent-retrieval models.
- [MASPO](https://arxiv.org/abs/2605.06623) is a useful multi-agent prompt-optimization signal, but it should be tested after prompt-only and single-agent baselines. Joint prompt optimization is not a substitute for delegation ledgers.
- GitHub Trending surfaced several demand signals — [agentmemory](https://github.com/rohitg00/agentmemory), [agent-skills](https://github.com/addyosmani/agent-skills), [CodeGraph](https://github.com/colbymchenry/codegraph), and [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp). Treat these as product-shape evidence until their benchmark claims are reproduced in a local harness.

## Scan quality note

The arXiv API returned HTTP 429 during category queries, so this scan used arXiv recent-category pages and direct abstract-page parsing. GitHub Trending was used only as a demand signal; repository findings were grounded with `gh repo view` metadata and raw README inspection. No external repository code was cloned, installed, built, or executed.
