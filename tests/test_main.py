import pytest  # type: ignore
from pytest_mock import MockerFixture  # type: ignore 
from fastapi import HTTPException  # type: ignore

from sample.main import get_user_by_last_name


@pytest.mark.asyncio
async def test_get_user_by_last_name__calls_validate_name(mocker: MockerFixture):

    # Arrange
    mock_validate_name = mocker.patch('sample.main.validate_name')   # override sample.main import validate_name

    mock_validate_name.return_value = False

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        await get_user_by_last_name('DoesNotMatter')  # Since we are mocking validate_name, the actual value is ignore (the real validdate_name is never called)    # noqa: E501

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == 'Invalid name'

# Note:  Mocking the validate_name method is not really needed in this case because it is pure function
# Technically: The Unit tests that isolate are good for robust edge case testing but limit refactoring
