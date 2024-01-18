from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///test.db')
meta = MetaData()

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer),
)

meta.create_all(engine)

class CRUD:
    @staticmethod
    def insert(name, age):
        query = users.insert().values(name=name, age=age)
        conn = engine.connect()
        conn.execute(query)

    @staticmethod
    def select_all():
        query = users.select()
        conn = engine.connect()
        result = conn.execute(query)
        for row in result:
            print(row)

    @staticmethod
    def update_age(name, age):
        query = users.update().where(users.c.name==name).values(age=age)
        conn = engine.connect()
        conn.execute(query)

    @staticmethod
    def delete(name):
        query = users.delete().where(users.c.name==name)
        conn = engine.connect()
        conn.execute(query)

        
if __name__ == '__main__':
    print("-----데이터 입력-----")
    CRUD.insert('심교훈', 35)
    CRUD.insert('문태호', 36)
    CRUD.insert('황희', 33)
    
    print("-----데이터 조회-----")
    CRUD.select_all()
    
    print("-----데이터 수정-----")
    CRUD.update_age('심교훈', 31)

    print("-----데이터 조회-----")
    CRUD.select_all()

    print("-----데이터 삭제-----")
    CRUD.delete('심교훈')

    print("-----데이터 조회-----")
    CRUD.select_all()