# Strategy Daily Sovereignty: 2026-10-16

## Scope

This scan covers security and observability papers submitted on October 15 and first listed by arXiv on October 16, 2026. Public repositories were inspected read-only through GitHub metadata, trees, README files, and releases. No external source was cloned or executed.

## Thesis

Approval and observability fail when they rely on narratives. Approval must bind to the exact effect that will execute. Observability must preserve which evidence was asserted by the agent, observed by the operating system, or inferred by correlation.

## Approve a canonical effect, then execute the stored call

Agent Step-Up tests whether an approval is truly separate from the compromised agent and whether it names the exact effect. The reference gateway builds a canonical effect descriptor, renders the approval card from that descriptor, has a passkey sign its digest, and executes only the stored call.

The study audited ten agent runtimes. It found no third-party verifiable approval record and reproduced post-approval argument changes in four of eight runtimes where binding was measurable. Across 27,108 scripted trials and 609 AgentDojo attack pairs, the reference design stopped substitution, replay, and grant stretching. Trusted rendering reduced forged-narration attack success from 0.54 to 0.03 and raised automated-approver catch rate from 0.30 to 0.98, with a 16 percent refusal rate on harmless near misses.

### Why it matters

A click on an agent-written summary does not authorize a concrete side effect. The approval record needs the exact tool, target, arguments, effect class, freshness token, and single-use execution identity.

### Strategy fit

This is a concrete release gate for payments, deletion, outbound messages, credentials, and other high-consequence actions. It strengthens context-to-execution integrity and execution control.

### Practical tools and methods worth exploring

- Canonicalize the complete effect descriptor outside the model.
- Render the approval surface from the stored call, not from agent prose.
- Bind a passkey or equivalent signature to the effect digest.
- Execute the stored call once and reject any resubmitted or changed arguments.
- Cap pending approvals, rate-limit denials, and preserve verifiable receipts.
- Use RFC 8785 canonical JSON, WebAuthn, and Tamarin-style proofs where the risk justifies them.

### Evidence and artifact status

The public repository has a populated main branch with 454 tree entries, code, data, and proof material. GitHub reports no declared license and no release, so reuse needs a licensing review. The study has no human data, uses one scripted technique per scenario, and notes that a best-response attacker could find attacks absent from the workloads.

Implementability score: 0.72

Core sources:
- [paper v1](https://arxiv.org/abs/2610.21063v1)
- [Agent Step-Up repository](https://github.com/Sports-Vision-Inc/agent-step-up)

## Keep semantic and OS evidence separate until attribution is justified

ExecWeave combines provider or framework events with independently observed process, file, and network events in a typed execution graph. It labels evidence by source and distinguishes observed identity, inferred association, and causal status. Its command-to-process correlator emits a bridge only when one compatible observed process remains, and still marks the bridge as inferred and non-causal.

### Why it matters

Application traces describe intended operations. Operating-system telemetry describes machine activity. Treating one as proof of the other can assign an effect to the wrong agent or tool.

### Strategy fit

ExecWeave belongs in evidence provenance, incident reconstruction, and local-first observability. It is a complement to OpenTelemetry, not a replacement for it.

### Practical tools and methods worth exploring

- Preserve provider, gateway, and OS observations as separate evidence classes.
- Store supporting event IDs and confidence for every derived relation.
- Abstain when multiple processes fit or required observations are missing.
- Propagate stable request and process identities when the runtime supports them.
- Keep content capture disabled by default and retain only fields required for audit.
- Test false uniqueness, missing events, short-lived processes, and remote-tool blind spots.

### Evidence and artifact status

The public repository has a populated main branch with 863 tree entries and five releases. The paper evaluates ExecWeave v0.8.25. GitHub classifies the license as `Other`, so reuse needs a license check. The measurements are Linux-only, the end-to-end integration uses one AutoGen and Ollama case, and human debugging benefit is not measured.

Implementability score: 0.70

Core sources:
- [paper v1](https://arxiv.org/abs/2610.21146v1)
- [ExecWeave repository](https://github.com/Irish-kw/ExecWeave)

## Strategic decision

Treat approval as a signed release of an exact effect and observability as a typed evidence graph. A narrative can help a person understand the action, but it cannot define the action or prove who caused the effect.
