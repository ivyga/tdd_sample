
from fastapi import FastAPI
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
