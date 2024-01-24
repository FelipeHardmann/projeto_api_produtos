import re
from app.schemas.base import CustomBaseModel
from pydantic import validator


class Category(CustomBaseModel):
    name: str
    slug: str

    @validator('slug')
    def validate_slug(cls, v):
        if not re.match('^([a-z]|-|_)+$', v):
            raise ValueError('Invalid Slug')
        return v
