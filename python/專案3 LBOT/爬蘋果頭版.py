# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 09:33:10 2020

@author: ASUS
"""


import requests
from bs4 import BeautifulSoup



headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)'\
    'AppleWebkit/537.36 (KHTML, like Gecko) chrome/56.0.2924.87 Safari/537.36'
    }

rs = requests.Session() #建立rs物件

res = rs.get('https://hk.appledaily.com/realtime/index',headers = headers)


soup = BeautifulSoup(res.content, "lxml")



items = soup.find("div",{"class":"LHSContent_inner NoTab"}).find_all("a")

for i in items:
    print(i.text.strip())
									

