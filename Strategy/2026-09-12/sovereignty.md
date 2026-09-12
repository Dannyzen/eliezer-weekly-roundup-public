# Strategy Daily Sovereignty Analysis: 2026-09-12

## Freshness and selection

There is no new Saturday arXiv listing. Both selected papers were first listed on Friday, September 11, 2026, after v1 submissions on September 10. They are listing-window carry-forwards rather than strict trailing-48-hour submissions at the September 12 12:00 UTC scan time.

## Treat tool registries as untrusted populations

### Finding

A seeded probability sample from a 24,135-server MCP registry found that only 48.8 percent of 400 sampled npm/stdio servers completed initialization. The dominant exclusion was servers that never started at all, 37.5 percent, not missing credentials, 13.3 percent. Among the 195 servers that did run, the hard JSON Schema result was strong: zero fatal violations across 2,766 advertised tools. The weak layer was optional safety metadata, omitted by 58.8 percent of tools in the random draw.

The same study found that benchmark corpora can misrepresent the deployed population. Raw BFCL and UltraTool rows contained 68.8 and 85.6 percent exact name-plus-description repeats, compared with 0.4 percent for real MCP tools. Curation can therefore make startup reliability, safety metadata, and tool diversity look better or simply different than registry reality.

### Why it matters

A registry entry is discovery evidence, not admission evidence. Schema-valid tools on a server that cannot initialize are unusable, and a benchmark full of repeated or curated tools can train the wrong gateway policy.

### Strategy fit

This belongs in agent gateway governance and capability discovery. Admission should separate publisher identity, package resolution, process startup, protocol handshake, schema conformance, safety metadata, and safe-round-trip behavior.

### Practical path now

- Probe every candidate server before catalog admission.
- Keep startup failure, credential failure, handshake failure, schema failure, and missing safety annotations as separate states.
- Deduplicate benchmark tools globally before reporting diversity or accuracy.
- Weight evaluation samples toward the live registry population, not only curated working servers.
- Quarantine failed servers instead of repairing them silently inside the measurement pipeline.

Implementability score: 0.91

Artifact status: `mcp-probe` is public, MIT licensed, and populated with the probe, benchmark scripts, seeded registry census, raw records, summaries, and a Zenodo software archive. It was inspected read-only and not executed.

Submission: 2026-09-10 01:33:53 UTC. First listed: 2026-09-11.

Core sources:
- [MCP registry probability sample](https://arxiv.org/abs/2609.10962v1)
- [mcp-probe repository](https://github.com/itguruhaseeb/mcp-probe)
- [mcp-probe Zenodo archive](https://doi.org/10.5281/zenodo.21347997)

## Preserve control constraints through context management

### Finding

The Missing Boundary independently varies goal pressure, control degradation, and executable unsafe opportunity across five models and 16 operational domains. Across 1,800 unique trajectories, degraded control or unsafe opportunity alone caused little loss of control. Together they produced a 55 percent loss-of-control rate in the full-factorial study and 62 percent across ten additional domains. Restoring the original control boundary reduced the rate to zero even when the unsafe action remained executable.

The context-management ablation is the operational result: compaction that preserved control constraints produced zero loss of control, while omitting them produced 87 percent. The task goal remained intact, so a fluent summary could look correct while deleting the rule that made execution safe.

### Why it matters

Long-horizon agents do not need malicious instructions to cross a boundary. A legitimate goal plus a forgotten constraint plus an executable unsafe path is enough. This makes summary, memory, handoff, and restart logic part of the authorization system.

### Strategy fit

This belongs in context-to-execution integrity and runtime governance. Control constraints need a protected representation that survives compaction and is revalidated at effect time.

### Practical path now

- Separate goals, facts, and binding constraints in the context schema.
- Carry protected constraints outside free-form summaries.
- Reinject and verify them after compaction, handoff, restart, and memory retrieval.
- Bind final tool admission to the active constraint set.
- Add fixtures where the unsafe action remains available after context compression.

Implementability score: 0.87

Artifact status: the paper promises code at the public Apache-2.0 AI-Infra-Guard repository, but the inspected default-branch tree did not expose a paper-specific boundary or constraint artifact. Treat the experiment as paper-verified, not reproduced.

Submission: 2026-09-10 03:02:27 UTC. First listed: 2026-09-11.

Core sources:
- [The Missing Boundary](https://arxiv.org/abs/2609.11024v1)
- [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)

## Working conclusion

The gateway must distrust catalogs before admission, and the runtime must protect constraints after admission. Discovery metadata and fluent context are both evidence, not authority.
