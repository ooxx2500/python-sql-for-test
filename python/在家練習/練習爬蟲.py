# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:37:39 2020

@author: 莫再提
"""


from bs4 import BeautifulSoup
import requests

url = r'http://blog.castman.net/py-scraping-analysis-book/ch2/table/table.html'
html = requests.get(url)
bs = BeautifulSoup(html.text , 'html.parser')

alltr = bs.find('table','table').tbody.find_all('tr')
total = []
for tr in alltr: 
    tds=tr.find_all('td')
 
    price = eval(tds[2].text)
    total.append(price)
    
print(html.status_code)
print(sum(total))
