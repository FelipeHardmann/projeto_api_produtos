from fastapi import (
    APIRouter,
    Response,
    status,
    Depends
)
from sqlalchemy.orm import Session
from app.routes.deps import get_db_session
from app.use_cases.product import ProductUseCases
from app.schemas.product import Product, ProductInput, ProductOutput
from typing import List


router = APIRouter(prefix='/product', tags=['Product'])


@router.post(
        '/add',
        status_code=status.HTTP_201_CREATED,
        description='Add new product')
def add_product(
    product_input: ProductInput,
    db_session: Session = Depends(get_db_session)
):
    uc = ProductUseCases(db_session=db_session)
    uc.add_product(
        product=product_input.product,
        category_slug=product_input.category_slug
    )

    return Response(status_code=status.HTTP_201_CREATED)


@router.put(
        '/update/{id}',
        description='Update Product'
    )
def update_product(
    id: int,
    product: Product,
    db_session: Session = Depends(get_db_session)
):
    uc = ProductUseCases(db_session=db_session)
    uc.update_product(id=id, product=product)

    return Response(
        status_code=status.HTTP_200_OK
    )


@router.delete(
        '/delete/{id}',
        description='Delete Product'
    )
def delete_product(
    id: int,
    db_session: Session = Depends(get_db_session)
):
    uc = ProductUseCases(db_session=db_session)
    uc.delete_product(id=id)

    return Response(
        status_code=status.HTTP_200_OK
    )


@router.get(
        '/list',
        response_model=List[ProductOutput],
        description='List Product'
    )
def list_product(
    search: str = '',
    db_session: Session = Depends(get_db_session)
):
    uc = ProductUseCases(db_session=db_session)
    products = uc.list_products(search=search)

    return products
