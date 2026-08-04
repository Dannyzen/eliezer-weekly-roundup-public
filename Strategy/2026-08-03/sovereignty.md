# Strategy Daily Sovereignty - 2026-08-03

## Scope

Today's strongest strategy finding is that memory consolidation can erase source authority while preserving an action trigger. Persistent memory therefore needs platform-owned provenance and an execution-time non-amplification gate.

## Memory summaries may compress information, not upgrade authority

Memory Provenance Laundering identifies a cross-task attack: untrusted external content is consolidated into a compact memory, then later retrieved as apparent user history, workflow support, or prior confirmation. The malicious surface wording can disappear while the action trigger survives.

The proposed Provenance-Preserving Memory Firewall stores platform-maintained source, trust, transformation history, risk labels, and confirmation state. Before tool execution, it binds action-relevant memories to the exact call arguments and checks whether their authority is sufficient for the effect. In the paper's schema-grounded evaluation, vulnerable consolidated memories reach attack success rates up to 1.000. With intact platform provenance, confirmation, and risk labels, no evaluated unauthorized high-risk action passes the gate while confirmed benign and targeted low-risk uses remain executable.

Why it matters: content filters protect the current prompt. They do not stop a later summary from laundering an external observation into trusted-seeming history. The invariant must survive write, transform, retrieve, and execute.

Strategy fit: memory authority, evidence provenance, untrusted-data boundaries, execution control, and tool authorization.

Implementable now:
- store provenance outside model-authored memory text;
- preserve source, trust tier, derivation chain, confirmation, scope, risk, and expiry through consolidation;
- compute which memories support each tool argument;
- deny high-risk actions when supporting memory lacks sufficient authority;
- require fresh trusted confirmation rather than allowing memory to invent or inherit it;
- test direct, summarized, trace-derived, browser-transfer, decoy, and metadata-corruption cases.

Tools and methodologies worth exploring:
- a PPMF-style memory middleware;
- Cedar, OPA, or a small deterministic risk policy;
- append-only memory lineage;
- exact-argument action manifests;
- memory-write, derive, retrieve, authorize, deny, and effect trace spans.

Implementability score: **0.67**

Caveat: the evaluation is author-controlled and schema-grounded. The paper says sanitized scenarios and scripts are planned for release, but no public artifact URL was exposed on the primary pages. The guarantee also depends on platform metadata remaining intact; adversarial confirmation or risk-label corruption is explicitly outside the trusted boundary.

Core source:
- https://arxiv.org/abs/2607.29167v1

## Working conclusion

Remembered information can remain useful without becoming permission. Authority must be platform-owned, non-amplifying through summaries, and checked again against the exact effect at execution time.
