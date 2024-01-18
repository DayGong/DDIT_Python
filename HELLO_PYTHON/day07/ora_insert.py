import cx_Oracle

conn = cx_Oracle.connect("python", "python", "localhost:1521/xe")
cur = conn.cursor() # cursor() = statement와 같다.

e_id = 4
e_name = 4
gen = 4
addr = 4

sql =   f"""
        INSERT INTO EMP (E_ID, E_NAME, GEN, ADDR)
        VALUES ('{e_id}', '{e_name}', '{gen}', '{addr}')
        """
cur.execute(sql)

print(cur.rowcount)

cur.close()
conn.commit()
conn.close()