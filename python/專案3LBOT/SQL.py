# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:40:59 2020

@author: 莫再提
"""
import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a tta228').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# 創造表格的SQL指令 = '''CREATE TABLE account(
#    user_id serial PRIMARY KEY,
#    username VARCHAR (50) UNIQUE NOT NULL,
#    password VARCHAR (50) NOT NULL,
#    email VARCHAR (355) UNIQUE NOT NULL,
#    created_on TIMESTAMP NOT NULL,
#    last_login TIMESTAMP
# );'''

# cursor.execute(創造表格的SQL指令)
# conn.commit()

# cursor.close()
# conn.close()


cursor.execute("SELECT * FROM account")

data = []
while True:
    temp = cursor.fetchone()
    if temp:
        data.append(temp)
    else:
        break
print(data)