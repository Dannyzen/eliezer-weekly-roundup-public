# Context Compaction Provenance

## Thesis

Agent context compaction must preserve typed origin and authority. A summary is a derived evidence object, not a new user instruction.

## Failure mode

Some harnesses serialize user messages, assistant messages, and tool output into one plain-text transcript with in-band role labels. Untrusted content can forge those labels. The summarizer then receives text in which true and forged roles are structurally indistinguishable, and the compacted memory can carry the forged instruction forward after the original evidence is gone.

Compaction Laundering measured this across nine coding-agent harnesses. Five flattening harnesses laundered forged approvals 87% to 100% of the time. Four role-typed harnesses rejected the identical attack in every measured case. The result isolates the serializer as the control point.

## Minimum control contract

1. Preserve role, source, principal, trust class, and message identity as typed fields.
2. Escape role-like markers inside untrusted payloads before serialization.
3. Record which source spans support each compacted claim.
4. Separate descriptive claims from permissions, procedures, and standing approvals.
5. Revalidate any compacted claim that could authorize a tool call or external effect.
6. Retain the uncompacted source or a tamper-evident reference long enough for audit and replay.
7. Run paired malicious and clean fixtures through the production serializer and summarizer.

## Admission test

A compactor passes only when:
- tool output cannot emerge as a user instruction;
- source references survive summarization;
- unsupported user-attributed claims are rejected or downgraded;
- effect authorization is checked against current policy outside the summary;
- the final receipt identifies the exact compacted claim and its source lineage.

## Evidence and limits

The paper includes pinned serializer captures, raw outputs, and a live paired demonstration. Its code-level result is stronger than a prompt-only attack because it explains why the model cannot recover deleted provenance. The evaluation remains author-run, targets specific versions, and does not establish that every current release remains vulnerable.

Implementability score: 0.91

Sources:
- [Compaction Laundering paper v1](https://arxiv.org/abs/2610.29869v1)
- [Compaction Laundering repository](https://github.com/pixee/compaction-laundering)

## November 25, 2026 deep dive: authenticated authority across context compaction

### Overview

The most important finding of the week is that context compaction is an authorization boundary, not only a context-management operation. `LLM Agent Authorization Across Context Compaction` shows that Claude Code and local Codex compaction can place model-written summaries where a request-derived authorizer expects user text. The summary may quote the user, third-party data, and injected content without preserving who authored each byte. The authorizer then treats a derived narrative as fresh authority.

This beats the week's recovery, benchmark, harness, and policy-administration findings because it identifies a general failure beneath all long-running agent products: once source identity is erased, a later security layer cannot reconstruct it from text alone. The paper contributes a formal limit, measurements on deployed harnesses, and a concrete gate that can be implemented and tested now.

### Core innovation

The paper separates the input used for reasoning from the input used for authorization.

- The acting agent may read a lossy model-written summary.
- The authorizer receives only authenticated authority-bearing turns.
- Each accepted user turn gets an immutable session-local occurrence record.
- A trusted packager carries the complete ordered sequence across compaction.
- A gate verifies occurrence witnesses, sequence completeness, ordering, and session binding.
- Any missing or inconsistent evidence installs an empty policy.

Theorem 1 states the reason this structure is necessary: a text-only authorizer can distinguish an attacker-written record from a legitimate record only to the extent that their text distributions are distinguishable. Prompts, marks, and stronger policy generators cannot restore authorship once the boundary has discarded it.

### Evidence

The paper reports:

- 319 AgentDojo episodes and 1,472 summaries for slot-placement tests;
- 192 task-tool pairs in a cross-benchmark check;
- shipped prompts from 11 harnesses;
- 100 Claude Code and 1,008 Codex live compactions;
- 320 frontier-model summaries tested with two policy generators;
- a banking case where summary-derived policy admitted the attacker account in 91% and 59% of cases, versus zero when policy used the user's words;
- 40 attacked AgentDojo episodes with the witnessed-request gate, with no completed attacker action;
- eight adaptive gate attacks, including replay through agent-writable files.

The artifact snapshot was inspected read-only. It contains the gate, experiment drivers, and analysis scripts. It excludes recorded outputs and requires provider access, pinned agent versions, AgentDojo 1.2.2, and Progent for a full rerun.

### Why it matters

Compaction is now part of the trusted computing base. A summary can preserve enough information for the agent to continue while changing the apparent source of a payee, recipient, path, or approval. Better summarization does not solve the problem because accurate retention can preserve attacker-controlled data just as faithfully as legitimate data.

The architectural rule is direct: descriptive context may be derived, compressed, and model-written; authority must remain bound to an authenticated principal and exact source bytes. Any product that lets a summary, memory, retrieval result, or handoff note enter an authorization slot has collapsed evidence and authority into one mutable representation.

### Fit into the agentic stack

This belongs primarily in the Strategy control plane:

1. Ingress authenticates principals and assigns immutable message identities.
2. The event log preserves typed origin, exact bytes, ordering, and session scope.
3. Compaction produces a derived reasoning view with source references.
4. Authorization reads a separate projection of authenticated authority-bearing records.
5. The execution boundary checks the resulting grant against the proposed effect.
6. Receipts bind source records, compaction identity, grant, policy version, and observed effect.

The model never owns the authority projection. It may propose actions from the reasoning view, but trusted runtime code constructs and validates the authorization view.

### Practical tools, repos, and methodologies worth trying now

- Use append-only event records with principal, origin class, session ID, occurrence counter, canonical bytes, and content hash.
- Sign or MAC authority-bearing occurrences at ingress, with keys unavailable to agent tools.
- Commit to the complete ordered occurrence list at every compaction boundary.
- Maintain dual projections: a compact reasoning transcript and an authenticated authority transcript.
- Add property tests that delete, reorder, duplicate, forge, or replay witnessed records and require a fail-closed empty grant.
- Replay AgentDojo injection episodes before and after compaction, grading actual effects rather than model explanations.
- Inspect the paper's [artifact snapshot](https://anonymous.4open.science/r/LLM-Agent-Authorization-Across-Context-Compaction-504E/) for the witness and completeness-check structure before designing a production-native equivalent.
- Evaluate [Progent](https://github.com/sunblaze-ucb/progent) only as the policy generator behind a source-authenticated boundary, not as a substitute for that boundary.

### Implementation complexity

The narrow control is straightforward: never derive authorization from a model-written summary. A production gate is harder because it needs trusted ingress, canonical framing, protected keys, monotonic counters, a complete sequence commitment, stable round trips, and migration of existing sessions.

A realistic first prototype can wrap one effectful workflow with:

1. an append-only user-message ledger;
2. HMAC witnesses over canonical message envelopes;
3. a compaction hook that commits the ordered witness list;
4. an authorizer adapter that reads only verified user records;
5. adversarial fixtures for omission, reordering, replay, and forged origin;
6. an effect receipt that names the exact source records used.

Implementability score: 0.72

### What remains conceptual or unproven

The gate was evaluated on replayed AgentDojo sessions and production-shaped prompts, not integrated end to end into a shipping Claude Code or Codex authorization hook. Its guarantees depend on protected keys, correct origin assignment, canonical framing, complete ordered packaging, and a trusted channel between the packager and authorizer.

The weakest point is delegated authority from documents. If the user says "pay the account in this invoice," the account value is not in the user's authenticated bytes. The paper correctly leaves that value under the text-only bound until the document source is independently authenticated, for example through signed tool output or a trusted business-system record. The gate protects direct user authority; it does not solve source trust for every referenced object.

### Strategic implications for Danny's worldview and product thinking

The agentic stack should carry two products of every context transformation: a useful reasoning view and a non-forgeable authority view. This sharpens the broader rule that evidence is not authority. Even accurate evidence becomes dangerous when a runtime silently places it in an authority-bearing slot.

For Hermes and FriendVM-style systems, session compaction, memory writeback, cross-agent handoff, and resumed jobs should all preserve principal-bound authority outside prose. The durable product opportunity is an authority ledger and release gate that survives model changes, context compression, channel movement, and long-running work.

### Core source links

- [LLM Agent Authorization Across Context Compaction v1](https://arxiv.org/abs/2611.32194v1)
- [Versioned PDF](https://arxiv.org/pdf/2611.32194v1)
- [Read-only artifact snapshot](https://anonymous.4open.science/r/LLM-Agent-Authorization-Across-Context-Compaction-504E/)
- [Progent](https://github.com/sunblaze-ucb/progent)

## November 3, 2026 update: retained policy still needs external enforcement

ARCBench shows that post-compaction compliance can fail even when the governing rule survives in context. Compacted runs that retained the rule violated more than twice as often as full-history runs, and the strongest summary defense restored the rule without eliminating violations.

Practical lesson:
- store governing policy outside lossy conversation summaries;
- preserve source identity and policy version through compaction;
- score rule retention and action compliance separately;
- test later requests that conflict with retained policy;
- reauthorize consequential effects against current policy after compaction.

Artifact status: the public repository contains benchmark cases, metrics, tests, a pinned harness, and reproduction scripts. Study rows are absent, and reproduction requires model access.

Implementability score: 0.84

Sources:
- [ARCBench paper v1](https://arxiv.org/abs/2611.03223v1)
- [ARCBench repository](https://github.com/VUAISec/ARCBench)


## November 5, 2026 update: summaries can manufacture policy without an attacker

Unsupported Policy in Self-Written Handoff Summaries shows that compaction can create authority errors even without prompt injection. Two readers confirmed unsupported restrictions in 1.2% and 2.4% of readable summaries and unsupported authorizations in 0.1% and 1.3%. Neutralizing false approvals reduced unauthorized actions from 24 to 7 of 120 held-out runs in a post hoc analysis.

Practical lesson:
- store permissions and requirements outside the model-authored summary;
- classify summary policy claims as quoted, derived, or unsupported;
- require source links for approval and prohibition claims;
- reauthorize every consequential effect after handoff;
- use same-snapshot replay to test whether a sentence changes successor behavior.

Evidence caveat: the pre-specified restriction replay was not significant. The restriction effect is fragile, while the false-approval result and source-of-authority prompt intervention are stronger operational signals.

Implementability score: 0.91

Sources:
- [paper v1](https://arxiv.org/abs/2611.06545v1)
- [read-only code and data repository](https://github.com/Chuw1/handoff-audit)
