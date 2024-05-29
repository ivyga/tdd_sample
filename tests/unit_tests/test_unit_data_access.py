import pytest  # noqa: F401

from sample.data_access import query_contact_count


def test_query_contact_count(mocker):
    # Arrange
    mock_connection, mock_result, mock_engine_connect = setup_query_mocks(mocker)
    mock_result.scalar_one.return_value = 5  # Example count value

    # Act
    count = query_contact_count()

    # Assert
    assert count == 5
    mock_engine_connect.assert_called_once()
    # mock_connection.execute.assert_called_once_with("SELECT COUNT(*) FROM public.contact")
    mock_result.scalar_one.assert_called_once()


def setup_query_mocks(mocker):
    # NOTE: This type of test is not for TDD
    # Why? It requires a high level knowledge of implemention details

    mock_connection = mocker.MagicMock()
    mock_result = mocker.MagicMock()

    # Patch `engine.connect` in the `sample.data_access` module
    mock_engine_connect = mocker.patch('sample.data_access.engine.connect', return_value=mock_connection)

    # Mock the behavior of the context manager
    mock_connection.__enter__.return_value = mock_connection
    mock_connection.__exit__.return_value = None

    # Mock the return value
    mock_connection.execute.return_value = mock_result
    return mock_connection, mock_result, mock_engine_connect
