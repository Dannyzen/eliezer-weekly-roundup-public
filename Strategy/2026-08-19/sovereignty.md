# Strategy Deep Dive, 2026-08-19

## Winner: skill packages need an admission loop

TRUSS is this week's strongest finding because it isolates the pre-mount decision that every other control plane inherits. A skill package can expand the action surface before memory, lowering, or harness scoring ever run. Installing it because the later task succeeded is not certification.

[Read the durable deep dive](../skill-admission-control/skill-admission-control.md#august-19-deep-dive-why-truss-is-the-weeks-control-primitive)

Core source: [TRUSS](https://arxiv.org/abs/2608.17588v1)

Implementability score: 0.72

## Why it won the week

The other finalists improve important adjacent gates:

- HarnessRisk scores configuration, extension, persistence, action, and recovery after a capability is already mounted.
- Authorization Before Context keeps recalled facts inside the audience that produced them.
- SkillEffect lowers generated tool programs onto bounded implementations.
- Self-improvement fragility shows that writeback needs multi-run and shuffled-order evidence.
- DeepSeek Harness makes skills and sandboxes into plugins, which increases the cost of an uncertified mount.

TRUSS sits below those findings. It asks whether the package may become part of the runtime at all.

## Evidence that changes the design

On 84 matched SkillInject pairs, a direct LLM checker reached 19.05% recall and 44.64% precision. Static inspection rose to 94.05% recall and 81.55% precision. Runtime evidence closed the rest and reached 100.00% precision, recall, and F1.

Repair on 155 SkillSafetyBench cases cut attack success from 38.71% to 19.35% with GPT-5.5 and from 46.45% to 29.68% with GPT-5.4, with zero attack regression. Generation on 187 SkillGenBench tasks raised effectiveness from 17.11% with no skills to 52.94%, and raised the benchmark Security rate from 50.80% to 100.00%. An intermediate LLM generator captured only part of that gain and left 46 unsafe outcomes.

The architecture is a Generator, Checker, and Refiner sharing one Function and Safety Record. The candidate is a complete package with a frozen digest. The Controllable Execution Environment mounts that digest read-only, brokers every action, and keeps blocked requests as evidence.

## What to implement now

1. Freeze every candidate skill as a content digest. Revisions get a new digest.
2. Inspect the complete package, including scripts and assets, not only SKILL.md.
3. Keep a fixed property catalog and convert residual criteria into runtime obligations.
4. Run a shadow agent through brokered tools in a disposable workspace.
5. Pair every candidate against an empty-skill control before claiming functional gain.
6. Release only on safe task completion: attack suppressed and authorized task completed.
7. Emit an uncertified residual record when the revision budget is exhausted.

## Adjacent strategy findings from today

### Authorize memory before it enters context

Authorization Before Context isolates the memory-to-context transition as its own authority boundary. A personal agent can learn a fact in one audience and later retrieve it for another. Relevance is not permission.

The proposed rule is model-neutral and anti-monotone. Each memory item carries the audience present when it was recorded. The current viewer set is read from channel metadata and falls back to public when ambiguous. The item is admitted only if every current viewer already belonged to that audience. The paper proves that this one check gives per-participant cross-channel recall and one-way confidentiality. Enforcement is exclusion from assembled context, not redaction or output scoring.

The claim is narrow and useful. In the evaluated configuration, no known forbidden fact entered unauthorized context, and every audited read path failed closed. Action safety, audience widening, and memory quality are explicitly out of scope.

Why it matters: yesterday's authority work asked what a delegated action may do. Today's work asks what a later prompt may even see. If unauthorized memory reaches the model, later filters are already late.

Practical paths:
- stamp `recorded_audience` at write time from channel participants;
- resolve the current viewer set from channel metadata, with public as the fail-closed fallback;
- admit a memory only when every current viewer is a subset of the recorded audience;
- apply the same check to search, direct reads, summaries, and derived notes;
- keep an exact-context receipt of admitted IDs, excluded IDs, and audience labels.

Caveat: this is a single-author workshop preprint. The evaluation is a synthetic suite plus an internal live-verification process. No public implementation repository was resolved from the primary pages.

Implementability score: 0.78

Core source:
- https://arxiv.org/abs/2608.17148v1

### Self-improvement needs order and variance controls

On the Fragility of Self-Improving Agents re-evaluates Agent Workflow Memory and ReasoningBank on WebArena, VisualWebArena, and SCUBA. The authors upgraded the model and harness, then added the two controls most papers skip: repeated runs and shuffled task order.

The reliability picture is worse than the original success claims. Self-improving methods increased run-to-run variance in 71% of cases, with best-to-worst gaps up to 10 percentage points. On the WebArena GitLab subset of 180 tasks, the no-memory baseline already had a 4.4% best-worst gap; ReasoningBank widened it to 7.8%. Under the default easy-to-hard order, ReasoningBank gained 1.5% on average. Under shuffled orders, it lost 4.5%. Adding rubrics and environment feedback closed only 31% of that shuffled-order degradation.

The mechanism is underspecification. Agents write plausible memories that do not apply, such as recommending APIs in a browser-only environment. Those memories then distract later tasks.

Why it matters: a self-improvement loop is a deployment pipeline. If the eval uses one run and a hidden curriculum, the loop can look like learning while amplifying noise and locking in wrong lessons.

Practical paths:
- require at least three identical runs before promoting a memory or workflow update;
- shuffle task order instead of using the benchmark's default curriculum;
- inject environment constraints into memory construction, not only into the acting prompt;
- inspect written memories for inapplicable advice before they become durable;
- keep a human correction path for wrong lessons instead of trusting automatic writeback.

Artifact status: the Apache-2.0 repository is public and populated, with separate WebArena and SCUBA trees. The Hugging Face dataset of trajectories is public. Both were inspected read-only only.

Implementability score: 0.84

Core sources:
- https://arxiv.org/abs/2608.18066v1
- https://github.com/SalesforceAIResearch/self-improve-fragility
- https://huggingface.co/datasets/Salesforce/self-improve-fragility

## Evidence boundary

TRUSS is a 14-page preprint with no resolved public implementation repository. The 100.00% detection result is on matched SkillInject pairs. Residual attack success after repair remains material. Treat the architecture as a strong admission pattern, not a drop-in product.

## Working conclusion

Context assembly and self-improvement remain authority operations. The deeper Wednesday claim is that skill loading is also an authority operation. Admit memory by audience. Promote learned artifacts after multi-run evidence. Certify skill packages before they expand the runtime.

## Sources

- [TRUSS abstract, immutable v1](https://arxiv.org/abs/2608.17588v1)
- [TRUSS PDF, immutable v1](https://arxiv.org/pdf/2608.17588v1)
- [Skill-Inject](https://arxiv.org/abs/2602.20156v1)
- [SkillSafetyBench](https://arxiv.org/abs/2605.12015v1)
- [SkillGenBench](https://arxiv.org/abs/2605.18693v1)
- [Authorization Before Context](https://arxiv.org/abs/2608.17148v1)
- [On the Fragility of Self-Improving Agents](https://arxiv.org/abs/2608.18066v1)
- [HarnessRisk](https://arxiv.org/abs/2608.17597v1)
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)
