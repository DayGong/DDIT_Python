from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

DATABASES = create_engine('oracle://python:python@localhost:1521/xe', echo=True)

Base = declarative_base()

class Sample(Base):
    __tablename__ = 'sample'

    col01 = Column(Integer, primary_key=True)
    col02 = Column(String(20))
    col03 = Column(String(20))

    def __init__(self, col01, col02, col03):
        self.col01 = col01
        self.col02 = col02
        self.col03 = col03


if __name__ == '__main__':

    Base.metadata.create_all(DATABASES)
    Session = sessionmaker()
    Session.configure(bind=DATABASES)
    session = Session()

    
    samples = session.query(Sample).all()
    
    for s in samples:
        print(s.col01,s.col02,s.col02)
