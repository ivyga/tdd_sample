
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn  # type: ignore

from sample.data_access import query_contact_count

app = FastAPI()


@app.get("/")
async def root():
    return {"contactCount": query_contact_count()}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()


@app.get("/client", response_class=HTMLResponse)
async def get_client():
    print(os.path.dirname(__file__))
    client_path = os.path.join(os.path.dirname(__file__), "demo.html")
    with open(client_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact API Client</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <script>
        async function getContactCount() {
            const response = await fetch('http://localhost:8000/');
            const data = await response.json();
            document.getElementById('contactCount').innerText = `Contact Count: ${data.contactCount}`;
        }

        async function getContactsByLastName() {
            const lastName = document.getElementById('lastName').value;
            const response = await fetch(`http://localhost:8000/contacts?last_name=${lastName}`);
            if (response.status === 400) {
                document.getElementById('contacts').innerText = 'Invalid name';
                return;
            }
            const contacts = await response.json();
            const contactList = contacts.map(contact => `<li class="list-group-item">${contact.first_name} ${contact.last_name} (${contact.email})</li>`).join('');
            document.getElementById('contacts').innerHTML = `<ul class="list-group">${contactList}</ul>`;
        }
    </script>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Contact API Client</h1>
        <div class="text-center mb-4">
            <button class="btn btn-primary" onclick="getContactCount()">Get Contact Count</button>
            <p id="contactCount" class="mt-3"></p>
        </div>
        <div class="card">
            <div class="card-header">
                <h2>Search Contacts by Last Name</h2>
            </div>
            <div class="card-body">
                <div class="form-group">
                    <input type="text" id="lastName" class="form-control" placeholder="Enter last name">
                </div>
                <button class="btn btn-success" onclick="getContactsByLastName()">Search</button>
                <div id="contacts" class="mt-3"></div>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
"""
