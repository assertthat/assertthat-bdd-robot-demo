*** Settings ***
Documentation    A test suite with a single Gherkin style test.
Resource    ./login_step_definitions.robot
Metadata    Feature    Login
Metadata    Generated by    _gherkin2robotframework on 2021-02-22T22:32:05.506961_

*** Test Cases ***
Valid Login
    [Tags]    AUTOMATED
    Given browser is opened to login page
    When user "demo" logs in with password "mode"
    Then welcome page should be open


