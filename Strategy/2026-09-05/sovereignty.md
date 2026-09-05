# Strategy Daily Analysis - 2026-09-05

No new Saturday arXiv listing. These findings were submitted 2026-09-03 UTC and first listed Friday, 4 Sep 2026. They were not in yesterday's weekly synthesis.

## Termination is an authority decision, not a missing action

GUI agents that succeed on feasible tasks still execute blindly when the instruction is infeasible. ConflictGUI studies two conflict classes: instruction-internal conflicts, and instruction-GUI context conflicts. Vanilla agents' conflict success rate stays below 10% on average, with average False Execution above 70%. That is execution-biased overcompliance: the agent treats "do something" as the default authority, and "stop and report the conflict" as a missing skill.

ConflictGuard is an inference-time pair, not a new policy model. A feasibility verification protocol asks the agent to check instruction logic and GUI-side evidence before acting. Conditional action modulation then steers from over-compliant execution toward termination when either conflict-direction cosine exceeds a calibrated threshold. Across five agents, including Qwen3-VL, UI-TARS, and UI-Venus, the intervention raises conflict-task success while preserving feasible-task performance. The public repo contains extract/evaluate scripts, configs, and released steering vectors. The ConflictGUI dataset resolves on Hugging Face.

Why it matters: "know when not to act" is the GUI version of an effect gate. Overcompliance is not a UX bug. It is unauthorized execution under a conflicting user request or a stale screen. A runtime that cannot terminate with a named conflict will spend the user's session on the wrong app, the wrong object, or a fabricated path through the UI.

Fit in strategy: this belongs in untrusted data boundaries and the execution control plane. The user utterance and the current GUI state are two different authority objects. Feasibility is checked before the click, not after the damage.

Practical tools and methodologies worth exploring now:
- add an explicit terminate-with-conflict action to GUI and computer-use contracts;
- score False Execution on infeasible instructions separately from feasible success;
- keep a feasibility prompt even when steering vectors are unavailable;
- treat ConflictGUI's two conflict classes as fixture types: instruction-internal versus screen-state;
- do not let "the user asked" override a detected conflict without a confirmation path.

Artifact status: [serein356/ConflictGuard](https://github.com/serein356/ConflictGuard) resolves, Apache-2.0, populated `main`, last push 2026-09-04. [serein356/ConflictGUI](https://huggingface.co/datasets/serein356/ConflictGUI) resolves, public, ungated. Inspected read-only. Nothing was cloned or executed.

Evidence caveat: Conflict SR "below 10%" and FEX "above 70%" are vanilla averages from the v1 PDF. Table 1 numbers are two-column and were not fully recovered. Steering vectors are model-family specific. This is an inference-time control, not a hard broker.

Implementability score: 0.64

Core sources:
- [Do GUI Agents Know When Not to Act?, arXiv:2609.03438v1](https://arxiv.org/abs/2609.03438v1)
- [ConflictGuard repository](https://github.com/serein356/ConflictGuard)

## Owned session memory is a dataset with an admission hook

funes makes coding-agent memory an owned dataset instead of a vendor service. That is the sovereignty claim. Local Lance storage, pinned on-device embedding and reranking, original-text recall, and private-by-default Hub datasets are the right defaults. The hazard is the install path. `funes add hermes` writes tools and a hook that indexes every completed turn. After HookPry, that hook is a privileged control-plane object. Pin its command hash. Treat agent add and binary update as new admissions. Keep Hub publishing behind the redaction plus push-gate pair, and do not make a memory public by accident.

Why it matters: a shared memory dataset can follow Danny across Hermes, Codex, and Claude Code. It can also leak credentials, publish private traces, or run attacker-controlled hook updates. Ownership without admission is just a new persistence surface.

Fit in strategy: memory-authority control plane plus runtime governance. Traces remain evidence. Publication is a separate authorization. The hook is neither.

Practical tools and methodologies worth exploring now:
- start local-only; bind a Hub dataset only after the redaction gate is proven on a dummy corpus;
- keep dataset repos private by default;
- pin `funes` binary checksums from the release bucket, noting that checksum and binary share the same bucket so they do not authenticate the bucket;
- review the installed hook as a HookPry-class object before enabling it on Hermes;
- never let recall output become standing policy without a human or typed release.

Implementability score: 0.88 for local recall; 0.62 once the install hook is in scope.

Core sources:
- [Give Your Coding Agents a Memory You Own](https://huggingface.co/blog/funes)
- [huggingface/funes](https://github.com/huggingface/funes)
- [HookPry](https://arxiv.org/abs/2609.03884v1)

## Working conclusion

Infeasible instructions and owned memory look like product features. They are authority surfaces. A GUI agent that cannot terminate is executing without a gate. A memory installer that writes a hook is extending the trusted computing base. Check feasibility before the click. Admit the hook before the index.
