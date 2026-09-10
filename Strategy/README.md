# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-10

### Ownership and local integrity need different evidence channels

Summary: TrajMark uses a robust owner layer and fragile local seals instead of asking one global watermark to prove both producer identity and local integrity. It reports exact owner recovery on all clean evaluated batches, 95.5% to 100% detection under eligible single-site attacks, and 95.8% protocol-region localization under random single-action corruption.

Analysis: [daily analysis](2026-09-10/sovereignty.md#ownership-and-local-integrity-need-different-evidence-channels)
Core source: [TrajMark](https://arxiv.org/abs/2609.10416v1)
Tools and methodologies worth exploring now: stable producer IDs, signed trajectory chunks, critical-segment commitments, independent attribution and localization gates, final-artifact binding
Implementability score: 0.46

## Current implication

Do not ask one provenance signal to prove two different things. Use robust evidence to attribute the producer, fragile local commitments to expose edits, and ordinary cryptographic receipts to bind both to the exact artifact and final effect.
