# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:11:06 2020

@author: 莫再提
"""


from tkinter import *
import pymysql
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


df=pd.read_csv(r"C:\Users\莫再提\Documents\python-sql-for-test\python\專案3LBOT\stockname.csv")
df=df[['證劵代號','證劵名稱']]
stock_num=[]
for i in df['證劵代號']:
    stock_num.append(i)
#print(stock_num)

stock_name=[]
for i in df['證劵名稱']:
    stock_name.append(i.strip())
#print(stock_name)

input_text="2317"
sname=[]




if input_text in stock_name:
    index=stock_name.index(input_text)
    num=stock_num[index]
    
    stock=num # 尋找股票號碼2347 聯強的資訊
    url="https://tw.stock.yahoo.com/q/q?s="+stock
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"lxml")
    
    
    
    tables=soup.find_all('table')
    tds=tables[2].find_all('td')
    stock_range=(eval(tds[2].text)-eval(tds[7].text))*100/eval(tds[7].text)
    
    
    retext=tds[0].text.replace('加到投資組合','')+"\n"+"成交時間:"+tds[1].text+"\n"+"成交價:"+tds[2].text+"\n"+"漲跌:"+tds[5].text.strip()[:]+"\n"+ "漲跌幅: %.2f%%"%stock_range
    
    
    print(retext)
    
    
elif input_text in stock_num:
    num=input_text
    
    stock=num # 尋找股票號碼2347 聯強的資訊
    url="https://tw.stock.yahoo.com/q/q?s="+stock
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"lxml")
    
    
    
    tables=soup.find_all('table')
    tds=tables[2].find_all('td')
    stock_range=(eval(tds[2].text)-eval(tds[7].text))*100/eval(tds[7].text)
    
    
    retext=tds[0].text.replace('加到投資組合','')+"\n"+"成交時間:"+tds[1].text+"\n"+"成交價:"+tds[2].text+"\n"+"漲跌:"+tds[5].text.strip()[:]+"\n"+ "漲跌幅: %.2f%%"%stock_range
    
    
    print(retext)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    