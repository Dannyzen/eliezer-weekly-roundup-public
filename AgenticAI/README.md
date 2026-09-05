# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-05

### A crash-passing patch is not a security acceptance

Summary: SEC-BENCH top agents clear Single-PoC rates above 97%, then drop to 75-82% with multiple PoCs and to roughly half with semantic validation. 25% of agent patches match historical developer fixes. 81% of Codex + GPT-5.6 Sol patches edit the crash stack even when the root cause is elsewhere.

Analysis: [daily analysis](2026-09-05/reasoning.md#a-crash-passing-patch-is-not-a-security-acceptance)
Core source: [PatchBench](https://arxiv.org/abs/2609.04075v1)
Tools and methodologies worth exploring now: related-PoC security suites, semantic validation on benign inputs and unit tests, diff-aware historical-patch similarity, crash-stack versus root-cause counters
Implementability score: 0.70

### Index traces as owned memory, not as a chat archive

Summary: funes indexes Claude Code, Codex, pi, and Hermes sessions into one local Lance dataset, returns original text with session and turn provenance, and can publish a private-by-default Hugging Face dataset. Embedding and reranking stay on-device.

Analysis: [daily analysis](2026-09-05/reasoning.md#index-traces-as-owned-memory-not-as-a-chat-archive)
Core sources: [blog](https://huggingface.co/blog/funes), [huggingface/funes](https://github.com/huggingface/funes)
Tools and methodologies worth exploring now: `funes add hermes`, local `recall`/`get`, on-device embedding, private Hub datasets, hook-hash admission
Implementability score: 0.88

### Speculate into a snapshot, commit only matching macros

Summary: Speculative Macro Commit drafts multi-step action chains on an isolated snapshot and commits them only when the actor's next tool call matches the first drafted action. AppWorld wall time falls 44.9% versus sequential execution, with TGC 70/168 to 68/168.

Analysis: [daily analysis](2026-09-05/reasoning.md#speculate-into-a-snapshot-commit-only-matching-macros)
Core source: [Speculative Macro Commit](https://arxiv.org/abs/2609.03236v1)
Tools and methodologies worth exploring now: isolated draft snapshots, first-action match before commit, macros as a runtime library rather than extra tools, committed-versus-discarded draft counters
Implementability score: 0.55

## Current implication

PoC-pass, a sequential tool loop, and a session log are observations. Security acceptance needs a second oracle. Serving needs snapshot isolation before speculative commits. Memory needs indexed provenance, not a transcript paste.
