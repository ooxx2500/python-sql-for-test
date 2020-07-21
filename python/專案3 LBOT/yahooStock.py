# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:09:50 2020

@author: ASUS
"""


import requests
from bs4 import BeautifulSoup
stock="2330" # 尋找股票號碼2347 聯強的資訊
url="https://tw.stock.yahoo.com/q/q?s="+stock
list_req=requests.get(url)
soup=BeautifulSoup(list_req.content,"lxml")



tables=soup.find_all('table')
tds=tables[2].find_all('td')
print(tds[2].text) #成交
print(tds[5].text.strip()[1:]) #漲跌
print(tds[7].text) #昨收
print(tds[9].text) #最高
print(tds[10].text) #最低