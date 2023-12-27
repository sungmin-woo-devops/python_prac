from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASe = 'postgresql://postgres:postgres@localhost:5432/QuizApplication'

engine = create_engine(URL_DATABASe)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

