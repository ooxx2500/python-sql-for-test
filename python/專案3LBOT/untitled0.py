# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:24:32 2020

@author: ASUS
"""

import requests
from bs4 import BeautifulSoup



url=r'https://24h.pchome.com.tw/'
req=requests.get(url)
soup=BeautifulSoup(req.text,'html.parser')

a=soup.find_all('dl','site_mkt festival extend')
for i in a:
    print(i)