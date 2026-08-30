# Strategy Daily Analysis - 2026-08-29

## Scope note

arXiv had no new Saturday listing. The newest complete sections were Friday, August 28, and both selected papers were submitted on August 27 and first listed on August 28. The scan covered seven relevant arXiv categories plus Hugging Face, GitHub Changelog, OpenAI, and Anthropic primary sources. The findings below were selected because they change authorization and containment design, not because they merely add another agent benchmark.

External code was not cloned, installed, built, imported, or executed. NotebookLM remained disabled.

## Treat user policy as preference input, not standing authorization

### Finding

[Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach?](https://arxiv.org/abs/2608.27443v1) compared three permission designs with 113 participants without professional software backgrounds: per-action human approval, automated model review, and user-authored `allow`, `ask`, or `never` rules over plain-language consequence categories.

Participants supervised an 18-action simulated day containing seven overreach actions. User-authored policy blocked 20.1 percentage points less overreach than per-action approval and 14.5 points less than automated review. Runtime prompts fell from 18.0 to 10.9, but total intervention time was not reliably lower once rule setup was included. Participants selected `ask` for 114 of 140 rules. Of 148 overreach actions executed in the policy condition, 133 followed human approval and 15 ran under `allow`.

### Why it matters

A reusable policy can reduce prompts without settling authority. Users often encode uncertainty as `ask`, then approve actions at runtime that exceed the original request. The security failure is not only bad rule syntax. It is the collapse of three different objects into one:

- preference: what the user generally likes;
- policy: what classes of action are normally allowed, denied, or escalated;
- authorization: permission for one exact effect under current evidence.

A runtime should preserve all three and never treat preference or an old `ask` choice as a durable grant.

### Strategy fit

This extends authority manifests and stateful effect governance. Standing policy should narrow the decision surface, but consequential effects still need exact action identity, current scope, destination, amount or resource, evidence, and terminal closure. Permission UX also needs overreach fixtures, not only satisfaction or prompt-count metrics.

### Practical path now

- Keep `allow`, `ask`, and `never` policies typed and versioned by consequence category.
- Bind `allow` to explicit limits such as destination, data class, amount, resource, and time.
- Treat `ask` as no authorization until an exact-effect manifest is approved.
- Show the delta from the user's original request at approval time.
- Test permission UX with required actions and plausible overreach actions together.
- Measure blocked overreach, completed required work, prompts, total intervention time, and approval reversals.

The study is a simulated day rather than production deployment, and the participant population was intentionally non-professional. It is strong evidence about permission UX, not a universal estimate of real-world compromise.

Implementability score: 0.84

Core source: [paper](https://arxiv.org/abs/2608.27443v1)

## Constrain destinations and capabilities instead of asking the model to recognize injection

### Finding

[The Framing Gap](https://arxiv.org/abs/2608.27092v1) tested indirect prompt injection in a synthetic lab with a canary secret, mock tools, and matched clean-versus-poisoned tasks. Across six models, ten overt injection classes were refused, yet reframing the same exfiltration as an integrity signature, configuration field, or trusted-looking host drove GPT-4o from 0 percent to 100 percent on the strongest wordings.

Three paraphrases of a known framing produced about 96 percent success, while authoring a fresh page around a new mechanism failed in 0 of 130 attempts. The reusable attacker asset was the framing template. A closed destination allowlist and a capability-isolating planner/reader split each reduced attack success to 0 percent in the reported setup. A broad confidentiality clause also reached 0 percent but reopened to 48.8 percent when the catch-all wording was removed. SecAlign remained at 32.5 percent, channel separation at 38.8 percent, and an output normalizer failed against a held-out ROT13 encoding at 100 percent.

### Why it matters

Prompt-injection defense fails when the model that reads untrusted content also holds the capability to send secrets. Recognition-based guards must understand every future framing. Payload-blind controls only need to enforce where data may go and which component can cause the effect.

The architecture should therefore constrain capability before interpretation:

1. A reader can inspect untrusted content but cannot transmit sensitive data.
2. A planner receives structured observations, not raw attacker instructions.
3. An effect executor accepts typed actions only.
4. Destination and capability allowlists are enforced outside the model.
5. Unknown destinations or mixed-trust payloads fail closed.

### Strategy fit

This belongs in untrusted-data boundaries, execution control, and gateway governance. Content classification may add defense in depth, but it should not be the authority plane. The invariant is structural: untrusted data cannot acquire an outbound capability merely because the model describes it as required.

### Practical path now

- Split browser or document reading from email, HTTP, payment, and file-write capabilities.
- Pass source-labeled facts or candidate actions across the split, not raw executable instructions.
- Enforce destination allowlists and data-class rules in the gateway.
- Use canary secrets and matched clean-versus-poisoned fixtures in regression tests.
- Test paraphrase families and held-out encodings, not only overt jailbreak text.

The experiment used synthetic tasks, mock tools, and a canary secret. The exact rates are model- and harness-specific, but the capability-separation result is directly actionable.

Implementability score: 0.91

Core source: [paper](https://arxiv.org/abs/2608.27092v1)
