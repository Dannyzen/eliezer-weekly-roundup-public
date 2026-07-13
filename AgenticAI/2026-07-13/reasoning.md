# AgenticAI Daily Reasoning - 2026-07-13

## Daily thesis

The strongest new signal is that agent reliability depends on explicit intermediate artifacts. A final pass or failure is too late. Coding agents need temporal failure checkpoints, memory needs typed promotion rules, and AI-generated validation needs a shared intent artifact that can be both proved and executed.

The papers below were submitted on July 10 and appeared in the Monday arXiv batch after the July 12 scan. No external repository was cloned, installed, built, imported, or executed.

## CLI coding-agent failures need three timestamps, not one verdict

**Core sources:** [Failure as a Process](https://arxiv.org/abs/2607.09510v1), [public replication package](https://github.com/xz-Sean/cli_trajectory_analysis)

### What the paper adds

The study analyzes 3,843 CLI coding-agent runs from seven frontier models, three scaffolds, and Terminal-Bench. Its manually adjudicated dataset contains 1,794 complete trajectories and more than 63,000 execution steps.

The useful abstraction is a three-stage failure record:

- `t_err`: the decisive error that starts the eventual failure chain;
- `t_lock`: the point after which no correct recovery is observed;
- `t_obs`: the first externally observable sign of the failure.

Across failed trajectories, the reported medians are step 7 for `t_err`, step 12 for `t_lock`, and step 16 for `t_obs` among failures that surface. The paper reports that 28% of failures never become externally visible. A final verdict therefore hides both the intervention window and the silent tail after recovery has effectively disappeared.

### Why it matters

A run monitor should not wait for a failed test at the end. It should ask whether the current trajectory has crossed from a recoverable mistake into an accumulating error chain. This converts trajectory logging from postmortem storage into an online intervention surface.

### How it fits into the stack

- **Harness:** preserve task requirements, action steps, observations, and verifier results with exact step IDs.
- **Evaluation:** score onset, lock-in, observability lag, recovery attempt, and final outcome separately.
- **Runtime:** run bounded prefix checks after high-risk decisions and before irreversible changes.
- **Learning loop:** turn recurring early error signatures into deterministic checks, route changes, or regression fixtures.

### Practical tools, repositories, and methodologies

- Use the public `xz-Sean/cli_trajectory_analysis` codebook and annotated data as a schema reference.
- Add `t_err`, `t_lock`, and `t_obs` labels to internal failed-run reviews.
- Compare OpenHands, MiniSWE, Terminus2, and any local harness on the same task and model set.
- Insert prefix checkpoints after task interpretation, environment discovery, first edit, first test, and pre-commit validation.
- Preserve the task specification alongside the trace, because some failures are visible only relative to a violated requirement.

### Weakest point

The three timestamps are retrospective, human-adjudicated labels. The authors explicitly define unrecoverable as empirically unrecovered, not impossible to recover. The replication package provides annotations and analysis scripts but omits raw trajectories and currently declares no repository license. It is strong for schema and analysis reuse, but weaker as a complete online-monitor implementation.

**Implementability score: 0.80**

## Selective memory should preserve configuration and discard old reasoning traces

**Core source:** [Shared Selective Persistent Memory for Agentic LLM Systems](https://arxiv.org/abs/2607.09493v1)

### What the paper adds

The paper separates reusable agent context into four durable categories:

1. task specifications;
2. data schemas;
3. tool configurations;
4. output constraints.

It explicitly discards prior reasoning traces, tool logs, intermediate states, and recovery paths from the next session's active context. The deployed workspace keeps generated artifacts in Git, isolates drafts, applies role-based access control to shared workspaces, and decouples generated programs from runtime data.

The reported enterprise study reaches 96% task completion with selective memory, compared with 79% without memory and 71% with full-history persistence. For recurring compatible-data updates, its zero-token refresh path avoids model reinvocation and reports a 14x time reduction. Summary-driven generation reports a 97x token reduction compared with injecting raw data.

### Why it matters

More history is not better memory. The reusable object is often the configuration contract that made the prior artifact correct, not the transcript that happened to produce it. Persisting full traces can bias a new run toward stale actions while consuming context budget.

### How it fits into the stack

- **Memory:** store typed durable configuration separately from episodic evidence.
- **Artifact runtime:** version generated programs and bind fresh data at execution time.
- **Collaboration:** scope shared memory by workspace, role, and version.
- **Context economy:** inject compact schemas and constraints, not raw tables or old tool traces.

### Practical tools, repositories, and methodologies

- Use typed records for task rules, schemas, tool manifests, and output contracts.
- Keep raw episodes in an evidence store, but require an explicit promotion step before anything enters active durable context.
- Version artifacts and promoted memory together in Git or an event-sourced store.
- Separate generated logic from runtime data so safe refreshes do not require another model call.
- Add no-memory, full-history, summary, and selective-memory ablations to internal agent evals.

### Weakest point

The implementation is a closed Apple deployment and no public code or dataset link is exposed. The enterprise evaluation is small and product-specific, and the public-dataset replication primarily supports zero-token refresh rather than the full collaborative memory architecture. Treat the four memory categories as a strong design pattern, not a drop-in validated system.

**Implementability score: 0.68**

## Property templates make AI-written tests prove and execute the same intent

**Core sources:** [Agentic Proof and Property-Based Testing via Property-Templates](https://arxiv.org/abs/2607.09072v1), [browsable artifact](https://anonymous.4open.science/r/AgentLeanDiscprop-1597/)

### What the paper adds

The paper introduces a dual verification pattern for recurring correctness properties. One typed property template with explicit holes produces two artifacts:

- a Lean 4 proof over a formal model;
- a property-based test that exercises the real PySpark implementation.

The same intent is therefore checked against both model truth and runtime behavior. A proof that succeeds while the property-based test finds a counterexample exposes a model-to-implementation gap instead of producing false confidence.

Across 400 properties in four Apache Spark families, property templates increase agentic proof success by up to 2.6x, reduce proof hallucinations by 59%, cut property-based-test intent mismatches from 22 to 1, and reduce synthesis cost by up to 5.7x.

### Why it matters

AI makes code generation cheaper, so intent validation becomes the bottleneck. Test generation alone is not enough if the generated test checks a weaker property than the requirement. Formal proof alone is not enough if the formal model omits behavior present in the real system. A shared typed template keeps both tracks attached to the same claim.

### How it fits into the stack

- **Specification:** encode recurring invariants once as typed property families.
- **Harness:** let the agent fill bounded holes rather than author the full proof and test architecture.
- **Verification:** require both a machine-checked proof and executable randomized tests for high-value invariants.
- **Evidence:** preserve disagreements between proof and runtime as first-class defect reports.

### Practical tools, repositories, and methodologies

- Start with one recurring invariant family, such as serialization round trips, authorization monotonicity, or aggregate decomposition.
- Use Lean 4 for the model-side proof and Hypothesis or another property-based testing framework for runtime checks.
- Store the property template, proof result, generated test, counterexamples, and model assumptions in one evidence packet.
- Inspect the anonymous artifact as a read-only reference for property cards, proof templates, PySpark tests, and cross-validation outputs.

### Weakest point

The evaluation is concentrated on Apache Spark and four property families. The artifact is complete enough to inspect but operationally heavy: Lean 4, PySpark, generated workloads, model calls, and manual review of compiling but vacuous proofs. Generalizing the pattern requires domain-specific formal models and invariant families.

**Implementability score: 0.72**

## What to implement first

1. **Instrument** failed runs with `t_err`, `t_lock`, and `t_obs` during postmortems, then add prefix checkpoints at the earliest repeated error classes.
2. **Separate** durable configuration memory from raw episodic evidence, and add an explicit promotion contract.
3. **Template** one high-value recurring invariant into a shared proof and property-based-test artifact.
4. **Replay** all three changes on a small fixed suite before connecting them to production side effects.

## Selection notes

- arXiv recent-category pages were parsed directly across cs.AI, cs.SE, cs.CR, cs.CL, cs.LG, cs.MA, and cs.HC.
- Hugging Face and GitHub changelog feeds had no newer agent-specific entry after July 10.
- GitHub Trending was used only as a demand signal and did not determine the selected findings.
- Public repository checks were read-only. No external source code was downloaded or executed.
