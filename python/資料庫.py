# -*- coding: utf-8 -*-
"""
#SQLite：
→是包含在一個相對小的C程式庫中的關聯式資料庫管理系統。
→不是一個用戶端/伺服器端結構的資料庫引擎。
→被整合在用戶程式中，使用動態的SQL語法操作。
→特性：
    →支援交易ACID(單一性、一致性、孤立性、耐久性)
    →無需設定與管理，因此若要管理，需要搭配第三方套件所提供的工具。
    →支援ANSI-SQL92語法(資料庫查詢語言標準)
    →資料庫系統是一個檔案。
    →檔案大小最大支援到2TB。
    →記憶體需求小：原始程式採用不到30000行的C語言撰寫，僅需要小於250KB的程式空間。
    →免費使用。
    →使用 unicode。

#Python使用sqlite3模組(2.5版以上已內建)
→使用方法：
    →sqlite3.connect：開啟資料庫的連結，成功開啟則傳回一個連線物件。
    →sqlite3.cursor：建立cursor(資料指標)
    →sqlite3.execute：執行SQL語法
    →sqlite3.commit：提交目前的交易(執行資料庫的操作)
    →sqlite3.rollback：回復上一次呼叫commit()對資料庫的更改。
    →sqlite3.close：關閉資料庫連結。
"""
#在資料庫新增一個table
import sqlite3
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
conn=sqlite3.connect(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\test.db')
print('opened database successfully')
c=conn.cursor()  #建立 cursor(游標物件) 供資料庫後續操作
#執行 SQL 指令，用c指向執行SQL語法
c.execute(''' Create table COMPANY1 
          (ID int primary key not null,
          NAME text not null,
          AGE int not null,
          ADDRESS char(50),
          SALARY real);''')
print('table created successfully')
conn.commit() #執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
conn.close()  #關閉資料庫
--------------------------------
#新增資料
import sqlite3

#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
conn = sqlite3.connect(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\test.db')

#建立 cursor(游標物件) 供資料庫後續操作 **** 有跟沒有一樣可以統一用conn代替 ****
c = conn.cursor()
print("Opened database successfully")

#執行 SQL 指令
#新增記錄(insert into)
c.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (1, 'Paul', 32, 'California', 20000.00 )");
c.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
c.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
c.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

#執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
conn.commit()
print("Records created successfully")

#關閉資料庫(不會自動呼叫 commit())
conn.close()
------------------------------------
#查詢資料
import sqlite3

conn = sqlite3.connect(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\test.db')
c = conn.cursor()
print("Opened database successfully")
#執行 SQL 指令
#查詢記錄(select)
cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
#以 cursor 物件c 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
#以迴圈將查詢結果 cursor 中每一筆記錄取出(row物件)，
#再以索引將記錄的欄位資料取得後設定給對應的變數，取得後顯示。
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
print("Operation done successfully")

#關閉資料庫(不會自動呼叫 commit())
conn.close()
---------------------------
#修改資料庫
import sqlite3

conn = sqlite3.connect(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\test.db')
c = conn.cursor()
print("Opened database successfully")
#執行 SQL 指令
#更新記錄(update set)
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit()
#conn.total_changes：取得資料庫改變(修改、新增)的總次數。
print("Total number of rows updated :", conn.total_changes)

#執行 SQL 指令
#更新記錄(select)
#以連線物件 conn 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
#以迴圈將查詢結果 cursor 中每一筆記錄取出(row物件)，
#再以索引將記錄的欄位資料取得後顯示。
cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
print("Operation done successfully")

#關閉資料庫(不會自動呼叫 commit())
conn.close()

---------------------------------
#刪除資料庫
import sqlite3
conn = sqlite3.connect(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\test.db')
c = conn.cursor()
print("Opened database successfully")

#執行 SQL 指令
#刪除記錄(delete)
c.execute("DELETE from COMPANY1 where ID=2;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)
cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
print("Operation done successfully")
conn.close()

-----------------------------------------------------
#連結MYSQL

import pymysql

#建立資料連結 ('127.0.0.1'或'Localhost' , '帳號' , '密碼' ,'資料庫名' '編碼 UTF8')
db = pymysql.connect( "Localhost"  ,'root' ,'AQpseHAsZTk07pB4' ,'firstdb' ,charset='utf8')
test = db.cursor()  #建立cursor物件 
test.execute("select * from table_1")
data = test.fetchall() #取出所有紀錄
#取出查詢結果每一筆
for row in data:
    print(row[0],row[1])
db.close()
-----------------------------------------------
#建立資料給MYSQL
import pymysql
student ="9,mon,忠孝東路50號,0920555888"
a= student.split(",")
print(a)
#建立資料連結 ('127.0.0.1'或'Localhost' , '帳號' , '密碼' ,'資料庫名' '編碼 UTF8')
db = pymysql.connect( "Localhost"  ,'root' ,'AQpseHAsZTk07pB4' ,'firstdb' ,charset='utf8')
test = db.cursor()  #建立cursor物件 
sql = """INSERT INTO order2 (c_id,name ,address, phone) 
VALUES ( '{0}' , '{1}' ,'{2}' ,'{3}')"""
sql = sql.format(a[0],a[1],a[2],a[3])

#sql = """ INSERT INTO `order2` ( `name`, `address`, `phone`) VALUES ( '5555dgsdg', 'sdgsdg', 'sdggsdgs');"""
print(sql)

test.execute(sql)
db.commit()
db.close()


data = test.fetchall()

print(data)




import pymysql
#建立資料連結 ('127.0.0.1'或'Localhost' , '帳號' , '密碼' ,'資料庫名' '編碼 UTF8')
db = pymysql.connect( "Localhost"  ,'root' ,'1111' ,'firstdb' ,charset='utf8')
test = db.cursor()  #建立cursor物件 
#sql = """INSERT INTO 'order2' ('c_id','name' ,'address', 'phone') VALUES ( '{0}' , '{1}' ,'{2}' ,'{3}')"""
#sql = sql.format(a[0],a[1],a[2],a[3])

sql = """ select sum(c_id) from order2"""


a=test.execute(sql)
data = test.fetchall()

print(data)
db.commit()
db.close()




----------------------------------------------------
#執行單機版SQL語法

import sqlite3

sql = "INSERT INTO students(id , name , phone , email) VALUES (3 , 'god','0955222222','jsa@gmail.com') "


print(sql)
conn = sqlite3.connect("12345.db")
cursor = conn.execute (sql)
print(cursor.rowcount)
conn.commit()  
conn.close()




#執行PHP SQL語法

import pymysql
db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
test = db.cursor()  

sql = """select name from students group by name"""


a=test.execute(sql)
db.commit()
db.close()

data = test.fetchall()
for i in data:
    print(i)


#PHP自動輸入資料區

txt = """mona,0920222222,oosdk@gmail.com,188
judy,0983333333,dasf@yahoo.com.tw,799
allan,0979555666,sadfas@yahoo.com,555
sam,0983346565,dasfafafsf@gmail.com,12
tami,098555555,dasdsa@gmail.com,34
alal ,09865656,asdsad@gmail.com,79
43534,09202222,fasfasdfas@gmail.com,588""" 
s = txt.split("\n")

import pymysql

db = pymysql.connect( "Localhost"  ,'root' ,'EcAVI31yZ1j00Q3H' ,'firstdb' ,charset='utf8')
test = db.cursor() 


for i in s:     
    a=i.split(",")
    print(a)
    
    sql = "INSERT INTO students ( name , phone, email, score) VALUES ( '{0}' , '{1}' ,'{2}','{3}')"
    sql = sql.format(a[0],a[1],a[2],a[3])
    print(sql)
    result = test.execute(sql)
    data = test.fetchall()
    db.commit()
db.close()











