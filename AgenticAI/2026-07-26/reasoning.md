# AgenticAI Daily Analysis - 2026-07-26

## Verdict

A realistic benchmark should make agent work look like real work while keeping evaluation authority outside the agent-visible workspace. Tencent WorkBuddy Bench is useful because it combines role-played requests, heterogeneous deliverables, sandboxed execution, and post-episode verification. Its custom license and operating cost make it a methodology source before it is a default dependency.

## Scan boundary

- As of the 2026-07-26 12:18 UTC publication cutoff, arXiv's newest relevant category heading was Friday, 2026-07-24. This non-duplicate carry-forward was submitted on 2026-07-23.
- The primary PDF was downloaded as a document on Bigs and checked with `pdftotext -layout`.
- GitHub, Hugging Face, the project page, repository tree, and license were inspected read-only. No external repository was cloned or executed.
- `blogwatcher-cli` was unavailable; direct official pages and primary feeds covered discovery.

## Real-work agent benchmarks need isolated verifier authority

Core sources: [paper](https://arxiv.org/abs/2607.20911v1), [repository](https://github.com/Tencent/workbuddy-bench), [dataset](https://huggingface.co/datasets/tencent/workbuddy-bench)

Submission: 2026-07-23 04:34:06 UTC. First listed: 2026-07-24.

### What it found

WorkBuddy Bench packages 260 tasks across four work surfaces: 80 Code, 70 Web, 50 Office, and 60 Security. Tasks are reverse-engineered from commits, pull requests, CVEs, or business scenarios, then rewritten as colloquial requests rather than copied from searchable issue text.

Each task separates the agent-visible workspace from post-episode grading assets. Code uses hidden-at-solve-time tests, Web combines deterministic rules with LLM, VLM, and agent judges, Office combines rule checks with evidence-grounded semantic rubrics, and Security uses programmatic scoring. Code-task admission requires an unchanged baseline reward at or below 0.3 and an oracle reward of 1.0.

The public repository has a populated main branch with 173 tree entries, model and harness configuration, evaluation scripts, task skills, and dataset checksum handling. Hugging Face exposes four archives totaling about 363 MB and a `SHA256SUMS` manifest. The dataset viewer currently fails, so task contents were not inspected through the viewer.

### Why it matters

Organizations need a repeatable task format that binds a realistic request, isolated workspace, fixed harness, post-episode evidence, and domain-appropriate verifier. WorkBuddy Bench preserves that shape across code, web, office, and security without pretending the scores are directly comparable.

The weak point is adoption friction. The custom Tencent license says WorkBuddy Bench is not intended for use within the European Union. It also requires Python 3.12, uv, Docker, model credentials, dataset archives, and substantial execution budgets. Copy the methodology only after legal review.

### Fit in the stack

- **Harness evaluation:** keep task packaging stable while varying model and harness.
- **Artifact grading:** use domain-specific instruments for patches, pages, office files, state, and security effects.
- **Contamination control:** rewrite prompts from source artifacts and version public releases.
- **Release evidence:** keep graders outside the agent-visible environment until the episode ends.

### Implementable now

1. Define a local task directory with instruction, isolated workspace, resource limits, and post-episode grader.
2. Add baseline and oracle admission checks before a fixture enters the suite.
3. Build a small organization-owned set across code, web, office, and security.
4. Pin model, harness, context policy, tools, image, and verifier version.
5. Report per-domain scores, cost, turns, and failure types without averaging incompatible instruments.

Tools and methodologies: Harbor-style task directories, Docker, uv, deterministic rules, evidence-grounded judges, checksum manifests, dataset versioning.

Implementability score: **0.74**

The architecture is reusable now. The custom license, EU limitation, setup, and evaluation cost prevent a higher score.

## Working conclusion

Realistic requests belong inside the evaluation fixture. Grader authority does not. Separate the work surface from the proof surface.
