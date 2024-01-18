import sqlite3

conn = sqlite3.connect('.\\python.db')
cur = conn.cursor()

e_id  = 8
e_name  = 8
gen  = 8
addr  = 8

sql = f"""
        UPDATE EMP
        SET 
            e_name='{e_name}', 
            gen='{gen}', 
            addr='{addr}'
        WHERE 
            e_id='{e_id}'
        """
    
cur.execute(sql)
print(cur.rowcount)

conn.commit()

cur.close()
conn.close()