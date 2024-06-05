from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sample.main import app

from sample.get_db_connection_string import get_db_connecion_string

engine = create_engine(get_db_connecion_string())

client = TestClient(app)


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
