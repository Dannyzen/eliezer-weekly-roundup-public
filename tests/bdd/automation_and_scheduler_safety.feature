Feature: Automation, scheduler safety, and idempotent recurring runs
  As the operator relying on recurring automation
  I want scheduled work to be safe around locks, no-op reruns, and missed windows
  So that background syncs never duplicate work or publish silently after a missed deadline

  Background:
    Given scheduled daily syncs and Friday publication may run without an operator present

  Rule: Scheduled work respects active writers
    Scenario: Scheduled sync exits cleanly when a manual same-week run owns the lock
      Given a manual sync already holds the current week's lock
      When the scheduled sync starts for that same week
      Then the scheduled run should exit without remote mutation
      And the manual run should remain the only writer

  Rule: Recurring syncs are no-ops when nothing changed
    Scenario: Repeated scheduled sync with an unchanged source fingerprint is a no-op
      Given the current week was already synchronized successfully
      And the current source fingerprint has not changed since the last successful sync
      When the next scheduled daily sync runs
      Then no new notebook, source, audio, or share side effect should be created
      And the run summary should say that no actionable weekly changes were found

  Rule: Missed automation does not silently publish later
    Scenario: Missed Friday auto-publication requires explicit operator review
      Given Friday publication did not run during the intended publishing window
      And the system first regains a chance to publish on a later day
      When the scheduled automation evaluates that missed week
      Then the week should remain unpublished until explicit operator review
      And the operator should be told that the scheduled publish window was missed
