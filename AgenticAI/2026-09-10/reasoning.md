# AgenticAI Daily Analysis - 2026-09-10

## Freshness and selection

arXiv exposed a real Thursday, 10 Sep 2026 listing batch. The two selected arXiv v1 papers were submitted on 9 Sep 2026 at 14:48 UTC and 17:59 UTC. GitHub's product signal was published on 9 Sep. The scan covered current cs.AI, cs.CL, cs.LG, cs.MA, cs.SE, and cs.CR listings, Hugging Face and vendor feeds, GitHub changelog items, and read-only repository metadata. No external repository was cloned, downloaded, installed, built, imported, or executed.

Two evaluation papers first listed on 10 Sep were not promoted because their v1 submissions were dated 6 and 7 Sep, outside the strict rolling window. A-JIT was also left as a watchlist item because it is a design paradigm rather than an evaluated implementation.

## Detect specification gaps before a coding agent invents the method

IdeaAMBIG measures whether an implementation-facing research specification is complete enough to code faithfully. Its 660 evidence-grounded instances include 163 real gaps from reproducibility reports and GitHub issues plus 497 controlled synthetic gaps. The benchmark separates readiness assessment, defect localization, and clarification-action generation.

The important result is the gap between finding a missing decision and acting once somebody points to it. Across 13 models, the best real-world Macro Defect Recovery Rate was only 9.6%, while the best Macro Clarification Action Success Rate reached 80.6% when the defect was supplied. In an oracle study, providing the supported resolution raised downstream codification readiness from 14% to 98%.

Why it matters: a coding agent can produce working code while silently choosing a method the specification never authorized. Preflight should therefore be a first-class phase, with three explicit outcomes: ready to implement, blocked on a localized gap, or ready to ask one evidence-seeking question.

How it fits the stack: this belongs before planning and code generation in the agent harness. The defect taxonomy can become typed preflight findings, and the gold clarification action can become an acceptance fixture for the orchestrator.

Practical tools and methodologies worth exploring:

- use IdeaAMBIG's public dataset and evaluation code as a read-only design reference;
- add a codification-readiness gate before implementation cards are released;
- require each blocker to name the missing decision, affected implementation surface, and evidence needed to resolve it;
- fail closed when the model proposes an unsupported assumption instead of a clarification;
- score localization separately from question quality so fluent questions do not hide missed defects.

Artifact status: contents inspected read-only. The public repository contains the 660-instance dataset, construction pipeline, and evaluation code. It has no top-level requirements lock and instructs users to install dependencies as import errors surface, so reproducibility is weaker than the benchmark release itself.

Implementability score: 0.84

Core sources:

- [IdeaAMBIG paper](https://arxiv.org/abs/2609.10539v1)
- [Yiling-Ma/IdeaAMBIG](https://github.com/Yiling-Ma/IdeaAMBIG)

## Preserve memory, but make influence query-conditioned

RD-Forget separates the retained source archive from the memory view used for one answer. A frozen curator extracts evidence into semantic slots, same-slot replacement links suppress superseded values for current-state questions, historical intent can re-admit older evidence, and a bounded selector packs the answer-time view.

The evidence is broader than a single synthetic toy. The main comparison covers five task suites and four language models. On fact consolidation, RD-Forget beats the better baseline by 11 to 26 points across the four backbones. In matched Luna ablations, removing forgetting lowered the three reported scores from 91.86, 93.59, and 74.00 to 68.60, 60.26, and 51.00. Removing query conditioning produced the second-largest deficits.

Why it matters: deletion is the wrong default for stale memory. A fact can be wrong for a current-state answer and necessary for a historical one. The durable object should remain immutable or superseded in the archive; authority to influence the current answer belongs to a query-specific view.

How it fits the stack: this is a memory-policy layer between source retention and context assembly. It complements provenance and temporal supersession rather than replacing them.

Practical tools and methodologies worth exploring:

- retain raw observations with source, timestamp, subject, relation, and scope;
- add explicit active, superseded, and historically eligible states;
- build query-conditioned evidence views under a measured token budget;
- test current-state, historical, evolution, contradiction, and multi-hop queries separately;
- preserve selected memory IDs and exclusion reasons in the run receipt.

Artifact status: no paper-owned public code or dataset link resolved from the primary paper surfaces. The method is training-free, but implementation still requires a curator, slot schema, temporal logic, selector, and evaluation harness.

Implementability score: 0.68

Core source:

- [What Should an Agent Forget?](https://arxiv.org/abs/2609.10263v1)

## Remediation agents should start from owned findings and land through review

GitHub Code Quality can now assign up to 25 findings at once to Copilot. Copilot works on a branch, validates its changes, and opens a pull request for review and merge. The feature follows the existing enterprise Code Quality policy rather than creating a second policy plane.

Why it matters: the useful product pattern is not bulk autonomous mutation. It is a bounded queue whose inputs are already-owned findings, whose write surface is an isolated branch, and whose finality remains a reviewed pull request.

How it fits the stack: this is an immediately available coding-agent control-plane pattern for Team and Enterprise Cloud repositories with GitHub Code Quality enabled. It consumes AI credits and does not remove the need for independent tests, review-constraint checks, or repository-specific acceptance gates.

Practical tools and methodologies worth exploring:

- pilot on a low-risk repository with a small finding batch;
- preserve finding IDs, branch identity, validation results, review comments, and merge decision;
- compare accepted fixes, rejected fixes, regressions, latency, and credit cost;
- keep repair tests and final acceptance under independent authority.

Implementability score: 0.92

Core source:

- [Remediate Code Quality findings with agentic autofix](https://github.blog/changelog/2026-09-09-remediate-code-quality-findings-with-agentic-autofix/)

## Build order

1. Add a codification-readiness status and blocker schema before implementation begins.
2. Preserve memory source records, then build a query-conditioned influence gate above them.
3. Pilot branch-isolated bulk remediation only where findings and acceptance tests already have independent owners.
4. Record every preflight decision, selected memory item, repair branch, verifier result, and final merge as replayable evidence.
