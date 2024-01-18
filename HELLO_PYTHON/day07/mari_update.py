import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', 
                       password='python', db='python', charset='utf8')

e_id = '4'
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
    
cnt = cur.execute(sql)
conn.commit()
print(cnt)

cur.close()
conn.close()