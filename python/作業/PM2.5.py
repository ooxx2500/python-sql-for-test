# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:19:55 2020

@author: ASUS
"""

import csv
with open(r'C:\Users\ASUS\Documents\Python-SQL\python\作業\2.5.csv','r',encoding = 'utf8') \
    as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')#用reader方法讀取 plots是個串列
                              #用delimiter設定資料以逗號分隔字元，藉以取出每個資料
        for row in plots:
            print('測站:',row[0],'縣市:',row[1],'PM2.5 =',row[2])
            
            
--------------------------------------
import json
with open(r'C:\Users\ASUS\Documents\Python-SQL\python\作業\2.5.json',encoding = 'utf8')\
    as file:
    data = json.load(file)    
    for item in data:
        print('測站:',item['Site'],'縣市:',item['county'],'PM2.5 =',item['PM25']) #以索引列印item各欄位資料            


--------------------------------------            

import xml.etree.ElementTree as et #載入xml.etree.ElementTree套件 解析為數狀結構
tree = et.ElementTree(file=r'C:\Users\ASUS\Documents\Python-SQL\python\作業\2.5.xml')
#讀取XML檔，儲存到 tree 變數
root = tree.getroot() #取得根節點(即XML標籤)
for aa in root: #(menu標籤下的子標籤)
    #子標籤下的子標籤
    print('測站:',aa[0].text,'縣市:' ,aa[1].text,'PM2.5 =', aa[2].text)
-------------------------------------

import xml.etree.ElementTree as et #載入xml.etree.ElementTree套件 解析為數狀結構
tree = et.ElementTree(file=r'C:\Users\ASUS\Documents\Python-SQL\python\作業\2.5.xml')
#讀取XML檔，儲存到 tree 變數
root = tree.getroot() #取得根節點(即XML標籤)
for i in root.findall('Data'): #(menu標籤下的子標籤)
    #子標籤下的子標籤
    site = i.find('Site').text
    area = i.find('county').text
    pm2 =i.find('PM25').text
    print('測站:',site,'縣市:' ,area,'PM2.5 =', pm2)



















