# Agile Story Board

## Epic: Lookup Contacts

### Story 1
- **Description**: New API to Query Existing DB
- **Acceptance Criteria (AC)**:
  - `GET /` returns 200 with `{ contactCount: }` matching DB
- **Notes on Value / Priority**:
  - Initial story to address deployment and connectivity risks
- **Tests**:
  - Test FastAPI Route Against Mock DB
  - Test Route Using Real DB
- **Discussion**:
  - Unit vs Integrated Test strategies
  
### Story 2
- **Description**: New Route to Query Contacts By Last Name
- **Acceptance Criteria (AC)**:
  - `GET /contacts?last_name` returns 200 with contact details
- **Notes on Value / Priority**:
  - Crucial for project value, essential MVP component
- **Tests**:
  - Ditto
- **Discussion**:
  - MVP considerations
  
### Story 3
- **Description**: Route Requires Valid Input
- **Acceptance Criteria (AC)**:
  - `GET /contacts?last_name=<invalid>` returns 400 with specific error messages
- **Notes on Value / Priority**:
  - Reduce load on DB and protect against attacks
- **Tests**:
  - Start with Unit, Then Integration Testing Strategies
- **Discussion**:
  - TDD discussion initiation
  
### Story 4
- **Description**: Allow Partial Lookups
- **Acceptance Criteria (AC)**:
  - `GET /contacts?last_name=<starts-with>` supports partial lookups
- **Notes on Value / Priority**:
  - Nice-to-have feature
- **Tests**:
  - To be determined (TBD)
- **Discussion**:
  - Further refinement needed
  
### Story 5
- **Description**: Phonetic Search
- **Acceptance Criteria (AC)**:
  - TBD
- **Notes on Value / Priority**:
  - Complexity and value assessment pending
- **Tests**:
  - Not Sure If We'll Get That Far
- **Discussion**:
  - TBD
