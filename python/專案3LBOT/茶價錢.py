# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 01:23:22 2020

@author: 莫再提
"""


import requests
import re
from bs4 import BeautifulSoup

def search_price(intext):   
    
    url=r"https://feebee.com.tw/s/"+intext.replace('#','').replace(' ','%20')+r'/?sort=d&mode=l&ptab=0'
    
    
    
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)'\
        'AppleWebkit/537.36 (KHTML, like Gecko) chrome/56.0.2924.87 Safari/537.36'
        }
    
    rs=requests.get(url, headers = headers)
    
    
    
    soup=BeautifulSoup(rs.text,"lxml")
    lis=soup.find('ol','promo-results').find_all('li','pure-g items')
    
    retext=''
    c=1
    for li in lis:
        
        if c==1 or c==2:
            c+=1
            continue
    
        elif c==8:
            break
        else:
            c+=1
            retext+= li.find('h3').text+'\n'
            retext+= "商品售價: %s" % li.find('li','price ellipsis xlarge').text+'\n'
            
            llis = li.find_all('li','pure-g')
            print(llis.find(''))
            
            retext+=li.find('a','items_link')['href']+'\n'
        print('*************')
            
    return retext


input_text='# 2060 顯示卡'

if re.match('^#.+',input_text):

    print(search_price(input_text))
else:
    print('NONONONON')


