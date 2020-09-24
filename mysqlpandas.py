import pandas as pd
import pymysql
from datetime import datetime

print('[mysql select 내용 출력 프로그램]')
print('start-time : ', str(datetime.now())[:19] )

conn = pymysql.connect(
    user='user',
    password='password',
    host='hostname',
    db='dbname',
    charset='utf8'
)

cursor = conn.cursor()
cursor.execute("set names utf8")

query = "select * from user; "

df = pd.read_sql_query(query, conn)
df.rename(columns={'id':'ID'}, inplace=True)
df.to_csv(r'select리스트.csv', index=False)

print('end-time : ', str(datetime.now())[:19])
