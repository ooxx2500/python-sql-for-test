# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:33:32 2020

@author: ASUS
"""


from tkinter import *
import pymysql
import time
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv(r"C:\Users\莫再提\Documents\python-sql-for-test\python\專案3LBOT\stockname.csv")
df=df[['證劵代號','證劵名稱']]
stock_num=[]
for i in df['證劵代號']:
    stock_num.append(i)
#print(stock_num)

stock_name=[]
for i in df['證劵名稱']:
    stock_name.append(i.strip())
#print(stock_name)



#--------------------------------------------


s_name="中信"  #搜尋名稱

a=df['證劵代號']
b=df['證劵名稱']
c=df['證劵名稱'].str.contains(s_name)
d=df[c]
e=d['證劵名稱']
f=[]

for i in e:
    f.append(i.strip())
 
if len(d)==0:
    print("查無資料")
    
elif len(d)==1 and s_name==f:
    print("找到拉")
    for i in d['證劵名稱']:
        print(i)
    for i in d['證劵代號']:
        print(i)
        
elif len(d)>1 and (s_name ==f[0]):
    print("找到拉 但是好多個我只給你最少字的")
    getstock_num=[]
    
    for i in d['證劵代號']:
        getstock_num.append(i)
    print(getstock_num[0])
       
else:
    print("沒找到")
    for i in d['證劵名稱']:
        print(i)

    
    
    
