import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', 
                       password='python', db='python', charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor) #Dictionary 사전 배열, 연관 배열

    
    def selectList(self):
        sql = """ 
            SELECT e_id, e_name, gen, addr
            FROM emp
            """
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def select(self, e_id):
        sql = f""" 
            SELECT e_id, e_name, gen, addr
            FROM emp
            WHERE e_id='{e_id}'
            """
        self.curs.execute(sql)
        
        vo = self.curs.fetchone()
        return vo
    
    def insert(self, e_id, e_name, gen, addr):
        sql = f"""
            INSERT INTO EMP (e_id, e_name, gen, addr)
            VALUES ('{e_id}', '{e_name}', '{gen}', '{addr}')
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def update(self, e_id, e_name, gen, addr):
        sql =   f"""
            UPDATE EMP
            SET 
                e_name='{e_name}', 
                gen='{gen}', 
                addr='{addr}'
            WHERE 
                e_id='{e_id}'
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def delete(self, e_id):
        sql =   f"""
            DELETE FROM EMP
            WHERE 
                e_id='{e_id}'
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
            
    def __del__(self):
        self.curs.close()
        self.conn.close()