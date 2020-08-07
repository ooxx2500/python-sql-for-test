# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:39:59 2020

@author: ASUS
"""
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


#用以儲存所爬到的大樂透號碼
lotto_list=[]

driver=webdriver.Chrome('chromedriver.exe')
driver.get( 'http://www.taiwanLottery.com.tw/Lotto/Lotto649/history.aspx')



#勾選要以年月查詢的選項
driver.find_element_by_id( 'Lotto649ControL_history_radYM').click()


while True:
    select_year= Select(driver.find_element_by_id('Lotto649ControL_history_dropYear'))
    year= input('輸入年份')
    print ('等等等')
    select_year.select__by_value(year)
    for i in range(12):
        #却找出選擇月份的標簽
        select_month=Select (driver. find_element_by_id( ' Lotto649ControL_history_dropMonth '))
        select_month.select_by_value( str(i+1 ))

        #點擊「查詢」按鈕
        driver.find_element_by_id('Lotto649ControL_history_btnSubmit' ). click()

        #妙抓取網頁内容
        html= driver.page_source
        soup=bs(html, 'htmL.parser' )

        #數網頁中有多少個table
        table_count=len (soup.findAll( 'table' ,{ 'cLass ': 'td_hm' }))
        #转針對每一個table"抓取樂透號碼並加入串列
        for i in range(table_count):
            for j in range(1,7):                        
               temp=soup.find('span', {'id ': 'Lotto649ControL_history_dLQuery_No' + str(j)+'_'+str(i)})
    check=input('繼續請按Y')
    if check.upper()!='Y':
        print('end')
    break