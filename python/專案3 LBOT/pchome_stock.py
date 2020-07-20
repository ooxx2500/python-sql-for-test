# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:10:11 2020

@author: ASUS
"""


import requests
from bs4 import BeautifulSoup
stock="2330" # 尋找股票號碼2347 聯強的資訊
url='https://stock.pchome.com.tw/stock/sto0/ock3/sid'+stock+'.html'
header = {

    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Connection': 'keep-alive'
}


list_req=requests.post(url ,headers=header)
print(list_req.text)
soup=BeautifulSoup(list_req.content,"html.parser")
print(soup)
getstock=soup.find("table", {"id":"to_chart"})
print(getstock)

