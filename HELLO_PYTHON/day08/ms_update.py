import pymssql

conn = pymssql.connect(server=r"(local)", user='sa', password='python', database='python')

e_id = '3'
e_name = '6'
gen = '6'
addr = '6'

cur = conn.cursor()

sql =   f"""
        UPDATE EMP
        SET 
            e_name='{e_name}', 
            gen='{gen}', 
            addr='{addr}'
        WHERE 
            e_id='{e_id}'
        """
    
cur.execute(sql)
res = cur.rowcount
conn.commit()
print(res)

cur.close()
conn.close()