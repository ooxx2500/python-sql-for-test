# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:52:37 2020

@author: 莫再提
"""

import json
import pandas as pd
with open(r'C:\Users\莫再提\Downloads\109交通A1.json',encoding = 'utf8')as file:
    data = json.load(file)    
    
        

#用pd將表格分成三藍
df = pd.DataFrame(data,columns=['發生時間','發生地點','車種'])

new_data=[] 
area_dic=dict() #地區分類
date_dic=dict() #月份車禍
cars_dic=dict() #車量分類字典
scooter_dic=dict()#機車字典一個縣市計重複出現次數#
scooter_area_dic=dict()#機車字典一個縣市只計一次#
total_scooter=0
total_cards=0
total_not_cars=0  #非四輪車總數
all_cars=[]
df=df.drop([768,769],axis=0) #刪除尾端三欄費資料

#----------------------------------------
for i in range(len(df)): #統計區域事故人數
    district = df['發生地點'][i][0:3]
    month_date =df['發生時間'][i][0:7]
    year=df['發生時間'][i][0:4]
    cars=df['車種'][i]
    all_cars.append(cars.split(';'))
    

    print(month_date)
    print(district)
    print(cars)
    print(all_cars)






#----------------------------------------

all_cars=[]
for i in df['車種']:
    all_cars.append(i.split(';'))


#機車字典一個縣市只計一次
for i in range(len(all_cars)): 
    for ii in all_cars[i]:
        if '機車' in ii:
            if df['發生地點'][i][0:3] not in scooter_area_dic:
                scooter_area_dic[df['發生地點'][i][0:3]] =1
                
            else:
                scooter_area_dic[df['發生地點'][i][0:3]] +=1
                
        break

#print(scooter_area_dic)
        
#機車字典一個縣市計重複出現次數
for i in range(len(all_cars)): 
    for ii in all_cars[i]:
        if '機車' in ii:
            if df['發生地點'][i][0:3] not in scooter_dic:
                scooter_dic[df['發生地點'][i][0:3]] =1
            else:
                scooter_dic[df['發生地點'][i][0:3]] +=1
       

#print(scooter_dic)
