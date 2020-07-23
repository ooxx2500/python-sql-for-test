# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:21:30 2020

@author: ASUS
"""




stock_number=[]
stock_name=[]
import datetime
import time
import requests
from bs4 import BeautifulSoup
import csv #載入csv套件
import pandas as pd #載入pandas 取名為pd
import datetime
import io
#date=str(datetime.date.today())# 取今天的日期
#date=date.replace("-", "")#去除日期"-"的符號
date='20200722'
"""
下面網址為證交所每日收盤行情 不含權證
"""
url="https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="+date+"&type=ALLBUT0999"
page=requests.get(url) # 取得當天收盤行情資料
use_text=page.text.splitlines() #page 資料分成一行一行處理
"""
用for迴圈 找出要的資料位址起始 initial_point : i
"""
for i,text in enumerate(use_text):
        if text == '"證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比",':
            initial_point = i
            break
"""
1.將資料轉成dataframe格式
"""
df = pd.read_csv(io.StringIO(''.join([text[:-1] + '\n' for text in use_text[initial_point:]])))
df['證券代號'] = df['證券代號'].str.replace('=','')#刪除 證券代號欄位的=符號
df['證券代號'] = df['證券代號'].str.replace('"','')#刪除 證券代號欄位的"符號
for i in  df['證券代號'] :
    stock_number.append(i)    
for a in  df['證券名稱'] :
    stock_name.append(a)    


def check_stock_value(stock_number): # 即時股票價格 漲跌用+ or -的符號
    import datetime
    import time
    import requests
    from bs4 import BeautifulSoup 
    stock_number=str(stock_number)
    url="https://tw.stock.yahoo.com/q/q?s="+stock_number
    list_req=requests.get(url)
    soup=BeautifulSoup(list_req.content,"html.parser")
    try:
        stock_name=soup.find(href="/q/bc?s="+stock_number).text
        print("股票名稱:",stock_name)
        retext="股票名稱:"+stock_name+"\n"
        
        
        time = soup.find_all("td", align="center",bgcolor="#FFFfff")[0].text
        print("時間:",time)
        retext+="時間"+str(time)+"\n"
        
        getstock=eval(soup.findAll("b")[1].text)
        print("即時股價: %.2f" % getstock)
        retext+="即時股價:"+str("%.2f" % getstock)+"\n"
        
    
        b = eval(soup.find_all("td", align="center",bgcolor="#FFFfff")[6].text) # b:昨收價
        c = getstock-b
        if (c>=0):
            print("漲跌: "+"+%.2f" % c)
            retext+="漲跌: "+str("+%.2f"% c)+"\n"
            
        else:
            print("漲跌: %.2f" % c)
            retext+="漲跌: "+str("%.2f"% c)+"\n"
          
        
        Quote=((getstock-b)/b)*100
        if Quote>=0:
            print("漲跌幅: "+"+"+"%.2f" % Quote+"%")
            retext+="漲跌幅: "+"+"+str("%.2f" % Quote)+"%"
            return retext
        else:
            print("漲跌幅: %.2f" % Quote+"%")
            retext+="漲跌幅: %.2f" % Quote+"%"
            return retext
    except:
        print('輸入錯誤2')
        
def check_stock_number():
    stock=str(input("輸入股票代號或名稱:")) 
    if stock in stock_name :
        index=stock_name.index(stock)
        a=stock_number[index]
        retext=''
        return a,retext
    elif stock in stock_number: 
        retext=''
        return stock,retext
    else :
        print("輸入錯誤")
        retext="輸入錯誤" 
        return False,retext
       
    
a ,retext =check_stock_number()
if a:
    retext=check_stock_value(a)
print('****************************************')    
print(retext) #得到結果的字串