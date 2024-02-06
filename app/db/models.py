'''
    Migrations com alembic
    As migrations servem para
    refltir alterações que
    acontecem no banco de
    dados.
    É interessante rodarmos as
    migrations dentro do container

    Se utilizarmos o seguinte comando:
    docker compose run --user 1000 app sh -c 'alembic init migrations'
    Teremos permissão para modificar
    os arquivos do alembic

    --- O revision cria um script na versão

    Esse é o comando para executar:
    docker compose run --user 1000 app sh -c 'alembic upgrade head'
'''

from app.db.base import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Float,
    func
)
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'categories'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    products = relationship('Product', back_populates='category')


class Product(Base):
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    price = Column('price', Float, nullable=False)
    stock = Column('stock', Integer)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())
    category_id = Column(
        'category_id', ForeignKey('categories.id'), nullable=False
    )
    category = relationship('Category', back_populates='products')
