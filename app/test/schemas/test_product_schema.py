from app.schemas.product import Product, ProductInput
import pytest


def test_product_schema():
    product = Product(
        name='Camisa Adidas',
        slug='camisa-adidas',
        price=109.9,
        stock=100
    )

    assert product.dict() == {
        'name': 'Camisa Adidas',
        'slug': 'camisa-adidas',
        'price': 109.9,
        'stock': 100
    }


def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Adidas',
            slug='camisa adidas',
            price=109.9,
            stock=100
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Adidas',
            slug='dogão',
            price=109.9,
            stock=100
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Adidas',
            slug='Camisa-adidas',
            price=109.9,
            stock=100
        )


def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Adidas',
            slug='camisa-adidas',
            price=0,
            stock=100
        )


def test_product_input_schema():
    product = Product(
            name='Camisa Adidas',
            slug='camisa-adidas',
            price=109.9,
            stock=100
    )
    product_input = ProductInput(
        category_slug='roupa',
        product=product
    )

    assert product_input.dict() == {
        "category_slug": "roupa",
        "product": {
            "name": "Camisa Adidas",
            "slug": "camisa-adidas",
            "price": 109.9,
            "stock": 100
        }
    }
