# AgenticAI Daily Analysis - 2026-10-20

This scan covers papers first listed by arXiv on 2026-10-20 and submitted on 2026-10-19. External repositories were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Test evidence exposure, not only tool execution

Same Simulation, Different Evidence isolates a failure that final-answer grading hides. Agents used the deterministic PHREEQC simulator on 158 execution-verified questions. Moving long reports behind a section index reduced GPT-5.1 and GPT-5.2 accuracy by 11.3 and 7.9 percentage points, while the underlying computation remained about as reliable. Replay of 11,007 simulator calls showed that retrieval changed which evidence the agent used. The agents often substituted their own higher-precision files for the authoritative report and rounded to a neighboring option.

The practical fix was small. Naming the authoritative output improved accuracy by 6.3 to 7.9 points across three GPT models. Asking for correct rounding did not fix the problem. This makes evidence exposure a harness variable, separate from tool correctness and model capability.

Why it matters:
- correct tool execution can coexist with a wrong evidence path;
- retrieval policies can create regressions that aggregate task success masks;
- authoritative source identity should be part of the tool contract and trace.

Implementable now:
- label authoritative outputs in tool schemas and tool results;
- record build, exposure, and closure stages separately;
- replay deterministic tool calls to isolate computation from evidence use;
- compare inline, indexed retrieval, and authority-labeled retrieval on identical tasks.

Evidence caveat: the study uses one scientific simulator, 158 multiple-choice items, and closed models. The paper does not identify a public implementation artifact.

Implementability score: 0.88

Core source: [Same Simulation, Different Evidence v1](https://arxiv.org/abs/2610.26836v1)

## Grade compression on evidence preservation

KEEP-Bench evaluates the compressed context itself instead of relying on downstream QA accuracy. Its 4,102 cases require compressors to retain parallel interpretations, explicit qualifiers, and minority perspectives. The best reported open-weight model preserved all required evidence in 66.8 percent of cases, and the best proprietary model reached 61.6 percent, despite inputs averaging only 3.1K tokens.

The benchmark also introduces Evidence Preservation Return, which relates evidence recall to inference FLOPs. The metric peaks at moderate model scales, but recall remains low. Larger output budgets mainly help stronger models and do not remove the fidelity problem.

Why it matters:
- a reader can answer correctly from an unfaithful compression;
- summary quality and evidence preservation are different release criteria;
- compaction should preserve qualifiers, alternatives, and minority evidence, not only a plausible dominant narrative.

Implementable now:
- run proposition-level evidence recall before adopting a compressor;
- test parallel, conditional, and imbalanced evidence structures;
- retain raw source spans and source identities outside the compressed view;
- track evidence recall, token reduction, FLOPs, latency, and downstream outcome together.

Artifact status: the public repository and Hugging Face dataset resolve and were inspected read-only. The repository contains compression, evaluation, scoring, and FLOPs tooling. Reproduction requires multiple model environments and 15,953 judge requests per method and budget. Code is MIT; the dataset is CC BY-NC 4.0.

Implementability score: 0.76

Core sources:
- [KEEP-Bench paper v1](https://arxiv.org/abs/2610.26827v1)
- [KEEP-Bench repository](https://github.com/PlusLabNLP/KEEP-Bench)
- [KEEP-Bench dataset](https://huggingface.co/datasets/uclanlp/KEEP-Bench)

## Evaluate coding agents against complete delivery contracts

PACE evaluates PRD-driven work in mature repositories with 43 enterprise tasks and 750 expert-audited Code Points. Across 11 model and scaffold configurations, the best complete-delivery rate was 14.0 percent. Incomplete implementation and missing integration were the dominant failures. Individual components and passing isolated tests did not establish full delivery.

The evaluator reached 95.2 percent agreement with expert consensus. Successive harness revisions raised mean performance from 59.4 to 63.0 using the same model and task suite, which shows that requirement reconstruction and evidence presentation are controllable harness variables.

Why it matters:
- issue-level success can hide unimplemented business and integration obligations;
- acceptance criteria should be reconstructed into frozen, auditable units before the run;
- review capacity becomes the bottleneck when agent output volume grows faster than complete-delivery evidence.

Implementable now:
- decompose PRDs into atomic Code Points with allowed alternatives;
- bind each criterion to source, test, integration, or inspection evidence;
- report component completion, integration completion, and full-delivery rate separately;
- retain independent expert review for a sampled acceptance set.

Artifact caveat: the paper names `TianqiLiu1/PACE-Bench`, but that GitHub repository did not resolve during this scan. The benchmark method is usable; exact reproduction is blocked until the artifact becomes public.

Implementability score: 0.62

Core source: [When Coding Agents Outpace Review v1](https://arxiv.org/abs/2610.26394v1)

## Working conclusion

Agent evaluation should follow the evidence path from computation through exposure, compression, integration, and acceptance. A plausible answer or passing component is weak proof when the runtime cannot show which authoritative evidence survived and which obligations were actually delivered.
