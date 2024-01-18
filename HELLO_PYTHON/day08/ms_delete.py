import pymssql

conn = pymssql.connect(server=r"(local)", user='sa', password='python', database='python')

e_id = '3'

cur = conn.cursor()

sql =   f"""
        DELETE FROM EMP
        WHERE 
            e_id='{e_id}'
        """
    
cur.execute(sql)
res = cur.rowcount
conn.commit()
print(res)

cur.close()
conn.close()