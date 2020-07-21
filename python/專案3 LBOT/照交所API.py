# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:36:18 2020

@author: ASUS
"""


from twstock import *
stock = Stock('2330')
stock_price = stock.fetch_31()
price=realtime.get('2330')  
print(price)
https://zys-notes.blogspot.com/2020/01/api.html

參數 = tse_2330.tw|otc_6488.tw
https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_2330.tw|otc_6488.tw&json=1&delay=0