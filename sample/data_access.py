from sqlalchemy import create_engine, Column, Integer, String  # func, Index 
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
from pydantic import BaseModel, ConfigDict  # type: ignore

from sample.get_db_connection_string import get_db_connecion_string

engine = create_engine(get_db_connecion_string())

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


class ContactDB(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


Base.metadata.create_all(bind=engine)


class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config(ConfigDict):
        from_attributes = True


def query_contact_count() -> int:
    session = SessionLocal()
    try:
        count = session.query(ContactDB).count()
        return count
    finally:
        session.close()


def query_contacts_by_last_name(input: str) -> list[Contact]:
    session = SessionLocal()
    try:
        db_contacts = session.query(ContactDB).filter(ContactDB.last_name == input).all()
        contacts = [Contact.from_orm(contact) for contact in db_contacts]
        return contacts
    finally:
        session.close()
