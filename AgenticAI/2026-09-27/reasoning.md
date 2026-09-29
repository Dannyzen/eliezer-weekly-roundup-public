# AgenticAI Daily Analysis - 2026-09-27

No new arXiv listing today. Category pages still show Friday, 25 September 2026 as the newest announcement batch. These leftover Friday papers were not promoted in the 2026-09-25 synthesis or the 2026-09-26 leftover scan.

## Grade governance with behavior gates

SWE-Prometheus asks coding agents to improve a pinned repository without an issue, failing test, or reference patch. Scoring covers six dimensions: Tests and CI, Code Quality Gates, Documentation and Collaboration, Structure and Maintainability, Reproducible Environment, and Dependency and Security Health. Credit requires paired evidence, clean-environment probes, and a characterization-test behavior gate. A no-op run has median Normalized Governance Improvement (NGI) of zero and standard deviation 0.073; two teachers agree exactly on 57 of 60 no-op dimension scores.

On the shared 22-repository public subset, mean NGI ranges from 0.0568 to 0.5760 and observed behavior-breakage rates range from 0% to 23% (Figure 3 reports 0% to 22.7%). A repository-blind template reaches mean NGI 0.272 on a frozen ten-repository batch, yet it improves Reproducible Environment and Dependency and Security on none of those repositories. Adding a workflow file is not the same as producing an execution-backed improvement.

### Why it matters

Issue-level SWE benchmarks start after a human has named the defect. Governance work starts earlier: the agent must decide what to change, keep current behavior green, and prove the new controls actually run. That is closer to how Danny should grade coding-agent "hardening" PRs.

### How it fits

This belongs in trajectory-aware evaluation and the coding-agent control plane. It extends Friday's custody thesis from traces and completion claims to repository state after an open-ended retrofit.

### Practical tools and methodologies

- Pin a repository SHA, empty FAIL_TO_PASS, and characterization tests that must stay green.
- Score each governance dimension from treated versus base evidence, then drop behavior-broken runs from the mean.
- Report NGI, breakage rate, coverage, and verified-claim rate together.
- Use the public 22-task package at `CosmosMind-ai/SWE-Prometheus` and the Hugging Face dataset `CosmosMind/SWE-Prometheus` as a fixture, not as a private leaderboard.

Artifact status: contents inspected read-only. The GitHub default branch is `main`; the Hugging Face dataset card confirms 22 public tasks, 38 held out, CC-BY-4.0. No clone or execution.

Implementability score: 0.80

Core source: [SWE-Prometheus](https://arxiv.org/abs/2609.29465v1)

Supporting sources:

- [CosmosMind-ai/SWE-Prometheus](https://github.com/CosmosMind-ai/SWE-Prometheus)
- [CosmosMind/SWE-Prometheus dataset](https://huggingface.co/datasets/CosmosMind/SWE-Prometheus)

## Delegate GUI actions to a typed executor

Jev-Mobile splits mobile GUI control into low-frequency VLM planning and high-frequency typed execution. The VLM emits a local goal. The current accessibility tree defines the executable action space. Jev, a remote typed Decisions service, selects one or more actions under that goal and returns when it is blocked or the goal is done. Each action is grounded in a freshly observed tree.

On the full AndroidWorld suite, Jev-Mobile reaches 0.79 task success versus 0.78 for SeeAct-V and 0.84 for a step-wise VLM. Among successful trajectories, mean end-to-end time falls 32.7% and mean model API cost falls 73.4% relative to the step-wise VLM (from $0.273694 to $0.072744). The paper reports no public implementation repository on its HTML or PDF surfaces.

### Why it matters

Paying a frontier VLM for every tap is the expensive default. The cheaper stack is a planner that names a local goal plus a typed executor that can only choose currently visible, labeled controls.

### How it fits

This is GUI-tool path orchestration and harness architecture. It is the mobile version of compiled skill machines from 2026-09-26: the model reasons inside a state, the runtime owns the action grammar.

### Practical tools and methodologies

- Build candidates from the live accessibility tree, not from a remembered screenshot.
- Allow several executor steps under one planner goal, then force a fresh observation before the next planner call.
- Treat BLOCKED as a first-class return so the planner cannot invent a coordinate click for an unseen target.
- Keep timing and dollar metrics conditional on success, and keep the independent AndroidWorld terminal score as the outcome.

Artifact status: claimed implementation in the paper; no public GitHub URL resolved. Do not treat this as ready-to-run tooling.

Implementability score: 0.46

Core source: [Jev-Mobile](https://arxiv.org/abs/2609.30186v1)
