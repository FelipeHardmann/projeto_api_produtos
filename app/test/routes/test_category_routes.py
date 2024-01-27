from fastapi.testclient import TestClient
from app.main import app
from fastapi import status
from app.db.models import Category as CategoryModel


client = TestClient(app)


def test_add_category_route(db_session):
    body = {
        "nome": "Roupa",
        "slug": "roupa"
    }

    response = client.post('/category/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    categories_on_db = db_session.query(CategoryModel).all()
    assert len(categories_on_db) == 1
    db_session.delete(categories_on_db[0])
    db_session.commit()
