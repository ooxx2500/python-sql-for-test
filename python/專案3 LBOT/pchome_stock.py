# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:10:11 2020

@author: ASUS
"""


import requests
from bs4 import BeautifulSoup
stock="2330" # 尋找股票號碼2347 聯強的資訊
url="https://tw.stock.yahoo.com/q/ts?s="+stock
headers = {

    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Connection': 'keep-alive'
}

list_req=requests.get(url,headers=headers)

soup=BeautifulSoup(list_req.content,"lxml")

tables=soup.find_all('table')


print(tables[2].find_all('td')[1].text) #股票名稱
TH=tables[3].find_all('tr')[0].find_all('td')
TD=tables[3].find_all('tr')[1].find_all('td')

title=[]

for i in TH:
    title.append(i.text)
    
