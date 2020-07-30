# -*- coding: utf-8 -*-
"""
XHR資料:
    XMLHttpRequest
    使用網頁的情況下更新資料
使用函式:(自定函式)
    convertDate:民國年份日期字串至轉為西元年字串
    
def convertDate(date):
    str1=str(date)
    yearst=str1[:3]    
    ryear=str(int(yearst)+1911)
    findate=ryear+str1[4:6]+str1[7:9]
    return findate
    
查股票 pip install twstock

"""
import twstock

stock=twstock.Stock('2002') #股票代號 S要大寫
print('近三十個收盤價')
print(stock.price)#進31個收盤價
print('近6個收盤價')
print(stock.price[-6:])#進6個收盤價

rel = twstock.realtime.get('2002')
if rel['success']:
    print('股票即時資料')
    print(rel)
    print('錯誤:'+rel['rtmessage'])
    print('目前資訊:')
    print(rel['realtime']['latest_trade.price'])
    
    
'''




'''    

def twdigit(n):
    if (n<10):
        rstr='0'+str(n)
    else:
        rstr=str(n)
    return rstr

url1='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019'
url2='01&stockNo=2885&_=1595922586982'
for i in range(1,13):
    urlfinal=url1+twdigit(i)+url2
    print(urlfinal)


------------------------------------------------
def convertDate(date):
    strl = str(date)
    yearstr = strl[:3]
    realyear = str(int(yearstr) + 1911)
    realdate = realyear + strl[4:6] + strl[7:9]
    return realdate

import requests
import json, csv
import pandas as pd
import os

pd.options.mode.chained_assignment = None

filepath = r'C:\Users\ASUS\Documents\Python-SQL\python\stockmonthGl.csv'

if not os.path.isfile(filepath):
    url_twse = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20191101&stockNo=2885&_=1595922586982'
    res = requests.get(url_twse)
    jdata = json.loads(res.text)

    outputfile = open(filepath, 'w' , newline='', encoding='utf-8')
    outputwriter = csv.writer(outputfile)
    outputwriter.writerow(jdata['fields'])
    for dataline in (jdata['data']):
        outputwriter.writerow(dataline)
    outputfile.close()

pdstock = pd.read_csv(filepath, encoding='utf-8')
for i in range(len (pdstock['日期'])):
    pdstock['日期'][i] = convertDate(pdstock['日期'][i])
pdstock['日期'] = pd.to_datetime(pdstock['日期'])
pdstock.plot(kind= 'line', figsize=(12, 6),x='日期',y=['收盤償','最低價','最高價'])


---------------------------------------------------------------


def twodigit(n):
    if(n < 10):
         retstr = 'O' + str(n)
    else:
         retstr = str(n)
    return retstr

def convertDate(date):
    strl = str(date)
    yearstr = strl[:3]
    realyear = str(int(yearstr)+ 1911)
    realdate = realyear + strl[4:6] + strl[7:9]
    return realdate

import requests
import json, csv
import pandas as pd
import os
import time

pd.options.mode.chained_assignment = None

urlbase ='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2018'
urltail = '&stockNo=2885&_=1595922586982'


filepath = r'C:\Users\ASUS\Documents\Python-SQL\python\figure\stockyear2018.csv'

if not os.path.isfile(filepath):
    for i in range(1, 13):
        url_twse = urlbase + twodigit(i) + urltail
        res = requests.get(url_twse)
        jdata = json.loads(res.text)

        outputfile = open(filepath, 'a', newline='', encoding='utf-8')
        outputwriter = csv.writer(outputfile)
        if i==1:
            outputwriter.writerow(jdata['fields'])
        for dataline in (jdata['data']):
            outputwriter.writerow(dataline)
        time.sleep(0.5)
    outputfile.close()

pdstock = pd.read_csv(filepath, encoding='utf-8')
for i in range(len(pdstock['日期'])):
    pdstock['日期'] [i] = convertDate(pdstock['日期'] [i])
pdstock['日期'] = pd. to_datetime(pdstock['日期'])
pdstock.plot(kind='line', figsize=(12, 6),x= '日期',y=['收盤價','最低價','最高價'])

------------------------

import requests, bs4

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'}) #驗證我已經18
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')
articles = 0
pttdivs = objSoup.find_all('div','r-ent')
for p in pttdivs:
    if p.find('a'):
       articles += 1
print('本頁文章數=',articles)

---------------------------
import requests, bs4

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
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
    
------------------------------------------


import requests, bs4

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')
articles =[]
pttdivs = objSoup.find_all('div', 'r-ent')
for p in pttdivs:
    if p.find('a'):
        title = p.find('a').text
        author = p.find('div', 'author').text
        href = p.find('a')['href']
        push_num = p.find('div','nrec').text
        articles.append({'title':title,
                        'author':author,
                        'href':href,
                        'push_num':push_num,
})
print('本頁文章數:',len(articles))
count = 0
for article in articles:
    count += 1
    print('文章編號：',count)
    print ('文章標題：',article['title' ])
    print ('文章作者：',article[ 'author' ])
    print ('文章連結: ',article['href'], '\n')
    print ('推文數量: ',article['push_num'], '\n')


------------------------------------------------
import requests, bs4


url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ptthtml = requests.get(url, cookies={'overl8':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

articles =[]
pttdivs = objSoup.find_all( 'div', 'r-ent')
for p in pttdivs:
    if p.find('a' ):
        title = p.find('a').text
        author = p.find('div', 'author').text
        href = p.find('a')['href']
        push_num = p.find('div', 'nrec').text
        if push_num.startswith('X'):
            push_num = '0'
        if push_num == '爆':
            push_num = '100'
        publish_time = p.find( 'div', 'date') .text
        articles.append({'title':title,
                          'publish_time' :publish_time,
                          'author' :author,
                          'href' :href,
                          'push_num':push_num,
                        })
print('本頁的文章數量=',len(articles))
count = 0
pushcounts = 10

print ('下列是推文數大於20的文章' ,'\n')
for article in articles:
    count += 1
    if article['push_num'] !='':
       push_min = int(article['push_num'])
    else:

        push_min = 0
    if push_min > pushcounts:
        print('文章編號：',count)
        print ('文章標題：',article['title'])
        print('發表時間:',article['publish_time'])
        print ('文章作者：',article[ 'author'])
        print ('文章連結: ',article['href'], '\n')
        print ('推文數量: ',article['push_num'], '\n')
    

---------------------------------------
#pm25用json的dump load讀取json

import requests
import json

url = r'http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json'

try:
    aqijsons = requests.get(url)
    print("下載成功")
except Exception as err:
    print("下載失敗")

print(aqijsons.text)

fn = r'C:\Users\ASUS\Documents\Python-SQL\python\aqi.json'
with open(fn, 'w') as f:
    json.dump(aqijsons.json(),f)#將網頁讀取的JSON檔轉儲存 用dump儲存(轉為json)
       
#--------------------------------------------    
import json

fn = r'C:\Users\ASUS\Documents\Python-SQL\python\aqi.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj) #將json黨獨取為py物件 用load

for getData in getDatas:
    county = getData['County']
    sitename = getData['SiteName']
    siteid = getData['SiteId']
    pm25 = getData['PM2.5']
    print('城市名稱 =%4s 站台ID =%3s PM2.5值 =%3s  站台名稱 = %s ' %  
    (county, siteid, pm25, sitename))


#------------------------------------------------    
import json

fn = r'C:\Users\ASUS\Documents\Python-SQL\python\aqi.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)

for getData in getDatas:
    if getData[ 'County' ]== '新北市' :
         sitename = getData['SiteName']
         siteid = getData['SiteId']
         pm25 = getData['PM2.5']
         print('站台ID =%3s  PM2.5 值=%3s  站台名稱=%s ' %(siteid, pm25, sitename))




















