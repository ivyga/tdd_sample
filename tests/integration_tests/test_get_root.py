from fastapi.testclient import TestClient
from unittest.mock import patch
from sample.data_access import query_contact_count  # noqa F401
from sample.get_db_connection_string import get_db_connecion_string
from sample.main import app

from sqlalchemy import create_engine, text

engine = create_engine(get_db_connecion_string())

client = TestClient(app)


def query_expected_count() -> int:
    # Note: This is the same implemention as query_contact_count
    # Why? Simplest way. More important: it protects any alteration of the implementation (accidentally)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT COUNT(*) FROM public.contact"))
        count = result.scalar_one()
        return count


def test_get_root__real_query__returns_query_count():
    # Arrange
    expected_count = query_expected_count()

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"contactCount": expected_count}
