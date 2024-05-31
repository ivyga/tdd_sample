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