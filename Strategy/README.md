# Strategy

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-02

### Ambient audio cannot carry execution authority by itself

Summary: AudioAgentSecurity reports high concurrent audio-injection success across eleven multimodal agents and shows that acoustic source separation plus cross-modal verification can materially reduce the attack. The governance lesson is broader than one defense: perceived speech is evidence, not authenticated intent.

Analysis: [daily sovereignty](2026-08-02/sovereignty.md#audio-is-untrusted-content-not-user-authority)
Core sources: [paper](https://arxiv.org/abs/2607.28165v1), [public repository](https://github.com/Limax666/AudioAgentSecurity), [gated dataset](https://huggingface.co/datasets/Limax11/AudioAgentSecurity)
Implementable now:
- label audio source, timing, overlap, and confidence;
- quarantine source-inconsistent instructions;
- require trusted-channel confirmation for high-impact tools;
- bind accepted intent to exact effects and expiry.
Tools, repositories, and methodologies:
- AudioAgentSecurity, source separation, speaker attribution, cross-modal consistency, action manifests
Implementability score: 0.64

## Current implication

Multimodal perception must remain below the authority boundary. An agent may hear an instruction, but a separately authenticated channel must grant permission for consequential effects.
