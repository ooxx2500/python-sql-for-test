# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:07:51 2020

@author: 莫再提
"""

import requests
from bs4 import BeautifulSoup

#查詢車輛登記網址 https://stat.motc.gov.tw/mocdb/stmain.jsp?sys=100&funid=b3301 
#107年 
htm='https://stat.motc.gov.tw/mocdb/stmain.jsp?sys=220&ym=10701&ymt=10712&kind=21&type=9&funid=b330102&cycle=1&outmode=0&compmode=0&outkind=1&fld21=1&codspc0=0,6,8,1,11,1,14,15,&rdm=4pgqhmtm'

#108年 
#htm='https://stat.motc.gov.tw/mocdb/stmain.jsp?sys=220&ym=10801&ymt=10812&kind=21&type=9&funid=b330102&cycle=1&outmode=0&compmode=0&outkind=1&fld21=1&codspc0=0,6,8,1,11,1,14,15,&rdm=lxacdcYa'
#109年1-5月 
#htm='https://stat.motc.gov.tw/mocdb/stmain.jsp?sys=220&ym=10901&ymt=10905&kind=21&type=9&funid=b330102&cycle=1&outmode=0&compmode=0&outkind=1&fld21=1&codspc0=0,6,8,1,11,1,14,15,&rdm=9eWWqani'


html = requests.get(htm).text 


soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table',class_='tblcls') 

trs =  table.find_all('tr')
area_ths=trs[1].find_all('th')
area_list=[] #縣市

for th in area_ths: #爬縣市
    area_list.append(th.text.strip())
del area_list[0]

all_cars_data=[]
    
for i in range(len(trs)): #爬放在TD內的數據
    tds=trs[i].find_all('td')
    all_cars_data.append([])
    for td in tds:
        if td.text==''or eval(td.text.strip().replace(',',''))=='':
            continue
        else:
        
            all_cars_data[i].append(eval(td.text.strip().replace(',','')))        

del all_cars_data[0:2] #刪除前兩個[] []的串列

import pandas as pd
import numpy as np





df=pd.DataFrame(all_cars_data,columns=area_list)
#print(all_cars_data_array)


df=df.drop(['總計','臺灣地區'],axis=1) #刪除兩欄沒用的資訊
print(df)
total_area_dict=dict()   #加總個欄位的數量
for area in df:
    t=df[area].sum()
    total_area_dict[area]=t
    
print(total_area_dict)


