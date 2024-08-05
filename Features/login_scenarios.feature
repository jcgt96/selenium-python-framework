Feature: Login Scenario

  Scenario: Success Login
    Given A login website
    When The username and password are input
    When I click in the login button
    Then The login is successful
