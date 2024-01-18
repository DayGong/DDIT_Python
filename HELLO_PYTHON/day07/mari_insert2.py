import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', 
                       password='python', db='python', charset='utf8')

e_id = '4'
e_name = '4'
gen = '4'
addr = '4'

cur = conn.cursor()

sql =   f"""
        INSERT INTO EMP (e_id, e_name, gen, addr)
        VALUES ('{e_id}', '{e_name}', '{gen}', '{addr}')
        """
    
cnt = cur.execute(sql)
conn.commit()
print(cnt)

cur.close()
conn.close()