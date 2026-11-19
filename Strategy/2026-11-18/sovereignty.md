# Strategy Deep Dive: 2026-11-18

This week's strongest strategic finding is that natural-language policy can become a fast, attributable runtime verification layer. The Verifier Foundation Model makes hundreds of criteria operational without asking a large generative judge to reread the full trace for every rule.

## 1. Put a policy verifier between trace and authority

VFM encodes a shared agent context and target once, then evaluates each atomic natural-language criterion as an isolated tree-attention branch. It returns per-rule YES, NO, or N/A probabilities.

Why this won the week: the other strong findings improve one subsystem. ReTrace compiles repeated plans, HEAMS evaluates memory responsibilities, CapLite constrains prompt-injected writes, and Copilot Evals regression-tests capability changes. VFM defines a reusable runtime policy plane that can govern all of those systems.

Measured evidence:

- 0.885 trace-level FAIL F1 on 543 held-out DynaBench dialogues, compared with 0.720 for DynaGuard-4B;
- 97.6 percent top-one localization of the violated rule on failing traces;
- 0.946 FAIL F1 when the top three suspected rules were escalated to a 26B judge;
- 1.81 seconds and 10.5 GB VRAM to evaluate 1,000 criteria against a roughly 4,000-token trace on one H100.

Implementable now:

- define one canonical policy bundle as stable atomic questions;
- run VFM-0.6B or VFM-4B in shadow mode on retained traces;
- measure false passes, false blocks, N/A rates, latency, and localization by policy family;
- escalate uncertain and high-risk verdicts to a stronger judge or human;
- retain policy version, criterion IDs, checkpoint, thresholds, verdicts, final authority decision, and effect as one receipt.

The main weakness is material. On real insurance calls, finetuned 4B variants falsely passed 19 to 26 percent of gold violations, often confidently. The paper also says zero-shot verification remains poorly calibrated. VFM is ready for shadow triage and focused escalation. It is not ready to replace deterministic authorization for irreversible actions.

Artifact status: the immutable paper, public repository tree and README, model links, benchmark manifests, and tests were inspected read-only. No external code or model was executed.

Implementability score: 0.76

Deep dive: [Runtime policy verification](../runtime-policy-verification/runtime-policy-verification.md)

Core source: [Runtime Verification of Multiple Natural Language Criteria for Agent Governance](https://arxiv.org/abs/2611.23074v1)

Implementation source: [spitis/vfm](https://github.com/spitis/vfm)

## Working conclusion

Natural-language policy should become a versioned runtime object with per-rule verdicts and explicit escalation. The verifier can narrow attention and produce evidence. Deterministic execution control must still own final authority.
