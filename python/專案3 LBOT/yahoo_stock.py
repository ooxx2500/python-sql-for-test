# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:58:49 2020

@author: ASUS
"""


import requests
from bs4 import BeautifulSoup
stock="2330" # 尋找股票號碼2347 聯強的資訊
url="https://tw.stock.yahoo.com/q/q?s="+stock
list_req=requests.get(url)
soup=BeautifulSoup(list_req.content,"lxml")
#getstock=soup.find('b').text
#print(getstock)
getstock=soup.findAll("b")[1].text
print("%s的即時股價:%s" % (stock,getstock))