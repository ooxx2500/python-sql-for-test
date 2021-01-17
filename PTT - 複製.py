# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 01:14:56 2021

@author: 55
"""

import requests, bs4 ,time

while True:
    url = 'https://www.ptt.cc/bbs/HardwareSale/index.html'
    ptthtml = requests.get(url, cookies={'over18':'1'})
    objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')
    articles =[]
    pttdivs = objSoup.find_all('div', 'r-ent')
    search_txt =["1070","1080","3070","3080","3090",'2060','2070','2080']
    
    for p in pttdivs:
        if p.find('a'):
            title = p.find('a').text
            author = p.find('div', 'author').text
            href = p.find('a')['href']
            
            for i in search_txt:
                if i in title and '賣' in title:
                    new_url="https://www.ptt.cc"+href                     
                    ptthtml = requests.get(new_url, cookies={'over18':'1'})
                    objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')
                    pttdivs2 = objSoup.find_all('div',{"id":'main-container'})                
                    for PP in pttdivs2:
                        numb=PP.text.find('欲售價格')
                        price=PP.text[numb+5:numb+20]
      
                        timenumb=PP.text.find('時間') 
                        time2=PP.text[timenumb+13:timenumb+26]
                        articles.append({'title':title,
                                         'time':time2,
                             'price':price,            
                            'author':author,
                            'href':href,
    })
    
    
                    
    
    count = 0
    for article in articles:
        count += 1
        print('文章編號：',count)
        print ('文章標題：',article['title' ])
        print ('時間：',article['time' ])
        print ('價格：',article['price'])
        print ('文章作者：',article[ 'author' ])
        print ('文章連結: ',"https://www.ptt.cc"+article['href'], '\n')
        print('***************************************')
    time.sleep(30)