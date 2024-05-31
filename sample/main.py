
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
