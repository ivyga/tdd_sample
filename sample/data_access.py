from sqlalchemy import create_engine, text

from sample.get_db_connection_string import get_db_connecion_string

engine = create_engine(get_db_connecion_string())


def query_contact_count() -> int:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT COUNT(*) FROM public.contact"))
        count = result.scalar_one()
        return count


def query_contacts_by_last_name(last_name):
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT id, first_name, last_name, email FROM public.contact WHERE last_name = '{last_name}'"))
        fetched = result.fetchall()
        contacts = [dict(row._mapping) for row in fetched]
        return contacts
