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

    Session = sessionmaker()
    Session.configure(bind=DATABASES)
    session = Session()


    sam = Emp('4','4','4', '4')
    session.add(sam)
    session.commit()
    