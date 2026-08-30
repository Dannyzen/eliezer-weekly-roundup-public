# Strategy Daily Sovereignty - 2026-08-23

## Scope note

There is no Sunday arXiv announcement batch. COPA was first listed on Friday, August 21 and submitted on Thursday, August 20. It is outside the strict trailing 48-hour submission window at run time, but it is the newest verified strategic extension not already covered in the repository. The paper PDF was downloaded as a document and converted to text. No external repository source was cloned, downloaded, installed, or executed.

## Adaptive prompt-injection defense needs a versioned learning loop

COPA reframes prompt-injection defense from a fixed filter into a continual preference-optimization loop. A frozen base model receives a lightweight LoRA adapter trained with GRPO. Margin-weighted replay retains difficult earlier attacks while new attack variants enter a sequential curriculum.

The experiment starts from 102 cybersecurity preference pairs, trains over nine prompt-injection variants, holds out six variants, and uses a replay buffer of 60 preference pairs. COPA kept attack success below 0.06 across three escalating scenarios, while the strongest reported baseline reached 0.25 in the hardest scenario. The paper reports up to a 6.3 times reduction in attack success, 4.4 times on average, plus 0.119 higher backward transfer and 0.156 higher average performance than the strongest defense baseline.

Why it matters: static defenses decay as adversaries recombine known techniques. A governed agent platform needs a recurring evidence loop that collects new attacks, evaluates old and new variants, updates a bounded defense artifact, and preserves rollback and prior-attack coverage.

The weak point is substantial. The study uses one controlled attack family, a binary judge, one lightweight adapter setup, and no public implementation artifact. A learned defense can also become another opaque authority surface. It must supplement, not replace, deterministic separation between untrusted content, instructions, tool authority, approvals, and side effects.

Practical paths worth exploring now:
- maintain a versioned prompt-injection corpus split into train, retained regression, and held-out attack families;
- shadow-train adapters and compare them against frozen and static-defense controls;
- record attack variant, judge version, base model, adapter, replay sample, seed, and terminal policy result;
- require backward-transfer and general-utility gates before promotion;
- preserve a one-step rollback to the prior adapter;
- keep browser isolation, tool allowlists, approval gates, and exact-effect brokers outside the learned defense.

Artifact status: the paper and PDF were inspected. No public COPA code, model, dataset, or exact artifact repository was exposed in the primary sources.

Implementability score: 0.38

Core sources:
- [COPA paper](https://arxiv.org/abs/2608.19982v1)
- [COPA PDF](https://arxiv.org/pdf/2608.19982v1)
