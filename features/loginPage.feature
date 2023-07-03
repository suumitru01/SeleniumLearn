Feature: Login Fetaure for OrangeHRMLive
  Scenario: 1. Test login functionality with in-valid credentials
    Given I launch the browser
    When I navigate to the url
    Then I enter username as Sumit and password as admin
    And I click on Login button
    And I validate error message as Invalid credentials on home screen
    And I close the browser


