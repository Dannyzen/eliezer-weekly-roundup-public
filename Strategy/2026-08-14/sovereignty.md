# Strategy Weekly Sovereignty Analysis, 2026-08-14

## Thesis

Evidence is not authority. The strategic stack should let models propose and reason while runtime-owned mechanisms control promotion, admission, execution, recovery, and release. If the same adaptive component owns both the action and the proof that clears it, the control plane is theater.

## Proposal, authority, and verification must have separate owners

### Finding

QuoteBench shows that a downstream parser can damage a fixed model reply by 55.4 to 73.2 percentage points. CAPRI shows that a candidate can pass Isabelle while changing protected text. The IaC regression study shows that cumulative-best security can improve while the current repair regresses properties that already passed.

These are one governance problem at different layers. The generated intent, decoded action, executed effect, final outcome, edit grant, and preservation obligations are distinct objects.

### Why it matters

A green build or business result proves one predicate. It does not prove that the exact effect was authorized, that transport preserved intent, or that prior guarantees survived. The release boundary needs independent ownership.

### Fit into the strategy stack

Primary layers: context-to-execution integrity, execution control, runtime governance, and evidence provenance.

### Practical tools and methods

- Represent the requested effect as a typed action manifest.
- Bind approval to the decoded action and exact target identity.
- Run outcome validators separately from authority and preservation checkers.
- Convert previously passing properties into preservation obligations.
- Require explicit waivers for intentional regression.
- Retain original state, candidate state, diff, contract, transforms, verdicts, and final-state receipt.

Implementability score: 0.86

Core sources:
- https://arxiv.org/abs/2608.13547v1
- https://arxiv.org/abs/2608.13459v1
- https://arxiv.org/abs/2608.13404v1

## Retained state needs an authority lifecycle

### Finding

Trajectory poisoning, temporal memory, provenance-aware shared memory, and malicious skill files all show that retained state can change later policy. The important transition is not write versus read. It is evidence versus instruction.

Three poisoned records in a 30-record promotion batch embed attacker behavior in hundreds of later trials. TEPA’s explicit temporal and provenance model handles reversal far better than append-only baselines. MAP-Graph prevents unauthorized retrieval with permission filtering, yet still demonstrates that relevance and action authorization must remain separate.

### Why it matters

A summary can inherit a source’s restrictions. A memory can become stale or revoked. A skill can package executable authority. A derived claim can hide the origin that should limit its use. Treating these as plain text loses the policy state.

### Fit into the strategy stack

Primary layers: memory authority, agent self-improvement governance, shared state, and untrusted-data boundaries.

### Practical tools and methods

- Assign stable IDs and ancestry to evidence, memories, summaries, and skills.
- Store active, superseded, revoked, quarantined, and re-promoted states.
- Propagate restrictions through summaries, transfers, and derived artifacts.
- Filter by principal permission before relevance ranking.
- Require source diversity and adversarial replay before promotion.
- Keep promotion authority separate from the agent that generated the candidate.

Implementability score: 0.68

Weakest point: several strong designs remain paper-only, synthetic, or unreplicated. This is implementable as policy and data modeling, but the operational burden is real.

Core sources:
- https://arxiv.org/abs/2608.05563v1
- https://arxiv.org/abs/2608.07429v1
- https://arxiv.org/abs/2608.10509v1
- https://arxiv.org/abs/2608.05223v1

## The evaluation substrate is a governance plane

### Finding

AgentChaos, SpecPath, HarnessSafe, and Beyond Final Scores all vary a condition that normal leaderboards hold implicit: runtime faults, specification history, persistent carrier stage, or process stability. Their shared lesson is that endpoint scoring cannot reveal how authority and evidence moved through the run.

### Why it matters

An organization cannot govern what it cannot attribute. If the harness does not retain candidate identity, history variant, fault location, carrier lineage, recovery decision, and final state, later audit reduces to a score and a story.

### Fit into the strategy stack

Primary layers: evaluation containment, evidence provenance, runtime observability, and release governance.

### Practical tools and methods

- Freeze candidate identity and budgets before evaluation.
- Keep hidden tests and alternate histories outside the optimizer’s control.
- Inject faults only through test-owned adapters.
- Trace carriers across memory, skills, tools, summaries, delegation, and shared artifacts.
- Record attempted action, realized effect, earliest consequential error, and recovery.
- Report reliability and peak capability separately.

Implementability score: 0.78

Core sources:
- https://arxiv.org/abs/2608.06790v1
- https://arxiv.org/abs/2608.09799v1
- https://arxiv.org/abs/2608.06984v1
- https://arxiv.org/abs/2608.13417v1

## Denial and recovery belong inside the authority model

### Finding

POLIS’s immutable-provenance guard admits 0 of 96 laundering violations, compared with 22 of 96 for a local-state guard. More importantly, 44 of 51 blocked episodes later complete safely. Denial can be both strict and recoverable when the reason and safe next action are explicit.

This week’s stable SDK releases move the same idea into implementation. OpenAI Agents Python 0.20.0 adds durable staged input and explicit sandbox credential-exposure acknowledgement. Agno 2.9.0 persists paused human-in-the-loop runs and closes an MCP approval bypass. Microsoft Agent Framework Python 1.14.0 adds durable approval stores, checkpoints, enforcement middleware, and approval recovery fixes.

### Why it matters

A block with no recovery path encourages bypasses, retries, and shadow state. A permissive fallback silently widens authority. Typed denial plus bounded recovery preserves both safety and progress.

### Fit into the strategy stack

Primary layers: execution control, multi-agent governance, approval state, and event-sourced recovery.

### Practical tools and methods

- Model denial as a typed state with reason, scope, and permitted alternatives.
- Bind approvals to exact invocation identity and tool signature.
- Persist pending input, approval state, and checkpoint identity across restart.
- Fail loudly when recovery state is stale or cannot be rehydrated.
- Record whether a denied attempt later completed through an authorized path.

Implementability score: 0.80

Core sources:
- https://arxiv.org/abs/2608.09828v1
- https://github.com/openai/openai-agents-python/releases/tag/v0.20.0
- https://github.com/agno-agi/agno/releases/tag/v2.9.0
- https://github.com/microsoft/agent-framework/releases/tag/python-1.14.0

## Portable packages increase the need for client-specific admission

### Finding

Agent Plugins 1.0 standardizes capability packages across several GitHub clients. That is useful infrastructure, but it also lowers the cost of distributing skills and MCP configuration. The malicious-skill and ToolHazard results show why package identity cannot equal trust.

Tool architecture itself changes behavior. Interface design changes repeat-run consistency and token cost, while stateful hostile environments reveal failures that static manifest inspection cannot. Admission therefore needs both static package evidence and executable behavior evidence.

### Why it matters

A package approved in one client, tenant, or policy profile may be unsafe in another. Authority belongs to the deployment context, not to the package author or marketplace listing.

### Fit into the strategy stack

Primary layers: agent gateway governance, community governance, skills-as-control, and sandboxing.

### Practical tools and methods

- Verify package identity, manifest, digest, namespace, license, and component tree.
- Grant skills, tools, and MCP servers separately for each client.
- Bind approval receipts to package and interface-schema versions.
- Exercise packages in stateful hostile-world fixtures before promotion.
- Keep read-only pilots separate from write-capable admission.
- Revoke by component and version, not only by package name.

Implementability score: 0.84

Core sources:
- https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/
- https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md
- https://arxiv.org/abs/2608.05223v1
- https://arxiv.org/abs/2608.11878v1

## The weakest point

This architecture adds objects, state machines, and trusted validators. That cost is real. It is survivable because the full machinery is not needed everywhere at once.

Start at irreversible boundaries: external writes, permission changes, memory promotion, package admission, and release. Use deterministic checks there first. Expand only when traces show repeated ambiguity or failure upstream.

## Current implication

The durable strategic asset is not a smarter planner. It is a runtime that makes evidence, authority, execution, recovery, and receipts independently inspectable.
