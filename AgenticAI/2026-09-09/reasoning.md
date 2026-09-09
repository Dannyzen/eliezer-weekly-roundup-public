# AgenticAI Daily Analysis - 2026-09-09

## Freshness and selection

arXiv exposed a real Wednesday, 9 Sep 2026 listing batch. The selected v1 papers were submitted on 8 Sep UTC. Hugging Face, GitHub Trending, and official vendor feeds were scanned as discovery surfaces; claims below come from immutable arXiv records, full paper HTML, and read-only artifact inspection. No external repository was cloned, downloaded, installed, built, imported, or executed.

## Independent tests must be frozen before repair

ExecCritic separates behavioral test construction from source repair. A Test agent creates a repository-native test patch, exact execution command, and structured behavior contract. A fail-closed harness qualifies the bundle on the buggy base, freezes it, and prevents the Repair agent from editing tests while it revises source code from execution feedback.

The paper shows why the separation matters. Holding the base Qwen repair agent fixed, tests from the base Test agent lowered SWE-bench Verified resolution from 61.2% without generated tests to 57.3%. GPT-5.6-sol-generated tests raised it to 65.3%. Role-specific post-training raised Base-to-Gold test success from 22.2% to 62.2%, and the composed trained agents reached 72.6%, 11.4 points above the original no-test baseline.

Why it matters: executable feedback is not automatically evidence. When one trajectory writes both the patch and the test, a shared misunderstanding can make the test and patch agree while both are wrong. Separate principals and immutable acceptance artifacts reduce that coupling.

Fit in the stack: coding-agent harness architecture and deterministic quality gates.

Practical tools and methodologies worth exploring now:
- assign independent test and repair principals with different write permissions;
- require a structured behavior contract, exact command, clean base failure, and isolated execution before admitting a generated test;
- freeze admitted tests across repair attempts;
- run official or held-out verification after the generated-test gate;
- store test identity, test author, base result, gold-audit result, repair identity, and final verifier result in one receipt chain.

Artifact status: `MSR-Orchard/execcritic` is public with a populated `main` branch, harness code, prompts, test-map builders, repair loops, offline tests, and training launchers. Full reproduction still requires a sandbox pool, model endpoint, SWE-bench assets, and substantial GPU infrastructure. The repository notes that packaging checks did not run live training or official SWE-bench verification.

Implementability score: 0.72

Core sources:
- [ExecCritic, arXiv:2609.09133v1](https://arxiv.org/abs/2609.09133v1)
- [MSR-Orchard/execcritic](https://github.com/MSR-Orchard/execcritic)

## Runtime state must own progress and completion

The Unreliable Progress Bar tests model-generated lifecycle reports against environment-owned state. On both tau-squared-bench and the controlled StageIF testbed, reliability changes by task stage. Six of seven primary StageIF deployments showed statistically significant nonterminal-to-terminal gaps spanning 29.4 to 89.3 percentage points. The most extreme deployment reached 97.4% adherence at completion but only 8.2% across intermediate checkpoints. At post-done checkpoints, most deployments produced false reports 90% to 100% of the time when correct behavior was to remain silent.

The failure is not one mislabeled value. StageIF separates tool use instead of reporting, omission, malformed output, wrong stage, and failure to withhold a report. Simple reporting interventions did not generally remove the deficits.

Why it matters: a model can finish the task while reporting the wrong state, or claim completion while the environment still shows unmet obligations. Final task success and accurate progress reporting cannot substitute for each other.

Fit in the stack: agent-serving runtime, sessionful loops, cancellation, retry, and completion control.

Practical tools and methodologies worth exploring now:
- derive lifecycle state from durable task records, tool outcomes, pending obligations, and verifier receipts;
- treat model status as a proposal or diagnostic, never as the sole continue-or-stop signal;
- score state emission, value correctness, withholding, and premature completion separately;
- add checkpoints before action, after observation, before completion, after completion, and after cancellation;
- persist the runtime oracle value before exposing the model output to the grader.

Evidence caveat: the paper studies specific deployed model-and-configuration bundles, not intrinsic model rankings. Its provider-free checks rederive stored metrics, but the complete companion artifact remains private during review.

Implementability score: 0.90

Core source: [The Unreliable Progress Bar, arXiv:2609.08589v1](https://arxiv.org/abs/2609.08589v1)

## Procedural knowledge should be an editable graph, not a flat note

Procedural Graphs represents what-to-do knowledge as typed transitions among procedures. At each step, a guidance model localizes the active node, reads a two-hop neighborhood, and generates situational guidance. Offline, a refiner contrasts successful and failed trajectories, proposes graph edits, validates candidates on held-out tasks, and retains rejected edits to prevent repeated failed mutations.

Across six benchmarks and four model families, the method ranked first or tied first in 21 of 24 model-benchmark cells, with 19 wins, two ties, and three losses against the strongest baseline. On EnterpriseArena, the returned evolved graph reached 85% test survival versus 0% for the unguided baseline. The paper explicitly reports the returned graph rather than the best search-time round.

Why it matters: flat reflection notes make the solver reconstruct ordering and prerequisites every time. A graph can expose admissible transitions, verification steps, and failure loops while keeping runtime guidance local.

Fit in the stack: knowledge-state orchestration, procedural memory, and harness evolution.

Practical tools and methodologies worth exploring now:
- represent nodes as tools, skills, reasoning steps, or lifecycle states;
- type edges with preconditions, expected observations, verification requirements, and stop rules;
- localize guidance to the current node and bounded neighborhood;
- freeze the graph during each run;
- accept offline edits only after held-out validation and retain rejected edit fingerprints.

Evidence caveat: the paper provides extensive experiments but no public implementation repository on its primary surfaces. The design also adds guidance-model calls and an offline refinement loop, so a small deterministic workflow graph should be tested before self-evolution.

Implementability score: 0.61

Core source: [Procedural Graphs, arXiv:2609.09153v1](https://arxiv.org/abs/2609.09153v1)

## Working conclusion

Agent loops should not author their own proof of correctness, declare their own lifecycle truth, or rediscover procedure order from flat history. Separate evidence production from repair, derive state from the runtime, and admit procedural changes through held-out gates.
