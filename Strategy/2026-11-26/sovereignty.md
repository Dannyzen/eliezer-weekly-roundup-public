# Daily Strategy Analysis: 2026-11-26

## Thesis

Agent outputs should become authority only after evidence-bearing verification, and human operator answers should be treated as claims to audit rather than unquestioned training truth.

## Agent-as-a-Verifier replaces scalar confidence with checkable certificates

Agent-as-a-Verifier decomposes a candidate result into a verdict-blind claim graph, independently compiles the task's acceptance contract, derives checkable obligations, and collects evidence into a certificate. It separates check proposal, execution, and evidence audit. The paper reports stronger best-of-N selection on Terminal-Bench 2.1, improvements when wrapped around the same agent on FrontierMath and CyberGym, and detection of reward-hacking solutions that fooled the benchmark evaluator.

Why it matters: a score can rank outputs while hiding why the result is safe to release. A certificate creates a reviewable object that can bind each acceptance condition to a check and its evidence.

Strategic fit: evidence provenance, release gates, verifier independence, and recursive improvement.

Practical tools and repositories worth exploring now:
- [General-Verifier](https://github.com/sunyxedu/General-Verifier), public Apache-2.0 repository, contents inspected read-only;
- compile acceptance criteria before inspecting the candidate's claimed success;
- isolate claim extraction, check generation, check execution, and evidence audit;
- preserve obligations and evidence as a release artifact;
- test the verifier against deliberately reward-hacking outputs.

Evidence and caveat: the implementation repository is public and populated, but this run did not clone or execute it. The results are paper-reported and need independent replay before operational adoption.

Implementability score: 0.74

Core source: [Agent-as-a-Verifier v1](https://arxiv.org/abs/2611.34132v1)

## Operator replies are evidence candidates, not gold labels

The customer-support study found that about a quarter of factual claims in operator replies lacked full support in the knowledge base and tool records available to the agent. The authors verify operator replies claim by claim. Supported claims become coverage targets for a GRPO reward, while unsupported claims identify knowledge-base or tool gaps instead of becoming imitation targets.

The reported offline hallucination flag rate fell from 13.6% for supervised fine-tuning to 8.6% for the claim-level GRPO agent. In a randomized online test with about 17,500 conversations per arm, the share closed without a human operator rose from 63.3% to 80.8% relative to the procedural bot.

Why it matters: human-written answers often contain tacit access, judgment, or unsupported detail. Copying them directly can train the agent to reproduce claims it cannot verify at runtime.

Strategic fit: training-data provenance, evidence-bound rewards, knowledge-gap management, and deployment evaluation.

Practical methods worth exploring now:
- split human answers into atomic factual claims;
- verify each claim against the exact knowledge and tool evidence available at answer time;
- use verified claims as coverage targets and unsupported claims as remediation tickets;
- measure precision and abstention separately from answer coverage;
- require controlled online evaluation because offline helpfulness did not reliably predict automation.

Evidence and caveat: the study covers one language and one customer-support setting. No public implementation artifact was identified, so the method is implementable from the paper but not ready for direct reuse.

Implementability score: 0.68

Core source: [Learning from Unreliable Operator References v1](https://arxiv.org/abs/2611.34341v1)
