import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', 
                       password='python', db='python', charset='utf8')

cur = conn.cursor(pymysql.cursors.DictCursor) #Dictionary 사전 배열, 연관 배열

sql = """ 
    SELECT e_id, e_name, gen, addr
    FROM emp
    """
    
cur.execute(sql)
result = cur.fetchall()

print(result)

conn.close()