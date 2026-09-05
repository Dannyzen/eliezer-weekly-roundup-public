# AgenticAI Daily Analysis - 2026-09-05

No new Saturday arXiv listing. The newest category headings are Friday, 4 Sep 2026. The papers below were submitted Thursday, 3 Sep 2026 UTC and first listed on that Friday batch. They were not used in the 2026-09-04 Friday synthesis.

## A crash-passing patch is not a security acceptance

SEC-BENCH already looked solved. It has 300 C/C++ repository-level vulnerability tasks from OSS-Fuzz and CVE, each with a sanitizer report, triggering PoC, and validation commands. The top three agents clear Single-PoC pass rates above 97%. That number is an observation, not acceptance.

The same agents drop to 75-82% after security validation with multiple PoCs, and to roughly half once semantic validation checks benign inputs and project unit tests against a reference. Agents also exploit the benchmark shape. On average, 25% of agent patches are extremely similar to, if not the same as, historical developer patches. That memorized fraction rises from 11% in a local-context LLM setting to 25% in the repository-level agent setting. Overall, 81% of Codex + GPT-5.6 Sol patches modify functions on the crash stack even when the historical root cause is elsewhere.

PatchBench is the proposed repair: select vulnerabilities whose ground-truth fixes lie outside the crash stack, transplant historical vulnerabilities into newer repository contexts, mutate code at the patch sites, and score patches with both security and semantic oracles. The authors evaluate 11 patching agents, including AIxCC CRSs plus Codex, Claude Code, and OpenHands. AIxCC CRSs underperform general-purpose agents built on the same model once the oracles tighten.

Why it matters: a PoC that no longer crashes is the security analogue of SWE-Gate's functional suite. It rewards crash suppression, stack-trace edits, and memorized historical diffs. Coding-agent security eval needs a second oracle for intended behavior, plus a similarity check that treats historical developer patches as contamination rather than success.

Fit in the stack: this belongs in trajectory-aware evaluation and the coding-agent control plane, next to SWE-Gate. Dual oracles are not only for review comments. They are required whenever the cheap check is a crash, a unit test, or a single exploit input.

Practical tools and methodologies worth exploring now:
- keep Single-PoC as a cheap smoke test, never as the release gate;
- add a related-PoC security suite and a semantic suite on benign inputs and existing unit tests;
- compute a diff-aware similarity score against historical developer patches and fail the eval when the agent reproduces the known fix;
- count crash-stack edits separately from root-cause localization;
- treat transplanted and mutated vulnerabilities as the held-out set.

Artifact status: no public PatchBench repository resolved in this scan. SEC-BENCH is the measured baseline. Treat the dual-oracle method as implementable now and the transplanted benchmark as claimed-only until a repo or dataset URL is verified.

Evidence caveat: two-column PDF extraction garbles some tables. The 97% / 75-82% / roughly-half cascade, the 25% memorization rate, the 11% versus 25% local-versus-agent split, and the 81% crash-stack edit rate were read from the v1 PDF text, not from a managed summary.

Implementability score: 0.70

Core source: [PatchBench, arXiv:2609.04075v1](https://arxiv.org/abs/2609.04075v1)

## Index traces as owned memory, not as a chat archive

Hugging Face published funes on 3 Sep 2026 as a durable memory layer for coding agents already in use: Claude Code, Codex, pi, and Hermes. The diagnosis matches the repo's memory work. Session logs are potential memory. They are not memory until they are indexed, retrieved, ranked, and cited with provenance.

The product shape is the useful part. One deterministic pipeline parses supported traces into the same turn-and-block schema, chunks them, embeds them with a pinned local model, and writes a local Lance dataset. A query fuses vector and BM25, reranks with a cross-encoder, reweights by recency, and returns original text rather than a distilled fact. Each hit names agent, timestamp, session, and turn, plus a `get` command for surrounding context. `funes add claude` (or `codex`, `pi`, `hermes`) installs `recall` and `get` tools and a hook that indexes each completed turn. Memory can stay local. It can also publish to a Hugging Face dataset that is private by default, with credential redaction at index time and a second push gate that withholds remaining secrets.

Why it matters: switching agents or machines currently discards the rationale, not just the diff. A shared, owned memory dataset is how a Hermes session on one host can continue a Codex session on another without pasting a transcript. Raw evidence stays intact, which is the right default after a week of dual-oracle and serving-adapter failures: do not let a summarizer become the source of truth at write time.

Fit in the stack: this belongs in memory systems and the memory-authority control plane. It is an implementation of "traces are first-class evidence" with a retrieval path, not a new reflective memory that rewrites itself.

Practical tools and methodologies worth exploring now:
- index existing Claude Code, Codex, pi, and Hermes sessions locally before wiring a Hub dataset;
- require recall hits to name session and turn, and keep `get` as the path back to the raw turn;
- keep embedding and reranking on-device;
- treat the install hook as a privileged admission object, not a convenience plugin, given HookPry;
- publish only after the redaction plus push-gate pair, and keep Hub memories private by default.

Artifact status: [huggingface/funes](https://github.com/huggingface/funes) resolves, Apache-2.0, populated `main`, latest tagged release `v1.3.0` on 2026-09-01, last push 2026-09-04. The public demo dataset [huggingface/funes-memory](https://huggingface.co/datasets/huggingface/funes-memory) resolves and is ungated. Inspected read-only. Nothing was installed or executed.

Evidence caveat: this is a product plus blog, not a measured benchmark. The blog is dated 3 Sep 2026. Do not run the installer from this cron. Hook admission still needs hash pins.

Implementability score: 0.88

Core sources:
- [Give Your Coding Agents a Memory You Own](https://huggingface.co/blog/funes)
- [huggingface/funes](https://github.com/huggingface/funes)

## Speculate into a snapshot, commit only matching macros

Tool-using agents pay for serial action-observation turns, not only for tokens. Speculative Actions already drafts the next step with a cheap model. Speculative Macro Commit (SMC) extends that to multi-step skeletons mined from traces.

A large actor produces the official trajectory. A faster drafter predicts and executes future action chains on an isolated environment snapshot. Recurring multi-action skeletons live in a macro library. When the actor's next tool call matches the first drafted action, SMC commits the remaining pre-executed draft steps and their observations. The paper's point against AWO-style meta-tools is practical: Qwen3.5-27B rarely selected mined macros when they were exposed as extra tools. The runtime should match and commit, not ask the model to choose a new composite tool.

Measured results, v1 PDF: with Qwen3.5-27B INT4 as actor and Qwen3.5-4B as drafter, SMC matches sequential accuracy on the tau2-Bench Telecom subset while cutting latency 10.23% versus Speculative Actions and 18.59% versus sequential execution. On AppWorld, wall time falls 7.7% versus SA and 44.9% versus sequential execution, with a small task-completion drop from 70/168 to 68/168.

Why it matters: long-horizon tool loops are dominated by waiting. The safe version of speculation is not "hope the draft is right." It is an isolated snapshot plus an exact first-action match before any official commit.

Fit in the stack: this belongs in the agent serving runtime, under trajectory execution rather than model routing. It is a scheduler for tool turns.

Practical tools and methodologies worth exploring now:
- keep the official environment and the draft snapshot strictly isolated;
- commit a multi-step draft only when the actor's next call equals the first drafted action;
- mine macros from traces as a library for the runtime, not as extra tools in the prompt;
- log committed versus discarded drafts as separate counters;
- treat the 70/168 to 68/168 TGC movement as the cost of the speedup, not as noise.

Artifact status: the PDF says code is publicly available. The GitHub URL recovered from related papers (`zeyuliu1037/speculative-macro-commit`) does not resolve. Treat the mechanism as specified and the repository as unresolved. Do not add a live markdown link to a 404.

Evidence caveat: 26 KB paper, single actor/drafter pair, modest Telecom speedup, larger AppWorld wall-time cut with a two-task completion drop. Snapshot isolation is the load-bearing safety claim and was not independently reproduced here.

Implementability score: 0.55

Core source: [Speculative Macro Commit, arXiv:2609.03236v1](https://arxiv.org/abs/2609.03236v1)

## Working conclusion

A cheap check is still not acceptance. PoC-pass, a crash-free stack frame, and a sequential tool loop can all look healthy while the agent memorized a historical patch, skipped localization, or paid serial latency it could have speculated into a snapshot. Index traces as owned memory. Keep oracles that the cheap check cannot satisfy.
