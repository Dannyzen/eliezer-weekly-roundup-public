# Strategy Daily Sovereignty, 2026-07-05

Today's strategic pattern is that state is becoming authority. Memory, model routing, and skill catalogs all need policy-bearing evidence objects, not broad trust in whatever context the agent happens to see.

## Memory authority now includes sycophancy and ghost-state control

Source links:
- MemSyco-Bench paper: https://arxiv.org/abs/2607.01071v2
- MemSyco-Bench repository: https://github.com/XMUDeepLIT/MemSyco-Bench
- A-TMA paper: https://arxiv.org/abs/2607.01935v1

The strategic problem in long-term memory is no longer only poisoning. A user-aligned memory can be harmful even when it is not malicious. MemSyco-Bench shows the risk directly: retrieved memories can make an agent over-align with user preference at the cost of factual accuracy, objective evidence, or proper scope.

A-TMA adds the state-governance version. Long-term memory systems need to distinguish what is true now, what used to be true, and what changed. If old, current, and transition facts are mixed into one retrieval packet, the agent can answer from a ghost state even when the memory store contains the necessary evidence.

Strategic implication: memory authority is not only origin authority. It also needs validity state, scope, supersession, and downstream-use policy. A memory should not be allowed to override objective evidence or authorize action merely because it came from the user or was semantically close.

Fit in the stack: memory authority control plane, runtime governance, shared-state agents, evidence provenance, and local-first agents.

Practical implementation path:
- Add state fields to memory records: current, superseded, historical, transition, conflict, and personalization-only.
- Deny or downgrade memory influence when a task asks for objective facts or external evidence outranks preference.
- Preserve supersession lineage through summaries and derived memories.
- Evaluate memory separately at bank, retrieval, and answer layers.
- Treat personalization as scoped preference evidence, not general truth.

Tools, repos, and methodologies worth exploring now:
- MemSyco-Bench as a memory-induced sycophancy regression suite.
- ATMA-style state labels for existing memory stores.
- Conflict-heavy temporal fixtures for user preferences, account settings, code facts, vendor docs, and project conventions.
- Memory gateway policy that checks scope and state before retrieval is injected.

Implementability score: 0.67

The schema and eval changes are deployable now. The hard part is consistency: every summarizer, retriever, handoff file, and direct memory read has to preserve the same state and authority semantics.

## Router policy should buy reasoning before buying tool surface

Source links:
- Reasoning effort study: https://arxiv.org/abs/2607.02436v1
- Zenodo dataset and artifacts: https://doi.org/10.5281/zenodo.21134406

The governance lesson is simple: tool access is not the same as capability. In the retrospective-board study, browser-based testing increased cost by 42 to 68 percent without improving functional score or first-try reliability. Raising reasoning effort from High to xHigh lifted first-try perfect runs from 28 percent to 89 percent and cut corrective prompts about fivefold for 9 to 29 percent more cost.

That matters because agent platforms are tempted to solve reliability by exposing more tools. More tools expand the attack surface, context load, policy surface, credential surface, and audit burden. If the failure is reasoning, adding tools is an expensive and risky distraction.

Strategic implication: a router should treat reasoning effort, model class, tool exposure, verification depth, and user approval as separate policy knobs. The platform should buy the cheapest knob that addresses the observed failure class.

Fit in the stack: model-router governance, runtime governance, coding-agent control planes, and cost governance.

Practical implementation path:
- Classify failures into reasoning, missing evidence, missing verifier, UI polish, deployment boundary, and tool-availability buckets.
- Raise reasoning effort or model class before broadening tool access when planning defects dominate.
- Require an explicit justification before adding browser, shell, network, credential, or repo-wide authority.
- Log cost deltas and reliability deltas per knob change.
- Keep design prompts and functional verification separate.

Tools, repos, and methodologies worth exploring now:
- The Zenodo artifact set for per-run and per-criterion benchmark replication.
- Effective-token and corrective-prompt logging.
- Router policies that record requested and effective reasoning modes.
- Matched A/B harness runs over tool exposure versus reasoning effort.

Implementability score: 0.79

This is mostly operations discipline. The production challenge is provider heterogeneity: reasoning controls, hidden effort modes, and pricing do not mean the same thing everywhere.

## Skill marketplaces need composition policy, not isolated review

Source link:
- SkillFuzz: https://arxiv.org/abs/2607.02345v1

SkillFuzz makes the marketplace governance problem explicit. Skill review in isolation is too weak because the risky behavior can emerge only when benign skills are co-activated. In agent platforms, the loaded skill set is the real policy object.

The paper's formulation is useful: treat skill compositions as the unit under test, extract structured contracts, use search to prioritize risky combinations, and use a differential oracle against a skill-free baseline before execution. That gives marketplace operators a path between impossible exhaustive testing and naive per-skill linting.

Strategic implication: a skill marketplace should behave more like a package registry plus policy engine than a prompt library. Admission should include provenance, static scan, behavior detonation, and composition-risk records.

Fit in the stack: agent gateway governance, skills-as-control, runtime governance, and agent community governance.

Practical implementation path:
- Store individual skill verdicts and composition verdicts separately.
- Require side-effect contracts for each skill.
- Generate high-risk skill pairs and triples from overlapping tools, files, memory access, and intent conflicts.
- Run plan-diff fuzzing before runtime detonation.
- Block or review combinations that redirect objectives or expand side effects beyond declared scope.

Tools, repos, and methodologies worth exploring now:
- SkillFuzz's contract-guided composition-fuzzing method.
- Composition deny lists in a skill registry.
- Monte Carlo Tree Search over high-risk skill co-activation graphs.
- Differential planning oracles plus sandbox detonation for top-risk combinations.

Implementability score: 0.60

A small catalog can implement this now. A public marketplace needs much stronger scaling, contract quality, and adversarial coverage.

## Working conclusion

The strategic thesis is state before authority. A memory, routing choice, or loaded skill set should gain influence only when its state, scope, cost, and failure evidence are explicit enough to govern.
