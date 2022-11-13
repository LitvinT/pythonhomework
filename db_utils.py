from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from models import *
from setting import DB_PATH

def create_dbsession(db_path=None, **kwargs):
    db_path = db_path or DB_PATH
    engine = create_engine(db_path)
    SessionClass = sessionmaker(bind=engine)
    return SessionClass
