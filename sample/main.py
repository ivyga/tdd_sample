
from fastapi import FastAPI, HTTPException  # type: ignore
import uvicorn  # type: ignore

from sample.validators import validate_name
from sample.data_access import query_contact_count, query_contacts_by_exact_last_name

app = FastAPI()


@app.get("/contacts")
async def get_user_by_last_name(last_name: str):
    if validate_name(last_name) is False:
        raise HTTPException(status_code=400, detail="Invalid name")

    return query_contacts_by_exact_last_name(last_name)


@app.get("/")
async def root():
    return {"contactCount": query_contact_count()}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
