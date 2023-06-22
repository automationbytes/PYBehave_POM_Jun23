Feature: To test Sauce Demo Website

  Scenario: Login
    Given the user launches the application
    When the user verifies the application is loaded
    Then the user enters the valid credentials

  Scenario Outline: To verify Filter Option
    Given the user is on home page
    Then the user filters "<filter>"
  Examples:
    |filter|
    |Name (Z to A)|
    |Price (low to high)|
    |Price (high to low)|
  Scenario: Logout
    Given the user is on home page
    Given the user logouts from the site