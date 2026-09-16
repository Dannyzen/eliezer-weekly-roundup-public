# Agentic AI Research Analysis: 2026-09-16

## Freshness and evidence boundary

A real Wednesday arXiv batch was first listed September 16. Both selected v1 papers were submitted September 15, so they are inside the strict recent window. arXiv category listings, immutable pages, HTML papers, Hugging Face Daily Papers, GitHub Trending, the GitHub changelog feed, and web news were scanned. Public artifacts were inspected read-only. No external repository was cloned, installed, built, imported, or executed.

## Replace saturated coding-agent ranks with evidence-backed tiers

### Finding

SWE-bench Verified no longer supports the precision implied by its top ranks. An audit of 254 public submissions across four splits finds that the leading two Verified entries each solve 396 of 500 instances. The top ten share 285 successes and 51 failures, leaving only 164 instances that distinguish outcomes. All 29 frontier pairwise comparisons examined are statistically unresolved under the paper's audit.

### Why it matters

A one-point leaderboard gap is not an operational reason to switch coding agents when the benchmark cannot separate them. Model choice should use tiers first, then deployment-shaped evidence such as cost, latency, recovery behavior, repository fit, and the exact scaffold. The published score is a property of a model-scaffold-evaluation combination, not a model alone.

### Fit in the stack

This belongs in trajectory-aware evaluation and coding-agent control. Benchmark admission needs a resolution audit before a score can drive routing or procurement.

### Practical methods worth exploring

- compute per-instance agreement, effective comparison size, and paired separability before ranking systems
- publish tiers when adjacent systems are unresolved
- freeze model, scaffold, harness, task set, and verdict matrix in the evidence receipt
- add deployment-specific tie-breakers only after benchmark resolution is exhausted
- inspect the public `resolution-audit` package and its released tier/factorial tables before adapting the method

### Artifact status

The public repository contains analysis scripts, released tables, and fixed-seed reproduction instructions over public SWE-bench data. It has a populated default branch but GitHub reports no recognized license, so treat it as an inspectable methodology package rather than reusable licensed code.

Implementability score: 0.86

Core source: https://arxiv.org/abs/2609.17394v1
Artifact: https://github.com/Adkid-Zephyr/resolution-audit

## Treat agent-visible UI as a separate untrusted observation

### Finding

Mobile agents and people can receive materially different representations of the same interface. Across 546 tasks, 13 Android applications, five mobile-agent frameworks, and three backbone models, pre-deployment UI perturbations achieved average misleading rates of 77.9 percent in static evaluation and 66.9 percent in dynamic evaluation. A 186-person questionnaire tested whether the perturbations remained inconspicuous to users.

### Why it matters

A human approval based on the physical screen does not prove what the agent saw in a screenshot or accessibility tree. This is a representation-integrity failure at the action boundary. Accessibility metadata, occluded pixels, low-contrast content, and machine-clickable widgets must be treated as untrusted inputs, not as neutral render details.

### Fit in the stack

This belongs in GUI-tool path orchestration and adversarial harness design. The action gate must compare the agent's observation with the user's approval surface before a consequential tap, submission, or purchase.

### Practical methods worth exploring

- render and diff screenshot, framebuffer, accessibility tree, and human-visible preview
- reject hidden or non-human-actionable widgets from the executable action set
- bind approval to the exact observation hash and selected widget identity
- verify application provenance and signing before allowing autonomous operation
- add UI-desynchronization fixtures to mobile-agent regression suites

### Evidence caveat

The paper measures redirection to a honeypot widget, not a completed malicious payload. No paper-specific public implementation repository was found on the primary page. The defense pattern is actionable, but a production parity gate requires mobile instrumentation and platform-specific policy.

Implementability score: 0.62

Core source: https://arxiv.org/abs/2609.16732v1

## Practical next steps

1. Add a paired-separability gate before using any coding-agent leaderboard rank as a routing rule.
2. Build one UI parity fixture that compares the accessibility tree and screenshot shown to the agent with the approval view shown to the user.
3. Record benchmark tier, scaffold identity, observation hash, and action target in the same execution receipt.
