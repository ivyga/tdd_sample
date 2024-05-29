
from fastapi import FastAPI
import uvicorn
from http.client import HTTPException

from sample.validators import validate_name
from sample.data_access import users


app = FastAPI()


@app.get("/users")
async def get_user_by_last_name(last_name: str):
    if validate_name(last_name) is False:
        raise HTTPException(status_code=400, detail="Invalid name")

    matches = []    
    for user in users:
        if user["last_name"] == last_name:
            matches.append(user)

    return matches


@app.get("/")
async def root():
    return {"message": "Welcome to the User Lookup API"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()