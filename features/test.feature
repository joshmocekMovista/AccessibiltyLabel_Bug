Feature: tester
  Scenario: TestScenario
    Given set text in textField text1 to textField
    And set text in textField text2 to textField2
    When user enters text
    When user clicks View2
    Then text1 is textField and text2 is textField2
