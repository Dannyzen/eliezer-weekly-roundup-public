# AgenticAI Daily Analysis: 2026-10-13

## Scope

This scan covers the arXiv batch first listed on Monday, October 12, 2026, plus primary vendor releases published in the prior 24 hours. The selected papers were submitted October 9 and first listed October 12. External repositories were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Thesis

Agent quality improves when the harness owns explicit evidence state and independent test adequacy. A longer transcript is not a reliable evidence store, and a passing test suite is not proof that the suite distinguishes correct behavior from subtly broken behavior.

## LongHarness: separate evidence, conclusions, and unresolved gaps

LongHarness turns long-corpus reasoning into an explicit state machine. Its state separates source-linked evidence, current conclusions and open information gaps, and the prior action history. An EvidenceBank tracks whether evidence remains active, while the conclusion state tells the next search what is still unresolved.

### Why it matters

The key failure is evidence-state drift. Agents can retrieve the right fact, later discover a correction, and still answer from an obsolete conclusion buried in the transcript. LongHarness makes evidence revision an operation instead of hoping that another prompt will repair the model's attention.

On OfficeQA Pro, GLM-5.3-Flash exact match rose from 15.8% to 60.2% on V1 and from 4.4% to 61.1% on V2. Removing persistent states reduced V2 by 7.8 points, while removing evidence-conclusion coevolution reduced it by 9.4 points. The paper also separates retrieval, evidence adoption, and final transformation, which makes failure location inspectable.

### Stack fit

Primary layer: agent harness architecture.

Adjacent layers: agentic search, knowledge-state orchestration, evidence provenance, and context economy.

### Practical tools and methods worth exploring

- Use typed `Evidence`, `Conclusion`, `OpenGap`, and `EvidenceStatus` records outside the model transcript.
- Require every conclusion to cite active evidence IDs.
- Mark corrected evidence inactive and surface every conclusion that still references it.
- Search against unresolved gaps instead of broad topic similarity.
- Measure retrieval, adoption, and answer transformation separately.
- Bind the state schema, corpus version, model, budget, and final citations into one run receipt.

### Evidence and caveat

The paper reports one run per setting for its harness comparisons. AA-LCR harness outputs are graded by GPT-5.6-Luna, and no dedicated public implementation repository was identified from the paper or arXiv HTML. The architecture is concrete, while the reported ranking needs replication.

Implementability score: **0.66**

Core source: [LongHarness paper v1](https://arxiv.org/abs/2610.13075v1)

Duplicate status: extension of evidence-provenance and knowledge-state work. The new control is a live evidence lifecycle joined to explicit unresolved conclusions.

## TestSuiteBench: grade test adequacy against requirement-targeted mutants

TestSuiteBench asks coding agents to generate complete test suites from natural-language specifications for 165 open-source applications. Each task includes a reference implementation, reference tests, and requirement-targeted mutants. The benchmark averages 74 mutants per application; 73% are killed by exactly one reference test, and only 0.2% of the remaining reference tests kill a given mutant on average.

### Why it matters

Agents can generate tests that look valid without covering the behavior the specification requires. In the study, 88% of generated tests pass against the reference implementation, while every evaluated frontier agent remains below a 60% mutation score. Implementations generated from the same specifications pass 82% of the reference tests. The result exposes a verification gap: agents can build software they cannot adequately test.

### Stack fit

Primary layer: trajectory-aware evaluation and software quality harnesses.

Adjacent layers: coding-agent control planes, behavior-driven development, release evidence, and adversarial test generation.

### Practical tools and methods worth exploring

- Compile each requirement into at least one targeted mutant or independently wrong implementation.
- Score validity and mutation kill rate separately.
- Preserve the requirement, mutant, killing test, and agent trajectory as one evidence record.
- Add multiple valid implementations so tests do not overfit one reference.
- Freeze generated tests before running the hidden mutant set.
- Route surviving high-risk mutants to a human tester or a stronger test-generation pass.

### Artifact and caveat

The public [TestSuiteBench repository](https://github.com/eth-sri/testsuitebench) is MIT-licensed, has a populated 1,720-path tree, and links three populated Hugging Face datasets for reference implementations, tests, and mutants. The published setup requires Linux x86_64, Docker, provider credentials, and potentially about 100 GB for an offline dataset cache. The artifact was inspected read-only and was not executed.

Implementability score: **0.87**

Core sources:
- [TestSuiteBench paper v1](https://arxiv.org/abs/2610.13065v1)
- [TestSuiteBench repository](https://github.com/eth-sri/testsuitebench)
- [TestSuiteBench datasets](https://huggingface.co/collections/eth-sri/testsuitebench)

Duplicate status: extension of TestPrism and GTDD. The new control is repository-scale mutation adequacy generated from full specifications.

## Implementation order

1. Add typed evidence and open-gap records to one research or support-agent harness.
2. Add active or inactive evidence status and reject final citations to inactive records.
3. Add requirement-targeted mutants to one bounded software fixture.
4. Report test validity and mutation adequacy separately.
5. Keep model-authored completion outside release authority until both evidence and test oracles pass.
