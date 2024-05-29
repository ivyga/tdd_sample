# Note: Ideally you would be deal this iteratively as needed and maybe show alternative to ORM.
# But: I don't want to drag down the demo.
# Eiher way:  It is a best practice to not do this stuff in a controller.

from sqlalchemy import create_engine, Column, Integer, String  # func, Index 
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
from pydantic import BaseModel, ConfigDict  # type: ignore

DATABASE_URL = 'sqlite:///:memory:'
# DATABASE_URL = 'postgresql://username:password@localhost/mydatabase'
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


class ContactDB(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    # __table_args__ = (
    #     Index('soundex_idx', func.soundex('last_name')),
    # )


Base.metadata.create_all(bind=engine)


class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config(ConfigDict):
        orm_mode = True


def query_contact_count() -> int:
    session = SessionLocal()
    try:
        count = session.query(ContactDB).count()
        return count
    finally:
        session.close()


def query_contacts_by_exact_last_name(input: str) -> list[Contact]:
    session = SessionLocal()
    try:
        db_contacts = session.query(ContactDB).filter(ContactDB.last_name == input).all()
        contacts = [Contact.from_orm(contact) for contact in db_contacts]
        return contacts
    finally:
        session.close()


def query_contacts_by_partial_last_name(input: str) -> list[Contact]:
    session = SessionLocal()
    try:
        db_contacts = session.query(ContactDB).filter(ContactDB.last_name.like(f'%{input}%')).all()
        contacts = [Contact.from_orm(contact) for contact in db_contacts]
        return contacts
    finally:
        session.close()


# def query_contacts_by_phonetic_last_name(input: str) -> list[Contact]:
#     session = SessionLocal()
#     try:
#         db_contacts = session.query(ContactDB).filter(func.soundex(ContactDB.last_name) == func.soundex(input)).all()
#         contacts = [Contact.from_orm(contact) for contact in db_contacts]
#         return contacts
#     finally:
#         session.close()
