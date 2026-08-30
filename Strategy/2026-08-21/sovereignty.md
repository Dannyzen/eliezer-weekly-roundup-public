# Strategy Weekly Sovereignty Analysis - 2026-08-21

## Thesis

Reusable capability and delegated authority must be admitted as stateful, revocable control objects. Static scores and one-time policy checks are evidence, not permission.

## Skill packages need source-disjoint and behavioral admission evidence

### Finding

TRUSS treats a skill package as natural-language procedure plus executable resources. On 84 matched SkillInject pairs, direct LLM checking reached 19.05% recall and 44.64% precision. Static inspection reached 94.05% recall and 81.55% precision. Runtime evidence closed the remaining benchmark gap and reached 100.00% precision, recall, and F1 on those matched pairs.

MaliciousSkillBench tests whether static detection survives new publishers. It consolidates 9,740 normalized-unique skills from 13 frozen public sources. Learned detectors scored 0.882 to 0.932 Macro-F1 on random splits but only 0.653 to 0.665 when sources were held out. Its strongest word TF-IDF SVM preserved 95.6% malicious recall while falsely flagging 62.4% of held-out benign skills.

### Why it matters

A skill expands the runtime's procedural and executable action surface. Source overlap can make a scanner look deployment-ready when it has learned publisher conventions. Static detection also cannot prove the induced behavior of scripts, assets, tool calls, and multi-step instructions.

### Strategy fit

This is the skill-admission control plane: immutable package identity, complete inspection, source-disjoint regression, brokered shadow execution, and a residual-risk record. The admission result is versioned and revocable.

### Practical path now

- Freeze every candidate package by content digest.
- Inspect the complete package, including scripts and assets.
- Use source-disjoint and structural-family holdouts as the default scanner gate.
- Report malicious recall and benign false-positive rate beside aggregate F1.
- Pair a candidate against an empty-skill control in a disposable brokered environment.
- Release only on safe task completion: authorized work succeeds and the attack condition stays suppressed.

The TRUSS method is architecture-ready but no public implementation repository was resolved. MaliciousSkillBench is a populated Apache-2.0 repository with frozen protocols and a released dataset.

Implementability score: 0.84

Core sources:
- [TRUSS, immutable v1](https://arxiv.org/abs/2608.17588v1)
- [MaliciousSkillBench, immutable v1](https://arxiv.org/abs/2608.19901v1)
- [protectskills/MaliciousSkillBench](https://github.com/protectskills/MaliciousSkillBench)
- [MaliciousSkillBench dataset](https://huggingface.co/datasets/ProtectSkills/MaliciousSkillBench)

## Delegation authority must narrow across accumulated session state

### Finding

Bounded Agents introduces an Agentic Principal Chain that evaluates authority against accumulated session state rather than isolated requests. Across 3,154 instances, the reported evaluation blocked all 544 InjecAgent data-stealing cases and reduced AgentDojo exfiltration from a 75% to 100% range to 0% across four domains, with measurable utility cost.

The control principle is attenuation: a child agent receives a narrower envelope than its parent, and prior actions consume or alter the authority available for later actions.

### Why it matters

Static session permissions let individually permitted actions compose into prohibited outcomes. Delegation also becomes authority laundering when a child inherits the parent's broad capability instead of a task-bound subset.

### Strategy fit

This belongs in the execution-control broker and authority-manifest layer. The runtime tracks principal chain, scope, budget, time, allowed tools, allowed data, prior effects, and revocation state.

### Practical path now

- Issue signed or broker-owned delegation envelopes at every hop.
- Intersect child scope with the parent envelope and the exact delegated task.
- Consume budgets and record prior effects in shared session state.
- Deny delegation when the child envelope cannot be made strictly narrower.
- Keep a human and deterministic policy ceiling above model-proposed authority.

Implementability score: 0.76

Core source:
- [Bounded Agents, immutable v1](https://arxiv.org/abs/2608.15888v1)

## Remediation must invalidate dependent gate verdicts

### Finding

One Gate Is Not Enough formalizes remediation-induced control coupling. An authority, resource, or evidence gate can admit, reject, degrade, or remediate an action. If remediation changes the action, evidence, context, or policy state, another gate's earlier verdict may no longer apply.

### Why it matters

Individually correct controls can compose into an unsafe system. A budget gate might downgrade a model, changing the evidence quality an assurance gate approved. An authority gate might narrow a target, invalidating resource estimates. A content filter might rewrite an action after a policy gate inspected the original.

### Strategy fit

This is the dependency layer inside a stateful pre-action control plane. Every verdict identifies the object and revisions it evaluated. Transformations invalidate all dependent verdicts before execution.

### Practical path now

- Give proposed actions, evidence bundles, context, and policy state immutable revision identities.
- Record gate dependencies explicitly.
- After remediation, compute the changed fields and invalidate dependent verdicts.
- Repeat gating until the state reaches a fixed point or a bounded attempt limit.
- Emit the transformation and re-gating chain in the final execution receipt.

The paper supplies a useful protocol but no drop-in public implementation was verified. The first implementation is a small dependency graph around existing gates.

Implementability score: 0.70

Core source:
- [One Gate Is Not Enough, immutable v1](https://arxiv.org/abs/2608.18360v1)

## Working conclusion

Sovereignty lives in the transition from signal to permission. A scanner result, retrieved memory, model-selected privilege profile, or one-time gate verdict may guide the runtime. Authority remains bounded, versioned, dependency-aware, revocable, and brokered.
