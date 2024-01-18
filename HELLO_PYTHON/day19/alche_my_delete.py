from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASES = create_engine('mysql+mysqldb://root:python@localhost:3305/python', echo = True)

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


    session.query(Sample).filter(Sample.col01 == 1).delete()
    session.commit()
    
    
    