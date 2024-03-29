from fastapi import APIRouter, Depends, Response, status
from typing import List
from app.schemas.category import Category, CategoryOutput
from sqlalchemy.orm import Session
from app.routes.deps import get_db_session
from app.use_cases.category import CategoryUseCases


router = APIRouter(prefix='/category', tags=['Category'])


@router.post(
        '/add',
        status_code=status.HTTP_201_CREATED,
        description='Add new Category'
    )
def add_category(
    category: Category,
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session=db_session)
    uc.add_category(category)
    return Response(status_code=status.HTTP_201_CREATED)


@router.get(
        '/list',
        response_model=List[CategoryOutput],
        description='List Category'
    )
def list_category(
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session=db_session)
    response = uc.list_category()

    return response


@router.delete(
        '/delete/{id}',
        description='Delete Category'
    )
def delete_category(
    id: int,
    db_session: Session = Depends(get_db_session)
):

    uc = CategoryUseCases(db_session=db_session)
    uc.delete_category(id=id)

    return Response(status_code=status.HTTP_200_OK)
