# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-05

### Memory authority now includes sycophancy and ghost-state control

Summary: MemSyco-Bench and A-TMA extend memory governance beyond poisoning. A memory can be non-malicious and still be unsafe when it overrules objective evidence, escapes its scope, or mixes current and superseded state. Memory authority now needs state, scope, supersession, and downstream-use policy.

Analysis: [daily sovereignty analysis](2026-07-05/sovereignty.md#memory-authority-now-includes-sycophancy-and-ghost-state-control)
Durable topics: [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Shared-State Agents](shared-state-agents/shared-state-agents.md), [AgenticAI Memory Systems](../AgenticAI/memory-systems/memory-systems.md)
Core sources: [MemSyco-Bench paper](https://arxiv.org/abs/2607.01071v2), [MemSyco-Bench repo](https://github.com/XMUDeepLIT/MemSyco-Bench), [A-TMA](https://arxiv.org/abs/2607.01935v1)
Implementable now:
- tag memory records by current, superseded, historical, transition, conflict, and personalization-only state
- downgrade preference memory when objective evidence or current state outranks it
- preserve supersession lineage through summaries and derived memories
- evaluate bank, retrieval, and answer layers separately
Tools, repos, and methodologies worth exploring:
- MemSyco-Bench, ATMA-style state labels, conflict-heavy temporal fixtures, memory gateway policy over scope and state
Implementability score: 0.67

### Router policy should buy reasoning before buying tool surface

Summary: The retrospective-board study shows that extra browser testing can raise cost without improving reliability, while higher reasoning effort can dramatically improve first-try success. More tools are not a substitute for the right reasoning budget.

Analysis: [daily sovereignty analysis](2026-07-05/sovereignty.md#router-policy-should-buy-reasoning-before-buying-tool-surface)
Durable topics: [Model Router Governance](model-router-governance/model-router-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [AgenticAI Coding Agent Control Plane](../AgenticAI/coding-agent-control-plane/coding-agent-control-plane.md)
Core sources: [reasoning effort study](https://arxiv.org/abs/2607.02436v1), [Zenodo artifacts](https://doi.org/10.5281/zenodo.21134406)
Implementable now:
- classify failures before changing model, reasoning effort, tools, verifier, or approval mode
- log cost and reliability deltas for each routing knob
- require justification before expanding browser, shell, network, credential, or repo-wide authority
- separate style prompts from functional verification
Tools, repos, and methodologies worth exploring:
- per-criterion coding-agent rubrics, first-try reliability metrics, effective-token logging, matched routing A/B tests
Implementability score: 0.79

### Skill marketplaces need composition policy, not isolated review

Summary: SkillFuzz makes the skill-catalog control problem explicit: risk can emerge only when skills are co-activated. Marketplace governance therefore needs per-composition verdicts, not only per-skill provenance and static scans.

Analysis: [daily sovereignty analysis](2026-07-05/sovereignty.md#skill-marketplaces-need-composition-policy-not-isolated-review)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Community Governance](agent-community-governance/agent-community-governance.md), [AgenticAI Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core source: [SkillFuzz](https://arxiv.org/abs/2607.02345v1)
Implementable now:
- store individual skill verdicts and composition verdicts separately
- generate high-risk pairs and triples from overlapping tools, files, memory access, and goals
- use planner diffs before expensive detonation runs
- block combinations that expand side effects beyond declared scope
Tools, repos, and methodologies worth exploring:
- contract-guided composition fuzzing, composition deny lists, differential planning oracles, sandbox detonation for high-risk combinations
Implementability score: 0.60

## Supporting recent Strategy context

The 2026-07-01 Deep Dive remains the foundation: connection is not authority. The 2026-07-05 daily scan sharpens the next governance layer: memory state, reasoning effort, and skill composition should become policy-bearing objects before they influence action.
