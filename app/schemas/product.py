import re
from pydantic import validator
from app.schemas.base import CustomBaseModel


class Product(CustomBaseModel):
    name: str
    slug: str
    price: float
    stock: int

    @validator('slug')
    def validate_slug(cls, v):
        if not re.match('^([a-z]|-|_)+$', v):
            raise ValueError('Invalid Slug')
        return v

    @validator('price')
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Invalid Price')
        return v


class ProductInput(CustomBaseModel):
    category_slug: str
    product: Product
