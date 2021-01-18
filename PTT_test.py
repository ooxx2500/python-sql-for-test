# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:42:57 2021

@author: 55
"""

import requests, bs4 ,time
from playsound import playsound
     



articles =[]
names=[]
count_list=0

url = 'https://www.ptt.cc/bbs/HardwareSale/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')
pttdivs = objSoup.find_all('div', 'r-ent')
search_txt =["1070","1080","3070","3080","3090",'2060','2070','2080','470','570']

product=''

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
                    for pp in pttdivs2:
                        try:
                            pnum=pp.text.find('硬體型號：')
                            pnum2=pp.text.find('欲售價格：')
                            product=pp.text[pnum+6:pnum2]
                            print(product)
                        
                       
                            numb=pp.text.find('欲售價格')                            
                            numb2=pp.text.find('品樣狀況')
                            
                            
                            price=pp.text[numb+5:numb2]
          
                            timenumb=pp.text.find('時間') 
                            time2=pp.text[timenumb+13:timenumb+26]
                        except:
                            print('error')
                            
                        
                        articles.append({'title':title,
                                         'time':time2,
                                         'product':product,
                             'price':price,            
                            'author':author,
                            'href':href,
    })


                

                    print ('文章標題：',articles[count_list]['title' ])
                    print ('時間：',articles[count_list]['time' ])
                    print('內容:',articles[count_list]['product'].strip())
                    print ('價格：',articles[count_list]['price'].strip())
                    print ('文章作者：',articles[count_list][ 'author' ])
                    print ('文章連結: ',"https://www.ptt.cc"+articles[count_list]['href'], '\n')
                    print('***************************************')
                    count_list+=1
