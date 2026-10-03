# Daily Agent Research: 2026-10-03

Scope: the latest verified primary-source signals available Saturday morning. arXiv had no Saturday announcement batch; the newest category pages were Friday, October 2. The two selected papers are Friday carry-forwards with v1 submission dates of September 30 and October 1.

## Review the composed object

Deny Without Disabling identifies a multi-agent authorization failure that message-by-message review cannot see. Separately admissible fragments can compose into a governed object whose downstream use is prohibited. The review unit must therefore be the resolved object plus its permission and proposed action.

The controlled comparison is concrete: local review permitted 413 of 480 denied commits. Review of the combined artifacts permitted 0 of 480, while both arms supplied 459 of 480 required authorized objects. In the final configuration, object binding plus deterministic enforcement produced roughly 99 percent selective correctness and 0 of 2,304 verbatim disclosures at the registered action boundary.

Why it matters: multi-agent safety cannot be reduced to per-message filters or per-agent permissions. The runtime needs object resolution across contributions, trusted permission ranking, deterministic commit enforcement, and a paired utility metric that checks whether authorized work still completes.

Stack fit: multi-agent orchestration, context-to-execution integrity, and trajectory-aware evaluation.

Practical methods worth exploring now:
- resolve one canonical governed-object identity across all contributing artifacts;
- evaluate deny and allow outcomes in the same unit;
- keep permission review isolated from untrusted contributors;
- assemble validated artifacts in runtime code;
- enforce the final commit independently of the composing model.

Artifact status: the public Apache-2.0 FlowReview repository has a populated main branch, README, source, evaluation data, and 55 tree entries. It was inspected read-only and was not cloned or executed. It has no GitHub release.

Caveat: the strongest results come from controlled banks. The AgentDojo transfer covers Sonnet 4.5 under a relay selected during development, and the zero-disclosure claim applies to the registered verbatim boundary.

Implementability score: 0.78

Core sources: [paper](https://arxiv.org/abs/2610.00371v1), [HTML](https://arxiv.org/html/2610.00371v1), [FlowReview repository](https://github.com/yunbeizhang/FlowReview)

## Use held-out baselines for safety routing

False Floors shows that a safety router can be graded against an in-sample best-single-model baseline chosen with the test labels. Under random splits that selection cost was only 0.003 to 0.030 harm. Under held-out request categories it rose to 0.045 to 0.113, comparable to the router deficit being measured. On AgentDojo, holding out whole suites increased the selection cost sevenfold to ninefold.

Why it matters: the comparator is part of the benchmark contract. If the baseline sees the evaluation distribution while the router does not, the test can make routing look weaker than an honestly selected fixed model.

The practical correction is cheap: select the fixed comparator on training or validation data, score it on the same held-out folds as the router, and report both the honest and in-sample conventions. The paper's 200 random HELM assignments put the mean held-out-category cost at 0.037 with an interval of 0.026 to 0.045, versus 0.0026 under random splits.

Stack fit: model-router governance and trajectory-aware evaluation.

Practical methods worth exploring now:
- nest baseline selection inside every cross-validation fold;
- hold out categories or suites that represent deployment shift;
- report router benefit against an honest fixed-model baseline;
- measure judge sensitivity and model-pool saturation;
- branch trajectories if mid-run switching is the claimed production behavior.

Caveat: the four primary corpora are English and largely single-turn on the chat side. The large shift effect appeared only on HELM harm_bench among seven safety corpora, and most harm labels come from automated judges. No public implementation artifact resolved.

Implementability score: 0.72

Core sources: [paper](https://arxiv.org/abs/2610.01535v1), [HTML](https://arxiv.org/html/2610.01535v1)

## Trigger code review through the API

GitHub now exposes generally available REST and GraphQL requests for Copilot code review, with a review-effort choice per request. Balanced is the inherited default unless Lite was selected explicitly.

Why it matters: a coding-agent control plane can invoke review from its own state machine after a pull request is opened or updated. The review becomes a programmable gate rather than a UI-only convention.

Stack fit: coding-agent control planes and ticket-native orchestration.

Practical methods worth exploring now:
- request review only after repository-native checks pass;
- choose review effort from change risk, affected authority, and diff size;
- record request identity, effort level, review completion, and disposition;
- require a separate deterministic gate for security, tests, and merge authority.

Caveat: Copilot review is advisory and plan-gated. The Balanced default can change cost and latency, and higher-level settings may override repository choices.

Implementability score: 0.94

Core source: [GitHub changelog](https://github.blog/changelog/2026-10-02-copilot-code-review-api-support-and-new-default-effort-level/)

## Make long turns restart-safe

Cloudflare's Agents SDK added PiHarness, which binds Pi Durable to a Durable Object lifecycle. The SDK says in-progress work persists through restarts, crashes, network issues, and mid-turn interruption. Tools and prompt sections are supplied through extensions.

Why it matters: the harness can own continuity instead of forcing the application to replay an entire turn after process loss. This is the operational boundary needed for long research, coding, and tool workflows.

Stack fit: sessionful agent loops and agent serving runtime.

Practical methods worth exploring now:
- persist run identity, current step, tool receipt, and resume cursor;
- classify tools by replay safety before automatic recovery;
- test interruption before, during, and after every side effect;
- expose cancellation and terminal-state receipts separately from liveness.

Caveat: the release provides code and documentation but no reliability measurements. It ties the lifecycle to Cloudflare Durable Objects and Earendil's Pi packages, and more lifecycle capabilities are still forthcoming. External source code was not executed.

Implementability score: 0.86

Core source: [Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-10-02-pi-harness/)

## Action cut

1. Add composed-object test fixtures to one multi-agent workflow.
2. Re-score one router against a comparator selected inside held-out folds.
3. Trigger an API review after repository-native gates, with effort selected from risk.
4. Add interruption fixtures and replay-safety labels before adopting durable long turns.

Highest implementability score: 0.94 for API-triggered Copilot code review.

Lowest implementability score: 0.72 for honest safety-routing baselines under distribution shift.

No external repository was cloned, installed, built, imported, or executed.
