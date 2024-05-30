
from fastapi import FastAPI
import uvicorn  # type: ignore

from sample.data_access import query_contact_count, query_contacts_by_last_name

app = FastAPI()


@app.get("/")
async def root():
    return {"contactCount": query_contact_count()}


@app.get("/contacts")
async def get_contacts_by_last_name(last_name: str):
    return query_contacts_by_last_name(last_name)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
