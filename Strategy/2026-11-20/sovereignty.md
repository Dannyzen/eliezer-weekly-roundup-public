# Strategy Weekly Sovereignty: 2026-11-20

## Scope

This synthesis covers primary sources captured from 14 through 20 November 2026. It compresses the week's governance findings into two control-plane patterns. Public artifacts were inspected read-only. No external source was cloned or executed.

## 1. Put a deterministic effect boundary between intent and execution

The strongest weekly signal is that model-written intent cannot authorize its own effects.

[CapLite](https://arxiv.org/abs/2611.17115v1) avoids asking the acting model to write the security artifact that will constrain it. [System 1 Agents](https://arxiv.org/abs/2611.21053v1) compiles bounded tool calls instead of generating free-form action text. [Runtime Verification of Multiple Natural Language Criteria](https://arxiv.org/abs/2611.23074v1) moves many policy criteria into a runtime verifier. [Tether](https://arxiv.org/abs/2611.25599v1) evaluates stateful policy over sandbox-observed effects before host mutation.

The pattern is a release boundary. The agent can propose. Trusted code derives a typed action, computes or observes the effect set, checks current state and policy, then commits or refuses. The boundary must persist labels and prior decisions outside model context.

Why it matters: command text, intent summaries, and model-authored policies are evidence about a proposed action. They are weaker than the action's reachable effects. Scripts, subprocesses, retries, and multi-step staging widen that gap.

Fits into the stack: execution control, tool gateways, sandboxing, policy verification, and agent skills.

Implementable now:
- separate planning from execution credentials;
- compile bounded action schemas from validated inputs;
- run risky actions in disposable sandboxes before commit;
- normalize observed effects into a small typed algebra;
- apply deny-overrides policy with persistent labels;
- emit refusal or commit receipts tied to the exact action manifest;
- use [SystemOneAgents](https://github.com/eltzanis/SystemOneAgents) and [VFM](https://github.com/spitis/vfm) as read-only research references.

Artifact status: both repositories resolve with populated default branches. VFM describes code and checkpoints as an early public release with no stable release tags. Tether's public implementation was not verified.

Evidence limit: natural-language verifiers still inherit model error. Syscall-level policy misses semantic harm that produces no modeled system violation. Conservative effect inference can create false positives.

Implementability score: 0.76

Core sources: [CapLite v1](https://arxiv.org/abs/2611.17115v1), [System 1 Agents v1](https://arxiv.org/abs/2611.21053v1), [Runtime Verification v1](https://arxiv.org/abs/2611.23074v1), [Tether v1](https://arxiv.org/abs/2611.25599v1)

## 2. Check authority closure at the last trusted boundary

[Intent Contracts](https://arxiv.org/abs/2611.24025v1) gives the runtime a logged statement of goal, user words, and scope, while withholding tools from the planner. [Signed, Valid, and Unauthorized](https://arxiv.org/abs/2611.24989v1) shows why valid fields and signatures remain insufficient: the signing boundary must check every effect the delegated object can enable. The same week, GitHub's customization-source controls and framework middleware releases reinforced the operational split between provenance, policy, and runtime authority.

The strategic rule is simple: provenance explains where an instruction or object came from. Authority closure decides whether every reachable effect stays within the current mandate. Keep those decisions separate.

Why it matters: a signed object can be authentic and still exceed the user's mandate through retries, periods, downstream contracts, or alternate execution sequences. An intent contract can be a useful audit record while remaining an unsafe authorization primitive if trusted models can widen it.

Fits into the stack: authority manifests, tool gateways, delegated commerce, OAuth-like grants, middleware, and approvals.

Implementable now:
- bind grants to principal, resource, action, amount, time, retry, and sequence constraints;
- compute or conservatively approximate reachable effects before signing;
- compare the effect envelope with the human mandate at the last trusted boundary;
- keep provenance records immutable and separate from authorization decisions;
- revoke or expire capabilities independently of the conversation;
- log exact refusal reasons without exposing hidden policy internals.

Artifact status: [intent-contracts](https://github.com/zwang-devv/intent-contracts) resolves as a research artifact. The authority-closure paper links upstream protocols, but no public implementation of its Closure checker was verified.

Evidence limit: effect closure is bounded by the modeled object families, contracts, and adversary programs. Unknown downstream behavior requires refusal or a coarser grant.

Implementability score: 0.68

Core sources: [Intent Contracts v1](https://arxiv.org/abs/2611.24025v1), [Signed, Valid, and Unauthorized v1](https://arxiv.org/abs/2611.24989v1)

## Strategic conclusion

Evidence is allowed to be messy. Authority needs a deterministic boundary. The control plane should turn model proposals into typed, scoped, effect-checked releases and keep the power to commit outside the model.
