# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:58:12 2020

@author: ooxx2
"""

import csv
data=[]
with open(r'C:\Users\ooxx2\Desktop\108年交通B.csv','r',encoding = 'utf8') \
    as csvfile:#用編碼utf8開啟
        plots = csv.reader(csvfile, delimiter = ',')#用reader方法讀取 plots是個串列
                              #用delimiter設定資料以逗號分隔字元，藉以取出每個資料
    
        for i in plots:
            data.append(i)

del data[0]
del data[-2:]

new_data=[] 
area_dic=dict()
date_dic=dict()
for i in range(len(data)): #統計區域事故人數
    address = data[i][1]
    district = address[0:3] #取出XX市
    date = data[i][0]
    month_date =date[0:7]#取出年度月份
    
    if district not in area_dic:
        area_dic[district]=1
    else:
        area_dic[district] +=1
        
    if month_date not in date_dic:
        date_dic[month_date]=1
    else:
        date_dic[month_date] +=1
        
print(area_dic)
print(date_dic)

a = sorted(area_dic.items(), key=lambda item:item[1]) #照字典的V排序   

print(a)

print(a[0][0])

b = sorted(date_dic.items(), key=lambda item:item[1]) #照字典的V排序   

print(b)

print(b[0][0])






