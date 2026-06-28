# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-28

### Skill specifications need runtime reference monitors

Summary: Skill docs are not enforcement. VIGIL compiles behavioral specifications into policies over typed agent-tool event traces, so the runtime can catch temporal obligations, argument constraints, and cross-call value-flow violations before effects land.

Analysis: [daily sovereignty analysis](2026-06-28/sovereignty.md#skill-specifications-need-runtime-reference-monitors)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core source: [VIGIL](https://arxiv.org/abs/2606.26524v1)
Implementable now:
- select one high-risk skill and define finite-trace obligations for it
- log skill invocation, arguments, outputs, statuses, artifact IDs, and consuming calls
- block or escalate when event order, prerequisite, or artifact-binding rules are violated
- return denial feedback so the agent can replan through an allowed path
Tools, repos, and methodologies worth exploring:
- finite-trace policy templates, state-machine or SMT-style validators, skill manifests, event traces, multi-step skill violation fixtures
Implementability score: 0.64

### Prompt-injection defenses need adaptive out-of-band evaluation

Summary: Out-of-band prompt-injection defenses are the right direction, but static benchmarks are not enough. Capability systems, taint labels, and reference monitors need defense-aware adaptive attack suites that rerun after policy, tool, model, or prompt changes.

Analysis: [daily sovereignty analysis](2026-06-28/sovereignty.md#prompt-injection-defenses-need-adaptive-out-of-band-evaluation)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core source: [Adaptive Evaluation of Out-of-Band Defenses](https://arxiv.org/abs/2606.26479v1)
Implementable now:
- add defense-aware attack variants to prompt-injection regression suites
- separate model refusal, policy denial, tool denial, task success, and false positive metrics
- use least-privilege capability handles instead of broad tool access
- rerun adaptive tests after gateway policy, model, prompt, or tool changes
Tools, repos, and methodologies worth exploring:
- AgentDojo-style tasks, reference monitors, Biba/information-flow framing, capability handles, paired static/adaptive security evals
Implementability score: 0.69

## Supporting recent Strategy context

The 2026-06-26 weekly synthesis remains the broad current governance map: [weekly sovereignty analysis](2026-06-26/sovereignty.md). The 2026-06-27 daily scan focused on router headroom and catalog source control. The new 2026-06-28 scan raises the bar for enforcement: skills need live monitors, and prompt-injection defenses need adaptive evaluation.
