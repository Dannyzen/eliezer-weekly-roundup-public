# Strategy Daily Sovereignty - 2026-08-27

## Scope note

Metis was first listed by arXiv on Thursday, August 27 and submitted on August 26, inside the strict trailing 48-hour window. ToolMinimize was first listed on Wednesday, August 26 but submitted on August 25 at 03:48 UTC, outside the strict trailing 48-hour submission cutoff at this run. It is included as a listing-window carry-forward because it adds a distinct effect-boundary control and was not covered in the August 26 repository update.

Immutable v1 abstracts and HTML were inspected. No public implementation artifact was available for either paper. No external source code was cloned or executed. NotebookLM remained disabled and untouched.

## Mediate every proposed effect through typed runtime events

Metis separates three objects that agent systems often collapse: the model proposes an action, the harness supplies tools and feedback, and the runtime decides how an admitted action crosses into an external effect. Provider streams are normalized into typed events. Permission decisions, interference classes, terminal results, lifecycle transitions, context repair, and child authority then become explicit runtime objects rather than conventions hidden in prompts.

Across 30 matched real-I/O pairs, four-class mediation reduced median elapsed time from 25.958 ms under forced serialization to 14.146 ms and was faster in all pairs. That is a narrow dispatcher ablation, not a general runtime speed claim. A ten-case fault matrix exposed duplicate-identifier and rollback limits. A child-boundary ablation showed that a gate plus filtered registry blocked the declared unauthorized effect and hid all five escape tools, while removing both protections reversed both outcomes. A ten-case decision oracle matched declared permission outcomes across five invocation routes.

Why it matters: policy text cannot guarantee effect ordering, result closure, or delegated authority. Those guarantees belong in a runtime that can deny before execution, serialize interfering effects, pair every accepted tool-use identifier with a terminal result, and narrow child tool registries.

Practical tools and methodologies worth exploring:
- normalize every provider response into a shared typed event schema before dispatch;
- run permission checks after argument construction and before any external effect;
- classify tool calls by interference risk rather than serializing everything;
- require terminal-result closure for accepted, denied, failed, timed-out, and cancelled calls;
- derive child authority as the intersection of parent grants, role grants, and task grants, minus explicit denials;
- preserve duplicate-ID, partial-write, restart, and rollback failures as regression fixtures.

Weakest point: the author states that the supporting artifact is still being curated, and the evaluation is bound to private frozen evidence. The paper does not establish semantic safety, full rollback, host-loss recovery, process isolation, or superiority over another runtime. The control pattern is implementable, but the reported implementation cannot be inspected yet.

Implementability score: 0.74

Core source:
- [Metis paper](https://arxiv.org/abs/2608.25322v1)

## Rewrite tool arguments to the minimum necessary disclosure

ToolMinimize inserts a data-minimization layer after the model constructs a tool call and before the tool executes. It classifies privacy-sensitive data, scores exposure against tool trust and argument necessity, then applies removal, generalization, substitution, or truncation. This is stricter than an allow/block gate because it can preserve the useful call while reducing what crosses the trust boundary.

The motivating study used 20 everyday requests, five common tool types, and three production models. Default prompts produced unnecessary privacy-sensitive disclosure in 81 to 88 percent of calls. Explicit privacy instructions still left 36 to 76 percent over-sharing. In 307 live tool calls, the middleware reduced privacy cost by 81.2 to 92.0 percent while preserving 100 percent argument-level task validity under the paper's equivalence test. Across 25 unannotated MCP schemas it reduced privacy cost by 79.0 percent. Median middleware latency was 1.77 ms.

Why it matters: helpful models are structurally rewarded to include context. Privacy cannot depend on the same model remembering to self-censor on every call. The effect boundary should release only the fields and precision required for that tool invocation.

Practical tools and methodologies worth exploring:
- annotate JSON Schema fields with necessity, permitted precision, and substitution policy;
- insert an argument rewriter into the MCP or tool-dispatch middleware;
- distinguish removal, generalization, substitution, and truncation as separate auditable operations;
- retain original and rewritten arguments in access-controlled audit evidence, not normal application logs;
- test utility equivalence, classifier misses, implicit sensitive context, and multi-tool aggregation;
- fail closed or require approval when necessity cannot be established for high-sensitivity fields.

Weakest point: no public implementation artifact was linked. The system assumes JSON-shaped arguments and an interception hook, and it does not address prompt injection, malicious providers, training-data privacy, or all interaction effects between combined sensitive fields. The reported task-validity test is argument-level, not proof of downstream business correctness.

Implementability score: 0.82

Core source:
- [ToolMinimize paper](https://arxiv.org/abs/2608.24957v1)
