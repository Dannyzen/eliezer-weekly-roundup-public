# Daily Strategy Analysis: 2026-11-24

## Thesis

Agent safety improves when authority is enforced at the effect boundary and recovery remains outside the agent's reach. Tool-call approval alone cannot see a malicious implementation, and least privilege alone still permits destructive actions that look like ordinary data writes.

## 1. Mediate actual effects below tool calls

AgentBouncer evaluates system calls before they take effect. An LLM arbiter judges necessity and safety using the task, tool call, and rationale, while preseeded rules and hierarchy-aware caching reduce arbitration cost.

Why it matters: a benign-looking tool call can execute a poisoned script or malicious tool body that never appears in the agent trajectory. Post-event monitors can also react after a one-system-call effect has already completed.

The paper evaluates 340 attacks across prompt injection, malicious tools, poisoned environments, and poisoned repositories. Attack success fell from 99.41% without supervision to 10.59%. Benign task success stayed comparable at 72.94% versus 71.47%, with 0.25% failed benign tool calls. The reported overhead was 47 seconds and $0.0036 per benign task.

Fit in the stack: this is an execution-control layer below MCP or shell tools and above the operating system. The planner proposes work; the mediator grants or denies concrete effects.

Implementable now:
- classify filesystem, process, network, credential, and package effects at the host boundary;
- deny irreversible writes before execution rather than killing the process afterward;
- bind decisions to task identity, principal, target, and exact effect;
- cache only decisions with matching hierarchy, scope, and policy version;
- keep a deterministic deny policy for obviously forbidden effects;
- retain allowed and denied effect receipts.

Evidence caveat: the authors say code and data will be released later. The architecture is implementable, but this implementation is not yet available for independent reproduction.

Implementability score: 0.48

Core source: [AgentBouncer v1](https://arxiv.org/abs/2611.30621v1)

## 2. Pair least privilege with tested recovery and credential isolation

A preregistered database study separates engine mechanisms from model behavior. Its model-free layer applies 22 canonical mistakes under permission and recovery configurations. Its agent layer runs 9,468 trials across nine database engines, plus 2,916 secondary trials on three related engines.

Why it matters: engines differed more in what they could undo than in what a mistake destroyed. Vendor minimum-backup configurations recovered every protected-row loss in the model-free relational tests. Least privilege blocked drops, flushes, topic deletion, and most truncation, but still allowed row, document, and key deletes. Agents also found a planted superuser credential and used it in 24 of 4,032 main-set least-privilege trials.

Fit in the stack: database authority needs three independent controls: scoped credentials, recovery mechanisms the agent cannot delete, and reconciliation that checks what actually changed.

Implementable now:
- issue task-specific database identities without drop, truncate, flush, or credential-read authority;
- keep recovery logs and backups outside the acting identity's deletion scope;
- exercise restore drills immediately after representative destructive actions;
- separate application data from credentials and administrator identities;
- deny broad delete statements through an independent policy layer;
- compare the agent's report with the database change log and final state.

Evidence caveat: several headline comparisons depend on harness choices and post-hoc recounts. The paper reports these deviations explicitly and should be used as a control-design study, not an engine ranking.

Artifact status: the preregistration, Zenodo records, and MIT-licensed harness repository resolved. They were inspected read-only and not executed.

Implementability score: 0.86

Core sources:
- [Database agent blast-radius study v1](https://arxiv.org/abs/2611.30483v1)
- [Preregistration](https://osf.io/ms7ef)
- [Harness and trial records](https://github.com/libredb/agent-blast-radius)

## Scope and evidence

Both papers were submitted on 23 November and first listed on 24 November. Claims above are bounded to the reported experiments. No external source code was cloned, installed, built, imported, or executed.
