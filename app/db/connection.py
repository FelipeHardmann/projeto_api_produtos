'''
    O comando poll_pre_ping
    significa que sempre vai ter
    um ping no banco de dados
    Garantindo que ou vai dar error
    ou o banco vai estar funcionando

    -- A instância da sessionMaker,
    cria a sessão e só é inicializada
    quando a instância for chamada
'''

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL: str = config('DB_URL')

engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker()
