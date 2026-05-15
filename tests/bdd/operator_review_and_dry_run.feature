Feature: Operator review, dry run, and controlled execution
  As the operator responsible for publishing weekly roundups
  I want a review-first workflow before any NotebookLM mutation happens
  So that publication remains intentional and resilient under pressure

  Background:
    Given the system can assemble the weekly roundup payload without mutating NotebookLM

  Rule: Dry runs are safe and informative
    Scenario: Preview the weekly sync plan without mutating NotebookLM
      Given the current week's markdown and cited URLs are available
      When the operator requests a dry run of the weekly NotebookLM sync
      Then the operator should see the target week key, notebook title, source counts, and publication gates
      And no notebook, source, audio, or sharing mutation should occur

    Scenario: Preview a Friday publication gate before running it
      Given the current week has a synced notebook but no verified audio artifact
      When the operator requests a dry run of Friday publication
      Then the operator should see that publication is blocked by the missing or stale audio gate
      And no share link should be created during the dry run

  Rule: Sensitive actions require explicit intent
    Scenario: Require explicit approval before public sharing
      Given the weekly notebook is fully synced and audio-ready
      When the operator runs the weekly sync without a publish flag
      Then the notebook should remain private
      And the operator should be told that publication requires explicit approval
