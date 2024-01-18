import sqlite3

conn = sqlite3.connect('.\\python.db')
cur = conn.cursor()

e_id  = 8
e_name  = 5
gen  = 6
addr  = 7

sql = f"""
    insert into emp 
    (e_id, e_name, gen, addr)
    values 
    ('{e_id}', '{e_name}', '{gen}', '{addr}')
    """
    
cur.execute(sql)
print(cur.rowcount)

conn.commit()

cur.close()
conn.close()