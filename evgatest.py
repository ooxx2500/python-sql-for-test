# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 07:14:35 2021

@author: 55
"""

from selenium import webdriver
import time
driver_path = r'chromedriver.exe'
web = webdriver.Chrome(driver_path)
web.get('https://tw.evga.com/products/productlist.aspx?type=0&family=GeForce+30+Series+Family&chipset=RTX+3070')

web.set_window_position(0,0) #原點0,0再畫面左上角
web.set_window_size(700,700)  #設定網頁式窗大小    
time.sleep(5) #停5秒
web.find_element_by_link_text('Click this button to be notified once this product is available!').click() #找到連結叫衛星的點一下
time.sleep(5)
web.close() #關閉瀏覽器  
