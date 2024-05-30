from sqlalchemy import create_engine, text

from sample.get_db_connection_string import get_db_connecion_string

engine = create_engine(get_db_connecion_string())


def query_contact_count() -> int:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT COUNT(*) FROM public.contact"))
        count = result.scalar_one()
        return count
