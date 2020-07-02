# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:28:56 2020

@author: mona
"""

import pymysql
db =pymysql.connect('114.34.72.123','admin','Cspraqf3!','member')
test=db.cursor()


a=test.execute("""SELECT * From ppj.data""")
# db.commit()
# db.close()

data = test.fetchall()
for i in data:
    print(i)