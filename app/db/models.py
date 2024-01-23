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
    String
)


class Category(Base):
    __tablename__ = 'categories'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
