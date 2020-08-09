from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    
    """
    return create_engine(URL(**settings.DATABASE))

class DataPrices(DecarativeBasse):
    __tablename__ = "crypto_currencies_price"
    
    id = Column(Integer,primary_key = True)
    crypto_currency = Column('crypto_currency',String)
    price = column('price',float8)

