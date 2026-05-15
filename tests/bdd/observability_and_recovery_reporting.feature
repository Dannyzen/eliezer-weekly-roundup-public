Feature: Observability, classification, and manual recovery reporting
  As the operator debugging a brittle external integration
  I want stage-specific run summaries and recovery guidance
  So that every failed or degraded sync tells me exactly what to do next

  Background:
    Given the sync system records stage names and final run status for each weekly attempt

  Rule: Failures are classified into operator-useful states
    Scenario: Distinguish retryable failures from terminal policy failures
      Given one weekly run fails because NotebookLM is temporarily unavailable
      And another weekly run fails because notebook identity is ambiguous
      When the operator reviews the recorded run summaries
      Then the unavailable run should be marked retryable
      And the ambiguity run should be marked fail-closed until manual resolution

    Scenario: Record the exact failing stage for a degraded run
      Given a weekly sync fails after source attachment but before source readiness completes
      When the operator reviews the final run summary
      Then the summary should name the failing stage explicitly
      And the operator should be told which checkpoint can be resumed safely

  Rule: Manual verification requirements are explicit
    Scenario: Require manual verification before announcing a weakly verified publication
      Given a week was published but external visibility could not be fully verified
      When the system prepares the operator-facing completion summary
      Then the summary should require manual verification before any public announcement or distribution
      And the summary should include the share target that needs review
