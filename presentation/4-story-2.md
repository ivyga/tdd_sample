# Demo Story 2

## Prerequisites

```
git checkout main
git reset --hard @{u}
git checkout -b story-2-demo
touch tests/integration_tests/test_get_contacts.py
```

## TDD AC #1

AC: New Route GET /contacts?last_name={last_name} Returns 200

Paste into test_get_contacts.py:
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
```
poetry run pytest tests/integration_tests/test_get_contacts.py
```

Expect 404 because the route does not exist.

Fix by adding this method to main.py.  We are doing just enough to pass the test.

```
@app.get("/contacts")
async def get_contacts_by_last_name(last_name: str):
    return []
```

Test again.  Expect it to pass.

## TDD AC #2

AC: Returns [{ id, firstName, lastName, email ]]

Add this test:
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

```
def query_contacts_by_last_name(last_name):
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT id, first_name, last_name, email FROM public.contact WHERE last_name = '{last_name}'"))
        fetched = result.fetchall()
        contacts = [dict(row._mapping) for row in fetched]
        return contacts
```


