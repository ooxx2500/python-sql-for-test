# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 21:04:28 2020

@author: 莫再提
"""

from tkinter import *
import pymysql
import time
import pandas as pd
import matplotlib.pyplot as plt
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}#設定字形樣式大小
plt.rc('font', **font) #設定PY繪圖系統的字型項目  

db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
test = db.cursor() 
df=pd.read_sql("""SELECT * FROM momom""",con=db)
db.close()

# test.execute("Update momom SET name='喇叭' WHERE id_%5=0")
# db.commit()
print(df['name'])
if '喇叭' in df['name'].values:
    print(666666666666666)
