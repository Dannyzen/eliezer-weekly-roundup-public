# Persistent-State Agent Control

Last updated: 2026-10-21

Primary layer: Strategy / runtime governance

Implementability score: 0.78

Core sources:
- [After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents](https://arxiv.org/abs/2610.28425v1)
- [CarryoverBench repository](https://github.com/igloomatics/CarryoverBench)
- [Distributed Attacks in Persistent-State AI Control](https://arxiv.org/abs/2607.02514v1)
- [Persistent-state evaluation repository](https://github.com/josh-hills/control-arena-persistent-state-eval)

## Overview

Persistent-state agent control is the governance problem created when an agent can write information that later re-enters execution. Memory files, scheduled jobs, workspace configuration, caches, issue state, generated instructions, and code changes are not passive storage. They are delayed execution channels.

CarryoverBench makes this concrete. A one-time indirect prompt injection can persuade an agent to write a malicious instruction into long-term memory or a heartbeat file. The attacker then disappears. The stored instruction resurfaces in a later clean session or during a scheduled wake-up, often after the user has left.

The durable rule is:

> If state can influence a future action, writing that state is an authority event and reading it back is a new authorization decision.

## Why this won the week

This finding beat the week's other strong candidates because it changes the unit of control for deployed agents and tests that claim against Hermes itself.

- TraceLite showed how to reduce long traces without discarding phase-relevant evidence. That is valuable efficiency work.
- AgenTest showed that workflow rules need trajectory-level tests. That is valuable quality work.
- Proof-Carrying Contracts offered a stronger formal end state for enforceable commitments. Its current value is architectural because the paper does not provide a ready runtime artifact.
- CarryoverBench exposed an active production-shaped failure across memory and scheduling, shipped a populated benchmark, separated the failure into measurable stages, and reproduced the latent channel on Hermes.

The finding matters more because persistence is already a core feature of personal agents. It turns a useful product surface into a delayed authority surface, then gives us a testable path to harden it.

## Core innovation

CarryoverBench separates a carryover attack into two stages:

1. **Plant:** untrusted content persuades the agent to write a payload into persistent state.
2. **Trigger:** a later session or scheduled wake-up reads that state and performs the harmful action.

It evaluates three timing channels:

- **Instant:** the familiar same-session prompt injection baseline.
- **Autonomous:** a heartbeat file wakes the agent without a user present.
- **Latent:** long-term memory resurfaces during a later topically aligned request.

The benchmark contains 12 personal-assistant task families and 101 attack tasks: 35 Instant, 30 Autonomous, and 36 Latent. Rule-based verifiers grade both benign task utility and attack effects, avoiding an LLM judge that could itself be influenced by adversarial trace content.

This decomposition is the important advance. An overall attack-success number cannot tell a runtime team whether to harden ingestion, persistent writes, retrieval, scheduling, tools, or egress. Plant and trigger rates can.

## Evidence that changes the architecture

### Persistence did not fade

Across five evaluated models, planted payloads showed no monotonic decay over five follow-up trigger rounds. Autonomous attacks were especially persistent: conditional on planting, the reported trigger probability was approximately one across all five models. Latent triggering varied more, but the stored payload remained intact and could fire repeatedly when the follow-up was topically aligned.

The failure is structural. Conversation history resets between sessions, while the malicious entry in the workspace remains unchanged and is presented as the agent's own state.

### The trigger gate was usually open

Four of five models had conditional latent trigger rates of at least 66 percent once a payload was planted, and conditional Autonomous trigger rates above 80 percent. The practical implication is harsh: most tested defenses had one useful chance, at admission time, before the write became trusted-looking state.

### Text-only defenses acted mostly at planting

The paper tested three defenses: generic persistent-state safety principles, an instruction to inspect and edit suspicious state, and harness-added markup labeling persistent state as untrusted. They reduced planting in some model and channel combinations, but usually did little to the conditional trigger rate. Agents made zero voluntary amendments or deletions under the explicit review defense.

A warning placed beside the poisoned instruction still competes inside the same text channel. Strong trigger control needs a discriminator outside that channel.

### Hermes attenuated the attack and did not contain it

The authors replayed all 36 Latent variants on Hermes for four non-reasoning model configurations. Reported attack success changed as follows:

- Qwen3-235B-A22B: 52.8 percent on Nanobot to 27.8 percent on Hermes.
- Claude Sonnet 4.6: 22.2 percent to 5.6 percent.
- GLM-5: 11.1 percent to 8.3 percent.
- GPT-5.4: 8.3 percent to 2.8 percent.

Every model remained vulnerable. The paper reports that Hermes's memory scanner matched 0 of 89 payload files and that its review pipeline did not invoke removal or replacement. The authors attribute much of the reduction to model-side alignment exposed by Hermes's richer tool catalog, rather than proof that runtime controls closed the channel.

That is the load-bearing result for Danny's stack: Hermes has useful friction, while memory admission and resurfacing still need explicit runtime gates.

## Why it matters

Persistent agents create authority at a different time from execution. A session can appear successful, leave no immediate harmful effect, and still create a future action path. Traditional prompt-injection tests, per-turn approvals, and final-state checks miss that gap.

This affects:

- personal assistants that store preferences, summaries, or reminders;
- cron and background agents that wake without a user;
- coding agents that retain workspace instructions or hooks;
- multi-agent systems that share files or memory;
- support and operations agents that revisit prior customer state;
- any product that treats an agent-authored note as trusted context later.

The product risk is silent authority laundering. Untrusted web or tool content enters as data, is rewritten by the agent, and later returns as an apparent first-party instruction.

## Fit in the agentic stack

Persistent-state control spans six boundaries:

1. **Ingestion boundary:** classify webpages, emails, documents, tool results, and peer-agent messages as untrusted evidence.
2. **Admission boundary:** decide whether derived content may enter memory, schedules, skills, configuration, or workspace instructions.
3. **Storage boundary:** retain origin, principal, scope, trust class, expiry, and revocation state beside the stored object.
4. **Resurfacing boundary:** present stored content as evidence with provenance, not as fresh system authority.
5. **Execution boundary:** require current authorization for tools, filesystem changes, network calls, money movement, and external messages.
6. **Audit boundary:** preserve plant, persistence, resurfacing, proposed effect, decision, and receipt as one replayable chain.

This belongs primarily in Strategy because the central question is who may create future authority. AgenticAI supplies the implementation machinery: typed memory objects, schedulers, policy engines, sandboxed tools, egress gates, trace storage, and deterministic evaluators.

## Practical controls worth trying now

### 1. Make persistent writes typed

Replace free-form instruction append with an object containing:

- content and content hash;
- source origin and producing tool;
- initiating principal and session;
- intended purpose and scope;
- trust class;
- created, reviewed, expires, and revoked timestamps;
- allowed resurfacing contexts;
- allowed effect classes;
- evidence links and prior versions.

A stored object without this envelope remains quarantined evidence.

### 2. Separate memory from instructions

Keep descriptive facts, user-approved preferences, executable procedures, schedules, and authority grants in different stores or namespaces. Retrieval may combine evidence for reasoning, but only an explicit release step can turn evidence into an instruction or scheduled effect.

### 3. Reauthorize wake-ups

A cron entry should name its owner, purpose, allowed tools, data scope, expiry, and approval policy. At fire time, the runtime should re-evaluate those fields against current policy. A schedule created from untrusted content should never inherit the creator agent's ambient authority.

### 4. Gate resurfacing and effects separately

A memory object may be safe to display and unsafe to execute. Preserve two decisions:

- may this state enter the current context?
- may the proposed effect use authority derived from it?

Bind the second decision to the exact tool, arguments, destination, and current principal.

### 5. Put hard controls outside the model

Use tool allowlists, canonical filesystem roots, outbound destination policies, sandboxing, and signed single-use approvals. Model warnings and provenance markup remain useful, but they are advisory controls.

### 6. Test plant and trigger as separate fixtures

Adapt a small subset of CarryoverBench into isolated Hermes regression tests:

- one memory plant that must remain quarantined;
- one approved preference that must survive cleanly;
- one scheduled instruction from untrusted content that must fail admission;
- one approved schedule that must reauthorize at fire time;
- one delayed egress attempt that must be blocked after a clean session;
- one revocation test proving stale state cannot regain authority.

Run the trigger phase in a fresh session and score real tool receipts, not the agent's explanation.

## Repositories and methodologies to explore

- [CarryoverBench](https://github.com/igloomatics/CarryoverBench): task fixtures, payloads, rule-based verifiers, Dockerfile, and transcripts for stage-conditioned evaluation. Inspect and adapt only in an isolated test profile.
- [ControlArena](https://github.com/UKGovernmentBEIS/control-arena): control-evaluation methodology for useful agents operating under adversarial objectives.
- [Persistent-state evaluation artifact](https://github.com/josh-hills/control-arena-persistent-state-eval): cross-change attack and monitor patterns.
- [AgenticRV](https://github.com/AngeloFerrando/agentic-rv): event-contract and monitor architecture for runtime verification.
- [Proof-Carrying Contracts](https://arxiv.org/abs/2610.28484v1): a formal design reference for making exact commitments enforceable at an Airlock before operations run.

The cheapest useful experiment is CarryoverBench-shaped regression testing around Hermes memory admission and delayed egress. Formal proof-carrying commitments are the longer path.

## Implementation complexity

Implementability score: **0.78**

A thin control layer is implementable now with ordinary engineering effort: provenance envelopes, separate state classes, admission quarantine, schedule metadata, effect allowlists, fresh-session regression tests, and audit receipts.

A complete solution requires meaningful architecture:

- a typed persistent-state API rather than unconstrained file writes;
- scheduler integration that evaluates current policy at fire time;
- policy decisions bound to exact effects;
- safe migration of existing free-form memories and cron entries;
- explanations that users can understand without exposing sensitive monitor logic;
- low false-positive rates for legitimate adaptation.

The honest cost is reduced convenience. Some memories and schedules will require review, expiry, or narrower tool access. That friction is appropriate because those objects can act after the initiating session is gone.

## What remains conceptual or unresolved

- Detecting malicious meaning in arbitrary memory remains an open classification problem.
- Safe promotion rules for agent-learned procedures need independent evidence and replay.
- Cross-runtime scheduler semantics differ, so Autonomous benchmarks need runtime-specific adapters.
- Multi-agent shared state introduces principal and delegation conflicts beyond this benchmark.
- Recovering already-poisoned state without discarding valid user history remains difficult.
- Runtime policy must distinguish read permission, contextual influence, and effect authority.

## Weakest point and guardrail

The benchmark is new and synthetic. Its 12 task families were authored in-house, Latent rounds repeat the same topically aligned follow-up and therefore upper-bound realistic trigger rates, and its finite alias verifier can miss successful attacks. The Hermes transfer covers 36 Latent variants, excludes the Autonomous channel, and omits Gemini's reasoning configuration. The public repository is populated but currently has no declared license; the paper promises a permissive research license upon acceptance.

These limits are survivable because the result identifies a mechanism rather than claiming a universal deployment rate. Use the benchmark as a regression design, not as a production risk percentage. Keep all testing isolated, preserve benign-task utility, and treat every reported attack-success rate as comparative evidence.

## Strategic implications for Danny's product thinking

Persistent state should be sold and designed as governed continuity, not unlimited memory.

For FriendVM and Hermes-style personal agents, the differentiator is not remembering more. It is proving where remembered state came from, who authorized its continued influence, when that authority expires, and which effects it may cause later.

That supports four product principles:

1. **Evidence can persist without authority persisting.** Store history broadly, release influence narrowly.
2. **Schedules are delegated capabilities.** Every background job needs an owner, scope, expiry, and current-policy check.
3. **Receipts should span time.** Show the chain from source to stored state to resurfacing to effect.
4. **Safety should preserve usefulness.** Measure benign task completion beside blocked attacks, and keep controls reversible where possible.

This turns memory governance from a security afterthought into a visible product promise: the agent can continue work without silently carrying an attacker's authority forward.

## Related research lineage

- [Self-State Attacks on Self-Hosted AI Agents](https://arxiv.org/abs/2607.17986v1): legitimate writes to memory, identity, configuration, and instructions can evade OS-level intent controls.
- [HarnessSafe](https://arxiv.org/abs/2608.06984v1): delayed influence needs lineage across memory, skills, tools, summaries, delegation, and artifacts.
- [SkillRelay](https://arxiv.org/abs/2610.13227v1): files, caches, configurations, and records can relay influence into later skills and sessions.
- [Scoped Verification for Reliable Long-Horizon Agentic Context Evolution](https://arxiv.org/abs/2607.09175v1): learned persistent guidance needs graph-validated promotion and rollback.

## Working conclusion

Persistent memory and scheduled work are delayed execution surfaces. The control plane should admit, label, resurface, authorize, and audit them as policy-bearing objects. CarryoverBench supplies the best current regression shape, while Hermes supplies the immediate place to prove the control.
