'''
    Esse arquivo serve para ser os recursos
    de injeção de dependência dentro dos
    testes que temos
'''
import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModel
from app.db.models import Product as ProductModel


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


@pytest.fixture
def products_on_db(db_session):
    category = CategoryModel(name='Carro', slug='carro')
    db_session.add(category)
    db_session.commit()

    product = ProductModel(
        name='Camisa Nike',
        slug='camisa-nike',
        price=109.90,
        stock=100,
        category_id=category.id
    )

    db_session.add(product)
    db_session.commit()

    yield product

    db_session.delete(product)
    db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def product_on_db(db_session):
    category = CategoryModel(name='Roupa', slug='roupa')
    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)

    products = [
        ProductModel(
            name='Camisa Nike',
            slug='camisa-nike',
            price=100,
            stock=30,
            category_id=category.id
        ),
        ProductModel(
            name='Casaco Nike',
            slug='casaco-nike',
            price=100,
            stock=30,
            category_id=category.id
        ),
        ProductModel(
            name='Camiseta Nike',
            slug='camiseta-nike',
            price=100,
            stock=30,
            category_id=category.id
        ),
        ProductModel(
            name='Short Nike',
            slug='short-nike',
            price=100,
            stock=30,
            category_id=category.id
        ),
    ]

    for product in products:
        db_session.add(product)
    db_session.commit()

    for product in products:
        db_session.refresh(product)

    yield products

    for product in products:
        db_session.delete(product)

    db_session.delete(category)
    db_session.commit()
