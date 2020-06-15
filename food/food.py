"""

import sqlite3
conn = sqlite3.connect(r'C:\Users\ASUS\Desktop\SQL\food.db')

#建立 cursor(游標物件) 供資料庫後續操作 **** 有跟沒有一樣可以統一用conn代替 ****
c = conn.cursor()
print("Opened database successfully")

#執行 SQL 指令
#新增記錄(insert into)

c.execute("""INSERT INTO food (NAME,AVG_PRICE,ADDRESS,FOOD_TYPE) \
 VALUES ('燒肉店', 115, '你知道的', '燒肉飯');""")
c.execute("""INSERT INTO food (NAME,AVG_PRICE,ADDRESS,FOOD_TYPE) \
 VALUES ('饌香味', 80, '你知道的', '鍋貼水餃麵');""")
c.execute("""INSERT INTO food (NAME,AVG_PRICE,ADDRESS,FOOD_TYPE) \
 VALUES ('人人人人', 150, '你知道的', '牛排');""")

#執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
conn.commit()
print("insert data successfully")

#關閉資料庫(不會自動呼叫 commit())
conn.close()
"""
----------------------------------

import sqlite3
import random
conn = sqlite3.connect(r'C:\Users\ASUS\Desktop\SQL\food.db')
c = conn.cursor()
print("Opened database successfully")

lis =c.execute("""SELECT name,avg_price FROM FOOD  """)
conn.commit()
lis1=[]
for i in lis:
    lis1.append(i)
r_num = random.randint(0,len(lis1)-1)

print(lis1[r_num])
conn.close()

