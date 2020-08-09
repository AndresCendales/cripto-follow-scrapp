from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import scrapper_crypto_follow.settings as settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Conecta con la base de datos relacionada en settings    
    """
    return create_engine(URL(**settings.DATABASE))

class DataPrices(DeclarativeBase):
    """
    Modelo para guardar la informacion del item generado en los spiders
    """

    __tablename__ = "crypto_currencies_price"
    
    id = Column(Integer,primary_key = True)
    date = Column('date')
    crypto_currency = Column('crypto_currency',String)
    price = Column('price')
    source = Column('source')
    time_stamp = Column('time_stamp')
