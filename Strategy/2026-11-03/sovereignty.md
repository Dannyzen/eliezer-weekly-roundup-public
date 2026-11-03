# Strategy Daily Analysis: 2026-11-03

## Scope

Three November 3 arXiv listings converge on one control-plane claim: prompts and protocol conventions do not enforce policy. The runtime must preserve rules through compaction, distrust tool metadata and output, and own destructive-action approval at the host boundary.

## 1. Keep operating rules outside lossy compaction and test their use after summarization

ARCBench evaluates rule compliance inside the open-source pi agent harness rather than scoring isolated model answers. Its central result is sharper than simple rule loss: compaction rarely deletes the rule, yet compacted runs that retain it violate more than twice as often as full-history runs. The strongest compactor-targeted attack more than doubles violations, while the strongest defense restores the rule in most summaries and still leaves violations.

Why it matters: preserving policy text is insufficient. A later request can be interpreted as permission even when the compacted rule remains visible. Compaction therefore needs two controls: typed, source-linked rule retention and an external action gate that rechecks the current rule before an effect.

Implement now:
- store governing rules as typed policy state outside conversation summaries;
- preserve source identity and rule version through compaction;
- run production compactor fixtures with later conflicting requests;
- separate rule-retention scoring from action-compliance scoring;
- reauthorize consequential actions against current policy after compaction.

Evidence limit: the evaluation targets specific harness, model, compactor, and prompt configurations. The public repository includes the harness and reproduction scripts, but the paper's study rows are not included. Reproduction requires model access.

Artifact status: the public repository has a populated main branch with 175 files, benchmark cases, metrics, scripts, tests, a pinned agent dependency, and reproduction guidance. It was inspected read-only and not executed.

Implementability score: 0.84

Core sources:
- [ARCBench paper v1](https://arxiv.org/abs/2611.03223v1)
- [ARCBench repository](https://github.com/VUAISec/ARCBench)

## 2. Treat every MCP field as untrusted input and verify actual effects

MCP Tool Poisoning in Agentic AI Frameworks measures real execution across a 9,720-cell matrix covering 12 frameworks, 18 models, and 45 attack scenarios. It reports 2,113 vulnerable cells, a 22.9% overall attack-success rate. The evidence tiers include dispatched attacker calls, confirmed network contact, and verified secret exfiltration. The authors manually validated 1,259 transcripts.

The security result is architectural: nine core frameworks clustered between 23% and 26% attack success, with no statistically distinguishable framework effect and no intentional tool-poisoning defense found in the audited framework code. Model refusals provided most observed resistance. A description scanner rejected 20 of 45 scenarios with a 7.2% false-positive rate, which supports layered admission screening but not scanner-only trust.

Implement now:
- treat tool descriptions, schema fields, names, and responses as untrusted data;
- pin server identity, metadata digest, tool catalog, and permissions at admission;
- scan metadata before model exposure and preserve false-positive measurements;
- run canary-backed effect tests in a sandbox, not prompt-only compliance checks;
- block network and secret access by default at the server process boundary.

Evidence limit: the study is vendor-authored, evaluates a finite framework and model matrix, and uses a restricted distribution license for its artifact. Results support preflight and containment gates, not a claim that one scanner closes the problem.

Artifact status: the public repository has a populated main branch with frozen result data, 12 framework harnesses, 45 scenarios, analysis scripts, canary oracles, dependency freezes, and reproduction instructions. It was inspected read-only and not executed.

Implementability score: 0.82

Core sources:
- [MCP Tool Poisoning paper v1](https://arxiv.org/abs/2611.03555v1)
- [mcpvenom read-only repository](https://github.com/dynatrace-research/mcpvenom)

## 3. Make the host own destructive approval and fail closed when confirmation cannot run

When Neither Side Confirms measures both halves of MCP approval. In a 1,000-repository sample from the official MCP registry, an estimated 90% of destructive tools, with a 95% confidence interval of 82% to 95%, had no server-side confirmation. Of 41 popular open-source hosts and agent SDKs, 32 had no approval step by default, including 16 of 25 applications. Pairing destructive tools with applications left 60.7% of combinations without enforced approval.

The action evidence is direct: through four agent SDKs, four of five low-cost models executed an injected deletion in 479 of 960 runs. Host-side prompting for every tool not explicitly trusted as read-only or non-destructive would reduce the unapproved share to 5.4%. Universal elicitation support alone would leave 56.7%, because many servers never ask.

Why it matters: the server cannot know whether the host prompted, and the host cannot assume the server will ask. The effect-bearing host must own the final gate. Server elicitation is useful evidence, not the sole approval mechanism.

Implement now:
- classify every tool as trusted read-only, bounded write, destructive, or unknown;
- prompt at the host for destructive and unknown tools;
- bind approval to principal, tool, arguments, target, state, and expiry;
- refuse when elicitation or approval transport is unavailable;
- recheck mutable preconditions immediately before dispatch;
- issue a durable receipt after the effect.

Evidence limit: the study relies on a rule-based extractor and source-coded defaults across changing projects. Its application matrix is broad but remains a sampled snapshot. No paper-owned implementation repository was identified.

Implementability score: 0.90

Core source: [When Neither Side Confirms paper v1](https://arxiv.org/abs/2611.02527v1)

## Strategic cut

Use one host-owned effect gate after every context and tool boundary. The gate receives typed policy state, untrusted tool metadata, exact proposed arguments, current target state, and a scoped human grant. Missing confirmation must produce refusal, never an optimistic dispatch.
