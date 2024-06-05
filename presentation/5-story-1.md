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
# Demo Story 1

## Start Database

<button class="copy-btn">Copy Code</button>
```
git checkout main
git reset --hard @{u}
docker-compose
```

## Start API 
(Run this in another terminal)
```
poetry run sample
```

From `main.py`, the GET / route is not available to test.
```python
@app.get("/")
async def root():
    return {"contactCount": query_contact_count()}
```

## Manual Test
(Run this in another terminal)
```
curl http://localhost:8000
```

## Run automated tests

```
poetry run pytest
```

### Simple Unit Test

```python
def test_get_root__mocked_query__returns_query_count():
    # Arrange
    with patch('sample.main.query_contact_count', return_value=42):
        # Act
        response = client.get("/")

        # Assert
        assert response.status_code == 200
        assert response.json() == {"contactCount": 42}
```

### Complicated Unit Test

Notice how much "mocking" is needed for the DB query (in `test_unit_data_access.py`):

```python
def test_query_contact_count(mocker):
    # Arrange
    mock_connection, mock_result, mock_engine_connect = setup_query_mocks(mocker)
    mock_result.scalar_one.return_value = 5  # Example count value

    # Act
    count = query_contact_count()

    # Assert
    assert count == 5
    mock_engine_connect.assert_called_once()
    mock_result.scalar_one.assert_called_once()


def setup_query_mocks(mocker):
    mock_connection = mocker.MagicMock()
    mock_result = mocker.MagicMock()
    mock_engine_connect = mocker.patch('sample.data_access.engine.connect', return_value=mock_connection)
    mock_connection.__enter__.return_value = mock_connection
    mock_connection.__exit__.return_value = None
    mock_connection.execute.return_value = mock_result
    return mock_connection, mock_result, mock_engine_connect
```

### Integrated Test Easier and More Comprehensive

See `test_get_root.py`
```python
def query_expected_count() -> int:
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

```