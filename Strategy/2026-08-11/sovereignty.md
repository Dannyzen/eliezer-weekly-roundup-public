# Strategy Daily Sovereignty, 2026-08-11

The strongest strategy finding in the Tuesday batch treats a multi-agent deployment as an institution, not a collection of individually aligned models.

## Multi-agent governance needs provenance-aware authority and a recoverable denial path

POLIS freezes 5,280 episodes across four backbone model families and three additional frontier endpoints, then varies rules for delegation, shared resources, and post-block behavior.

A detailed constitutional prompt and a provenance-aware executable guard both produced 0 realized violations in 384 main-study episodes. The guard blocked prohibited attempts in 51 episodes, and 44 later completed safely because denial did not terminate the workflow. In matched policy-laundering scenarios, a local-state guard admitted 22 violations in 96 episodes while immutable-provenance enforcement admitted 0 in 96, with a reported paired p-value of 4.77 x 10^-7.

Why it matters: final violation rate can hide whether the system avoided unsafe intent, blocked an unsafe attempt, or dead-ended useful work. The authority source and recovery path are both parts of the institution.

Tools and methodologies worth exploring now:
- [POLIS repository](https://github.com/abdullah-x-bd/polis), inspected read-only;
- immutable authority roots and derivation chains;
- attempted-action versus realized-effect receipts;
- recoverable denials with bounded safe fallbacks;
- matched laundering scenarios;
- completion and utility metrics beside violation rate.

Implementability score: 0.82

Core sources: [POLIS paper](https://arxiv.org/abs/2608.09828v1), [POLIS repository](https://github.com/abdullah-x-bd/polis)

Evidence boundary: this is a single-author paper with a new, zero-star repository and no independent replication. GitHub reports a non-standard license with no SPDX assertion. Adopt the institutional test design before depending on the code.

## Working conclusion

Preserve immutable authority provenance, distinguish attempted from realized effects, and keep safe completion possible after a denial.
