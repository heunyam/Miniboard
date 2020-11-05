from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from board.config import DATABASE_URL
engine = create_engine(DATABASE_URL, echo=True, encoding="utf-8", pool_size=20,
                       pool_recycle=3600, max_overflow=20, pool_pre_ping=True)

Session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))
session = Session()

Base = declarative_base()
