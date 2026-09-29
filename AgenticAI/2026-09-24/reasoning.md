# AgenticAI Daily Analysis: 2026-09-24

## Thesis

Agent quality needs executable evidence at two levels: reason about what the repository actually does, and treat recurring agent instructions as maintained production specifications. Static code familiarity and a plausible workflow prompt do not prove runtime behavior or repeated operational safety.

## Measure dynamic execution reasoning with harvested runtime oracles

SWE-Flux evaluates whether models can reconstruct runtime behavior inside real repositories. Its 480 instances span 12 pinned Python repositories and seven behavior classes, including inter-procedural control flow, program state, dataflow, exceptions, and invariants. Gold answers come from instrumented test executions rather than model judges.

The gap is material. The strongest of five evaluated models reaches 37.71 percent accuracy. Runtime dataflow falls to 6 percent. Manual review of 299 wrong answers from the strongest model classifies 93 percent as substantive semantic failures. The perturbation pipeline produced valid variants for 52 of 58 selected instances and cut GPT-5.4 accuracy from 100 percent on the selected originals to 43.1 percent on the variants.

Why it matters: coding-agent gates usually ask whether tests pass after a change. SWE-Flux adds a different question: can the agent explain and predict the behavior it is about to modify? That is useful for debugging, test selection, change-impact analysis, and reviewer calibration when full execution is unavailable or unsafe.

Fit in the stack: this belongs in trajectory-aware evaluation and the coding harness. The runtime oracle supplies ground truth, the harness preserves repository and test identity, and perturbations prevent a fixed benchmark from becoming a memorized lookup.

Practical methods worth exploring now:
- harvest deterministic JSON oracles from instrumented tests;
- cover single-test and suite-level questions separately;
- pin repository SHA, environment, test identity, and oracle schema;
- generate fresh input perturbations and retain the original control;
- report semantic failures separately from formatting failures;
- keep runtime-behavior evaluation beside patch acceptance, not inside a model-judged rubric.

Artifact status: `HamedTaherkhani/SWE-Flux` has a populated public `master` branch with benchmark data, runtime metrics, repository snapshots, and analysis tooling. Its tree was inspected read-only through GitHub metadata. No code was cloned or executed.

Evidence caveat: the benchmark covers 12 Python repositories and five models. Its strongest claims concern repository-level dynamic reasoning within that scope, not universal coding-agent competence.

Implementability score: 0.82

Core sources:
- [SWE-Flux paper](https://arxiv.org/abs/2609.28449v1)
- [SWE-Flux repository](https://github.com/HamedTaherkhani/SWE-Flux)

## Treat recurring agent workflows as maintained executable specifications

An empirical study of GitHub Agentic Workflows analyzes 1,248 Markdown workflow files from 276 repositories, 20,841 commit-file events, and 288 resolved instruction-label sets. The files are substantial, with a median of 556.5 words, and 62.1 percent contain code blocks. Among files observed for at least 120 days, 78.2 percent still change in month four.

The governance gap is concrete. Tasks, outputs, constraints, and process instructions each appear in more than 93 percent of labeled workflows, while only 9.4 percent explicitly address prompt-injection defense. Safety instructions appear in 25 percent. These files combine natural-language policy with triggers, permissions, and tool access, so drift in either half changes production behavior.

Why it matters: recurring agent workflows are closer to programs than prompts. They need ownership, review, linting, versioning, and regression tests. Copied workflows also create update and provenance obligations across repositories.

Fit in the stack: this belongs in the coding-agent control plane. The Markdown source is the human-facing specification, the compiled Actions YAML is the execution artifact, and run evidence is the outcome record. Reviews should compare all three.

Practical methods worth exploring now:
- lint workflow instructions for task, output, process, constraint, safety, communication, budget, and evidence fields;
- diff frontmatter authority and instruction-body semantics separately;
- attach an owner and review cadence to every recurring workflow;
- track copied or referenced workflow provenance across repositories;
- require prompt-injection defense, resource budgets, and evidence-credibility rules where external content enters the run;
- bind compiled YAML and runtime receipts back to the exact Markdown revision.

Artifact status: `stilab-ets/ghaw` has a populated public `main` branch with methods, data, labels, and experiments. `github/gh-aw` is also active and public. Both were inspected read-only through GitHub metadata. No code was cloned or executed.

Evidence caveat: the corpus covers one workflow system during early adoption. Instruction presence does not prove runtime effectiveness, and the paper's classifier should support review rather than replace it.

Implementability score: 0.93

Core sources:
- [Empirical study](https://arxiv.org/abs/2609.27263v1)
- [Replication package](https://github.com/stilab-ets/ghaw)
- [GitHub Agentic Workflows](https://github.com/github/gh-aw)
