# Strategy Daily Sovereignty: 2026-10-19

## Discovery must not expand authority

Arcade's Tool Recommendation design places discovery inside the gateway. The recommender sees only the eligible catalog after gateway allowlists and access policy are applied. `UseTool` then executes under the calling user's authorization, checks service consent and tool scope again, and keeps provider credentials outside the agent context.

This is the strategic boundary: capability discovery is allowed to reduce context and broaden task coverage, while it is never allowed to broaden authority. Ranking must happen after policy filtering, and execution must repeat the authorization check because recommendation is not a grant.

Practical control pattern:
- compile the eligible catalog from principal, tenant, agent, service, and tool policy;
- rank only inside that catalog;
- return authorization links rather than credentials when consent is missing;
- bind each execution receipt to principal, tool version, input, policy decision, and resulting effect;
- test stale consent, policy changes between recommendation and use, and recommendation cache leakage.

Evidence caveat: this is a vendor-authored production report with no public implementation artifact identified.

Implementability score: 0.82

Core source: [Tool Recommendation for Multi-Step Agents v1](https://arxiv.org/abs/2610.23707v1)

## Relevant memory does not authorize interruption

ProPerAgent shows that proactive assistance fails on two independent axes: finding the right evidence and acting in the right time window. The useful governance lesson is broader than the benchmark. Retrieval produces candidate evidence. It does not grant an assistant the right to interrupt, notify, or mutate state.

Treat interruption as a scoped runtime effect:
- require a current observable trigger and source-linked memory evidence;
- evaluate silence outside the approved window;
- impose cooldown, deduplication, and user-configured attention budgets;
- separate notification authority from write or transaction authority;
- retain receipts for suppressed, issued, repeated, and user-rejected interventions.

Artifact caveat: the evaluation set and code are promised upon publication and are not public yet. The reported result uses controlled synthetic personal histories paired with Ego4D clips, so deployment privacy and preference learning remain open.

Implementability score: 0.45

Core source: [ProPerAgent v1](https://arxiv.org/abs/2610.22671v1)

## Working conclusion

Agent sovereignty depends on keeping selection separate from authority. A gateway may recommend a tool, and memory may surface a fact, but only explicit runtime policy may authorize the invocation or interruption that follows.
