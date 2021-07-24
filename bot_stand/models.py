  
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import Integer, ForeignKey, String, Column, TIMESTAMP, BIGINT, Boolean, VARCHAR, NUMERIC,JSON
from bot_stand import settings

DeclarativeBase = declarative_base()

def db_connect():
    """ Performs database connections using database settings from settings.py
        Returns sqlalchemy engine instance
    """
    engine = create_engine(settings.postgres_connection_url, echo=True)
    return engine
def create_tables(engine):
    """create all tables """
    DeclarativeBase.metadata.create_all(engine)
class Models(DeclarativeBase):
    """
    Defines the items model
    """
    ############################ CREATING  TABLE#########################
    __tablename__ = "dummy"
    ############################ ADDING COLUMNS NAMES #########################

    content = Column("COLUMN_NAME_1",String, primary_key=True, nullable=False,)
    website_name = Column("COLUMN_NAME_2",String,  nullable=False)

    #############INITIALIZING COLUMN NAME WHEN TABLE IS CREATED ###########

    def __init__(self, content, website_name):

        self.content = content
        self.website_name = website_name