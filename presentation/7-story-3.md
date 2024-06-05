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
# Demo Story 3



## AC: New route: GET /contacts?last_name={invalid-input} returns 400
* input is too short (less than 3)
* input is malformed (characters like *, !)
* input to has improper hypens (starts with, ends with, doubles)

Using the AC, we can write the following tests:
```python
from sample.validators import validate_name


def test_validate_name__too_short__returns_false():
    # arrange
    too_short = 'Iv'

    # act
    actual = validate_name(too_short)

    # assert
    assert actual is False



def test_name_input__malformed__returns_false():
	pass


def test_name_input__starts_with_hypen__returns_false():
	pass


def test_name_input__ends_with_hypen__returns_false():
	pass


def test_name_input__consecutive_hypens__returns_false():
	pass


def test_name_input__valid_input__returns_true():
	pass
```


## Start the dependencies

Run this in one terminal to get the code and start the DB:

<button class="copy-btn">Copy Code</button>
```
https://github.com/ivyga/tdd_sample.git
git checkout story-3-start
git reset --hard @{u}
poetry install
docker-compose
```
Run this in another terminal to start the API

<button class="copy-btn">Copy Code</button>
```
poetry run sample
```


In yet another terminal run this:

<button class="copy-btn">Copy Code</button>
```
poetry run pytest
```


## Write unit tests
```
touch tests/unit_tests/test_unit-validators.py
```

paste in the tests from earlier

```
touch sample/validators.py
```

```python

def validate_name(name: str) -> bool:
	return True
```

```
poetry run pytest tests/unit_tests/test_unit-validators.py

```


Possible solution:
```mport re


def validate_name(name: str) -> bool:
    print("Unpatched validate_name called!")
    
    # Check if the name is empty or None
    if not name:
        return False
    
    if len(name) < 3:
        return False

    # Check for valid characters: letters, spaces, and hyphens
    if not re.match(r'^[a-zA-Z\s-]+$', name):
        return False
    
    # Check for leading/trailing spaces or hyphens
    if name[0] in " -" or name[-1] in " -":
        return False
    
    # Check for consecutive spaces or hyphens
    if re.search(r'\s{2,}', name) or re.search(r'-{2,}', name):
        return False
    
    return True
```