# Strategy Weekly Sovereignty: 2026-11-07 to 2026-11-13

The strategic signal this week is that evidence should inform authority without becoming authority. Agent systems need explicit release boundaries for memory, recurring execution, generated interfaces, reviews, and actions derived from untrusted content.

## 1. Make provenance a first-class release input

GitHub's Copilot review APIs now expose explicit attribution, review effort, and reported skills, MCP servers, and custom instructions. The research findings on evidence-linked memory and delegated search show why this matters beyond code review: a result should carry enough provenance to reconstruct how it was produced and what evidence was omitted.

Why it matters: provenance makes review, rollback, and policy possible. A conclusion without source identity, tool path, exclusions, and model or workflow version is difficult to govern after the fact.

Implementable now:
- record actor, model, prompt or workflow version, tools, sources, and exclusions;
- bind approvals to an exact artifact digest and effect manifest;
- preserve failed retrievals and skipped files as evidence;
- use provenance fields as release-policy inputs rather than decorative metadata;
- retain human and machine review identities separately.

Implementability score: 0.91

Core sources: [GitHub Copilot code review API update](https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates/), [Evidence-Linked Memory v1](https://arxiv.org/abs/2611.14320v1), [Lost in Delegation v1](https://arxiv.org/abs/2611.16526v1)

## 2. Admit persistent memory through falsification gates

Falsification-Gated Self-Evolution treats each proposed lesson as a hypothesis with a precondition, behavior delta, expected effect, and verifier. It tests transfer, counterexamples, and archived regressions in temporary state before commit, refinement, or rejection. Anthropic's offline consolidation architecture and WikiTrace's source links provide complementary operational pieces.

Why it matters: a successful episode is evidence for a memory proposal, not permission to rewrite durable behavior. Memory promotion is a release process.

Implementable now:
- store candidate lessons outside active memory;
- require source links, typed preconditions, and expected effects;
- run transfer, falsification, and regression probes;
- bind promotion to exact test results and memory version;
- preserve rejected proposals as evidence without making them executable guidance.

The honest weakness is verifier quality. A weak oracle can approve a harmful lesson with a clean-looking receipt. Promotion should remain reversible and bounded even after tests pass.

Implementability score: 0.79

Core sources: [FGSE v1](https://arxiv.org/abs/2611.14326v1), [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory), [WikiTrace repository](https://github.com/yukyeongleee/wikitrace)

## 3. Render approvals through application-owned capability surfaces

A2UI 1.0 lets agents describe interfaces while host applications render registered native components and expose scoped functions. This is a useful authority boundary: the model can compose representation, while the application owns validation, accessible rendering, callable capabilities, and final action policy.

Why it matters: free-form generated UI can obscure exact effects or invent controls. Application-owned components let the user inspect structured values and bind mutation controls to stored action manifests.

Implementable now:
- begin with read-only cards, forms, and confirmation views;
- expose a small versioned component and function catalog;
- validate every message against protocol and application schemas;
- bind mutation controls to fresh state and one-shot approvals;
- record rendered values, user choice, invoked function, and observed outcome.

The protocol constrains representation. It does not authorize the underlying action. Product teams still own function scoping, policy, and receipts.

Implementability score: 0.91

Core sources: [A2UI 1.0 announcement](https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/), [A2UI repository](https://github.com/a2ui-project/a2ui), [A2UI documentation](https://a2ui.org/)

## 4. Separate triggers, evidence, and authority for recurring agents

Recurring agents combine three contracts that should remain distinct: when work starts, what it may do, and what proof it must retain. Prompt-injection research from the week reinforces the same boundary. Content can remain task-relevant while attempting to change values or authority. Source identity must therefore constrain how retrieved text can influence action.

Why it matters: a schedule or webhook should trigger evaluation, not grant broad authority. Retrieved content should be evidence, not policy. Approval should bind to the exact effect that will execute.

Implementable now:
- issue narrow, expiring capabilities per run;
- classify instructions by trusted source and allowed effect;
- keep untrusted content out of policy and tool-authorization channels;
- require fresh-state preconditions before mutation;
- emit trigger, authorization, action, and outcome receipts separately.

Implementability score: 0.82

Core sources: [A New Class of Prompt Injection Attacks v1](https://arxiv.org/abs/2611.07485v1), [Signed but Not Safe v1](https://arxiv.org/abs/2611.07483v1)

## Strategic conclusion

The strategic boundary is no longer text versus tools. It is evidence versus authority. Evidence can be messy, retrieved, generated, or delegated. Authority must be typed, scoped, versioned, and released through runtime-owned gates with receipts.
