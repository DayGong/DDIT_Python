import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', 
                       password='python', db='python', charset='utf8')

cur = conn.cursor()

sql =   """
        INSERT INTO `EMP` (e_id, e_name, gen, addr)
        VALUES (%s, %s, %s, %s)
        """
    
cur.execute(sql, ('4', '4', '4', '4'))
res = cur.rowcount
print(res)

cur.close()
conn.commit()
conn.close()