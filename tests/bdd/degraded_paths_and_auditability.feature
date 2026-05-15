Feature: Degraded paths, auditability, and safe recovery
  As the infrastructure owner for the weekly NotebookLM flow
  I want dependency failures and ambiguous outcomes to be visible and recoverable
  So that local roundup artifacts remain trustworthy even when external services drift or fail

  Background:
    Given the local roundup files remain the source of record during external failures

  Rule: Dependency drift fails safe
    Scenario: Fail safely when notebooklm-py returns an unexpected response shape
      Given notebooklm-py returns an unexpected response while the system creates or opens a weekly notebook
      When the operator runs the weekly NotebookLM sync
      Then the run should fail with a dependency compatibility error
      And no publish action should be attempted

  Rule: Publication claims must stay honest when remote verification is incomplete
    Scenario: Surface an ambiguous publish state when verification is unavailable
      Given the notebook share action returned success
      And follow-up verification cannot prove external visibility
      When the run finalizes publication status
      Then the run should be marked published with unverified visibility
      And the operator should be prompted for manual verification before public announcement

  Rule: Local curation survives complete external outage
    Scenario: Preserve the local roundup when NotebookLM is fully unavailable
      Given NotebookLM is unavailable for the entire run
      When the operator runs the weekly NotebookLM sync
      Then the curated markdown and sync manifest should remain the local source of record
      And the run should exit with a retryable degraded status
