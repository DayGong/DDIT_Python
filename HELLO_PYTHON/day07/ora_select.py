import cx_Oracle

sql =   """
        select e_id, e_name, gen, addr
        from EMP
        """
conn = cx_Oracle.connect("python", "python", "localhost:1521/xe")
cur = conn.cursor() # cursor() = statement와 같다.
cur.execute(sql)

rows = cur.fetchall()

print(rows)
    
cur.close()
conn.close()