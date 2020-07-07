# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:08:48 2020

@author: 莫再提
"""



data=[]
import json

import pandas as pd

with open(r'C:\Users\mona\Desktop\gogog.json.json',encoding = 'utf8')as file:
    rf_1 = json.load(file)
       
rf=pd.DataFrame(rf_1)


lst=[]
for i in rf['responseData']:
    lst.append(i)

rf2=pd.DataFrame(lst)

rf2=rf2.drop(368)
rf2=rf2.drop(369)

new_column=pd.DataFrame()
new_column['縣市']=rf2['site_id'].str[0:3].apply(lambda x:x[0:3])
rf2=pd.concat([rf2,new_column], axis=1)
rf2['people']=rf2['people'].astype(int)
rf2['area']=rf2['area'].astype(float)
rf2['population_density']=rf2['population_density'].astype(float)
print(rf2.info())


#排序後找出人口最低的縣市
rf2=rf2.sort_values('people', ascending=False)
print(rf2['縣市'].tail(3))
print(rf2['縣市'].tail(3).values)
#找出縣市別並插入後面
# aaaa=rf2.groupby('縣市').sum()
# aaaa=aaaa.sort_values('people').head(5)
# print(aaaa)
# target=aaaa.loc['金門縣',:]
# print(target)
# print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

#找出pandas中的特定自並印出來
# df1=rf2['site_id']
# print(df1)
# df1=rf2['site_id']=='新北市三重區'
# print(rf2[df1])

#找出區間 用兩次mask 4000~5000

# rr=(rf2['people']<5000)
# rf2=rf2[rr]
# rr=(rf2['people'][rr]>4000)
# print(rf2[rr])

    


'''
citis=set()
for i in rf2['縣市']:
    citis.add(i)
    
print(citis)
areas=[]
for i in citis:
    new=[]       
    mask=rf2['縣市']==i #mask=過濾器
    total_people=rf2[mask]['people'].sum()
    total_area=rf2[mask]['area'].sum()
    new.append(i)
    new.append(total_people)
    new.append(total_area)
    areas.append(new)
print(areas)



for i in areas:
    print(i)
   
'''