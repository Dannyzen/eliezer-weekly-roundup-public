# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-09

### Task-level policy is still ambient authority inside a multi-agent task

Summary: CapScope derives a task-wide authority ceiling before untrusted reads, stores typed capabilities outside model context, and attenuates them per sub-agent. Injected effects fell from 33/75 under the strongest global baseline to 3/75, while repair completion remained 68/75.

Analysis: [daily strategy](2026-09-09/sovereignty.md#authority-must-be-scoped-per-principal-not-per-task)
Core sources: [paper](https://arxiv.org/abs/2609.08371v1), [artifact](https://figshare.com/s/86184ed20f66d1f0cf91), [GitHub managed sandbox signal](https://github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains)
Tools and methodologies worth exploring now: trusted preflight ceilings, typed capability predicates, per-principal stores, delegation attenuation, dispatch hooks, reason-coded denial logs
Implementability score: 0.76

## Current implication

A task-level allowlist cannot safely govern delegated agents when different roles need different effects. Mint the maximum authority before untrusted reads, narrow it per principal, and enforce it outside the model.
