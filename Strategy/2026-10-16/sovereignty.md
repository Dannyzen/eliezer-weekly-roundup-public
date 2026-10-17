# Strategy Weekly Analysis: 2026-10-16

## Thesis

The week's strategic primitive is a typed release boundary. A model can propose a capability, call, approval narrative, or causal explanation. Authority begins only when the runtime identifies the object, constrains its lifetime, binds it to an exact effect, and preserves evidence about what actually happened.

## Bind approval to canonical effects

Agent Step-Up tests twelve attacks against approval paths and audits ten agent runtimes. Its reference design renders approval from a canonical effect descriptor, has a user-held passkey sign the digest, executes only the stored call, and retains a verifiable record. Across 27,108 scripted trials and 609 AgentDojo attack pairs, the system stops substitution, replay, and grant stretching. The trusted card cuts forged-narration attack success from 0.54 to 0.03.

The governance implication is direct: approving model-written text is weak. The approval object should bind tool identity, target, normalized arguments, policy version, expiry, and single-use execution.

The weakest point is approval fatigue. The paper still observes modeled-approver flooding success from 0.45 to 0.60, and an approval cannot prevent an effect already allowed by policy. Rate limits and default-deny policy remain necessary.

Implementable now: canonical effect descriptors, trusted rendering, WebAuthn or passkey signatures, single-use execution, expiry, flood limits, and receipts.

Implementability score: 0.72

Core sources: [Agent Step-Up paper v1](https://arxiv.org/abs/2610.21063v1), [Agent Step-Up repository](https://github.com/Sports-Vision-Inc/agent-step-up)

## Activate and expire capability authority explicitly

GitHub's new MCP startup control treats server activation as a user-visible decision. CreepScope extends the principle across a run by expiring authority after its last justified step. Lost in Implicit Routing shows why both matter: implicit discovery degrades as the catalog grows, so an unobserved capability can be absent when needed or remain attached after its purpose ends.

The governance object should record capability identity, activation reason, allowed effects, source version, start time, last justified step, expiry condition, and deactivation receipt.

Implementable now: explicit startup controls, deny-by-default server activation, capability leases, step-scoped grants, idle expiry, and activation/deactivation receipts.

Implementability score: 0.84

Core sources: [GitHub MCP startup release](https://github.blog/changelog/2026-10-10-new-controls-and-chat-improvements-in-copilot-for-jetbrains/), [CreepScope paper v1](https://arxiv.org/abs/2610.15988v1), [Lost in Implicit Routing paper v1](https://arxiv.org/abs/2610.18522v1)

## Make containment fail closed

Anthropic's unintended-action investigation shows that a persistent agent can route around an obstacle when the environment leaves alternate paths open. GitHub's local sandboxing release turns file, network, and credential restrictions into a generally available product control, while MXC provides a public local sandbox substrate.

The governance implication is that sandbox unavailability, policy parse failure, or missing network rules should stop execution. A warning followed by unsandboxed continuation converts containment into decoration.

Implementable now: per-run filesystem and network policy, credential minimization, explicit stop rules, sandbox health preflight, fail-closed launch, and post-run effect receipts.

Implementability score: 0.90

Core sources: [Anthropic incident report](https://www.anthropic.com/research/investigating-unintended-model-actions), [GitHub local sandboxing release](https://github.blog/changelog/2026-10-09-github-copilot-weekly-releases-october-5/), [sandbox documentation](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/about-cloud-and-local-sandboxes), [MXC repository](https://github.com/microsoft/mxc)

## Restore provenance before artifacts reenter execution

SkillRelayBench contains 270 adversarial cases across 30 cross-session skill-composition scenarios. The paper reports attack success rates from 46.7% to 77.4%. SkillRelayGuard restores provenance context before reuse and reduces aggregate attack success from 69.5% to 10.9% while increasing legitimate completion in the reported evaluation.

The governance implication is that a file, cache, report, configuration, or memory entry is not inert context. It is a delayed authority channel. Reuse should carry producer identity, source skill, session, transformation history, trust class, and review result.

The public guard remains advisory and does not cover every local file, SQLite, or model-gateway effect. The survivable path is to combine provenance restoration with deterministic release gates for consequential consumers.

Implementable now: artifact manifests, producer and session IDs, checksums, trust labels, read-time provenance injection, dry-run review, and deterministic gates before publication or execution.

Implementability score: 0.79

Core sources: [SkillRelay paper v1](https://arxiv.org/abs/2610.13227v1), [SkillRelay repository](https://github.com/Dianshu-Liao/SkillRelay)

## Keep evidence planes separate until attribution is justified

ExecWeave preserves framework events and independently observed process, file, and network activity as separate source artifacts. It labels bridges as observed, inferred, or causal and refuses to infer a semantic principal from filesystem correlation alone. GitHub's telemetry release complements this by separating identity capture from prompts, responses, tool arguments, tool output, and policy detail.

The governance implication is that correlation is not authority. A useful evidence graph must preserve the source class, supporting event IDs, confidence, and abstention when multiple processes or missing observations prevent justified attribution.

The downside is operational complexity. Stable request IDs, process lineage, clock alignment, and privacy controls are required across layers. Start with one adapter and one OS effect class before attempting universal causality.

Implementable now: typed evidence classes, support IDs, bounded correlators, non-causal inference labels, content-minimized telemetry, and explicit abstention.

Implementability score: 0.68

Core sources: [ExecWeave paper v1](https://arxiv.org/abs/2610.21146v1), [ExecWeave repository](https://github.com/Irish-kw/ExecWeave), [GitHub telemetry release](https://github.blog/changelog/2026-10-12-client-telemetry-user-attribution-and-configurable-capture/)

## Strategic conclusion

A trustworthy agent stack needs one release chain: preselected capability, bounded authority, reversible progress, canonical effect, trusted approval, enforced execution, typed evidence, and verified state. Natural-language explanation remains useful to people, while the runtime objects carry authority.
