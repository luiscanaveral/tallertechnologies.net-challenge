from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.exc import SQLAlchemyError


def _get_database_connection_string():
    # TODO:replace with .env
    return "postgresql://postgres:mysecretpassword@localhost:5432/task_management"


def _create_engine():
    return create_engine(_get_database_connection_string(), echo=False)


@contextmanager
def get_session(engine=None):
    if engine is None:
        print("Creating a engine")
        engine = _create_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    except SQLAlchemyError as e:
        print(f"An error occurred while creating the database session: {e}")
        raise
    finally:
        session.close()
