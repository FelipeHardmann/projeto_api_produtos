from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Product as ProductModel
from app.main import app


client = TestClient(app)


def test_add_product_route(db_session, categories_on_db):
    body = {
        "category_slug": categories_on_db[0].slug,
        "product": {
            "name": "Camisa Nike",
            "slug": "camisa-nike",
            "price": 109.90,
            "stock": 30
        }
    }

    response = client.post('/product/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    product_on_db = db_session.query(ProductModel).all()

    assert len(product_on_db) == 1

    db_session.delete(product_on_db[0])
    db_session.commit()


def test_add_product_route_invalid_category_slug(db_session):
    body = {
        "category_slug": 'invalid',
        "product": {
            "name": "Camisa Nike",
            "slug": "camisa-nike",
            "price": 109.90,
            "stock": 30
        }
    }

    response = client.post('/produt/add', json=body)

    assert response.status_code == status.HTTP_404_NOT_FOUND

    product_on_db = db_session.query(ProductModel).all()

    assert len(product_on_db) == 0


def test_update_product_route(db_session, products_on_db):
    body = {
        "name": "Updated camisa",
        "slug": "updated-camisa",
        "price": 23.88,
        "stock": 10
    }

    response = client.put(f'/product/update/{products_on_db.id}', json=body)

    assert response.status_code == status.HTTP_200_OK

    db_session.refresh(products_on_db)

    products_on_db.name == 'Updated camisa'
    products_on_db.slug == 'updated-camisa'
    products_on_db.price == 23.88
    products_on_db.stock == 10


def test_update_product_route_invalid_id():
    body = {
        "name": "Update camisa",
        "slug": "update-camisa",
        "price": 80.90,
        "stock": 10
    }

    response = client.put('/product/update/1', json=body)

    assert response.status_code == status.HTTP_404_NOT_FOUND
