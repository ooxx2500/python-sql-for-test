# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:15:50 2020

@author: mona
"""
# import pymysql
# db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
# test = db.cursor()  



# test.execute("""INSERT INTO `momom` (`id_`, `name`, `price`, `qualianty`) VALUES (NULL, 'momo', '2', '10');""")
# test.execute("""INSERT INTO `momom` (`id_`, `name`, `price`, `qualianty`) VALUES (NULL, 'gigi', '9', '6');""")
# test.execute("""INSERT INTO `momom` (`id_`, `name`, `price`, `qualianty`) VALUES (NULL, 'gugu', '9', '88');""")

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
        

#練習扣庫存
def sellsomething():
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    test = db.cursor()
    in_id=eval(input("請輸入ID:"))
    try:
        check=df['id_']==in_id
    except Exception as err:
        print(err)
    print("======= 資料如下 =======")
    print(df[check])
    print('===========================')
    quantity=df[check]['qualianty'].values[0]
    print("數量還剩:",quantity) 
    sell=eval(input("賣出數量:"))
    if sell >quantity:
        print('交易錯誤，庫存不足。')
        db.close()
    else:
        remain_number=quantity-sell #剩餘數量       
        SQL_update="UPDATE `momom` SET `qualianty` = '{0}' WHERE `momom`.`id_` = {1} and `qualianty`>{2}; "
        SQL_update=SQL_update.format(remain_number, in_id, sell )
        test.execute(SQL_update)#資料庫進行扣除
        db.commit()
        df=pd.read_sql("""SELECT * FROM momom""",con=db)
        print("交易成功，賣出%d，剩餘%d"%(sell, (quantity-sell)))
        print('=================================')
        print(df[check])
        print('=================================')
        db.close()

#補貨增加數量
def add_storage():
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    test = db.cursor()
    in_id=eval(input("請輸入ID:"))
    try:
        check=df['id_']==in_id
    except Exception as err:
        print(err)
    print("======= 資料如下 =======")
    print(df[check])
    print('===========================')
    quantity=df[check]['qualianty'].values[0]
    print("數量還剩:",quantity) 
    storage=eval(input("存入數量:"))
    if storage<=0:
        print('存入錯誤，不得為0或負數。')
        db.close()
    else:
        last_number=quantity+storage #存後數量       
        SQL_update="UPDATE `momom` SET `qualianty` = '{0}' WHERE `momom`.`id_` = {1}; "
        SQL_update=SQL_update.format(last_number, in_id )
        test.execute(SQL_update)#資料庫進行相加
        db.commit()
        df=pd.read_sql("""SELECT * FROM momom""",con=db)
        print("交易成功，存入%d，庫存%d"%(storage, (last_number)))
        print('=================================')
        print(df[check])
        print('=================================')
        db.close()
        
        
import pymysql
import pandas as pd
db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
test = db.cursor() 
#df=pd.read_sql("""SELECT id_, name FROM momom""",con=db) #用read_sql(con=db)可以直接讀取資料庫表格
df=pd.read_sql("""SELECT * FROM momom""",con=db)
db.close()

print(df['id_']<10)


# first_choose=eval(input("請選擇查詢區間 1:自定區間 2:全查"))
# if first_choose==1:
#     start=eval(input("請輸入查詢ID起始點:"))
#     end=eval(input("請輸入查詢ID終止點:"))
#     print(df[start:end])

# else:    
#     print(df)
    
    
# print("顯示row column數",df.shape) #顯示row column數
# print("顯示欄位資料類型",df.dtypes) #顯示欄位資料類型



#查詢ID區間


















