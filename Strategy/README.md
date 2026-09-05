# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-05

### Termination is an authority decision, not a missing action

Summary: Vanilla GUI agents stay below 10% conflict success and above 70% False Execution on infeasible instructions. ConflictGuard adds a feasibility check plus conditional steering toward termination, while preserving feasible-task performance.

Analysis: [daily strategy](2026-09-05/sovereignty.md#termination-is-an-authority-decision-not-a-missing-action)
Core sources: [paper](https://arxiv.org/abs/2609.03438v1), [ConflictGuard](https://github.com/serein356/ConflictGuard)
Tools and methodologies worth exploring now: terminate-with-conflict actions, False Execution metrics, instruction-internal versus screen-state fixtures, confirmation before overriding a detected conflict
Implementability score: 0.64

### Owned session memory is a dataset with an admission hook

Summary: funes makes coding-agent memory an owned local dataset that can follow Hermes, Codex, and Claude Code. The sovereignty win is on-device recall and private-by-default Hub datasets. The hazard is the install hook, which is a HookPry-class admission object.

Analysis: [daily strategy](2026-09-05/sovereignty.md#owned-session-memory-is-a-dataset-with-an-admission-hook)
Core sources: [blog](https://huggingface.co/blog/funes), [huggingface/funes](https://github.com/huggingface/funes)
Tools and methodologies worth exploring now: local-only first, private Hub datasets, binary checksum pins, hook-hash admission, redaction plus push gates
Implementability score: 0.88 local recall, 0.62 with the install hook in scope

## Current implication

A GUI agent that cannot stop is executing without a gate. A memory installer that writes a hook is extending the trusted computing base. Feasibility is checked before the click. The hook is admitted before the index.
