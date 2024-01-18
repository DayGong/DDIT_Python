import pymssql

class DaoMem:
    def __init__(self):
        self.conn = pymssql.connect(server=r"(local)", user='sa', password='python', database='python')

        self.curs = self.conn.cursor(as_dict=True) #Dictionary 사전 배열, 연관 배열

    
    def selectList(self):
        sql = """ 
            SELECT mem_id, mem_name, tel, email
            FROM mem
            """
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def select(self, mem_id):
        sql = f""" 
            SELECT mem_id, mem_name, tel, email
            FROM mem
            WHERE mem_id = '{mem_id}'
            """

        self.curs.execute(sql)
        row = self.curs.fetchone()
        
        return row
    
    def insert(self, mem_id, mem_name, tel, email):
        sql =   f"""
            INSERT INTO mem (mem_id, mem_name, tel, email)
            VALUES ({mem_id}, {mem_name}, {tel}, {email})
            """
        self.curs.execute(sql)
        self.conn.commit()
        
        return self.curs.rowcount
    
    def update(self, mem_id, mem_name, tel, email):
        sql = f""" 
            UPDATE mem
            SET
                mem_name='{mem_name}',
                tel='{tel}',
                email='{email}'
            WHERE
                mem_id='{mem_id}'
            """
            
        self.curs.execute(sql)
        self.conn.commit()
        
        return self.curs.rowcount
    
    def delete(self, mem_id):
        sql =   f"""
        DELETE FROM mem
        WHERE 
            mem_id='{mem_id}'
        """

        self.curs.execute(sql)
        self.conn.commit()
        
        return self.curs.rowcount
            
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoMem()
    cnt = de.delete()
    print(cnt)