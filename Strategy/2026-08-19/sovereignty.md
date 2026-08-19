# Strategy Daily Sovereignty Analysis - 2026-08-19

## Scope

The strategy findings come from immutable arXiv v1 submissions inside the 2026-08-17 12:00 UTC to 2026-08-19 12:00 UTC window and first listed on 2026-08-19. Abstracts and PDFs were inspected as primary sources. Implementation artifacts were checked read-only only. No external repository was cloned or executed.

## Authorize memory before it enters context

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

## Self-improvement needs order and variance controls

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

## Working conclusion

Context assembly and self-improvement are authority operations. Admit memory by audience, not relevance. Promote learned artifacts only after multi-run and shuffled-order evidence.
