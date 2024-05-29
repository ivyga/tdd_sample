from pydantic import BaseModel  # type: ignore

# TODO: Move to a DB


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


users = [
    {"id": 1, "first_name": "Alice", "last_name": "Smith", "email": "alice.smith@wwt.com"},
    {"id": 2, "first_name": "Bob", "last_name": "Smith", "email": "bob.smith@wwt.com"},
    {"id": 3, "first_name": "Charles", "last_name": "Smythe", "email": "charlie.smith@wwt.com"},
]
