# AgenticAI Daily Analysis - 2026-08-25

## Scope note

The selected papers were first listed by arXiv on Tuesday, August 25. Their immutable v1 submissions were received between August 23 at 10:16 UTC and August 24 at 09:45 UTC. AutoSaddler, ClawProBench, and the execution-edit checker fall inside the strict trailing 48-hour submission window at the 12:00 UTC run time. Boundary-Aware Skill Memory was first listed today but was submitted about 49 hours and 44 minutes before the run.

Hugging Face Daily Papers, the Hugging Face blog feed, GitHub Trending, the GitHub Copilot changelog, and official vendor news were scanned. Apodex 1.1 was the strongest Hugging Face release signal, with open weights and an open harness, but its broad vendor-authored performance claims did not displace the four more diagnostic control patterns selected here. `blogwatcher-cli` was unavailable, so direct RSS and primary pages were used.

External repositories were inspected read-only through GitHub metadata, trees, README pages, and documentation. No external source code was cloned, installed, built, imported, or executed. NotebookLM remained disabled and untouched.

## Optimize harnesses from verified failure traces, not free-form reflection

AutoSaddler treats harness improvement as offline learning. It diagnoses failed execution traces, generates structured patches across prompt, tool, and middleware surfaces, tests each patch on a validation split, and records accepted and rejected lineages in an EvoDAG. The durable object is not a reflection note. It is a patch with measured effects, regressions, and lineage.

The result is material across three long-horizon benchmarks. AutoSaddler improved the corresponding base harness by 9.0 percentage points on GAIA2, 9.6 points on SWE-Bench Pro, and 10.0 points on Terminal-Bench 2.0. On GAIA2 it reached 72.3 percent development accuracy with about 1,000 total task executions, while GEPA and Meta-Harness saturated at 64.6 and 61.5 percent after about 2,800 executions. Its best result used 147 optimization traces versus 1,400 for Meta-Harness.

Why it matters: self-improvement should modify bounded harness surfaces through a train, validation, and test protocol. Deep debugging, targeted patches, regression evidence, and held-out selection are the control loop. Unconstrained self-editing is not.

Practical tools and methodologies worth exploring:
- run one owned harness through a mini-batch diagnosis, patch, verification loop;
- separate steering patches from executable capability patches and gate them differently;
- store every patch, evaluated trace set, fixed case, regression, and score in a lineage DAG;
- deny optimizer access to evaluation code and hidden benchmark data;
- require held-out improvement, no safety regression, and human review before production promotion.

Artifact status: `microsoft/AutoSaddler` is a populated public repository with 233 tree entries, CI, a `pyproject.toml`, dataset and architecture documentation, scripts, and an MIT license. The paper points to a Microsoft project URL, while exact GitHub identity was resolved read-only through GitHub search and repository metadata. The artifact was not executed. The paper is heavily Microsoft-affiliated, and its evaluated tasks are stateless and independent, so stateful production generalization remains unproven.

Implementability score: 0.78

Core sources:
- [AutoSaddler paper](https://arxiv.org/abs/2608.23041v1)
- [AutoSaddler repository](https://github.com/microsoft/AutoSaddler)

## Put applicability, risk, avoidance, and recovery into every reusable skill

Boundary-Aware Skill Memory identifies a concrete failure in success-only skill distillation. A retrieved procedure can look semantically relevant while being invalid for the current state. More retrieved skills then increase confidence in the wrong tool rather than improving the choice.

BASM changes the skill record from a procedure into a seven-slot contract: goal, procedure, tools, applicability conditions, risk cues, avoidance rules, and recovery notes. At decision time, the agent can apply, suppress, or repair instead of blindly imitating. In the paper's probes, success-distilled skill memory raised the wrong-tool margin by 47 percent over a memory-free baseline. Across BFCL, AppWorld, and AgentDojo and four model scales, BASM improved AppWorld success by up to 23.8 percent, improved BFCL accuracy by up to 5.0 percent, reduced AgentDojo attack success by 4.6 percent, and reduced AppWorld steps by up to 6.6 percent against the memory-free baseline.

Why it matters: relevance is not permission. A skill should state where it applies, what invalidates it, which risky alternatives to avoid, and how to recover after a partial failure. Retrieval should surface those boundaries under the same token budget as the procedure.

Practical tools and methodologies worth exploring:
- extend existing skill schemas with applicability, risk, avoidance, and recovery fields;
- extract boundary evidence from both successful and failed trajectories;
- compare procedure-only, boundary-aware, and memory-free conditions on paired tasks;
- add wrong-tool decoys and post-failure repair states to skill evaluation;
- require a runtime boundary check immediately before consequential tool calls.

Artifact status: no public implementation repository or exact artifact URL appeared in the immutable arXiv page or inspected HTML, and an exact GitHub repository search returned no result. The seven-slot schema and evaluation method are implementable from the paper, but the authors' implementation was not independently inspectable.

Implementability score: 0.76

Core source:
- [When Not to Imitate](https://arxiv.org/abs/2608.22339v1)

## Evaluate the declared model-plus-runtime configuration from traces

ClawProBench makes the evaluation unit explicit: model endpoint, prompt wrapper, controller, runtime, tools, schemas, safety filters, execution policy, checker bundle, and scoring code. It scores the declared bundle from traces rather than assigning a final-answer score to a model name.

Its full profile has 102 scenarios, including 66 workspace tasks and 36 tasks across eight native OpenClaw surfaces. A frozen 68-scenario holdout supports fixed-contract comparison. The authors evaluated 68 configurations on the full profile and 37 on holdout. Native-runtime tasks scored 0.5238 versus 0.6415 for workspace tasks. On holdout, pass-at-k-any reached 0.6638 while strict three-trial pass was 0.2890. Full-profile and holdout rankings had Spearman correlation 0.13. Those gaps are the finding: one-off success, final correctness, and public-profile rank can hide runtime weakness.

Why it matters: product reliability belongs to a versioned model-plus-runtime manifest. The benchmark should preserve expected surfaces, exact checks, trace events, safety gates, repeated-trial status, and fixture hashes so a score can be reproduced and challenged.

Practical tools and methodologies worth exploring:
- version a declared runtime manifest alongside every benchmark result;
- freeze a realistic holdout with hashed fixtures and checker bundles;
- require three-trial strict pass in addition to pass-at-k-any;
- score correctness, process quality, safety, and efficiency separately before any composite;
- adapt ClawProBench's surface registry and trace schema to one Hermes runtime profile.

Artifact status: `suyoumo/ClawProBench` is a populated public Apache 2.0 repository with more than 7,000 tree entries, scenario YAML, custom checkers, pricing configuration, security documentation, and deterministic grading infrastructure. It was inspected read-only and not executed. The paper is single-author and instantiated on OpenClaw, so cross-runtime validity still needs an independent Hermes adaptation.

Implementability score: 0.88

Core sources:
- [ClawProBench paper](https://arxiv.org/abs/2608.22510v1)
- [ClawProBench repository](https://github.com/suyoumo/ClawProBench)
