### context ###

{Persona}

### task ###

Create tests in Jest which cover all test scenarios laid out in the Gherkin spec provided below. Tests must fully represent all test scenarios. All tests must run appropriately. Create only test code. Do not create any production code. Include only javascript source code. Do not format with any markup or markdown. Use the feature name as the top level description for jest tests.

Example:

**Feature source code**

Feature: count

  Scenario: increment 0 to 1
    Given starting value is 0
    When count is called with starting value
    Then count returns 1

**Jest test output**

describe('count', () => {
    it('increments 0 to 1', () => {
        const initialValue = 0;
        const result = count(initialValue);
        
        expect(result).toEqual(1);
    });
});

### gherkin spec ###

{Gherkin}