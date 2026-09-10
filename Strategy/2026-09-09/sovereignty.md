# Strategy Daily Sovereignty - 2026-09-09

## Freshness and selection

The core paper was submitted on 8 Sep 2026 and first listed on 9 Sep. Its full paper and Figshare package were inspected without downloading or executing the artifact. GitHub's 8 Sep managed-sandbox release was checked as a same-window product signal.

## Authority must be scoped per principal, not per task

CapScope treats tool calls as untrusted requests even when the requested operation is ordinary for the overall task. Before any repository content or tool output is read, a preflight step derives a task-wide authority ceiling from trusted input. Host code validates and freezes that ceiling outside model context, then attenuates typed capabilities per sub-agent. Every tool call is checked at dispatch against the issuing principal's capabilities.

Across five Python repairs, five injection surfaces, four authorization conditions, and three trials per cell, the study reports 300 runs. Injected effects executed in 47/75 ambient-authority runs, 46/75 static-global-policy runs, 33/75 task-specific-global-policy runs, and 3/75 CapScope runs. CapScope completed 68/75 repairs versus 72/75 for the unconstrained baseline. The cost was material: mean wall time rose from 145 seconds to 316 seconds, partly because five CapScope runs hit the 900-second timeout.

Why it matters: a task-wide allowlist must grant the union of what every role needs. That lets a reader or test runner inherit write authority needed only by a patcher. Per-principal attenuation prevents task-required authority from becoming universal authority.

Fit in strategy: execution control, untrusted repository content, and multi-agent delegation.

Practical tools and methodologies worth exploring now:
- derive the maximum authority from trusted user intent before reading repository content;
- store capabilities outside model context as effect type plus argument predicate;
- assign separate principals to scout, reader, runner, patcher, and releaser roles;
- parse compound commands and substitutions before policy evaluation;
- require every delegated grant to be a subset of the delegator's ceiling;
- log proposals, denials, allowed calls, missing-capability failures, and final effects.

The weakest point: the evaluation uses five small Python repairs, one model, and three trials per cell. It does not establish performance on large refactors or long workflows. This is survivable as an architecture pattern because the full 300-run dataset and implementation package are exposed through Figshare. The guardrail is to reproduce a small local fixture set before applying the policy to production coding agents.

Artifact status: the Figshare private-link landing page exposes a 531.36 kB CC BY 4.0 package described as containing the TypeScript capability layer, experiment driver, five-task corpus, decision logs, and table-rederivation script. It was not downloaded or executed. The underlying Pi toolkit has a populated public repository.

Product corroboration: GitHub's 8 Sep Copilot for JetBrains preview lets enterprise administrators centrally control sandbox enablement, filesystem and network access, proxy settings, developer tools, and Keychain access. That is useful task-level policy, but CapScope's distinct contribution is principal-level attenuation inside the delegated workflow.

Implementability score: 0.76

Core sources:
- [Authority Is Not a String, arXiv:2609.08371v1](https://arxiv.org/abs/2609.08371v1)
- [CapScope research artifact](https://figshare.com/s/86184ed20f66d1f0cf91)
- [earendil-works/pi](https://github.com/earendil-works/pi)
- [GitHub enterprise-managed sandbox preview](https://github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains)

## Deep Dive Wednesday: monitor the fleet, not only the call

[MOLE](https://arxiv.org/abs/2609.06966v1) is the week's strongest architectural finding because it covers the residual risk left after per-call authorization. It evaluates 150 persistent AI-operated accounts across nine stateful services and 30 workdays, labels completed harm from downstream service state, and ranks account-days under a fixed human-review budget.

The result that matters is economic as much as technical. Cheap action-rarity and peer/history-novelty features improved a mid-tier semantic monitor by 49% to 64% across held-out corpora. Selective escalation reached 0.629 budget-AUC at lower modeled cost than uniform use of GPT-5.5, whose budget-AUC was 0.571. Expensive semantic inspection should be routed, not sprayed across every trace.

This extends CapScope rather than replacing it. CapScope attenuates what each principal may do before dispatch. MOLE correlates what persistent principals actually did across services and time, verifies resulting harm in state, and directs scarce review capacity to the riskiest accounts.

The durable control-plane model, implementation boundary, and pilot sequence are in [Agent Fleet Monitoring Control Plane](../agent-fleet-monitoring-control-plane/agent-fleet-monitoring-control-plane.md).

Implementability score: 0.74

Core sources:
- [MOLE paper](https://arxiv.org/abs/2609.06966v1)
- [MOLE repository](https://github.com/aashiqmuhamed/mole)
- [MOLE dataset](https://huggingface.co/datasets/forgelab/mole)
- [OpenAI research acceleration disclosure](https://openai.com/index/research-acceleration-view-inside-openai/)

## Working conclusion

A task-level policy is still ambient authority inside a multi-agent task. Mint a trusted ceiling before untrusted reads, attenuate it per principal, and enforce it at the host dispatch boundary.
