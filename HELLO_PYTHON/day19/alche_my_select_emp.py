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

if __name__ == '__main__':

    Session = sessionmaker()
    Session.configure(bind=DATABASES)
    session = Session()

    
    emps = session.query(Emp).all()
    
    for e in emps:
        print(e.e_id,e.e_name,e.gen,e.addr)
