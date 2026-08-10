# Strategy Daily Sovereignty, 2026-08-10

The Monday arXiv batch is live. Both selected papers were submitted on Friday, 2026-08-07 and first listed on Monday, 2026-08-10. Exact-title and arXiv-ID checks found no prior coverage in this repository.

## Persistent-risk evaluation must trace the full carrier lifecycle

HarnessSafe models delayed agent attacks as a lifecycle rather than a single malicious prompt. Its 328 executable cases span seven carrier families: memory, skills, Tool/MCP, memory-to-skill transformation, subagent delegation, session summaries, and shared artifacts. A seven-stage trace scheme records the furthest progression supported by observable evidence, from no contact with the poisoned surface through oracle-verified violation.

The benchmark matters because a benign request can trigger attacker-influenced state that entered during an earlier task or session. A binary attack-success rate cannot distinguish rejection at ingestion, persistence without activation, attempted use blocked at the tool boundary, or a completed external effect. The paper also shows that containment depends on the harness-model configuration rather than either component alone.

Why it matters: memory, skill, tool output, summary, delegation context, and shared files are all authority-bearing carriers once a later run can consume them. A safety claim needs to show where influence entered, where it persisted, which boundary it crossed, what triggered it, and what observable effect occurred.

Strategic fit: persistent-state control, untrusted-data boundaries, harness governance, cross-session provenance, and release evaluation.

Implement now:
- assign stable identities to carrier objects and every transformation between them;
- record source principal, trust class, persistence event, boundary crossing, later trigger, proposed action, policy verdict, and effect receipt;
- grade the furthest verified lifecycle stage instead of reporting only attack success;
- require case-specific effect oracles rather than model intent or suspicious text;
- test memory, skills, tools, summaries, delegation, and shared artifacts under the same lifecycle schema;
- report results by exact harness, model backend, policy, tool set, and version.

Evidence caveat: the paper documents complete definitions and canonical result inventories for 328 cases, but native execution evidence is exhaustive only for part of the evaluated configurations. The artifact scope omits a unified case-level ledger for every harness and the complete five-arm matched-control pairing. No exact external artifact URL was exposed on the primary page in this scan.

Implementability score: 0.72

Core source: https://arxiv.org/abs/2608.06984v1

## Agent memory needs explicit validity and revocation states

TEPA treats stale memory as a lifecycle-state failure. Observations become keyed precedents. When fresh evidence conflicts under the same key, the prior precedent moves out of the active retrieval set into a revoked archive. History remains available for audit and possible re-promotion, but it no longer competes with current evidence by default.

The controlled reversal results are unusually clear. Across 50 seeds, append-only and last-write-wins memory both scored 0.210, below the no-memory baseline at 0.309, while TEPA scored 0.950. Under real file-backed execution, append-only scored 0.203, no memory 0.298, and TEPA 0.950. On clean single-hop MemoryAgentBench SH-6k, TEPA matched a strong last-write-wins cache. The paper also reports its limit: multi-hop and very-long-context settings still expose retrieval-chain and context-selection failures beyond fact validity.

Why it matters: append-only provenance is not enough if stale evidence remains active. Overwriting is also insufficient when auditability, rollback, and later re-promotion matter. Memory needs a visible state machine that separates active, superseded, revoked, quarantined, and re-promoted evidence.

Strategic fit: memory authority, evidence provenance, temporal policy, auditability, and conflict-aware retrieval.

Implement now:
- assign stable keys to facts, preferences, procedures, and environment claims;
- store validity state, source, observation time, supersession edge, reason, and reviewer or policy identity;
- remove revoked items from normal retrieval without deleting their history;
- retrieve current evidence by default and expose revoked evidence only for audit or explicit comparison;
- replay hidden-regime reversals, file-backed changes, and preference updates before promotion;
- measure stale-active rate, conflict-resolution latency, re-promotion accuracy, and multi-hop failure separately.

Evidence caveat: TEPA's strongest result is for single-key stale-conflict consolidation. The paper does not solve compositional retrieval, long-context selection, or multi-hop reasoning, and no public implementation repository was verified.

Implementability score: 0.88

Core source: https://arxiv.org/abs/2608.07429v1

## Working conclusion

Persistent state needs two explicit controls: lifecycle traces for how influence crosses carriers, and validity states for whether remembered evidence may remain active. Persistence without either control is hidden authority.
