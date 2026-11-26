# Daily Strategy Analysis: 2026-11-25

## Thesis

Authorization must preserve authorship and ownership across transformations. A compacted summary is model-written context, and a delegated permission answer is decision authority, neither is authenticated user intent or policy-administration authority.

## 1. Carry authenticated user intent across context compaction

`LLM Agent Authorization Across Context Compaction` shows that request-derived authorizers can lose their attribution guarantee when a harness replaces old turns with a model-written summary and places that summary in the user-message slot. The authorizer then derives permissions from text that may mix user requests, third-party data, and unresolved injected instructions.

Why it matters: in the paper's banking scenario, policy derived from a frontier compactor's summary admitted an attacker-specified account in 91% of cases. Policy derived from the user's original words admitted it in none. A summary can therefore preserve task continuity while silently changing who appears to have authorized an effect.

The proposed repair authenticates user text on arrival and carries it verbatim across compaction for authorization, while the acting model still reads the summary. In 40 attacked AgentDojo episodes rerun with the gate, no attacker action completed.

Fit in the stack: compaction is a representation boundary. The context used for reasoning can be lossy and model-written. The authority input must remain source-authenticated, immutable, and separately addressable.

Implementable now:
- assign immutable IDs and authorship labels to inbound user messages;
- derive grants from authenticated user text, never from a summary occupying a user role;
- carry a committed ordered list of authority-bearing messages across compaction;
- let summaries inform planning without granting permissions;
- fail closed when the authority witness is incomplete or inconsistent;
- retain the source text, grant, compaction identity, and effect receipt together.

Artifact status: the anonymous snapshot contains the gate and experiment scripts, but omits recorded outputs and requires third-party dependencies, provider access, and specified agent versions for reruns. It was inspected read-only.

Implementability score: 0.72

Durable deep dive: [Authenticated authority across context compaction](../context-compaction-provenance/context-compaction-provenance.md#november-25-2026-deep-dive-authenticated-authority-across-context-compaction). It explains the text-only impossibility result, dual reasoning and authorization views, the witnessed-request gate, implementation complexity, and the unresolved problem of authority delegated through external documents.

Core sources:
- [LLM Agent Authorization Across Context Compaction v1](https://arxiv.org/abs/2611.32194v1)
- [Read-only artifact snapshot](https://anonymous.4open.science/r/LLM-Agent-Authorization-Across-Context-Compaction-504E/)

## 2. Separate permission decisions from policy administration

`When Answering Is Administering` examines permission systems where a remote service, plugin, mobile client, or model can answer an approval prompt and attach persistent policy updates. The delegated party may be allowed to approve one command yet still delete a deny rule that governs later commands and sessions.

Why it matters: the paper finds that an answer to one permission prompt can rewrite the policy used for every later decision. In the demonstrated Claude Code path, deleting a deny rule could expose protected files in the current and later sessions even under the strict sandbox. The authors model 13 permission designs across 10 agent systems and survey 2,227 fetched marketplace plugins, finding two that send policy updates.

The control rule is source ownership. Without rule authorship, an update may only preserve every currently denied call. With authorship, a party may remove only restrictions that party previously created.

Fit in the stack: an approval response is a bounded decision object. Persistent policy mutation is a separate administrative capability with its own principal, scope, and receipt.

Implementable now:
- split one-shot allow or deny responses from policy-update payloads;
- reject updates that widen authority beyond the approved call;
- attach owner identity and provenance to every rule;
- permit a principal to remove only rules it owns;
- compare the pre-update and post-update denied sets before persistence;
- record the answer, update, principal, policy diff, and later effects.

Artifact status: the anonymous reproduction snapshot maps experiments to reported tables and includes isolated-home drivers and local scripted-model runs. Vendor binaries, third-party source trees, and one coordinated-disclosure client are excluded. It was inspected read-only.

Implementability score: 0.82

Core sources:
- [When Answering Is Administering v1](https://arxiv.org/abs/2611.32195v1)
- [Read-only reproduction snapshot](https://anonymous.4open.science/r/-When-Answering-Is-Administering-Permission-Replies-That-Rewrite-Coding-Agent-Policy-E5B0/)

## Scope and evidence

Both papers were submitted on 24 November and first listed on 25 November in cs.CR. Their artifacts resolved and were inspected read-only. No external source code was cloned, installed, built, imported, or executed.
