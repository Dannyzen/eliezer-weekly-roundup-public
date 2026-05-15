Feature: Operator overrides, manual repair, and audited recovery
  As the operator repairing a partially completed weekly run
  I want narrow overrides and manual recovery paths to stay auditable and safe
  So that repair work never bypasses the core policy gates or duplicate remote state

  Background:
    Given partial failures sometimes require operator-directed repair

  Rule: Scoped repair can resume from a known checkpoint
    Scenario: Resume from source readiness after the operator confirms attachment checkpoint
      Given file and URL sources were already attached for the current week
      And the failure occurred during source readiness waiting
      When the operator requests a scoped repair from the readiness stage
      Then the workflow should resume from source readiness without reattaching sources
      And the repair run should record that it was operator-scoped

  Rule: Dangerous repairs require explicit audit intent
    Scenario: Require a reason when force-rebinding a week to a different notebook id
      Given the local manifest points at one notebook id for the current week
      And the operator wants to rebind that week to a different notebook id
      When the operator requests the notebook rebind without a reason
      Then the repair should be rejected
      And the operator should be told that an audit reason is required

  Rule: Overrides cannot bypass hard safety policies
    Scenario: Refuse a force-publish override when auth or privacy checks are red
      Given the current week fails either the approved-account check or the privacy policy gate
      When the operator requests a force publish override
      Then publication should remain blocked
      And the override attempt should be recorded as denied
