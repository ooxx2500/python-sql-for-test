# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:28:54 2020

@author: ASUS
"""



from bs4 import BeautifulSoup
import random
import requests
import pandas as pd
input_text="三重"
url = 'http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json'
gets = requests.get(url)
df=pd.read_json(gets.text)
df2=df[['SiteName','County','AQI','Status','PM2.5']]
mask=  df2['SiteName'].values==input_text
sear=df2[mask]
retext=''
for i in sear.values:
    retext += '地區:%s'%i[0]+'\n'
    retext += '縣市:%s'%i[1]+'\n'
    retext += '品值:%s'%i[3]+'\n'
    retext += 'AQI:%s'%i[2]+'\n'
    retext += 'PM2.5:%s'%i[4]+'\n'

retext