import sqlite3

conn = sqlite3.connect('.\\python.db')
cur = conn.cursor()

e_id  = 8

sql =   f"""
        DELETE FROM EMP
        WHERE 
            e_id='{e_id}'
        """
    
cur.execute(sql)
print(cur.rowcount)

conn.commit()

cur.close()
conn.close()