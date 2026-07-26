# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Sunday, 2026-07-26

### Real-work agent benchmarks need isolated verifier authority

Summary: WorkBuddy Bench packages 260 tasks across Code, Web, Office, and Security. It separates agent-visible workspaces from post-episode grading and applies baseline and oracle admission gates. Adoption is constrained by a custom Tencent license and an EU-use limitation.

Analysis: [daily reasoning analysis](2026-07-26/reasoning.md#real-work-agent-benchmarks-need-isolated-verifier-authority)
Core sources: [paper](https://arxiv.org/abs/2607.20911v1), [repository](https://github.com/Tencent/workbuddy-bench), [dataset](https://huggingface.co/datasets/tencent/workbuddy-bench)
Implementable now:
- define isolated workspaces and post-episode graders;
- require baseline and oracle checks before admitting fixtures;
- pin model, harness, context, tools, image, and verifier;
- report domain scores without averaging incompatible instruments.
Tools, repositories, and methodologies:
- Harbor-style task directories, Docker, uv, deterministic rules, evidence-grounded judges, checksum manifests
Implementability score: 0.74

## Current implication

Realistic requests belong inside the evaluation fixture. Grader authority does not. Keep work and proof surfaces separate.
