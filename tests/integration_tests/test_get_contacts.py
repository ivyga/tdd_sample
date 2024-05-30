from fastapi.testclient import TestClient
from unittest.mock import patch
from sample.data_access import query_contact_count  # noqa F401
from sample.get_db_connection_string import get_db_connecion_string
from sample.main import app

from sqlalchemy import create_engine, text

engine = create_engine(get_db_connecion_string())

client = TestClient(app)


def test_get_contacts__returns_matching_contacts():
    # Arrange
    last_name = 'Smith'  # NOTE: This test in ONLY predicatable IF you are testing against the Dockerized DB
    expected_matches = query_expected_matches(last_name)

    # Act
    response = client.get("/contacts?last_name=" + last_name)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_matches


def query_expected_matches(last_name):
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT id, first_name, last_name, email FROM public.contact WHERE last_name = '{last_name}'"))
        fetched = result.fetchall()
        contacts = [dict(row._mapping) for row in fetched]
        return contacts
