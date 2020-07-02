# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:15:50 2020

@author: mona
"""
# import pymysql
# db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
# test = db.cursor()  


# test.execute("""SELECT * FROM momom;""")
# test.execute("""INSERT INTO `momom` (`id_`, `name`, `price`, `qualianty`) VALUES (NULL, 'juju', '20', '1');""")
# test.execute("""INSERT INTO `momom` (`id_`, `name`, `price`, `qualianty`) VALUES (NULL, 'didi', '34', '6');""")
# test.execute("""INSERT INTO `momom` (`id_`, `name`, `price`, `qualianty`) VALUES (NULL, 'oril', '17', '18');""")


# db.commit()


# data = test.fetchall()

# for row in data:
#     print(row[0],row[1])
# print(data)
# db.close()


# ----------------------------------------------------------------

import pymysql
import pandas as pd
db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
test = db.cursor()  


# test.execute("""UPDATE `momom` SET `qualianty` = '9' WHERE `momom`.`id_` = 1 and `qualianty`>0; """)

test.execute("""SELECT * FROM momom;""")
# db.commit()


data = test.fetchall()
db.close()
# for row in data:
#     print(row[0],row[1],row[2],row[3])


df=pd.DataFrame(data)
print(df)
print('-------------------------')
# mask=df.iloc[:,1]=='momo'
# print(df[mask])

search_name=input('搜尋姓名')

if search_name in df[1].values:
    mask=df.iloc[:,1]==search_name
    print(df[mask])


print(2)

























