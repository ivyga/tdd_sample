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

TODO