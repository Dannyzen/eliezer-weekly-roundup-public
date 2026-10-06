# Strategy Daily Analysis: 2026-10-06

The strategy signal is concrete: shared agent infrastructure needs hard tenant gates, and fleet security controls need visible adoption state. Soft retrieval scope and invisible enablement both create governance gaps.

## Enforce memory ownership after retrieval

MemLeak studies shared vector stores in multi-tenant personal-agent deployments. Ordinary semantic retrieval produced 70 to 100 percent incidental cross-user leakage under pooled same-team retrieval. Crafted memories reached 90 to 100 percent top-k placement. End-to-end contamination reached 5.00 out of 5 on one production-style retrieval path and 4.67 out of 5 with Claude Sonnet 4.5.

Metadata filtering failed once retrieval scope included an attacker. Prefix-based defenses reduced some leakage. Hard post-retrieval ownership gating consistently restored contamination to the clean 1.00 out of 5 baseline across Gemini 2.5 Flash and Claude Sonnet 4.5, with roughly 1.4 milliseconds of measured overhead per query.

Why it matters: embedding similarity is a relevance signal, not an authorization decision. Shared stores can remain operationally efficient only when every retrieved object is rechecked against a trusted owner and audience boundary before it reaches generation.

Strategy fit: memory authority, shared-state governance, tenant isolation, retrieval control.

Tools and methodologies worth exploring now:
- owner and tenant identifiers on every memory object;
- hard post-retrieval authorization before context assembly;
- adversarial semantic-neighbor fixtures;
- separate retrieval leakage and response-contamination metrics;
- fail-closed behavior when identity or ownership metadata is missing.

Artifact status: the paper exposes no public implementation repository in its primary page. The mitigation is straightforward to prototype against an existing retrieval service, but the reported result has not been independently reproduced here.

Evidence caveat: the experiments use bounded teams and authored scenarios. The paper reports small samples for some embedder ablations, so the direction is stronger than any universal leakage rate.

Implementability score: 0.93

Core source:
- [MemLeak paper v1](https://arxiv.org/abs/2610.04195v1)

## Make security-control adoption visible by repository

GitHub now exposes AI Scan for pull requests enablement in the organization and enterprise security overview. Administrators can see enabled and not-enabled repository counts, inspect each repository effective state, filter the coverage view, and export the status in CSV.

Why it matters: a security control that exists but is not enabled across the intended fleet is an inventory gap. The new field gives operators a machine-readable adoption surface that can feed rollout checks, exception queues, and evidence reports.

Strategy fit: agent fleet monitoring, coding-agent governance, security-control inventory.

Tools and methodologies worth exploring now:
- export AI Scan coverage on a schedule;
- reconcile expected repositories against effective enablement;
- assign owners and expiry dates to exceptions;
- distinguish enabled, scanned, finding-free, and remediated states;
- retain coverage snapshots with release evidence.

Product caveat: this is visibility into enablement, not proof that a scan ran, found every issue, or blocked a release. Availability depends on GitHub organization or enterprise security features.

Implementability score: 0.97

Core source:
- [GitHub AI Scan enablement status](https://github.blog/changelog/2026-10-06-code-scanning-ai-scan-enablement-status-in-security-overview)

## Working conclusion

Control planes need explicit object authority and explicit coverage state. Enforce ownership at memory assembly, then prove which repositories have the intended security controls enabled.
