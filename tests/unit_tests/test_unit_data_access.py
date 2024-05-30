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
