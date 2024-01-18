import cx_Oracle

conn = cx_Oracle.connect("python", "python", "localhost:1521/xe")
cur = conn.cursor() # cursor() = statement와 같다.

e_id = 5
e_name = 6
gen = 6
addr = 6

sql =   f"""
        UPDATE EMP 
        SET 
            E_NAME='{e_name}', 
            GEN='{gen}', 
            ADDR='{addr}'
        WHERE 
            E_ID = '{e_id}'
        """
cur.execute(sql)

print(cur.rowcount)

cur.close()
conn.commit()
conn.close()