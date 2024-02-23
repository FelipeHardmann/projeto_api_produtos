from app.db.models import Product as ProductModel
from app.schemas.product import Product
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

    product_on_db = db_session.query(ProductModel).first()

    assert product_on_db is not None
    assert product_on_db.name == product.name
    assert product_on_db.price == product.price
    assert product_on_db.slug == product.slug
    assert product_on_db.stock == product.stock
    assert product_on_db.category.name == categories_on_db[0].name

    db_session.delete(product_on_db)
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
