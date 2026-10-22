# Strategy Deep Dive Wednesday - 2026-10-21

This deep dive covers sources published or first listed from 2026-10-15 through 2026-10-21. Primary papers and official release sources were checked directly. External repositories were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Winner: treat persistent state as delayed execution authority

CarryoverBench is the week's strongest finding because it identifies an active control-plane failure in memory and scheduling, measures the failure by lifecycle stage, ships a populated evaluation artifact, and reproduces the Latent channel on Hermes.

The benchmark contains 12 personal-assistant scenarios and 101 attack tasks across same-turn, scheduled, and memory-resurfaced channels. Across five models, planted payloads showed no monotonic decay over five trigger rounds. Conditional on a successful plant, the later trigger gate was frequently open. The attacker could leave, the initiating session could close cleanly, and the agent could still perform the stored instruction later.

The Hermes transfer is the decisive evidence for this repo. On 36 Latent variants, Hermes reduced attack success relative to Nanobot, but every tested model remained vulnerable. Reported Hermes attack success ranged from 2.8 percent to 27.8 percent. The paper also reports that Hermes's content scanner matched 0 of 89 payload files and that its review pipeline did not remove or replace the planted entries.

Deep dive: [Persistent-State Agent Control](../persistent-state-agent-control/persistent-state-agent-control.md)

Core sources:
- [After the Attacker Leaves paper v1](https://arxiv.org/abs/2610.28425v1)
- [CarryoverBench repository](https://github.com/igloomatics/CarryoverBench)

## Why it beat the alternatives

TraceLite offered immediate context-cost savings, AgenTest offered strong trajectory-level business-rule testing, and Proof-Carrying Contracts offered an important formal direction. CarryoverBench won because it combines architectural importance, direct relevance to Hermes, a populated artifact, and a bounded first implementation.

The finding changes the system boundary. Memory and cron cannot be treated as convenience features with prompt-level warnings. A persistent write is a future authority request. Resurfacing is a fresh authorization decision. Tool execution and egress need independent gates outside the model's text channel.

## Core control stack

Implementable now:

1. Label every persistent write with origin, principal, purpose, scope, trust class, expiry, and revocation state.
2. Separate descriptive memory, approved preferences, executable procedures, schedules, and authority grants.
3. Quarantine instructions derived from webpages, documents, email, tool results, and peer agents.
4. Reauthorize scheduled wake-ups and memory-derived effects against current policy.
5. Bind approvals to exact tools, arguments, destinations, and principals.
6. Test planting and triggering in separate sessions with deterministic effect receipts.

## Implementation complexity

Implementability score: **0.78**

A thin version uses provenance envelopes, admission quarantine, typed schedules, effect allowlists, and isolated regression fixtures. A full version needs a typed persistent-state API, scheduler integration, migration for existing free-form state, and user-facing explanations. The cost is deliberate friction around some memories and schedules.

## Evidence limits

The benchmark uses synthetic task families and sandboxed tools. Latent rounds repeat a topically aligned follow-up, so their trigger rates are an upper bound for real mixed-session traffic. The rule-based verifier may miss rewritten attack targets. The Hermes comparison covers only the Latent channel, excludes one reasoning-model configuration, and may reflect model behavior exposed by the runtime rather than effective runtime defenses. The public repository is populated but currently unlicensed.

Use the benchmark as a regression design, not a production incident-rate estimate.

## Secondary finding: policy can fail across executions

[Local Allow, Global Deny](https://arxiv.org/abs/2610.27620v1) shows that individually permitted actions can combine into a forbidden purpose, consent, provenance, or delegation outcome. It reinforces the winner: authorization must include workflow history, not only the current call. The advertised repository exists but has no populated default branch, so this remains a formal design reference with an implementability score of 0.56.

## Strategic implication

Danny's useful product claim is governed continuity: an agent can remember and act later while preserving source lineage, current authority, bounded effects, and replayable receipts. Memory capacity is easy to copy. Controlled carryover is the differentiator.
