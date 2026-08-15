# Strategy Daily Sovereignty - 2026-08-15

## Thesis

Action boundaries are where evidence becomes authority. The system fails when confidence, duplicated agents, successful experience, or plausible tool output is allowed to cross that boundary without an independent release contract.

## The action boundary is the unit of governance

SteerBench-Work shows that commit-time gates need two operating targets. Across 30 model conditions, wrong holds reached 28.1% while wrong acts reached 1.0%. A gate optimized only to prevent unsafe action can make authorized work impossible.

The strategic requirement is a typed release decision over one exact action manifest. The gate must report false allows, false holds, and recovery after denial. It must not inherit authority from the proposer.

Implementability score: 0.90

Core sources:
- https://arxiv.org/abs/2608.12654v1
- https://github.com/AgentDock/steerbench-work

## Redundancy without dependence evidence is false assurance

Agent Behavioral Contracts II finds 90.0% co-failure among missions where either same-model agent failed in a preregistered 18,000-mission handoff. Different models reduced the association; vendor diversity after model diversity did not.

The strategic implication is blunt: agent count is not a resilience metric. Every multi-agent reliability claim needs matched joint-failure evidence and a certificate that does not assume independence.

Implementability score: 0.78

Core sources:
- https://arxiv.org/abs/2608.12895v1
- https://github.com/qualixar/agentassert-abc

## Persistent adaptation is a release process

Practice Makes Unsafe shows how a bad success becomes durable authority. All 21 evolved configurations authored unsafe artifacts, but only 15 produced later harm. That gap matters: terminal behavior alone misses dangerous state that has not yet been retrieved.

Governance must cover the whole lifecycle: author, inspect, replay, promote, retrieve, execute, retire. Write admission and reuse admission are separate decisions. Every reusable artifact needs identity, lineage, policy state, revocation, and downstream-use receipts.

Implementability score: 0.72

Core sources:
- https://arxiv.org/abs/2608.12851v1
- https://github.com/henrymao2004/misevolve

## Perception needs source-scoped authority

PIPES reduces state-corruption attack success from 84.7% to 2.3% on its Gemma 4 evaluation by screening response units against semantic priors and provenance. The important abstraction is not the specific screening model. It is that a tool-response component cannot make claims beyond its source and field authority.

Governance starts before planning. Raw content, extracted claims, trusted provenance, and admitted state must remain separate objects. An action gate cannot repair a plan built on corrupted perception unless the observation boundary preserved enough evidence to detect it.

Implementability score: 0.64

Core source:
- https://arxiv.org/abs/2608.12789v1

## The weakest point

These controls add more gates, metadata, and failure states. PIPES has no verified public artifact, MisEvolve is early and unlicensed, SteerBench uses described rather than live actions, and the behavioral-contract result comes from a controlled two-agent motif.

That weakness is survivable because the first pilot is small: one high-impact action class, one mirrored proceed-or-hold fixture set, one persistent-skill promotion gate, and one provenance-bearing tool schema. Expand only after local traces show where the boundary actually fails.

## Current implication

Do not ask whether the agent is confident. Ask what exact object is crossing into authority, which independent contract admits it, and what receipt proves the realized effect.
