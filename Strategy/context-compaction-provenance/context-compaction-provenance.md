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
