# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:25:37 2020

@author: 莫再提
"""


import requests
from bs4 import BeautifulSoup
stock="2330" # 尋找股票號碼2347 聯強的資訊
url="https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=1"
list_req=requests.get(url)
soup=BeautifulSoup(list_req.content,"lxml")
lu=soup.find_all("ul")

print(lu)