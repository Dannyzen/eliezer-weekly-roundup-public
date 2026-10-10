# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-10 Daily Scan

Today's implementation signal is evidence timing plus deterministic release. A trace must prove what the agent saw before acting, and a probabilistic classifier must not become the final authority for a tool effect.

### Prove the evidence window before interpreting an injected fault

Summary: SSCBench shows that eventual counterevidence does not prove timely counterevidence. Of 44 adopted runs where a correcting observation later appeared, only 17 received it before first use and 27 received it afterward.

Analysis: [daily analysis](2026-10-10/reasoning.md#prove-the-evidence-window-before-interpreting-an-injected-fault)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [SSCBench paper v1](https://arxiv.org/abs/2610.11514v1)
Tools and methodologies worth exploring now: evidence-availability events, exposure timestamps, first-use markers, claim-specific denominators, late-correction metrics
Implementability score: 0.68

### Red-team the option channel, then remove it from authority

Summary: Seven typed decision models show brittle allow-or-block behavior under irrelevant logs and option-label changes. A public MIT artifact makes the attack matrix reproducible, while deterministic rules over typed fields provide the safer dispatch path.

Analysis: [daily analysis](2026-10-10/reasoning.md#red-team-the-option-channel-then-remove-it-from-authority)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.12292v1), [public repository](https://github.com/ArminAzizi98/option-channel-attack)
Tools and methodologies worth exploring now: split fail-open and fail-closed metrics, option-label mutation, irrelevant-context mutation, deterministic-rule baselines, cached-result replay
Implementability score: 0.90

## Current implication

Grade the evidence path, not only the final decision. Then keep the release path deterministic: validated fields, versioned policy, exact verdict, and effect receipt.

Latest roundup: [2026-10-10 daily scan](../roundups/2026-10-10.md).
