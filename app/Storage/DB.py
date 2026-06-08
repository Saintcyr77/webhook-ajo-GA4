from sqlalchemy import create_engine, Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from pydantic import BaseModel
from typing import Optional, List

engine = create_engine("sqlite:///events.db", connect_args={"check_same_thread":False})

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()
    try:
        yield db

    finally:
        db.close()

get_db()