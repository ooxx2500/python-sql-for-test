# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:08:48 2020

@author: 莫再提
"""



data=[]
import json

import pandas as pd

with open(r'C:\Users\莫再提\Desktop\J.json',encoding = 'utf8')as file:
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
    


