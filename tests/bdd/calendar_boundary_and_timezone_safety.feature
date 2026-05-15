Feature: Calendar boundaries and publishing timezone safety
  As the operator relying on week-based automation
  I want week identity and Friday gates to remain stable across clock boundaries
  So that sync and publication target the correct week under real-world time drift

  Background:
    Given the workflow resolves a target week and a publishing timezone for each run

  Rule: Long runs keep a stable target week
    Scenario: Freeze the target week for a run that crosses midnight
      Given a weekly sync starts before midnight and continues into the next day
      When the run proceeds past midnight
      Then the originally resolved week key should remain fixed for that run
      And the notebook target should not switch mid-execution

  Rule: Friday gates use the configured publishing timezone
    Scenario: Evaluate Friday publication in the configured publishing timezone
      Given the host clock says Friday
      And the configured publishing timezone is still Thursday
      When the operator requests Friday publication
      Then the notebook should remain private
      And no public share link should be emitted yet

  Rule: Historical backfills do not inherit today's publication window
    Scenario: Do not auto-publish a historical backfill just because today is Friday
      Given today is Friday
      And the operator is backfilling a prior week
      When the backfill sync completes
      Then the historical week should remain private unless publication was explicitly requested
      And the current week's publication state should remain unchanged
