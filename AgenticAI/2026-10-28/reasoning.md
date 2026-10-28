# AgenticAI Daily Analysis, 2026-10-28

The strongest new evidence says static success labels are too weak for agents that search changing systems, inherit ongoing work, or generate their own tests. Reliable evaluation needs executable current truth, explicit inherited state, and behavioral oracles that distinguish a passing test from an adequate one.

## 1. Recompute the gold answer from live source systems

LiveSearch stores each benchmark question as executable verifier code: a typed program calls a professional financial data service and a declarative extractor produces the current gold answer. A daily job re-executes the program without a language model in the grading path. Across six contemporary tool-calling models, general web search accuracy ranged from 70.9% to 76.7%. Over three days, 70% of served questions changed their gold value, and a reused snapshot failed on a majority of questions within one day even with tolerance-aware matching.

Why it matters: a static benchmark can reward memorized answers after the underlying world changes. The reusable pattern is to freeze the question and version the verifier while recomputing truth from the authoritative source.

Fit in the stack: trajectory-aware evaluation and live operational testing. The verifier, source identity, as-of time, tolerance, and execution receipt belong to each score.

Implementable now:
- encode mutable answers as typed source calls plus deterministic extraction;
- separate question version from gold-answer execution time;
- retain source, query, extractor, tolerance, and result receipts;
- track per-item correctness across runs instead of only aggregate accuracy;
- fail closed when the professional source or verifier cannot produce current truth.

Artifact status: paper methodology only; no public implementation artifact was linked from the paper in this scan.

Implementability score: 0.84

Core source: [LiveSearch v1](https://arxiv.org/abs/2610.37166v1)

## 2. Evaluate takeover from inherited work state

HSC-Bench contains 1,039 tasks across repository evidence recovery and continuation from conversational, tool, and file-work state. Six receiving models were tested. Structured handoff state improved repository evidence recovery for every model and continuation for most models. Rankings differed between evidence recovery and continuation, showing that finding prior facts does not prove a receiver will preserve commitments, completed effects, rejected attempts, or protected boundaries.

Why it matters: a handoff is successful only when the next agent continues the actual work without repeating effects or erasing decisions. Memory recall alone cannot prove that.

Fit in the stack: multi-agent orchestration and event-sourced runtime. Handoff state should carry decisions, observations, completed effects, pending work, rejected paths, file state, and verification status as distinct fields.

Implementable now:
- serialize structured handoff state beside the human summary;
- mark completed and non-repeatable effects explicitly;
- preserve rejected attempts and protected files as constraints;
- grade evidence recovery and continuation separately;
- test takeover with a different receiver model before production routing.

Artifact status: paper methodology only; no public benchmark repository was linked from the paper in this scan.

Implementability score: 0.86

Core source: [Benchmarking Task Takeover Across Agent Handoffs v1](https://arxiv.org/abs/2610.36523v1)

## 3. Grade generated tests by behavior, not execution success

Req2Test-Bench recovers 5,086 execution-validated requirement-to-test instances from 8 open-source projects, covering 5 languages and 4 BDD frameworks. The best tested configuration produced passing tests for 82.8% of instances, but only 33.8% were behaviorally adequate under kill-completeness, meaning they killed every mutant killed by the developer test. Along the target-hidden Pareto frontier, four times the cost bought only 6.1 percentage points of KillComplete@1, and more spending produced no measurable gain.

Why it matters: a generated test can run and pass while failing to constrain the required behavior. Test execution is a transport check; mutation-equivalent behavior is the release evidence.

Fit in the stack: agent harness architecture and coding-agent quality gates. Requirements, interfaces, hidden behavioral mutations, and cost should be versioned as one evaluation fixture.

Implementable now:
- derive target-hidden tests from Gherkin or another explicit requirement contract;
- grade syntax, execution, assertion reach, and mutation kill-completeness separately;
- preserve developer tests as hidden behavioral oracles;
- route under-specified requirements back for clarification instead of rewarding shallow passing tests;
- measure behavior gained per dollar before escalating model or reasoning effort.

Artifact status: the paper advertises a GitHub repository and Hugging Face dataset. The repository returned 404 and the dataset API returned 401 during this scan, so neither artifact is verified as publicly usable.

Implementability score: 0.80

Core source: [Req2Test-Bench v1](https://arxiv.org/abs/2610.36584v1)

## Working conclusion

Use executable current truth for mutable domains, structured state for agent takeover, and behavioral adequacy for generated tests. A fresh answer, a coherent handoff, and a passing test each need stronger evidence than their surface form provides.
