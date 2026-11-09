# AgenticAI Daily Analysis: 2026-11-09

There is no new Monday arXiv listing yet. Today’s strongest implementation signals come from two public artifact releases: a verifier-trained small tool agent and an interaction-aware MoE pruning package.

## 1. Train exact workflows against executable verifiers

TaxOps turns a bounded professional workflow into six typed tools, a scripted oracle, exact field-level grading, and explicit waste metrics. The 3.35B Tiny Aya base model solved none of 60 initial cases and averaged 27.8 wasted calls. After supervised fine-tuning, the v6 adapter solved 93.3 percent of 300 held-out synthetic returns with 0.030 wasted calls per case. It reached 74.0 percent on a 150-case shifted set.

The useful lesson is the training shape. A failed v4 taught recovery after irrelevant reads and regressed. The stronger v6 changed the demonstrations so the corrected form was read first and the superseded form was skipped. That improved the decision policy without adding tool calls.

Why it matters: small tool agents become useful when the workflow has a deterministic oracle, typed actions, and measurable waste. More examples do not repair a bad demonstration policy.

Use now:
- compile the workflow into typed tools and an exact final-state verifier;
- generate scripted oracle trajectories before fine-tuning;
- score valid calls, wasted calls, field accuracy, tokens, and time separately;
- hold out shifted cases with unseen decoys and document layouts;
- review failure transitions before adding recovery demonstrations.

Caveat: this is a community-authored synthetic tax environment, not an independently replicated production tax system. The public repository, model, dataset, and replay Space resolve read-only, but none was executed in this scan.

Implementability score: 0.78

Core source: [TaxOps](https://huggingface.co/blog/Manoj2142/taxops-efficient-tool-agent)

Artifacts: [code](https://github.com/ydv-manoj/taxops-agent), [model](https://huggingface.co/Manoj2142/taxops-tinyaya-sft-v6), [data and traces](https://huggingface.co/datasets/Manoj2142/taxops-traces), [replay demo](https://huggingface.co/spaces/Manoj2142/taxops-replay)

## 2. Preserve expert cooperation when shrinking MoE models

HOPE replaces independent expert rankings with a pairwise interaction matrix. A single calibration pass records router weights, output norms, and co-activation statistics. A quadratic program then chooses the expert set whose removal minimizes a second-order pruning-error bound.

Across three MoE models, two calibration sets, and five pruning methods, HOPE had the best average rank. At 50 percent pruning its average rank was 1.58 versus 2.42 for REAP. On Qwen3.5-35B-A3B, the pruned model scored 42.3 on SWE-Bench Pro versus 41.8 unpruned and 36.2 with REAP.

Why it matters: the model-serving decision is not only which experts look individually weak. Agentic tasks exercise cooperative expert groups over long sequences. Independent pruning can remove a low-scoring expert that supports a high-value group.

Use now:
- calibrate on representative agent trajectories, not generic text alone;
- compare interaction-aware pruning with first-order baselines at the same pruning rate;
- retain the prune-set JSON as a versioned deployment artifact;
- run the target agent benchmark and general benchmarks before promotion;
- bind memory savings, latency, and task quality to the exact checkpoint.

Caveat: the paper was submitted in September. The new signal is Amazon’s November 9 implementation walkthrough. The repository is Apache-2.0 and populated, but has six commits, one star, no releases, and was not executed in this scan. The result requires large-model calibration infrastructure.

Implementability score: 0.58

Core source: [Amazon and Hugging Face implementation walkthrough](https://huggingface.co/blog/amazon/higher-order-pruning-experts)

Supporting sources: [paper v3](https://arxiv.org/abs/2609.18916v3), [public package](https://github.com/awslabs/HOPE)

## Working conclusion

Executable verifiers and interaction-aware calibration solve the same class of problem at different layers: preserve the structure that actually controls outcomes. Train small agents against exact effects, and compress large models against cooperative behavior rather than isolated scores.
