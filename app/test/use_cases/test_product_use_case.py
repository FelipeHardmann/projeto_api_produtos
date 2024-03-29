from app.db.models import Product as ProductModel
from app.schemas.product import Product, ProductOutput
from app.use_cases.product import ProductUseCases
from fastapi.exceptions import HTTPException
import pytest


def test_add_product_uc(db_session, categories_on_db):
    uc = ProductUseCases(db_session)

    product = Product(
        name='Camisa Nike',
        slug='camisa-nike',
        price=109.90,
        stock=100,
    )

    uc.add_product(product=product, category_slug=categories_on_db[0].slug)

    products_on_db = db_session.query(ProductModel).first()

    assert products_on_db is not None
    assert products_on_db.name == product.name
    assert products_on_db.price == product.price
    assert products_on_db.slug == product.slug
    assert products_on_db.stock == product.stock
    assert products_on_db.category.name == categories_on_db[0].name

    db_session.delete(products_on_db)
    db_session.commit()


def test_add_product_uc_invalid_category(db_session):
    uc = ProductUseCases(db_session)

    product = Product(
        name='Camisa Nike',
        slug='camisa-nike',
        price=109.90,
        stock=100,
    )

    with pytest.raises(HTTPException):
        uc.add_product(product=product, category_slug='invalid')


def test_update_product(db_session, products_on_db):
    product = Product(
        name='Camisa Mike',
        slug='camisa-mike',
        price=22.99,
        stock=22
    )

    uc = ProductUseCases(db_session=db_session)
    uc.update_product(id=products_on_db.id, product=product)

    product_updated_on_db = db_session.query(
        ProductModel
    ).filter_by(id=products_on_db.id).first()

    assert product_updated_on_db is not None
    assert product_updated_on_db.name == product.name
    assert product_updated_on_db.slug == product.slug
    assert product_updated_on_db.price == product.price
    assert product_updated_on_db.stock == product.stock


def test_update_product_invalid_id(db_session):
    product = Product(
        name='Camisa Mike',
        slug='camisa-mike',
        price=22.99,
        stock=22
    )

    uc = ProductUseCases(db_session=db_session)

    with pytest.raises(HTTPException):
        uc.update_product(id=1, product=product)


def test_delete_product(db_session, products_on_db):
    uc = ProductUseCases(db_session=db_session)
    uc.delete_product(id=products_on_db.id)

    product_on_db = db_session.query(ProductModel).all()

    assert len(product_on_db) == 0


def test_delete_product_non_exist(db_session):
    uc = ProductUseCases(db_session=db_session)

    with pytest.raises(HTTPException):
        uc.delete_product(id=1)


def test_list_product(db_session, product_on_db):
    uc = ProductUseCases(db_session=db_session)

    products = uc.list_products()

    for product in product_on_db:
        db_session.refresh(product)

    assert len(products) == 4
    assert isinstance(products[0], ProductOutput)
    assert products[0].name == product_on_db[0].name
    assert products[0].category.name == product_on_db[0].category.name


def test_list_product_with_search(db_session, product_on_db):
    uc = ProductUseCases(db_session=db_session)

    products = uc.list_products(search='nike')

    for product in product_on_db:
        db_session.refresh(product)

    assert len(products) == 3
    assert isinstance(products[0], ProductOutput)
    assert products[0].name == product_on_db[0].name
    assert products[0].category.name == product_on_db[0].category.name
