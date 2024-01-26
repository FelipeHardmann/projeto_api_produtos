'''
    Esse arquivo serve para ser os recursos
    de injeção de dependência dentro dos
    testes que temos
'''
import pytest
from app.db.connection import Session


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()
