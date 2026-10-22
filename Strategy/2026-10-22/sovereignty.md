# Strategy Daily Analysis - 2026-10-22

This scan covers a paper first listed by arXiv on 2026-10-22 and submitted on 2026-10-21. The public artifact was inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Preserve origin through context compaction

Compaction Laundering identifies a code-level trust-boundary failure in coding agents that flatten typed user, assistant, and tool messages into one plain string before summarization. An attacker-controlled file or webpage can include an in-band marker such as `[User]:`, which the summarizer may preserve as a genuine instruction after the original provenance has been discarded.

Across five flattening harnesses, the forged approval survived compaction 87% to 100% of the time, including contexts up to roughly 908,000 tokens. The same attack succeeded 0% across four role-typed harnesses. A paired live pi TUI demonstration produced attacker-controlled sandbox execution at roughly 50% versus 0% in the clean arm. A provenance-contrast check caught 77% of laundering while demoting 2% of legitimate summary content.

The decisive finding is architectural: once the serializer destroys origin, a prompt cannot recover it. Compaction is a typed state transition, not a text-summarization convenience.

Implementable now:
- keep message roles and source identities typed through compaction;
- escape role-like labels inside untrusted content before any flattening step;
- compare user-attributed summary claims against genuine user turns;
- preserve links from compacted claims to source messages;
- test malicious files, webpages, dependency docs, and tool output through real compaction;
- require fresh authorization before compacted content can approve an effect.

Artifact status: the paper's original URL redirects to the public MIT-licensed `pixee/compaction-laundering` repository. Its default branch is populated with 223 files, including experiment, data, and demonstration directories. The study is author-run and evaluates pinned harness versions, so current releases need separate checks.

Implementability score: 0.91

Core sources:
- [Compaction Laundering paper v1](https://arxiv.org/abs/2610.29869v1)
- [Compaction Laundering repository](https://github.com/pixee/compaction-laundering)

Durable deep dive: [Context Compaction Provenance](../context-compaction-provenance/context-compaction-provenance.md)

## Strategic implication

Context compaction is an authority boundary. The runtime must preserve who said what, where it came from, and whether it can authorize action. A shorter context that erases those distinctions is operationally unsafe even when its summary is semantically accurate.
