'''
    Esse arquivo serve para ser os recursos
    de injeção de dependência dentro dos
    testes que temos
'''
import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModel


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


@pytest.fixture()
def categories_on_db(db_session):
    categories = [
        CategoryModel(name='Roupa', slug='roupa'),
        CategoryModel(name='Carro', slug='carro'),
        CategoryModel(name='Chinelo', slug='chinelo'),
        CategoryModel(name='Tenis', slug='tenis')
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)

    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()
