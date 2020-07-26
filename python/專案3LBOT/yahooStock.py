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
stock_range=(eval(tds[2].text)-eval(tds[7].text))*100/eval(tds[7].text)


retext=tds[0].text.replace('加到投資組合','')+"\n"+"成交時間:"+tds[1].text+"\n"+"成交價:"+tds[2].text+"\n"+"漲跌:"+tds[5].text.strip()[:]+"\n"+ "漲跌幅: %.2f%%"%stock_range


print(retext)
 
# print(tds[0].text.replace('加到投資組合',''))
# print("成交時間:",tds[1].text)
# print("成交價:",tds[2].text) #成交
# print("漲跌:",tds[5].text.strip()[:]) #漲跌
# print("漲跌幅: %.2f%%"%stock_range)
# print(tds[7].text) #昨收
# print(tds[9].text) #最高
# print(tds[10].text) #最低