# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 04:36:11 2021

@author: 55
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 01:14:56 2021

@author: 55
"""

import requests, bs4 ,time
from playsound import playsound
     



articles =[]
names=[]
count_list=0
while True:
    url = 'https://www.ptt.cc/bbs/HardwareSale/index.html'
    ptthtml = requests.get(url, cookies={'over18':'1'})
    objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')
    pttdivs = objSoup.find_all('div', 'r-ent')
    search_txt =["1070","1080","3070","3080","3090",'2060','2070','2080','470','570']
    
    for p in pttdivs:
        if p.find('a'):
            title = p.find('a').text
            if title not in names:
                names.append(title)

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
                            
                            numb2=PP.text.find('◎品樣狀況')
                            
                            
                            price=PP.text[numb+5:numb2]
          
                            timenumb=PP.text.find('時間') 
                            time2=PP.text[timenumb+13:timenumb+26]
                            articles.append({'title':title,
                                             'time':time2,
                                 'price':price,            
                                'author':author,
                                'href':href,
        })
    
    
                    

                        print ('文章標題：',articles[count_list]['title' ])
                        print ('時間：',articles[count_list]['time' ])
                        print ('價格：',articles[count_list]['price'])
                        print ('文章作者：',articles[count_list][ 'author' ])
                        print ('文章連結: ',"https://www.ptt.cc"+articles[count_list]['href'], '\n')
                        print('***************************************')
                        count_list+=1
                        playsound("ttas.mp3")
    time.sleep(30)