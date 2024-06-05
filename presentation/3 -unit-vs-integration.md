# UNIT TEST

Test a small “unit” of application
- One Function
- One Class
- Any dependencies are always “mocked”

### Benefits
- Validate code in “isolation”
- Run faster
  - Great units with lots of edge cases
- Generally, easier to write
  - Depends on the level of difficulty in mocking dependencies

# INTEGRATION TEST

Tests prove the “units” integrate
- A few units
- An entire API call
- A “vertical slice” (Some call this End to End)
  - UI event
  - API Call
  - DB Query

### Benefits
- Proves more of the application still works
- Can be easier, at times, to write over unit
  - Less mocking (perhaps no mocking)