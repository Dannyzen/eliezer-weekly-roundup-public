# Strategy Daily Sovereignty - 2026-08-24

## Scope note

AID-Guard was first listed by arXiv on Monday, August 24 and submitted on August 21 at 14:31 UTC. It is outside the strict trailing 48-hour submission window at the 12:00 UTC run time, but it belongs to the newest official batch after the weekend gap. The immutable v1 PDF was read as a document. No external source code was cloned or executed.

## Authorization must remain live until the provider effect closes

Most agent authorization systems decide whether a request may begin. AID-Guard argues that this is too early to stop checking. The request can mutate before provider commit, the provider state can change, a successful effect can lose its response, and a retry can create a second effect from one approval.

AID-Guard carries one reservation lineage across admission, commit, ambiguous delivery, reconciliation, and recovery. The provider boundary revalidates the exact approved request and current provider state at commit. An ambiguous result keeps the reservation charged. Release or one successor is allowed only after a terminal result or certified no effect plus a delivery fence that prevents the predecessor from arriving later.

The evaluation is unusually concrete for a protocol paper. All 210 Stripe provider-contract trials matched predeclared outcomes. Across two SaaS providers, 40 terminalize-then-successor schedules, 30 overlapping Stripe confirm/cancel races, and 10 crash-recovery schedules completed without a duplicate effect. Under complete proposer compromise, the prototype blocked all 44 submitted attacks while admitting all 44 matched legitimate proposals. A composition study blocked all 20 tested post-admission lifecycle attacks and preserved all eight matched valid or exact-retry executions.

The cost is real. A strict exact-manifest profile reduced benign utility by 35.4 to 43.8 percentage points. A more flexible typed profile recovered benign completions with no observed unsafe effects across 864 frontier episodes, but that is still evidence within the declared provider contracts and schedules, not a universal guarantee.

Why it matters: human approval should bind to one effect lineage, not one transient request. Idempotency keys alone do not solve predecessor-versus-successor ambiguity, and a receipt alone does not prove that the final provider effect came from the approved delegation.

Practical tools and methodologies worth exploring:
- a durable reservation table with canonical request digest, acting identity, provider operation, and effect lineage;
- commit-time revalidation against current provider state;
- explicit pending, ambiguous, terminal, certified-no-effect, fenced, and successor states;
- provider adapters that expose stable predecessor identity, reconciliation, terminalization, and delivery fences;
- adversarial schedules for response loss, retries, confirm/cancel races, delayed predecessors, and crash recovery;
- public receipts plus privileged replay for protected provider evidence.

Weakest point: the prototype trusts a maintainer-controlled host, SQLite authority store, provider adapters, and declared provider contracts. The inspected paper says a versioned artifact will be released, but no public artifact URL was present in the immutable page or PDF. The guardrail is fail-closed provider-contract admission and adversarial schedule tests before any protected effect is enabled.

Implementability score: 0.62

Core source:
- [AID-Guard](https://arxiv.org/abs/2608.21159v1)
