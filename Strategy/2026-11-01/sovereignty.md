# Strategy Daily Sovereignty: 2026-11-01

## Scope

There is no Sunday arXiv listing. These are unreported papers from the Friday, October 30 listing, submitted October 28 or 29. External artifacts were inspected read-only only.

## 1. Treat repository instruction files as untrusted policy-bearing input

Security Impact of Coding Agent's Memory Files tests whether malicious project guidance such as `CLAUDE.md` can steer coding agents toward vulnerable implementations without changing the developer's prompt. Across 12 CWE classes, 36 SecRepoBench tasks, and three agent configurations, malicious files changed secure-completion rates by minus 8 to plus 6 percentage points with no consistent pattern across agents or instruction variants.

The important result is the control gap. Claude Code named the file in about two thirds of final messages, while OpenCode mentioned it mostly in hidden reasoning. Agents that recognized the file as an attack still generated vulnerable code. Disclosure and self-awareness are weak controls.

Why it matters: repository instructions are executable context. A pull request can change them, and the model may treat the change as trusted project authority before a developer notices it.

Fit in the strategy: untrusted-data boundaries, coding-agent control planes, provenance, and release governance.

Implementable now:
- protect agent instruction files with CODEOWNERS and branch rules;
- show instruction-file diffs as a separate review surface;
- record source commit, path, author, and trust class in the run manifest;
- block instruction files from increasing tool or write authority;
- run security regression fixtures when instruction files change;
- treat model disclosure as advisory evidence, never as authorization or proof of safety.

Evidence caveat: this is a small empirical study with 36 tasks and heterogeneous agent behavior. It establishes a real attack surface, not a production prevalence estimate.

Implementability score: 0.90

Core source: https://arxiv.org/abs/2610.38521v1

## 2. Keep behavioral probes advisory and enforce secrets at the release boundary

Pre-Crime for Agents studies whether a monitor can detect a recruited agent just before it reveals a secret. In six controlled workplace scenarios, a peer pressures a target for up to 20 rounds. On held-out Qwen3-32B episodes, a linear activation probe catches 82% of leaking calls at a threshold that flags 5% of benign calls. A zero-shot decision monitor catches 26% at a similar rate. On gpt-oss-20b, a reasoning probe reaches AUROC 0.91.

The limitations control the strategy. A trained bag-of-words classifier comes close to the activation probe, the probe also flags permitted disclosures, warnings are short-range, and halting on any alarm stops most benign episodes. The signal predicts disclosure more reliably than policy violation.

Why it matters: learned monitors can provide a useful late warning, but they do not know whether the disclosure is authorized. Deterministic release policy still needs to bind the secret, recipient, purpose, channel, and workflow state.

Fit in the strategy: runtime governance, multi-agent containment, secret release, and observability.

Implementable now:
- enforce secret release with exact recipient and purpose grants;
- use trained text classifiers as a cheap shadow-warning baseline;
- test open-weight activation probes only after the text baseline;
- calibrate permitted and prohibited disclosure twins;
- pause or escalate on a warning, then decide with external policy;
- preserve peer pressure, model state, proposed output, and final disposition as one trace.

Artifact status: the MIT repository contains prompts, transcripts, results, and analysis code and was inspected read-only. The paper is single-author and the benchmark is controlled.

Implementability score: 0.38

Core sources:
- https://arxiv.org/abs/2610.40588v1
- https://github.com/leonidas1712/precrime-agents

## Daily conclusion

Context and behavioral signals can inform control, but neither grants authority. Protect instruction files before they enter context, and enforce secret release with external, typed policy after the model proposes an action.
