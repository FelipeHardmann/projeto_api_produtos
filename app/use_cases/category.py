from app.db.models import Category as CategoryModel
from app.schemas.category import Category
from sqlalchemy.orm import Session


class CategoryUseCases:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def add_category(self, category: Category) -> None:
        category_model = CategoryModel(**category.dict())
        self.db_session.add(category_model)
        self.db_session.commit()
