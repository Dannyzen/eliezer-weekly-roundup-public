# Strategy Daily Sovereignty, 2026-07-31

## Verdict

System prompts are policy-bearing runtime artifacts, not trusted prose. AISPA's useful contribution is a reviewable assurance taxonomy, but the public corpus also proves that provenance and reviewer identity must remain attached to every audit result.

## Scan boundary

AISPA was submitted as v1 on Thursday, 2026-07-30 and first listed on Friday, 2026-07-31. The PDF, public System Prompt Index, and GitHub repository were inspected read-only. The repository was created on July 31 and contains prompt and audit data, but GitHub reports no license. No external source code was cloned, installed, built, imported, or executed.

## AISPA makes system prompts auditable governance artifacts

### What it found

AISPA defines eight user-centered dimensions for auditing system-prompt spans: identity transparency, truthfulness, privacy, action safety, user agency, unsafe-request handling, harm prevention, and fairness. The paper reviews 3,249 instructions from 88 commercial products. It reports that 98.9 percent include at least one protective instruction, only about 24 percent cover all eight dimensions, and roughly 40 percent contain at least one instruction that works against user interests.

The public System Prompt Index expands the corpus to 1,017 prompts with span-level audit records. The current repository intentionally drops fields that distinguished automated from human-reviewed findings. Its own commit history states that readers can no longer determine which records had a human reviewer. The site also warns that included prompts may not be authentic, current, or officially released.

### Why it matters

A hidden system prompt can encode identity concealment, manipulation, unsafe action defaults, or incentives that conflict with user interests. Model-level safety does not neutralize application-level policy. Prompts therefore need the same versioning, provenance, review, testing, and release discipline as code and policy files.

The corpus caveat is equally important. An audit verdict without source authenticity, prompt version, reviewer class, and methodology version is evidence without enough lineage to govern a release.

### Fit in the stack

Primary layer: runtime governance and policy assurance.

The system prompt sits above the model but below user-visible behavior. It should be compiled into reviewable claims and tested against runtime traces. AISPA is an audit taxonomy, not an enforcement mechanism.

### Implementable now

- store every system prompt as a versioned artifact with source, product, model, date, digest, and approval identity;
- audit exact spans against the eight AISPA dimensions and preserve reviewer class and confidence locally;
- connect each claimed protection to a behavioral regression test and each problematic instruction to a release blocker or documented exception;
- diff prompt versions semantically before deployment and invalidate approval when protected claims change;
- keep proprietary prompts private while publishing aggregate assurance claims and evidence methodology where appropriate.

Tools, repositories, and methodologies:
- AISPA taxonomy, System Prompt Index, Git diffs, policy-as-code review, prompt manifests, behavioral regression suites, provenance receipts, independent review

Implementability score: 0.80

Artifact status: the public repository is populated with 1,017 prompts and audit records and the website exposes the paper's aggregate findings. It has no declared GitHub license. Authenticity and freshness are not guaranteed, and the latest export removes reviewer-source fields, so the expanded corpus is best treated as discovery data rather than ground truth.

Sources:
- [AISPA paper](https://arxiv.org/abs/2607.28617v1)
- [System Prompt Index](https://systempromptindex.com/)
- [System Prompt Index repository](https://github.com/XiangningLin/SystemPromptIndex)

## Adjacent control surfaces from today's scan

Three implementation findings reinforce the same strategy:

- AgentRadio shows that cross-agent messages need thread, sender, recipient, evidence, and delivery receipts before they can redirect work.
- Change2Task shows that benchmark tasks need provenance, frozen state, executable checks, and restoration evidence.
- OSReward shows that model judges are not neutral oracles and systematically over-accept persuasive failed runs.

Sources:
- [AgentRadio](https://arxiv.org/abs/2607.28430v1)
- [Change2Task](https://arxiv.org/abs/2607.28591v1)
- [OSReward](https://arxiv.org/abs/2607.28609v1)

## Working conclusion

> Treat prompts, messages, tasks, and judge verdicts as versioned evidence objects. Their prose may guide a model, but only provenance, tests, and independent gates can grant authority.
