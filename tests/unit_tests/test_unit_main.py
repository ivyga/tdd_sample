from fastapi.testclient import TestClient
from unittest.mock import patch
from sample.data_access import query_contact_count  
from sample.main import app

client = TestClient(app)


def test_get_root__mocked_query__returns_query_count():
    # Arrange
    with patch('sample.main.query_contact_count', return_value=42):
        # Act
        response = client.get("/")

        # Assert
        assert response.status_code == 200
        assert response.json() == {"contactCount": 42}


def test_get_contats__mocked_validator__returns_400():
    # Arrange
    with patch('sample.main.validate_name', return_value=False):
        # Act
        response = client.get("/contacts?last_name=DoesNotMatter")

        # Assert
        assert response.status_code == 400



