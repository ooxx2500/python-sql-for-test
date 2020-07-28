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

