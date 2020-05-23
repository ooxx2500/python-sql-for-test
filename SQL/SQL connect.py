# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
建立資料庫

CREATE DATABASE [if not exists] mona_db;

建立資料表
CREATE TABLE student_table(
_ID int ,
_Name varchar(30) ,
_Age date ,
_Sex varchar(2)  );

建立資料表三個欄位
CREATE TABLE table_name (欄位1 格式1 , 欄位2 格式2 , 欄位3 格式3)
CREATE TABLE customer(_ID int not null UNIQUE,
                     _name varchar(20) ,
                     _adress varchar(80))

創造資料表並將_id及_phone設定為主鍵
CREATE TABLE customer(_ID int not null,
                     _name varchar(20),
                     _phone varchar(50),
                     _address varchar(80),
                     CONSTRAINT pk_customer_id PRIMARY KEY (_ID , _phone))

建立資料表並將C_id 設為主鍵
CREATE TABLE order2(
    c_id int AUTO_INCREMENT,
    name varchar(50) ,
    address varchar(200) ,
    phone varchar(20),
    PRIMARY KEY(c_id));


修改資料表欄位
ALTER TABLE table_name MODIFY COLUMN 欄位名 格式
ALTER table table_1 MODIFY COLUMN  _HAHA varchar(10);

修改資料名稱 型態
ALTER TABLE table_name CHANGE  原欄位名 改的欄位名(沒改就用原本的) 欄位格式;
ALTER table table_1 CHANGE _gogogo _HAHA int;

刪除欄位
ALTER TABLE 表名 DROP COLUMN  欄位名
ALTER table table_1 DROP COLUMN  _gogogo;

在資料表新增欄位放在_ID後面
ALTER TABLE 資料表 ADD COLUMN 新欄位 新格式 after 欄位;
ALTER TABLE student ADD COLUMN _phone varchar(50) after _id;

在資料表新增欄位放在最前面
ALTER TABLE 資料表 ADD COLUMN 新欄位 新格式 first;
ALTER TABLE student ADD COLUMN _phone varchar(50) first;


一次增加多個欄位為UNIQUE								
ALTER TABLE customer ADD CONSTRAINT u_customer_id UNIQUE (_Name , cPrice);


一次設定多個主鍵給_id及_phone
ALTER TABLE student ADD CONSTRAINT pk_customer_id PRIMARY KEY (_ID , _Sex);


刪除資料庫
DROP DATABASE [IF EXISTS] mona;

刪除資料表
DROP TABLE [IF EXISTS] student;

刪除欄位
ALTER table table_1 DROP COLUMN  _gogogo;


清空資料表的內容
TRUNCATE TABLE student;



設定UNIQUE
ALTER TABLE customer ADD UNIQUE (c_id) ;

設定為外鍵(FOREIGN KEY)
CREATE TABLE _orders ( o_id int not null ,
                     order_No int not null,
                      cId int ,
                      PRIMARY KEY(o_id),
                      FOREIGN KEY(cId) REFERENCES guest(cId)
                      );

修改資料表增加外鍵
ALTER TABLE orders ADD FOREIGN KEY (cid) REFERENCES customer(cid) ; 

建立資料表有多個外鍵
CREATE TABLE orders_2 ( o_id int not null ,
                     order_No int not null,
                      cId int ,
                      mona int,
                      PRIMARY KEY(o_id),
                      CONSTRAINT fk_student_id FOREIGN KEY(mona) REFERENCES student(_ID)  );


建立一個VIEW
CREATE VIEW view_name (建立欄1 , 建立欄2) AS SELECT 欄位1, 欄位2 FROM 資料表

CREATE VIEW _view (product , p_sum) AS SELECT product , price * quantity from orders1





增加資料
INSERT INTO 資料表 (欄1 , 欄2 , 欄3) VALUES (資料1 ,資料2 資料3)
INSERT INTO orders1 (price , product , quantity) VALUES (60, apple , 5) , (80 , berry , 3) , (100, grape, 6);

複製舊資料到薪資料表
CREATE TABLE new_t2 SELECT cName , cPhone from customer;)

把女生男生分開複製到一個新的資料表
CREATE TABLE man SELECT * from students where csex = "m";
CREATE TABLE woman SELECT * from students where csex = "f";


更新資料
UPDATE grade 
SET name = “楊墨那” , math = 100
WHERE no =1

刪除資料(不會珊欄位)
DELETE FROM customers WHERE Name = “小嫩嫩”

清空資料表資料
DELETE FROM customers;

查詢資料
SELECT 欄位名稱 FROM 資料表 ;

查詢所有欄位
SELECT * FROM students ;

查詢欄位另外命名 AS
SELECT name AS 姓名 FROM student_table;

查詢特定欄位
SELECT name FROM student_table WHERE ID=10;

複製舊資料到薪資料表
CREATE TABLE new_t2 SELECT cName , cPhone from customer;)





'''

'''
以下版本為py執行檔與資料庫XX.db在同一路徑下
'''
--------------------------------------------

#import sqlite3模組 建立聯結
import sqlite3
#建立資料庫連結
#如果路徑不一樣請打r"C:\Users\ASUS\Desktop\Software\資料庫\students.db" 前面加r
conn = sqlite3.connect(r"C:\Users\莫再提\Desktop\Sql資料庫\students.db")
#執行SQL語法"select XXXX"
cursor = conn.execute ("select * from students")

#取出查詢結果的資料放在變數cursor
for row in cursor:
    print(row[0] ,row[1], row [2])
   
conn.close()

--------------------------------------------------


#建立資料庫+表
import sqlite3

sql = "CREATE TABLE students (id  int ,  name varchar(30) ,phone varchar(30) ,  email varchar(50) ) "
print(sql)
#連結資料庫 如果沒有就會建立一個資料庫
conn = sqlite3.connect(r"C:\Users\莫再提\Desktop\Sql資料庫\12345.db")
#執行SQL語法"select XXXX"
cursor = conn.execute (sql)
print(cursor.rowcount)
conn.commit()  
conn.close()



#帶入資料
import sqlite3
f=['1','mona','0920222888','ooxx55555@gmail.com']
sql = r"INSERT INTO students(id , name , phone , email) VALUES ('{0}','{1}','{2}','{3}') "
sql = sql.format(f[0], f[1],f[2] ,f[3])
print(sql)
conn = sqlite3.connect("12345.db")
#執行SQL語法"select XXXX"
cursor = conn.execute (sql)
print(cursor.rowcount)
conn.commit()   
conn.close()

#帶入資料 直接用語法寫
import sqlite3

sql = "INSERT INTO students(id , name , phone , email) VALUES (3 , 'god','0955222222','jsa@gmail.com') "
print(sql)
conn = sqlite3.connect("12345.db")
#執行SQL語法"select XXXX"
cursor = conn.execute (sql)
print(cursor.rowcount)
conn.commit()  
conn.close()

#SELECT

sql = "SELECT * FROM students "
conn = sqlite3.connect("12345.db")
#執行SQL語法"select XXXX"
cursor = conn.execute (sql)
for i in cursor:
    print(i[0],i[1],i[2],i[3])
conn.commit()  
conn.close()


-----------------------------------------------
import sqlite3

book = "今天天,氣很好,出去走走"
#用字串.split()方法切割文字字串
f = book.split(",")
print(f)

sql = "INSERT INTO book (id , name , price) VALUES ( '{0}' , '{1}' ,'{2}')"
sql = sql.format(f[0],f[1],f[2])

print(sql)
conn = sqlite3.connect(r"C:\Users\莫再提\Desktop\Sql資料庫\students.db")
#執行SQL語法"select XXXX"
cursor = conn.execute (sql)

print(cursor.rowcount)
conn.commit()
   
conn.close()
-----------------------------------------
#test區 一次建立多筆

txt = """id,name,phone,email 
1,mona,0920222222,oosdk@gmail.com 
2,judy,0983333333,dasf@yahoo.com.tw 
3,allan,0979555666,sadfas@yahoo.com 
4,sam,0983346565,dasfafafsf@gmail.com  
5,tami,098555555,dasdsa@gmail.com 
6, alal ,09865656,asdsad@gmail.com 
7,43534,09202222,fasfasdfas@gmail.com""" 
s = txt.split("\n")

import sqlite3

for i in s:     
    a=i.split(",")
    print(a)
    conn = sqlite3.connect(r"C:\Users\莫再提\Desktop\Sql資料庫\12345.db")
    sql = "INSERT INTO students (id , name , phone , email) \
    VALUES ( '{0}' , '{1}' ,'{2}','{3}')"
    sql = sql.format(a[0],a[1],a[2],a[3])
    cursor = conn.execute (sql)
    conn.commit()
    conn.close()

#執行SQL語法"select XXXX"


print(cursor.rowcount)





----------------------------------------------------------
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
db = pymysql.connect( "Localhost"  ,'root' ,'EcAVI31yZ1j00Q3H' ,'firstdb' ,charset='utf8')
test = db.cursor()  

sql = """select name , sum(score) from students group by name"""


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












