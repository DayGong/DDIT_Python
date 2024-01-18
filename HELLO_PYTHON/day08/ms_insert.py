import pymssql

conn = pymssql.connect(server=r"(local)", user='sa', password='python', database='python')

cur = conn.cursor()

sql =   """
        INSERT INTO EMP (e_id, e_name, gen, addr)
        VALUES (3, 3, 3, 3)
        """
    
cur.execute(sql)
res = cur.rowcount
conn.commit()
print(res)

cur.close()
conn.close()