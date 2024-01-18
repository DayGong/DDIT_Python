import pymssql

# https://velog.io/@hkjs96/2020-11-25-python
conn = pymssql.connect(server=r"(local)", user='sa', password='python', database='python')

cur = conn.cursor(as_dict=True)

sql = """ 
    SELECT e_id, e_name, gen, addr
    FROM emp
    """

cur.execute(sql)

rows = cur.fetchall()
print(rows)

cur.close()
conn.close()