from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASES = create_engine('mysql+mysqldb://root:python@localhost:3305/python', echo = True)

Base = declarative_base()

class Emp(Base):
    __tablename__ = 'emp'

    e_id = Column(Integer, primary_key=True)
    e_name = Column(String(40))
    gen = Column(String(1))
    addr = Column(String(400))
    
    def __init__(self, e_id, e_name, gen, addr):
        self.e_id = e_id
        self.e_name = e_name
        self.gen = gen
        self.addr = addr


if __name__ == '__main__':

    Base.metadata.create_all(DATABASES)
    Session = sessionmaker()
    Session.configure(bind=DATABASES)
    session = Session()


    session.query(Emp).filter(Emp.e_id == 1).update({"e_name" : 3, "gen" : 3, "addr" : 3})
    session.commit()