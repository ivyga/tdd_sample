<script>
 document.addEventListener('DOMContentLoaded', (event) => {
        document.querySelectorAll('.copy-btn').forEach(button => {
            button.addEventListener('click', () => {
                // Find the next sibling <pre> element
                let preElement = button.parentElement.nextElementSibling;
                if (preElement && preElement.tagName.toLowerCase() === 'pre') {
                    let codeBlock = preElement.querySelector('code').innerText;

                    // Create a temporary textarea element
                    let tempTextarea = document.createElement("textarea");
                    tempTextarea.value = codeBlock;
                    document.body.appendChild(tempTextarea);

                    // Select the text in the textarea
                    tempTextarea.select();
                    tempTextarea.setSelectionRange(0, 99999); // For mobile devices

                    // Copy the text to the clipboard
                    document.execCommand("copy");

                    // Remove the temporary textarea element
                    document.body.removeChild(tempTextarea);

                    // Optionally, alert the user that the code has been copied
                    alert("Code copied to clipboard!");
                } else {
                    alert("No code block found to copy!");
                }
            });
        });
    });</script>
# Demo Story 2

## Prerequisites

<button class="copy-btn">Copy Code</button>
```
git checkout main
git reset --hard @{u}
git checkout -b story-2-demo
touch tests/integration_tests/test_get_contacts.py
```

## TDD AC #1

AC: New Route GET /contacts?last_name={last_name} Returns 200

Paste into test_get_contacts.py:
<button class="copy-btn">Copy Code</button>
```
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sample.main import app

from sample.get_db_connection_string import get_db_connecion_string

engine = create_engine(get_db_connecion_string())

client = TestClient(app)


def test_get_contacts__returns_200():
    # Arrange
    last_name = "DoesNotMatter"

    # Act
    response = client.get("/contacts?last_name=" + last_name)

    # Assert
    assert response.status_code == 200
```

Run the test
<button class="copy-btn">Copy Code</button>
```
poetry run pytest tests/integration_tests/test_get_contacts.py
```

Expect 404 because the route does not exist.

Fix by adding this method to main.py.  We are doing just enough to pass the test.
<button class="copy-btn">Copy Code</button>

```
@app.get("/contacts")
async def get_contacts_by_last_name(last_name: str):
    return []
```

Test again.  Expect it to pass.

## TDD AC #2

AC: Returns [{ id, first_name, last_name, email ]]

Add this test:
<button class="copy-btn">Copy Code</button>
```
def test_get_users__real_query__returns_matching_contacts():
    # Arrange
    last_name = 'Smith'  # NOTE: This test in ONLY predicatable IF you are testing against the Dockerized DB
    expected_matches = query_expected_matches(last_name)

    # Act
    response = client.get("/contacts?last_name=" + last_name)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_matches


def query_expected_matches(last_name):
    # Note: This is/will be duplicate in DataAccess (for now)
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT id, first_name, last_name, email FROM public.contact WHERE last_name = '{last_name}'"))
        fetched = result.fetchall()
        contacts = [dict(row._mapping) for row in fetched]
        return contacts
```

Expect it to fail. Add this method in data_access.py
<button class="copy-btn">Copy Code</button>
```
def query_contacts_by_last_name(last_name):
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT id, first_name, last_name, email FROM public.contact WHERE last_name = '{last_name}'"))
        fetched = result.fetchall()
        contacts = [dict(row._mapping) for row in fetched]
        return contacts
```

Call it from main.py
Test should pass.


## Refactor Time

Note: Switch query implementation to ORM:

<button class="copy-btn">Copy Code</button>
```python
from sqlalchemy import create_engine, Column, Integer, String  # func, Index 
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
from pydantic import BaseModel, ConfigDict  # type: ignore

from sample.get_db_connection_string import get_db_connecion_string

engine = create_engine(get_db_connecion_string())

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


class ContactDB(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


Base.metadata.create_all(bind=engine)


class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config(ConfigDict):
        from_attributes = True


def query_contact_count() -> int:
    session = SessionLocal()
    try:
        count = session.query(ContactDB).count()
        return count
    finally:
        session.close()


def query_contacts_by_last_name(input: str) -> list[Contact]:
    session = SessionLocal()
    try:
        db_contacts = session.query(ContactDB).filter(ContactDB.last_name == input).all()
        contacts = [Contact.from_orm(contact) for contact in db_contacts]
        return contacts
    finally:
        session.close()
```

Integration Test will still pass
Unit test broken (too contrained on the knowledge of implementation).  Fix it with this:


```python
import pytest
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sample.data_access import query_contact_count, ContactDB, SessionLocal

# Use pytest-mock fixture for mocking
def test_query_contact_count(mocker):
    # Arrange
    mock_count = 5  # Example count value
    mock_session = mocker.MagicMock(spec=Session)
    mocker.patch('sample.data_access.SessionLocal', return_value=mock_session)  # Mock SessionLocal to return the mock session
    mock_query = mock_session.query.return_value  # Mock the query method of the session
    mock_query.count.return_value = mock_count  # Mock the count method of the query object to return the example count value

    # Act
    count = query_contact_count()

    # Assert
    assert count == mock_count
```

