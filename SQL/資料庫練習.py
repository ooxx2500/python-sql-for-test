# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:15:50 2020

@author: mona
"""
# import pymysql
# db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
# test = db.cursor()  



# test.execute("""INSERT INTO `momom` (`id_`, `name`, `price`, `qualianty`) VALUES (NULL, 'Mmo', '20', '10');""")
# test.execute("""INSERT INTO `momom` (`id_`, `name`, `price`, `qualianty`) VALUES (NULL, 'dasd', '30', '20');""")
# test.execute("""INSERT INTO `momom` (`id_`, `name`, `price`, `qualianty`) VALUES (NULL, 'ords', '1', '18');""")

# test.execute("""SELECT * FROM momom;""")
# db.commit()


# data = test.fetchall()

# for row in data:
#     print(row[0],row[1])
# print(data)
# db.close()


# ----------------------------------------------------------------
#查詢姓名
def serch_name():
    search_name=input('搜尋姓名:')

    if search_name in df['name'].values:
        mask=df.iloc[:,1]==search_name
        print(df[mask])
    else:
        print("無此關鍵字")
        
        
import pymysql
import pandas as pd
db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
test = db.cursor() 
#df=pd.read_sql("""SELECT id_, name FROM momom""",con=db) #用read_sql(con=db)可以直接讀取資料庫表格
df=pd.read_sql("""SELECT * FROM momom""",con=db)
print(df)
print(df.shape) #顯示row column數
print(df.dtypes) #顯示欄位資料類型



        
#練習扣庫存
        
ids=10#int(input("輸入ID:"))
index=df['id_']
print(index)


# quantity=df['qualianty'].iloc[ids-1]
print("數量還剩:",quantity) 
       
SQL_update="UPDATE `momom` SET `qualianty` = '9' WHERE `momom`.`id_` = 1 and `qualianty`>0; "



#test.execute("UPDATE `momom` SET `qualianty` = '9' WHERE `momom`.`id_` = 1 and `qualianty`>0; ")

# db.commit()
# df=pd.read_sql("""SELECT * FROM momom""",con=db)
print(df)
# data = test.fetchall()
# db.close()


# mask=df.iloc[:,1]=='momo'
# print(df[mask])

























