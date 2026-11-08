# Strategy Daily Sovereignty: 2026-11-08

No new arXiv listing appeared on Sunday. These Friday carry-forwards show two authority failures that ordinary prompt-injection tests miss: untrusted content can alter values without changing the task, and a signed handoff can protect an incomplete requirement set.

## 1. Define prompt injection by source authority

Beyond Instruction Override introduces 90 validated cases across productivity, DevOps, and marketplace environments, with 1,343 single-primitive attacks plus compound attacks. The attacks keep the benign task intact while changing a decision input such as a rule, available action, expected consequence, observation meaning, or world state.

This matters because defenses tuned for obvious instruction override can miss value tampering. A detection-and-removal defense reduced objective-targeting attack success to 2.4 percent, while observation- and state-targeting attacks remained at 9.5 and 12.1 percent. A tool-policy defense allowed 15.4 percent success versus 17.0 percent without a defense because the attacks used expected tools and manipulated values obtained during execution.

Strategic fit: untrusted-data boundaries, tool-argument provenance, and effect authorization.

Implementable now:
- define which source may determine each consequential value;
- test false rules, false state, false observation semantics, and false consequences, not only malicious instructions;
- trace critical tool arguments back to authorized evidence fields;
- grade legitimate task completion and unauthorized effect separately;
- mutation-test defenses with wording that looks like ordinary evidence.

Artifact status: the public Amazon Science repository resolves and its metadata and README location were inspected read-only. No external source was cloned or executed.

Implementability score: 0.82

Core sources:
- [Beyond Instruction Override](https://arxiv.org/abs/2611.07640v1)
- [task-tampering-prompt-injection](https://github.com/amazon-science/task-tampering-prompt-injection)

## 2. Sign requirements after source-bound extraction

Signed but Not Safe compares free-text summaries, structured JSON, and signed requirement manifests. The manifest carries each requirement as a verbatim source quote plus a checkable predicate. Trusted code validates provenance, canonicalizes and signs the JSON, and checks the final decision deterministically.

Across 1,440 Qwen3-8B trajectories and five threats, signed manifests reduced unsafe commits under attack from 69.4 percent to 9.0 percent. A deterministic verifier caught 78.7 percent of violating decisions with 7 percent false alarms, versus 59.0 percent caught and 50 percent false alarms for an LLM checker. An oracle manifest removed the remaining unsafe commits, showing that residual risk came from extraction errors before signing.

The result is precise: signatures protect transit integrity. They do not prove that the signed object contains every real requirement or interprets it correctly.

Strategic fit: multi-agent handoffs, context-to-execution integrity, deterministic release gates, and provenance.

Implementable now:
- extract each mandatory requirement with a literal source quote and typed predicate;
- reject requirements whose quoted evidence is absent from the authenticated request;
- sign canonical manifests outside model access;
- verify every final effect against the manifest in code;
- fail closed on mismatch and audit pre-signing extraction separately.

Evidence caveat: the primary tasks are synthetic and exactly scorable. Code, task banks, freeze manifests, and run logs are available from the authors on request, not through a verified public artifact.

Implementability score: 0.76

Core source: [Signed but Not Safe](https://arxiv.org/abs/2611.07483v1)

## Strategic conclusion

Authority must stay attached to both the source and the decision variable it controls. Signed bytes and safe-looking tool calls are useful only after source-bound requirements and values have been extracted correctly.
