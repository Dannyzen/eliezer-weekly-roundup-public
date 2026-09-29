# Strategy Daily Analysis - 2026-09-27

No new arXiv listing today. These leftover Friday papers and Friday GitHub product notes were not promoted in the 2026-09-25 synthesis or the 2026-09-26 leftover scan.

## Treat leftover context as a secret store

PrivDrift audits whether a user-disclosed secret remains recoverable after the conversation drifts to unrelated topics and a later probe tries to extract it. The benchmark contains 1,000 controlled multi-turn dialogues with seeded secrets, content-dense drift turns, and standardized extraction probes. Across three long-context models, dialogue-level hybrid leakage stays between 38.7% and 54.6%. Additional drift inside the tested window does not reliably reduce leakage. Secret type and persuasion intensity move the rate more than elapsed topic shift.

The paper frames this as a persistent behavioral failure in the active context, not as training-data memorization and not as an immediate jailbreak. No public implementation repository resolved from the HTML or PDF surfaces.

### Why it matters

Family-scoped memory from 2026-09-26 answers who may retrieve a certified skill. PrivDrift answers a prior question: the live transcript itself is already a secret store. Compaction, topic change, and "we moved on" do not erase it.

### How it fits

This belongs in untrusted data boundaries, memory authority, and gateway governance. It extends Saturday's endpoint-credential finding from files on disk to secrets that never left the session.

### Practical tools and methodologies

- Redact or vault secrets at disclosure time, then keep only a handle in the model context.
- Add post-drift extraction probes to session evaluations: seed a secret, insert content-dense unrelated turns, then ask with increasing persuasion.
- Score leakage by secret type. Format-heavy identifiers leak more readily than a generic confidentiality rule would predict.
- Do not treat unused-memory TTL as a substitute for active-context suppression. GitHub Copilot Memory deletes unused facts after 28 days; that timer does not cover the current transcript.

Artifact status: methodology-only. No public code URL resolved.

Implementability score: 0.74

Core source: [PrivDrift](https://arxiv.org/abs/2609.30094v1)

## Bound shared agent memory before it teaches the next fixer

GitHub's 25 September changelog states that agentic autofix now reads Copilot Memory when generating a security fix and writes the resulting fix pattern back as a memory. Official docs say Copilot Memory is in public preview and is used by Copilot cloud agent, Copilot code review, Copilot CLI, and agentic autofix. Repository-level facts carry citations and are re-checked against the current branch before use. Unused entries can be deleted after 28 days. Facts captured by one feature can be consumed by another.

The same Friday changelog adds an in-product validator for enterprise managed Copilot settings. It flags malformed JSON, unsupported configurations, and invalid team mappings in `copilot/managed-settings.json`, `copilot/team-mappings.json`, and referenced team files inside the `.github-private` repository. Fixes must land on the default branch before the Agents page will treat the policy as valid.

### Why it matters

A security-fix pattern that lands in shared repository memory becomes standing instruction for review and cloud agents. That is useful if the pattern is correct and still true of the branch. It is a silent authority expansion if the pattern is wrong, stale, or learned from a closed pull request.

### How it fits

This is memory authority plus runtime governance. Saturday scoped certified skills by family. Today the product surface is a shared, citation-backed memory that can write itself during autofix.

### Practical tools and methodologies

- Enable Copilot Memory only after an admin policy, then review repository-level facts the way you review custom instructions.
- Require citation validation against the current branch before a stored fix pattern can fire.
- Keep user-level preferences out of code review, matching GitHub's own split.
- Run the in-product validator on `copilot/managed-settings.json` after every policy commit, and fail closed on invalid JSON rather than shipping an unenforced control.

Evidence caveat: both features are public preview. The changelog does not publish false-positive rates for stored fix patterns.

Implementability score: 0.86

Core sources:

- [Agentic autofix now uses Copilot Memory](https://github.blog/changelog/2026-09-25-agentic-autofix-now-uses-copilot-memory/)
- [About GitHub Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)
- [Enterprise managed settings in-product validator](https://github.blog/changelog/2026-09-25-enterprise-managed-settings-in-product-validator/)
