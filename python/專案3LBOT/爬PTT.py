# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:07:33 2020

@author: ASUS
"""



import requests, bs4

url = 'https://www.ptt.cc/bbs/HardwareSale/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')
articles =[]
pttdivs = objSoup.find_all('div', 'r-ent')
for p in pttdivs:
    if p.find('a'):
        title = p.find('a').text
        author = p.find('div', 'author').text
        href = p.find('a')['href']
        articles.append({'title':title,
                        'author':author,
                        'href':href,
})
print('本頁文章數:',len(articles))
count = 0
for article in articles:
    count += 1
    print('文章編號：',count)
    print ('文章標題：',article['title' ])
    print ('文章作者：',article[ 'author' ])
    print ('文章連結: ',article['href'], '\n')