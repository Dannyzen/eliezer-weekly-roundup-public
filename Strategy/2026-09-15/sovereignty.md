# Strategy Daily Sovereignty Analysis: 2026-09-15

## Thesis

Tool connectivity is not workflow correctness. A sovereign agent runtime must bind a tool to an exact identity before invocation and require transaction semantics before a successful call can count as a safe effect.

## Freshness and evidence boundary

arXiv first listed the selected papers on Tuesday, September 15, 2026. The transactional-tool paper was submitted September 14 and falls inside the strict recent window. The MCP census was submitted September 12 and is a current listing-window signal after the weekend cutoff. The arXiv API returned HTTP 429; category pages, immutable v1 pages, HTML, and PDF text were used instead. Public GitHub metadata, README text, and tree metadata were inspected read-only. No external repository was cloned, installed, built, imported, or executed.

## Require transactional contracts at every effect boundary

### Finding

When Tool Calls Succeed but Workflows Fail defines eight recurring external-effect anomalies across unresolved outcomes, workflow structure, and interaction with concurrent executions or outside observers. A tool can return success while the workflow still duplicates an effect, commits without a required effect, leaves aborted residue, or depends on provisional state that is later withdrawn.

The paper separates world events from runtime observations and derives the missing boundary capabilities: authoritative outcome resolution, idempotency keys, compensation, staging, dependency identity, commutativity, and visibility control. Its census of 98,291 tools from 4,838 reachable remote MCP servers finds that 74.0 percent emit at least one standard hint and 61.7 percent emit all four, yet the current annotation vocabulary fully expresses none of the required transactional capabilities.

### Why it matters

Retries and compensating actions are unsafe when the runtime cannot tell whether the first effect happened or whether the inverse is valid. The missing layer is not more agent reasoning. It is a typed effect contract that tells the runtime what can be resolved, repeated, staged, reversed, or coordinated.

### Fit in the stack

This belongs in stateful-effect governance and execution control, below orchestration and above provider-specific tools.

### Explore now

- Add effect IDs, idempotency keys, authoritative status lookup, and terminal outcome states to side-effecting adapters.
- Declare compensation preconditions and whether compensation neutralizes or merely adds another effect.
- Stage irreversible effects until workflow invariants pass.
- Record dependency identities and shared-resource coordination requirements.
- Reject speculation or automatic retry when the adapter cannot resolve an ambiguous outcome.

### Caveat

The anomaly model is formal and the MCP census measures declared annotations, not tool behavior. The verified MIT artifact covers the remote annotation census; it does not reproduce the full guarantee model. Strong semantics can exist behind a tool while remaining unusable to a runtime that cannot observe them.

Implementability score: 0.78

Core source: https://arxiv.org/abs/2609.15397v1
Artifact: https://github.com/flame-stream/mcp-annotation-census

## Pin MCP identity, interface, and endpoint across upgrades

### Finding

Same Name, Different Server takes an August 2026 census of 21,643 official-registry servers and 72,606 version records. Among 8,900 multi-version servers, 51.09 percent changed a versioned description, package, or endpoint; 40.58 percent had at least one silent semantic change under stable identifiers. Another 370 servers, 4.16 percent, redirected their endpoint host while keeping the registry identity.

The deeper gap is structural: the registry does not version tool definitions. An installed name cannot prove that the reviewed tool schema or destination is still the one being invoked. The study also reports a precision-corrected high-severity prevalence near 7.6 percent, driven mainly by fail-open exposure and unpinned dependencies, but its own validity section makes clear that pattern matches are risk indicators rather than confirmed exploits.

### Why it matters

A registry name is discovery metadata, not a durable identity. Review at install time expires as soon as the package, tool definitions, or endpoint can move without an explicit client decision.

### Fit in the stack

This belongs in agent-gateway governance and supply-chain admission. The gateway should compare the exact installed manifest against the previously approved manifest before reconnecting or upgrading.

### Explore now

- Pin package digest, source revision, tool-schema hash, transport, and endpoint origin in one admission manifest.
- Diff every field before upgrade and require explicit approval for endpoint-host or authority changes.
- Bind cached credentials and capabilities to the approved origin, not the registry name.
- Treat stars, recency, and license as discovery signals only; require attestations and local policy evidence.
- Keep the last approved manifest available for rollback and incident reconstruction.

### Caveat

The source scan covers 66.3 percent of registry servers, uses pattern-based detection with one human rater, and does not establish exploitability. The reported drift-security relationship is correlational. The paper says an anonymized artifact exists, but its exact URL was not exposed in the extracted primary text, so no artifact link is claimed here.

Implementability score: 0.88

Core source: https://arxiv.org/abs/2609.14119v1
